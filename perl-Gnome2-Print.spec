%define module Gnome2-Print

Summary: Perl module for the gnome print library
Name:    perl-%module
Version: 1.000
Release: %mkrel 10
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk+2-devel 
Buildrequires: perl-ExtUtils-Depends 
Buildrequires: perl-Gnome2 >= 0.30
Buildrequires: perl-Glib > 1.00
Buildrequires: perl-ExtUtils-PkgConfig
Buildrequires: perl-devel
BuildRequires: libgnomeprintui-devel >= 2.2
Requires: gtk+2 

%description
This module provides perl access to the libgnomeprint+-2.x library,
the Gnome Printing Architecture.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/*


