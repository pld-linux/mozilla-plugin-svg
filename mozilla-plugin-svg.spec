Summary:	A Mozilla plug-in to view W3C's SVG (Scalable Vector Graphics) content
Summary(pl):	Wtyczka dla przegl±darek opartych na Mozilli do ogl±dania SVG (Scalable Vector Graphics)
Name:		mozilla-plugin-svg
Version:	3.0
Release:	0.1
License:	? See LICENSE.txt
Group:		X11/Applications/Multimedia
Source0:	http://download.adobe.com/pub/adobe/magic/svgviewer/linux/3.x/%{version}x77/en/adobesvg-%{version}-linux-i386.tar.gz
# Source0-md5:	2f450f5074549c81dcca734a84fe11a1
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

%description -l pl
Wtyczka Adobe SVG pozwala przegl±darkom opartym na mozilli
przegl±danie plików SVG z sieci oraz lokalnych. SVG to niedawno
zaaprobowany przez W3C standard grafiki wektorowej. Jest oparty na
XML-u, co czyni go od razu dostêpnym dla szerokiego zakresu narzêdzi
do XML-a. Ma bardzo du¿e mo¿liwo¶ci graficzne, przewy¿szaj±ce
wszystkie inne aktualnie u¿ywane formaty graficzne.

%prep
%setup -q -n adobesvg-%{version}
chmod -R u+w ../adobesvg-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins

install *.so $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.html *.svg
%attr(755,root,root) %{_libdir}/mozilla/plugins/*.so
