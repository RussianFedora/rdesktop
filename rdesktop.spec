Summary: X client for remote desktop into Windows Terminal Server
Name: rdesktop
Version: 1.3.1
Release: 7
URL: http://www.rdesktop.org/
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-optflags.patch

## CVS backports or stuff that should be in the next version
Patch100: rdesktop-1.3.1-fi-keymap.patch
Patch101: rdesktop-1.3.1-fi-warning.patch
Patch102: rdesktop-1.3.1-xembed.patch

License: GPL
Group: User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: openssl-devel, XFree86-devel

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 & 2003 Terminal Services, capable of natively speaking 
Remote Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
%setup -q
%patch0 -p0

## CVS backports
%patch100 -p0
%patch101 -p2
%patch102 -p0

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
%doc COPYING doc/AUTHORS doc/ChangeLog doc/TODO doc/keymapping.txt
%{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/*

%changelog
* Wed Mar  2 2005 Mark McLoughlin <markmc@redhat.com> 1.3.1-7
- Rebuild with gcc4

* Thu Nov 18 2004 Than Ngo <than@redhat.com> 1.3.1-6
- add cvs patch to make krdc working again

* Thu Jul 08 2004 Warren Togami <wtogami@redhat.com>
- #127207 Finnish "fi" keymap fix
          "fi" ISO_Level3_Shift warning fix

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 23 2004 Ville Skyttä <ville.skytta at iki.fi> - 1.3.1-3
- Honor $RPM_OPT_FLAGS.
- Include ChangeLog and TODO in docs.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Warren Togami <wtogami@redhat.com> 1.3.1-1
- upgrade to 1.3.1

* Thu Jan 15 2004 Warren Togami <wtogami@redhat.com> 1.3.0-3
- upgrade to 1.3.0
- improve summary
- BuildPrereq -> BuildRequires, the former is deprecated
- Remove doc files that no longer exist
- Add missing XFree86-devel
- There was no -1 or -2.  Nothing to see here.  Move along.

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

