# Text console RPM spec
Name: tconsole
Version: 3.3
Release: 9%{dist}
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
%if "0%{dist}" == "0.v7"
%{?systemd_requires}
BuildRequires: systemd
%endif

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
install -D -m 644 deploy/gconsole.service %{buildroot}/%{_unitdir}/gconsole.service

# Clean-up
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Post install
%post
%if "0%{dist}" == "0.v7"
%systemd_post gconsole.service
%endif

# Pre uninstall
%preun
%if "0%{dist}" == "0.v7"
%systemd_preun gconsole.service
%endif

# Post uninstall
%postun
%if "0%{dist}" == "0.v7"
%systemd_postun_with_restart gconsole.service
%endif

# Files
%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/start-gconsole
%{_sbindir}/tc-yum
%{_sbindir}/tconsole
%if "0%{dist}" == "0.v7"
%attr(644,root,root) %{_unitdir}/gconsole.service
%endif
