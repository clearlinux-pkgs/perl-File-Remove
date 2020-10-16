#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Remove
Version  : 1.59
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Remove-1.59.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Remove-1.59.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-remove-perl/libfile-remove-perl_1.57-1.debian.tar.xz
Summary  : 'Remove files and directories'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Remove-license = %{version}-%{release}
Requires: perl-File-Remove-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution File-Remove,
version 1.59:
Remove files and directories

%package dev
Summary: dev components for the perl-File-Remove package.
Group: Development
Provides: perl-File-Remove-devel = %{version}-%{release}
Requires: perl-File-Remove = %{version}-%{release}

%description dev
dev components for the perl-File-Remove package.


%package license
Summary: license components for the perl-File-Remove package.
Group: Default

%description license
license components for the perl-File-Remove package.


%package perl
Summary: perl components for the perl-File-Remove package.
Group: Default
Requires: perl-File-Remove = %{version}-%{release}

%description perl
perl components for the perl-File-Remove package.


%prep
%setup -q -n File-Remove-1.59
cd %{_builddir}
tar xf %{_sourcedir}/libfile-remove-perl_1.57-1.debian.tar.xz
cd %{_builddir}/File-Remove-1.59
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Remove-1.59/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Remove
cp %{_builddir}/File-Remove-1.59/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Remove/c01411e4535ce0aea0deda74411ac0f2f5158bcd
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Remove/f426ec8af368f27f7a70de9c09e25b81dae8d8ac
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Remove.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Remove/c01411e4535ce0aea0deda74411ac0f2f5158bcd
/usr/share/package-licenses/perl-File-Remove/f426ec8af368f27f7a70de9c09e25b81dae8d8ac

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/File/Remove.pm
