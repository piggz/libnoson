 
#
# spec file for package noson
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libnoson
Version:        1.16.2
Release:        0
Summary:        C++ library for accessing sonos devices
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/janbar/noson/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  zlib-devel

%description
C++ library for accessing sonos devices
The API supports basic features to browse music index and control playback
in any zones.

%package -n libnoson1
Summary:        C++ library for accessing sonos devices
Group:          System/Libraries

%description -n libnoson1
C++ library for accessing sonos devices
The API supports basic features to browse music index and control playback
in any zones.

%package devel
Summary:        Development files for noson library
Group:          Development/Libraries/C and C++
Requires:       libnoson1 = %{version}

%description devel
Development files for noson library. The noson library supports basic features
to browse music index and control playback in any zones.

%prep
%setup -q -n %{name}-%{version}/noson

%build
  %cmake \
    -DCMAKE_INSTALL_FULL_LIBDIR=%{_libdir}
  make

%install
  %make_install -C build

%post -n libnoson1 -p /sbin/ldconfig
%postun -n libnoson1 -p /sbin/ldconfig

%files -n libnoson1
%{_libdir}/libnoson.so.*

%files devel
%{_includedir}/noson
%{_libdir}/pkgconfig/noson.pc
%{_libdir}/cmake/noson/
%{_libdir}/libnoson.so

%changelog