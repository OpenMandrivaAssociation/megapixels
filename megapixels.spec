Name:		megapixels
Version:	0.16.0
Release:	3
License:	GPLv3
URL:		https://git.sr.ht/~martijnbraam/megapixels
Source0:	%{name}-%{version}.tar.gz
Source1:	ch.lindev.camera.svg
Summary:	Camera app for mobile devices
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(zbar)
# For postprocess.sh
Requires:	imagemagick
Requires:	libraw-tools
Recommends:	perl-Image-ExifTool

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
# Replace the text and icons -- we want a newbie to be able
# to find the camera app without knowing its name
cp -f %{S:1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Megapixels.svg
sed -i -e 's,^Name=Megapixels,Name=Camera,' %{buildroot}%{_datadir}/applications/org.postmarketos.Megapixels.desktop

%files
%{_bindir}/megapixels
%{_bindir}/megapixels-camera-test
%{_bindir}/megapixels-list-devices
%{_datadir}/applications/org.postmarketos.Megapixels.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Megapixels.svg
%{_datadir}/megapixels
%{_datadir}/metainfo/org.postmarketos.Megapixels.metainfo.xml
