Summary:	XprintUtil library
Summary(pl):	Biblioteka XprintUtil
Name:		xorg-lib-libXprintUtil
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libXprintUtil-%{version}.tar.bz2
# Source0-md5:	5596c2debac370cafadc0ddf1e9e7eba
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XprintUtil library.

%description -l pl
Biblioteka XprintUtil.

%package devel
Summary:	Header files for libXprintUtil library
Summary(pl):	Pliki nag³ówkowe biblioteki libXprintUtil
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXt-devel

%description devel
XprintUtil library.

This package contains the header files needed to develop programs that
use libXprintUtil.

%description devel -l pl
Biblioteka XprintUtil.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXprintUtil.

%package static
Summary:	Static libXprintUtil library
Summary(pl):	Biblioteka statyczna libXprintUtil
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XprintUtil library.

This package contains the static libXprintUtil library.

%description static -l pl
Biblioteka XprintUtil.

Pakiet zawiera statyczn± bibliotekê libXprintUtil.

%prep
%setup -q -n libXprintUtil-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXprintUtil.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXprintUtil.so
%{_libdir}/libXprintUtil.la
%dir %{_includedir}/X11/XprintUtil
%{_includedir}/X11/XprintUtil/*.h
%{_pkgconfigdir}/xprintutil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXprintUtil.a
