# Text console RPM spec
Name: tconsole
Version: 3.3
Release: 5%{dist}
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
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: ncurses-devel

%description
Text-based console tool
Report bugs to: http://www.clearfoundation.com/docs/developer/bug_tracker/

# Build
%prep
%setup -q
./autogen.sh
CXXFLAGS="${CXXFLAGS:-%optflags -Wno-unused-result}"; export CXXFLAGS;
%{configure}

%build
make %{?_smp_mflags}

# Install
%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# Clean-up
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Files
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/start-gconsole
%{_sbindir}/tc-yum
%{_sbindir}/tconsole

