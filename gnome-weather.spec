%global gjs_version 1.49.4
%global gobject_introspection_version 1.35.9
%global gtk3_version 3.11.4
%global libgweather_version 3.25.91

Name:		gnome-weather
Version:	3.26.0
Release:	1%{?dist}
Summary:	A weather application for GNOME

License:	GPLv2+ and LGPLv2+ and MIT and CC-BY and CC-BY-SA
URL:		https://wiki.gnome.org/Apps/Weather
Source0:	https://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz

BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	gjs-devel >= %{gjs_version}
BuildRequires:	glib2-devel
BuildRequires:	gobject-introspection >= %{gobject_introspection_version}
BuildRequires:	gtk3-devel >= %{gtk3_version}
BuildRequires:	libgweather-devel >= %{libgweather_version}
BuildRequires:	pkgconfig(libgeoclue-2.0) >= 2.3.1

Requires:	gdk-pixbuf2
Requires:	gjs >= %{gjs_version}
Requires:	glib2
Requires:	gobject-introspection >= %{gobject_introspection_version}
Requires:	gtk3 >= %{gtk3_version}
Requires:	libgweather >= %{libgweather_version}

%description
gnome-weather is a weather application for GNOME

%package tests
Summary: Tests for the gnome-weather package
Requires: %{name} = %{version}-%{release}

%description tests
The gnome-weather-tests package contains tests that can be used to verify
the functionality of the installed gnome-weather package.

%prep
%autosetup

%build
%configure --disable-static --enable-installed-tests
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -print -delete

# Fix appdata file name
mv %{buildroot}%{_datadir}/appdata/org.gnome.Weather.appdata.xml \
   %{buildroot}%{_datadir}/appdata/org.gnome.Weather.Application.appdata.xml

%find_lang org.gnome.Weather

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Weather.Application.desktop

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f org.gnome.Weather.lang
%license COPYING
%doc NEWS data/CREDITS
%{_bindir}/gnome-weather
%{_datadir}/appdata/org.gnome.Weather.Application.appdata.xml
%{_datadir}/applications/org.gnome.Weather.Application.desktop
%{_datadir}/dbus-1/services/org.gnome.Weather.Application.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.Application.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Weather.png
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Weather-symbolic.svg
%{_datadir}/org.gnome.Weather/

%files tests
%{_libexecdir}/installed-tests/org.gnome.Weather/
%{_datadir}/installed-tests

%changelog
* Mon Sep 11 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0
- Resolves: #1511093

* Thu Feb 23 2017 Matthias Clasen <mclasen@redhat.com> - 3.20.2-1
- Rebase to 3.20.2
  Resolves: rhbz#1386969

* Mon Mar 23 2015 Richard Hughes <rhughes@redhat.com> - 3.14.1-1
- Update to 3.14.1
- Resolves: #1174587

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.2-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.2-3
- Mass rebuild 2013-12-27

* Thu Dec 5 2013 Zeeshan Ali <zeenix@redhat.com> - 3.8.2-2
- Add categories to desktop file (#1037834).

* Tue May 14 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Wed Apr 17 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Thu Mar 28 2013 Cosimo Cecchi <cosimoc@gnome.org> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Cosimo Cecchi <cosimoc@gnome.org> - 3.7.92-1
- Initial packaging

