Summary: show a Windows Terminal Server desktop in X
Name: rdesktop
Version: 1.1.0
Release: 2
URL: http://www.rdesktop.org/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: openssl-devel

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 Terminal Services, capable of natively speaking Remote
Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --mandir=%{_mandir} --with-openssl
make

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/rdesktop

%changelog
* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 12 2002 Alexander Larsson <alexl@redhat.com>
- Initial build.

