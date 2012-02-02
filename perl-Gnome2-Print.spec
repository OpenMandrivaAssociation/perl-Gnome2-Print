%define	module	Gnome2-Print

Summary:	Perl module for the gnome print library
Name:		perl-%module
Version:	1.000
Release:	13
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
