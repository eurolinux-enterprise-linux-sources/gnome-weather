%global gjs_version 1.39.91
%global gobject_introspection_version 1.35.9
%global gtk3_version 3.11.4
%global libgweather_version 3.9.5

Name:		gnome-weather
Version:	3.14.1
Release:	1%{?dist}
Summary:	A weather application for GNOME

License:	GPLv2+ and LGPLv2+ and MIT and CC-BY and CC-BY-SA
URL:		https://live.gnome.org/Design/Apps/Weather
Source0:	http://download.gnome.org/sources/%{name}/3.14/%{name}-%{version}.tar.xz

BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	gjs-devel >= %{gjs_version}
BuildRequires:	glib2-devel
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection >= %{gobject_introspection_version}
BuildRequires:	gtk3-devel >= %{gtk3_version}
BuildRequires:	libgweather-devel >= %{libgweather_version}

Requires:	gdk-pixbuf2
Requires:	gjs >= %{gjs_version}
Requires:	glib2
Requires:	gobject-introspection >= %{gobject_introspection_version}
Requires:	gtk3 >= %{gtk3_version}
Requires:	libgweather >= %{libgweather_version}

%description
gnome-weather is a weather application for GNOME

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang org.gnome.Weather

%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/org.gnome.Weather.Application.desktop

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
touch --no-create %{_datadir}/icons/HighContrast &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    touch --no-create %{_datadir}/icons/HighContrast &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/HighContrast &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/HighContrast &>/dev/null || :

%files -f org.gnome.Weather.lang
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
%{_datadir}/icons/hicolor/*/apps/org.gnome.Weather.Application.png
%{_datadir}/icons/HighContrast/*/apps/org.gnome.Weather.Application.png
%{_datadir}/org.gnome.Weather/

%changelog
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

