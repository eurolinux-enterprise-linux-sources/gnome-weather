Name:		gnome-weather
Version:	3.8.2
Release:	4%{?dist}
Summary:	A weather application for GNOME

License:	GPLv2+ and LGPLv2+ and MIT and CC-BY and CC-BY-SA
URL:		https://live.gnome.org/Design/Apps/Weather
Source0:	http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/3.8/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel
BuildRequires:	gnome-common
BuildRequires:	gtk3-devel
BuildRequires:  gobject-introspection >= 1.35.9

# libgd is not meant to be installed as a system-wide shared library.
# It is just a way for GNOME applications to share widgets and other common
# code on an ad-hoc basis.
Provides:	bundled(libgd)

# Filter out the libgd.so() provide, since we don't want to possibly
# satisfy any erroneous dependency on it.
%filter_provides_in %{_libdir}/%{name}/.*\.so$
%filter_setup

# https://bugzilla.redhat.com/show_bug.cgi?id=1037834
# Add a category to the desktop file
Patch0:		add-categories-to-desktop-file.patch

%description
gnome-weather is a weather application for GNOME

%prep
%setup -q
%patch0 -p1 -b .add-categories-to-desktop-file

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc NEWS data/CREDITS
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_libdir}/gnome-weather/

%changelog
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

