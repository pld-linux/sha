Summary:	File hashing utility
Name:		sha
# Upstream will continue in the next version
# with the behavior of shared libraries (specifically version 1.2)
Version:	1.0.4b
Release:	1
License:	BSD
Group:		Applications/File
Source0:	http://www.saddi.com/software/sha/dist/%{name}-%{version}.tar.gz
# Source0-md5:	acd674e4d518c7f67549f177264c8675
URL:		http://hg.saddi.com/sha-asaddi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
file hashing utility that uses the SHA-1, SHA-256, SHA-384, & SHA-512
hash algorithms. It can be used for file integrity checking, remote
file comparisons, etc. The portable algorithm implementations can be
useful in other projects too

%package devel
Summary:	Development files for sha
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the libraries needed to develop applications
that use sha

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	CP="cp -p" \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la

install -d $RPM_BUILD_ROOT%{_includedir}/sha
cp -a *.h $RPM_BUILD_ROOT%{_includedir}/sha

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README README.SHA ChangeLog
%attr(755,root,root) %{_bindir}/sha
%{_mandir}/man1/sha.1*
%attr(755,root,root) %{_libdir}/libsha.so.*.*.*
%ghost %{_libdir}/libsha.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/sha
%{_libdir}/libsha.so
