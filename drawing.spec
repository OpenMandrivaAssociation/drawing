Name:           drawing
Version:        0.4.7
Release:        1
Summary:        Drawing application for the GTK desktops
License:        GPLv3+
URL:            https://github.com/maoschanz/drawing
Source0:        https://github.com/maoschanz/drawing/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  python-devel
BuildRequires:  pkgconfig(gtk+-3.0)
Requires:       icon-theme-hicolor

%description
This application is a basic image editor, similar to Microsoft Paint,
but aiming at the GNOME desktop.

PNG, JPEG and BMP files are supported.

Besides GNOME, some more traditional design layouts are available too,
as well as an elementaryOS layout. It should also be compatible with
Purism's Librem 5 phone.


%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome

desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%doc --no-dereference LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/*.appdata.xml
