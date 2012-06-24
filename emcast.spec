Summary:	Generic multicast utility
Summary(pl.UTF-8):	Wszechstronne narzędzia do multicastów
Name:		emcast
Version:	0.3.2
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.junglemonkey.net/emcast/src/%{name}-%{version}.tar.gz
# Source0-md5:	1031642c4f0e13a1c51d38ae7dcf7c93
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnet-devel >= 1.1.0
URL:		http://www.junglemonkey.net/emcast/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Emcast is a multicast toolkit for distributed/peer-to-peer
applications that require multicast communication. It includes the
program emcast, a generic multicast utility (like netcat), and the
library libemcast, a generic multicast library. Emcast supports IPv4
multicast (IM) and can easily support almost any end-host multicast
(EM) protocol. The EM protocols supported are Banana Tree Protocol
(BTP), Internet Relay Chat (IRC), and STAR (centralized TCP).

Emcast is pronounced em-cast.

%description -l pl.UTF-8
Emcast jest zestawem narzędzi do obsługi multicastów dla aplikacji
rozproszonych/p2p, które wymagają komunikacji multicastowej. Zawiera
program emcast - wszechstronne narzędzie do obsługi multicastów (jak
netcat), oraz bibliotekę libemcast - ogólną bibliotekę do multicastów.
Emcast obsługuje multicasty IPv4 (IM) i może łatwo obsłużyć prawie
dowolny protokół końcowego hosta (EM). Obsługiwane protokoły EM to
Banana Tree Protocol (BTP), Internet Relay Chat (IRC) i STAR
(scentralizowany TCP).

%package libs
Summary:	emcast library
Summary(pl.UTF-8):	Biblioteka emcast
Group:		Libraries

%description libs
Generic multicast library.

%description libs -l pl.UTF-8
Biblioteka do obsługi multicastów.

%package devel
Summary:	emcast header files
Summary(pl.UTF-8):	Pliki nagłówkowe emcast
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
emcast header files

%description devel -l pl.UTF-8
Pliki nagłówkowe emcast

%package static
Summary:	emcast static library
Summary(pl.UTF-8):	Statyczna biblioteka emcast
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
emcast static library.

%description static -l pl.UTF-8
Statyczna biblioteka emcast.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/%{name}-config

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc HACKING doc/*.txt
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/%{name}
%{_includedir}/btp
%{_libdir}/%{name}
%{_mandir}/man1/%{name}-config.1*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
