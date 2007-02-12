%define		maj_ver	3.01
%define		min_ver	x88
Summary:	A Mozilla plug-in to view W3C's SVG (Scalable Vector Graphics) content
Summary(pl.UTF-8):   Wtyczka dla przeglądarek opartych na Mozilli do oglądania SVG (Scalable Vector Graphics)
Name:		mozilla-plugin-svg
Version:	%{maj_ver}
Release:	0.%{min_ver}.1
License:	? See LICENSE.txt
Group:		X11/Applications/Multimedia
Source0:	http://download.adobe.com/pub/adobe/magic/svgviewer/linux/3.x/%{maj_ver}%{min_ver}/en/adobesvg-%{maj_ver}%{min_ver}-linux-i386.tar.gz
# NoSource0-md5:	fc619d96a81d9fa54e42532ca57b09ca
NoSource:	0
URL:		http://www.adobe.com/svg/
Prereq:		mozilla-embedded
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Adobe SVG plugin allows Mozilla-family browsers to view SVG
content on the Web or locally. SVG is a recently-approved W3C standard
for vector graphics. SVG is XML-based, making it immediately
accessible by the whole range of XML tools. It also has tremendously
rich graphical capabilities, surpassing most or all other currently
used vector graphics formats.

%description -l pl.UTF-8
Wtyczka Adobe SVG pozwala przeglądarkom opartym na mozilli
przeglądanie plików SVG z sieci oraz lokalnych. SVG to niedawno
zaaprobowany przez W3C standard grafiki wektorowej. Jest oparty na
XML-u, co czyni go od razu dostępnym dla szerokiego zakresu narzędzi
do XML-a. Ma bardzo duże możliwości graficzne, przewyższające
wszystkie inne aktualnie używane formaty graficzne.

%prep
%setup -q -n adobesvg-%{maj_ver}
chmod -R u+w ../adobesvg-%{maj_ver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins

install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins
# the .so's look for that file in plugindir
install SVGAbout.svg $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.html
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_libdir}/mozilla/plugins/*.svg
