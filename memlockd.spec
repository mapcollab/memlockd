Summary: Memlockd is a daemon that locks files into memory
Name: memlockd
Version: 1.1
Release: 1
Group: System Environment/Daemons
URL: https://doc.coker.com.au/projects/memlockd/
Vendor: Russell Coker
License: GPLv3
Packager: Builder <builder@thales-ktw.site>
Source: %{name}-%{version}.tar.gz
%{?systemd_requires}
BuildRequires: systemd


%description
Memlockd is a daemon that locks files into memory. Then if a machine starts
paging heavily the chance of being able to login successfully is significantly
increased.
The default configuration will lock all the files needed for login to a Debian
GNU/Linux system via the console or via ssh.


%prep
%setup -q -n %{name}-%{version}

%build
make

%install
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_sysconfdir}/memlockd.d
install -m755 memlockd         %{buildroot}/%{_sbindir}
install -m644 memlockd.service %{buildroot}/%{_unitdir}
install -m644 memlockd.cfg     %{buildroot}/%{_sysconfdir}

%post
%systemd_post memlockd.service

%preun
%systemd_preun memlockd.service

%postun
%systemd_postun_with_restart memlockd.service

%files
%attr(0755,root,root) %{_sbindir}/*
%attr(0644,root,root) %{_unitdir}/*
%attr(0644,root,root) %{_sysconfdir}/*

%changelog
* Wed Sep 07 2016 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> 1.1-1
- new package built with tito

