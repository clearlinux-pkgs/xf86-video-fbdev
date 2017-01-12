#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-video-fbdev
Version  : 0.4.4
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-0.4.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-0.4.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-fbdev-lib
Requires: xf86-video-fbdev-doc
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)

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
export CFLAGS="-O2 -g"
unset LDFLAGS
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
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
