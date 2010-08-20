Name:           rdesktop
Version:        1.6.0
Release:        8%{?dist}
Summary:        X client for remote desktop into Windows Terminal Server

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.rdesktop.org/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  openssl-devel, libX11-devel, pcsc-lite-devel

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 & 2003 Terminal Services, capable of natively speaking 
Remote Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
%setup -q

%build
%configure --with-ipv6 --enable-smartcard
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT STRIP=/bin/true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README doc/{AUTHORS,ChangeLog,HACKING,TODO,*.txt}
%{_bindir}/rdesktop
%{_datadir}/rdesktop/
%{_mandir}/man1/*

%changelog
* Fri Aug 20 2010 Dominik Mierzejewski <rpm@greysector.net> - 1.6.0-8
- drop hard dependency on pcsc-lite (bug #527712)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.0-7
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 1 2009 Soren Sandmann <ssp@redhat.com> - 1.6.0-5
- Enable SmartCard support

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 1.6.0-3
- rebuild with new openssl

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-2
- fix license tag

* Tue May 13 2008 Soren Sandmann <sandmann@redhat.com> - 1.6.0-1
Update to 1.6.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-5
- Autorebuild for GCC 4.3

* Tue Dec  4 2007 Matthias Clasen <mclasen@redhat.com> - 1.5.0-4
- Rebuild against openssl

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.5.0-4
- Rebuild for selinux ppc32 issue.

* Sat Jul 28 2007 Matthias Clasen <mclasen@redhat.com> - 1.5.0-3
- Produce useful debuginfo (#249962)

* Thu Apr 26 2007 David Zeuthen <davidz@redhat.com> - 1.5.0-2
- Fix segfault triggered by X11 update (#238032)

* Sun Nov 19 2006 Matthias Clasen <mclasen@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Thu Aug 31 2006 Behdad Esfahbod <besfahbo@redhat.com> - 1.4.1-4
- configure --with-ipv6 (bug 198405)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.4.1-3.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.4.1-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.4.1-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> - 1.4.1-3
- rebuilt against new openssl

* Tue Nov  1 2005 Carl Worth <cworth@redhat.com> - 1.4.1-2
- Require modular libX11-devel instead of monolithic xorg-x11-devel

* Thu Jun 30 2005 Warren Togami <wtogami@redhat.com> - 1.4.1-1
- 1.4.1

* Sat Mar 26 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.0-2
- Use the %%configure macro (rdesktop now has a real configure file).
- Patch rdesktop-optflags.patch no longer needed.
- Add several missing doc files.

* Mon Mar 21 2005 David Zeuthen <davidz@redhat.com> 1.4.0-1
- New upstream version; drop some patches that is now upstream
- Require xorg-x11-devel instead of XFree86-devel for building

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

