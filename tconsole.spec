# Text console RPM spec
Name: tconsole
Version: 3.2
Release: 2%{dist}
Vendor: ClearFoundation
License: GPL
Group: System Environment/Daemons
Packager: ClearFoundation
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}
Requires: app-network-core
Requires: sudo
Summary: Text-based console tool
BuildRequires: autoconf >= 2.63
BuildRequires: automake
BuildRequires: libtool
BuildRequires: ncurses-devel

%description
Text-based console tool
Report bugs to: http://www.clearfoundation.com/docs/developer/bug_tracker/

# Build
%prep
%setup -q
./autogen.sh
%{configure}

%build
make %{?_smp_mflags}

# Install
%install
make install DESTDIR=$RPM_BUILD_ROOT

# Clean-up
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Files
%files
%defattr(-,root,root)
%{_bindir}/start-gconsole
%{_sbindir}/tc-yum
%{_sbindir}/tconsole

