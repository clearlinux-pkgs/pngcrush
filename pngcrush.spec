#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF54984BFA16C640F (glennrp+bmo@gmail.com)
#
Name     : pngcrush
Version  : 1.8.13.nolib
Release  : 2
URL      : https://sourceforge.net/projects/pmt/files/pngcrush/1.8.13/pngcrush-1.8.13-nolib.tar.gz
Source0  : https://sourceforge.net/projects/pmt/files/pngcrush/1.8.13/pngcrush-1.8.13-nolib.tar.gz
Source1  : https://sourceforge.net/projects/pmt/files/pngcrush/1.8.13/pngcrush-1.8.13-nolib.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause X11
Requires: pngcrush-bin = %{version}-%{release}
Requires: pngcrush-license = %{version}-%{release}
BuildRequires : libpng-dev
BuildRequires : zlib-dev

%description
No detailed description available

%package bin
Summary: bin components for the pngcrush package.
Group: Binaries
Requires: pngcrush-license = %{version}-%{release}

%description bin
bin components for the pngcrush package.


%package license
Summary: license components for the pngcrush package.
Group: Default

%description license
license components for the pngcrush package.


%prep
%setup -q -n pngcrush-1.8.13-nolib
cd %{_builddir}/pngcrush-1.8.13-nolib

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607058438
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1607058438
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pngcrush
cp %{_builddir}/pngcrush-1.8.13-nolib/LICENSE %{buildroot}/usr/share/package-licenses/pngcrush/9106998c011505151896c39baaeb740701c73d2d
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pngcrush

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pngcrush/9106998c011505151896c39baaeb740701c73d2d
