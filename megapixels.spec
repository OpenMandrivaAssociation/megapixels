Name:		megapixels
Version:	0.16.0
Release:	1
License:	GPLv3
URL:		https://git.sr.ht/~martijnbraam/megapixels
Source0:	%{name}-%{version}.tar.gz
Summary:	Camera app for mobile devices
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(zbar)

%description
Camera app for mobile devices

%prep
%autosetup -p1
%meson \
	-Dtiffcfapattern=true

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/megapixels
%{_bindir}/megapixels-camera-test
%{_bindir}/megapixels-list-devices
%{_datadir}/applications/org.postmarketos.Megapixels.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Megapixels.svg
%{_datadir}/megapixels
%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml
