%define sonum  1
%define lname   libvmaf%sonum

# undefined reference to `vmaf_cpu_cpuid'
%define _lto_cflags %nil
Name:           vmaf
Version:        2.2.0
Release:        1
Summary:        Perceptual video quality assessment algorithm
License:        BSD-2-Clause-Patent AND BSD-3-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/Netflix/vmaf
Source:         https://github.com/Netflix/vmaf/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes

BuildRequires:  meson >= 0.47
BuildRequires:  nasm
BuildRequires:  pkgconfig
Provides:       bundled(libsvm) = 3.18

%description
VMAF is a perceptual video quality assessment algorithm.

%package -n %lname
Summary:        Perceptual video quality assessment algorithm
Group:          System/Libraries
Recommends:     %name-data

%description -n %lname
VMAF is a perceptual video quality assessment algorithm.

%package devel
Summary:        Development tools for Video Multi-Method Assessment Fusion
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
VMAF is a perceptual video quality assessment algorithm developed by
Netflix.
This package contains the library API definitions.

%prep
%autosetup

%build
rm -rf third_party
pushd libvmaf/
%meson
%meson_build
popd

%install
pushd libvmaf/
%meson_install
popd
rm -f "%buildroot/%_libdir"/*.a
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libvmaf.so.%{sonum}*

%files devel
%_bindir/vmaf*
%_includedir/libvmaf/
%_libdir/libvmaf.so
%_libdir/pkgconfig/*.pc
%license LICENSE
%doc FAQ.md README.md
