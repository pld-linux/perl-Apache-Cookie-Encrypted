#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	CookieEncrypted
Summary:	Apache::Cookie::Encrypted - encrypted HTTP cookies class
Summary(pl):	Apache::Cookie::Encrypted - klasa szyfrowanych ,,cookie'' HTTP
Name:		perl-Apache-Cookie-Encrypted
Version:	0.03
Release:	5
# same as Apache::Cookie or perl
License:	GPL v1+ or Artistic or Apache Software License 1.1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	d8dac472f79ccfc33418423137f1d4bb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Crypt-Blowfish >= 2.06
BuildRequires:	perl-Crypt-CBC >= 1.25
BuildRequires:	perl-libapreq >= 0.01
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Crypt::Blowfish) >= 2.06
Requires:	perl(Crypt::CBC)      >= 1.25
Requires:	perl(Apache::Cookie)  >= 0.01
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Cookie::Encrypted is a subclass of Apache::Cookie. It takes
the value you put in to the cookie and automaticaly encrypts it. It
automaticaly decrypts it when the value is retrieved. Other than that
it behaves just like Apache::Cookie.

%description -l pl
Apache::Cookie::Encrypted jest podklas± Apache::Cookie. Ka¿da warto¶æ,
zapisywana w ,,cookie'' jest automatycznie szyfrowana przy wysy³aniu i
rezszyfrowywana po otrzymaniu; poza tym modu³ zachowuje siê tak samo,
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
