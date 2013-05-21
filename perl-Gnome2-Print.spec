%define	module	Gnome2-Print

Summary:	Perl module for the gnome print library
Name:		perl-%module
Version:	1.000
Release:	14
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	%{module}-%{version}.tar.bz2
URL:		http://gtk2-perl.sf.net/
BuildRequires:	pkgconfig(gtk+-2.0)
Buildrequires:	perl-ExtUtils-Depends 
Buildrequires:	perl-Gnome2 >= 0.30
Buildrequires:	perl-Glib > 1.00
Buildrequires:	perl-ExtUtils-PkgConfig
Buildrequires:	perl-devel
BuildRequires:	pkgconfig(libgnomeprintui-2.2)

%description
This module provides perl access to the libgnomeprint+-2.x library,
the Gnome Printing Architecture.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/*


%changelog
* Thu Feb 02 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 1.000-13
+ Revision: 770563
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.000-10
+ Revision: 702774
- rebuilt against libpng-1.5.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.000-9
+ Revision: 667182
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.000-8mdv2011.0
+ Revision: 564478
- rebuild for perl 5.12.1

* Tue Jul 20 2010 J√©r√¥me Quelin <jquelin@mandriva.org> 1.000-7mdv2011.0
+ Revision: 555877
- rebuild for perl 5.12

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.000-6mdv2010.1
+ Revision: 426450
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.000-5mdv2009.1
+ Revision: 351778
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.000-4mdv2009.0
+ Revision: 223774
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.000-3mdv2008.1
+ Revision: 152092
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 1.000-2mdv2008.0
+ Revision: 44610
- rebuild


* Thu Nov 23 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.000-1mdv2007.0
+ Revision: 86825
- Import perl-Gnome2-Print

* Thu Nov 23 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.000-1mdv2007.1
- new release

* Tue Oct 11 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.951-3mdk
- Fix previous mistake

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 0.951-2mdk
- fix buildrequires

* Thu Aug 25 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.951-1mdk
- new release

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.94-3mdk
- rebuild for new perl

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.94-2mdk
- rebuild for perl-5.8.5

* Wed Jul 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.94-1mdk
- new release

* Sat Apr 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.91-2mdk
- fix summary
- use %%makeinstall_std

* Sun Mar 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.91-1mdk
- new release

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.61-1mdk
- new release

