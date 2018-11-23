#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Remove
Version  : 1.58
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Remove-1.58.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Remove-1.58.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-remove-perl/libfile-remove-perl_1.57-1.debian.tar.xz
Summary  : 'Remove files and directories'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Remove-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution File-Remove,
version 1.58:
Remove files and directories

%package dev
Summary: dev components for the perl-File-Remove package.
Group: Development
Provides: perl-File-Remove-devel = %{version}-%{release}

%description dev
dev components for the perl-File-Remove package.


%package license
Summary: license components for the perl-File-Remove package.
Group: Default

%description license
license components for the perl-File-Remove package.


%prep
%setup -q -n File-Remove-1.58
cd ..
%setup -q -T -D -n File-Remove-1.58 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Remove-1.58/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Remove
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Remove/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Remove/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/File/Remove.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Remove.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Remove/LICENSE
/usr/share/package-licenses/perl-File-Remove/deblicense_copyright
