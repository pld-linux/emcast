Summary:	Generic multicast utility
Summary(pl):	Wszechstronne narz�dzia do multicast�w
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

%description -l pl
Emcast jest zestawem narz�dzi do obs�ugi multicast�w dla aplikacji
rozproszonych/p2p, kt�re wymagaj� komunikacji multicastowej. Zawiera
program emcast - wszechstronne narz�dzie do obs�ugi multicast�w (jak
netcat), oraz bibliotek� libemcast - og�ln� bibliotek� do multicast�w.
Emcast obs�uguje multicasty IPv4 (IM) i mo�e �atwo obs�u�y� prawie
dowolny protok� ko�cowego hosta (EM). Obs�ugiwane protoko�y EM to
Banana Tree Protocol (BTP), Internet Relay Chat (IRC) i STAR
(scentralizowany TCP).

%package libs
Summary:	emcast library
Summary(pl):	Biblioteka emcast
Group:		Libraries

%description libs
Generic multicast library.

%description libs -l pl
Biblioteka do obs�ugi multicast�w.

%package devel
Summary:	emcast header files
Summary(pl):	Pliki nag��wkowe emcast
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
emcast header files

%description devel -l pl
Pliki nag��wkowe emcast

%package static
Summary:	emcast static library
Summary(pl):	Statyczna biblioteka emcast
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
emcast static library.

%description static -l pl
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
%attr(755,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/%{name}
%{_includedir}/btp
%{_libdir}/%{name}
%{_mandir}/man1/%{name}-config.1*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
