#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4C09DD83CAAA50B2 (ajax@nwnk.net)
#
Name     : xf86-video-fbdev
Version  : 0.5.0
Release  : 703
URL      : https://www.x.org/releases/individual/driver/xf86-video-fbdev-0.5.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-fbdev-0.5.0.tar.gz
Source99 : https://www.x.org/releases/individual/driver/xf86-video-fbdev-0.5.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-fbdev-lib
Requires: xf86-video-fbdev-license
Requires: xf86-video-fbdev-man
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-fbdev - video driver for framebuffer device
Please submit bugs & patches to the Xorg bugzilla:

%package lib
Summary: lib components for the xf86-video-fbdev package.
Group: Libraries
Requires: xf86-video-fbdev-license

%description lib
lib components for the xf86-video-fbdev package.


%package license
Summary: license components for the xf86-video-fbdev package.
Group: Default

%description license
license components for the xf86-video-fbdev package.


%package man
Summary: man components for the xf86-video-fbdev package.
Group: Default

%description man
man components for the xf86-video-fbdev package.


%prep
%setup -q -n xf86-video-fbdev-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530822257
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1530822257
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xf86-video-fbdev
cp COPYING %{buildroot}/usr/share/doc/xf86-video-fbdev/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/fbdev_drv.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/xf86-video-fbdev/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man4/fbdev.4
