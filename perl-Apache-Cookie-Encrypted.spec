#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Apache
%define		pnam	CookieEncrypted
Summary:	Apache::Cookie::Encrypted - encrypted HTTP cookies class
Summary(pl.UTF-8):	Apache::Cookie::Encrypted - klasa szyfrowanych ,,cookie'' HTTP
Name:		perl-Apache-Cookie-Encrypted
Version:	0.03
Release:	5
# same as Apache::Cookie or perl
License:	GPL v1+ or Artistic or Apache Software License 1.1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	d8dac472f79ccfc33418423137f1d4bb
URL:		http://search.cpan.org/dist/Apache-CookieEncrypted/
BuildRequires:	perl-Crypt-Blowfish >= 2.06
BuildRequires:	perl-Crypt-CBC >= 1.25
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libapreq >= 0.01
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Apache::Cookie) >= 0.01
Requires:	perl(Crypt::Blowfish) >= 2.06
Requires:	perl(Crypt::CBC) >= 1.25
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Cookie::Encrypted is a subclass of Apache::Cookie. It takes
the value you put in to the cookie and automaticaly encrypts it. It
automaticaly decrypts it when the value is retrieved. Other than that
it behaves just like Apache::Cookie.

%description -l pl.UTF-8
Apache::Cookie::Encrypted jest podklasą Apache::Cookie. Każda wartość,
zapisywana w ,,cookie'' jest automatycznie szyfrowana przy wysyłaniu i
rezszyfrowywana po otrzymaniu; poza tym moduł zachowuje się tak samo,
jak Apache::Cookie.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
echo '!' | perl Makefile.PL \
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
%dir %{perl_vendorlib}/Apache/Cookie
%{perl_vendorlib}/Apache/Cookie/Encrypted.pm
%{_mandir}/man3/*
