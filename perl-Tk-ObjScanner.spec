%define upstream_name       Tk-ObjScanner
%define upstream_version    2.012

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Tk data or object scanner
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::Adjuster)
BuildRequires: perl(Tk::HList)
BuildRequires: perl(Tk::ROText)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The scanner provides a GUI to scan the attributes of an object. It can also
be used to scan the elements of a hash or an array.

This widget can be used as a regular widget in a Tk application or can be
used as an autonomous popup widget that will display the content of a data
structure. The latter is like a call to a graphical the Data::Dumper
manpage. The scanner can be used in an autonomous way with the
'scan_object' function.

The scanner is a composite widget made of a menubar and the Tk::HList
manpage. This widget acts as a scanner to the object (or hash ref) passed
with the 'caller' parameter. The scanner will retrieve all keys of the
hash/object and insert them in the HList.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*


