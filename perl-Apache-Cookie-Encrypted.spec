%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	CookieEncrypted
Summary:	Apache::Cookie::Encrypted perl module
Summary(cs):	Modul Apache::Cookie::Encrypted pro Perl
Summary(da):	Perlmodul Apache::Cookie::Encrypted
Summary(de):	Apache::Cookie::Encrypted Perl Modul
Summary(es):	Módulo de Perl Apache::Cookie::Encrypted
Summary(fr):	Module Perl Apache::Cookie::Encrypted
Summary(it):	Modulo di Perl Apache::Cookie::Encrypted
Summary(ja):	Apache::Cookie::Encrypted Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Apache::Cookie::Encrypted ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Apache::Cookie::Encrypted
Summary(pl):	Modu³ perla Apache::Cookie::Encrypted
Summary(pt_BR):	Módulo Perl Apache::Cookie::Encrypted
Summary(pt):	Módulo de Perl Apache::Cookie::Encrypted
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Apache::Cookie::Encrypted
Summary(sv):	Apache::Cookie::Encrypted Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Apache::Cookie::Encrypted
Summary(zh_CN):	Apache::Cookie::Encrypted Perl Ä£¿é
Name:		perl-Apache-Cookie-Encrypted
Version:	0.03
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	d8dac472f79ccfc33418423137f1d4bb
BuildRequires:	perl-devel >= 5
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
deszyfrowana po otrzymaniu; poza tym modu³ zachowuje siê tak samo, jak
Apache::Cookie.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
echo '!' | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Apache/Cookie
%{perl_vendorlib}/Apache/Cookie/Encrypted.pm
%{_mandir}/man3/*
