Summary: X client for remote desktop into Windows Terminal Server
Name: rdesktop
Version: 1.3.0
Release: 2
URL: http://www.rdesktop.org/
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: openssl-devel, XFree86-devel

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 Terminal Services, capable of natively speaking Remote
Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
%setup -q -n rdesktop

%build
# Not autoconf, percentconfigure won't work
./configure --prefix=%{_prefix} --bindir=%{_bindir} --mandir=%{_mandir} \
	--with-openssl
make LDFLAGS="-L/usr/X11R6/%{_lib} -lX11 -lcrypto" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=$RPM_BUILD_ROOT%{_prefix} BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING doc/AUTHORS doc/keymapping.txt
%{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/*

%changelog
* Thu Jan 15 2004 Warren Togami <wtogami@redhat.com> 1.3.0-2
- upgrade to 1.3.0
- improve summary
- BuildPrereq -> BuildRequires, the former is deprecated
- Remove doc files that no longer exist
- Add missing XFree86-devel
- There was no -1.  Nothing to see here.  Move along.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 10 2003 Alexander Larsson <alexl@redhat.com> 1.2.0-1
- 1.2.0, new stable release
- Removed now-upstream ssl patch

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 1.1.0-5
- work around now-private definition of BN_CTX

* Wed Dec 11 2002 Elliot Lee <sopwith@redhat.com> 1.1.0-4
- Fix multilib builds by passing LDLIBS on make command line
- Use _smp_mflags

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- rebuild in current tree

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 12 2002 Alexander Larsson <alexl@redhat.com>
- Initial build.

