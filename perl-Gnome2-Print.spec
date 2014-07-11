%define	module	Gnome2-Print

Summary:	Perl module for the gnome print library
Name:		perl-%module
Version:	1.000
Release:	20
License:	GPLv2 or Artistic
Group:		Development/GNOME and GTK+
Source0:	%{module}-%{version}.tar.bz2
Url:		http://gtk2-perl.sf.net/
Buildrequires:	perl-ExtUtils-Depends 
Buildrequires:	perl-Gnome2 >= 0.30
Buildrequires:	perl-Glib > 1.00
Buildrequires:	perl-ExtUtils-PkgConfig
Buildrequires:	perl-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)

%description
This module provides perl access to the libgnomeprint+-2.x library,
the Gnome Printing Architecture.

%prep
%setup -qn %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc examples
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/*
%{_mandir}/man3/*

