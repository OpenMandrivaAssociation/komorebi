Name: komorebi
Summary: A beautiful and customizable wallpapers manager for Linux
Version: 2.1
Release: 2
Group: system
License: GPLv3
URL: https://github.com/cheesecakeufo/komorebi
Source0: https://github.com/cheesecakeufo/komorebi/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(clutter-gst-3.0)
BuildRequires: pkgconfig(vapigen)	
BuildRequires: vala

#Requires: vt323-fonts
#Requires: lato-fonts

%description
Komorebi is an awesome desktop manager for all Linux platforms. It provides
fully customizeable image and video wallpapers that can be tweaked at any time!

%prep
%setup -q
#sed -i -e 's|/System/Applications|/usr/bin|' -e 's|/System/Resources|/usr/share|' CMakeLists.txt

%build
%cmake -G Ninja \

%install
%ninja_install -C build

%files
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/Komorebi
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/wallpapercreator.desktop
%{_datadir}/fonts/AmaticSC-Regular.ttf
%{_datadir}/fonts/Bangers-Regular.ttf
%{_datadir}/fonts/BubblerOne-Regular.ttf
%{_datadir}/fonts/Lato-Hairline.ttf
%{_datadir}/fonts/Lato-Light.ttf
%{_datadir}/fonts/VT323-Regular.ttf
