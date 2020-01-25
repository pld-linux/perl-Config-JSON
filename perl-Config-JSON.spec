#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Config
%define		pnam	JSON
Summary:	Config::JSON - a JSON based config file system
Name:		perl-Config-JSON
Version:	1.5100
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26918705ca68a635d391e4d809a78e3b
URL:		http://search.cpan.org/dist/Config-JSON/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Any-Moose >= 0.13
BuildRequires:	perl-JSON >= 2.16
BuildRequires:	perl-Test-Deep >= 0.095
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package parses the config files written in JSON. It also does
some non-JSON stuff, like allowing for comments in the files.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Config/JSON.pm
%{_mandir}/man3/*
