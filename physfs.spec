Name:           physfs
Version:        3.0.1
Release:        4
License:        zlib
Summary:        Provide abstract access to various archives
URL:            http://www.icculus.org/physfs/
Source0:        http://www.icculus.org/physfs/downloads/physfs-%{version}.tar.bz2
BuildRequires:  gcc-c++ doxygen readline-devel libtool cmake
Provides:       bundled(lzma-sdk457)

%description
PhysicsFS is a library to provide abstract access to various archives.
It is intended for use in video games, and the design was somewhat inspired by Quake 3's file subsystem.

%package devel
Summary:        Libraries and headers for physfs
Requires:       physfs = %{version}-%{release}

%description devel
The package contains the libraries and headers necessary for physfs's function

%package_help

%prep
%autosetup -p1

%build
%cmake .
%make_build LIBTOOL=%{_bindir}/libtool
doxygen

%install
%make_install
%delete_la
install -d $RPM_BUILD_ROOT%{_mandir}/man3
install -m 0644 docs/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

for i in author description extension major minor patch url remove Deinit Free Init Malloc Realloc opaque; do
  mv $RPM_BUILD_ROOT%{_mandir}/man3/$i.3 $RPM_BUILD_ROOT%{_mandir}/man3/physfs-$i.3
done

touch -r LICENSE.txt docs/html/*
touch -r LICENSE.txt docs/latex/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc docs/CHANGELOG.txt docs/CREDITS.txt LICENSE.txt
%{_libdir}/*.so.*

%files devel
%exclude %{_libdir}/*.a
%{_bindir}/test_physfs
%{_includedir}/physfs.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/physfs.pc

%files help
%doc docs/TODO.txt docs/html/
%{_mandir}/man3/*


%changelog
* Fri Nov 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.0.1-4
- Package init
