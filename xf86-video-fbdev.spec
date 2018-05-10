#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-video-fbdev
Version  : 0.4.4
Release  : 15
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-0.4.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-0.4.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-fbdev-lib
Requires: xf86-video-fbdev-doc
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-fbdev - video driver for framebuffer device
Please submit bugs & patches to the Xorg bugzilla:

%package doc
Summary: doc components for the xf86-video-fbdev package.
Group: Documentation

%description doc
doc components for the xf86-video-fbdev package.


%package lib
Summary: lib components for the xf86-video-fbdev package.
Group: Libraries

%description lib
lib components for the xf86-video-fbdev package.


%prep
%setup -q -n xf86-video-fbdev-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507171664
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507171664
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/fbdev_drv.so
