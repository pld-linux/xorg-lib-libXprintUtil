# $Rev: 3309 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	XprintUtil library
Summary(pl):	Biblioteka XprintUtil
Name:		xorg-lib-libXprintUtil
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXprintUtil-%{version}.tar.bz2
# Source0-md5:	cfcc8082975abc6f0d79fe746869e5e8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXprintUtil-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XprintUtil library.

%description -l pl
Biblioteka XprintUtil.


%package devel
Summary:	Header files libXprintUtil development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXprintUtil
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXprintUtil = %{version}-%{release}
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXt-devel

%description devel
XprintUtil library.

This package contains the header files needed to develop programs that
use these libXprintUtil.

%description devel -l pl
Biblioteka XprintUtil.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXprintUtil.


%package static
Summary:	Static libXprintUtil libraries
Summary(pl):	Biblioteki statyczne libXprintUtil
Group:		Development/Libraries
Requires:	xorg-lib-libXprintUtil-devel = %{version}-%{release}

%description static
XprintUtil library.

This package contains the static libXprintUtil library.

%description static -l pl
Biblioteka XprintUtil.

Pakiet zawiera statyczne biblioteki libXprintUtil.


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
%attr(755,root,wheel) %{_libdir}/libXprintUtil.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/XprintUtil/*.h
%{_libdir}/libXprintUtil.la
%attr(755,root,wheel) %{_libdir}/libXprintUtil.so
%{_pkgconfigdir}/xprintutil.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXprintUtil.a
