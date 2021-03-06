#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipe
Version  : 7.2.23
Release  : 3
URL      : https://dl.bintray.com/otfried/generic/ipe/7.2/ipe-7.2.23-src.tar.gz
Source0  : https://dl.bintray.com/otfried/generic/ipe/7.2/ipe-7.2.23-src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: ipe-bin = %{version}-%{release}
Requires: ipe-data = %{version}-%{release}
Requires: ipe-lib = %{version}-%{release}
Requires: ipe-license = %{version}-%{release}
Requires: ipe-man = %{version}-%{release}
BuildRequires : gsl-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : lua-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libspiro)
BuildRequires : pkgconfig(zlib)

%description
Ipe 7.2.23
December, 2020
Ipe extensible drawing editor
=============================

%package bin
Summary: bin components for the ipe package.
Group: Binaries
Requires: ipe-data = %{version}-%{release}
Requires: ipe-license = %{version}-%{release}

%description bin
bin components for the ipe package.


%package data
Summary: data components for the ipe package.
Group: Data

%description data
data components for the ipe package.


%package dev
Summary: dev components for the ipe package.
Group: Development
Requires: ipe-lib = %{version}-%{release}
Requires: ipe-bin = %{version}-%{release}
Requires: ipe-data = %{version}-%{release}
Provides: ipe-devel = %{version}-%{release}
Requires: ipe = %{version}-%{release}

%description dev
dev components for the ipe package.


%package lib
Summary: lib components for the ipe package.
Group: Libraries
Requires: ipe-data = %{version}-%{release}
Requires: ipe-license = %{version}-%{release}

%description lib
lib components for the ipe package.


%package license
Summary: license components for the ipe package.
Group: Default

%description license
license components for the ipe package.


%package man
Summary: man components for the ipe package.
Group: Default

%description man
man components for the ipe package.


%prep
%setup -q -n ipe-7.2.23
cd %{_builddir}/ipe-7.2.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613763608
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
pushd src
make  %{?_smp_mflags}  IPEPREFIX=/usr IPELIBDIR=/usr/lib64 LUA_PACKAGE=lua
popd


%install
export SOURCE_DATE_EPOCH=1613763608
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipe
cp %{_builddir}/ipe-7.2.23/gpl.txt %{buildroot}/usr/share/package-licenses/ipe/8624bcdae55baeef00cd11d5dfcfa60f68710a02
pushd src
%make_install IPEPREFIX=/usr IPELIBDIR=/usr/lib64 LUA_PACKAGE=lua
popd

%files
%defattr(-,root,root,-)
/usr/lib/ipe/7.2.23/ipelets/align.lua
/usr/lib/ipe/7.2.23/ipelets/euclid.lua
/usr/lib/ipe/7.2.23/ipelets/goodies.lua
/usr/lib/ipe/7.2.23/ipelets/gridmaker.lua
/usr/lib/ipe/7.2.23/ipelets/move.lua
/usr/lib/ipe/7.2.23/ipelets/search-replace.lua
/usr/lib/ipe/7.2.23/ipelets/selectby.lua
/usr/lib/ipe/7.2.23/ipelets/symbols.lua

%files bin
%defattr(-,root,root,-)
/usr/bin/ipe
/usr/bin/ipe6upgrade
/usr/bin/ipecurl
/usr/bin/ipeextract
/usr/bin/ipepresenter
/usr/bin/iperender
/usr/bin/ipescript
/usr/bin/ipetoipe

%files data
%defattr(-,root,root,-)
/usr/share/ipe/7.2.23/doc/blank.png
/usr/share/ipe/7.2.23/doc/example1.svg
/usr/share/ipe/7.2.23/doc/example2.svg
/usr/share/ipe/7.2.23/doc/example3.svg
/usr/share/ipe/7.2.23/doc/example4.svg
/usr/share/ipe/7.2.23/doc/example5.svg
/usr/share/ipe/7.2.23/doc/example6.svg
/usr/share/ipe/7.2.23/doc/filming.html
/usr/share/ipe/7.2.23/doc/fontbbox.svg
/usr/share/ipe/7.2.23/doc/fontbbox2.svg
/usr/share/ipe/7.2.23/doc/intersection.svg
/usr/share/ipe/7.2.23/doc/ipe.dtd
/usr/share/ipe/7.2.23/doc/lingrad1.svg
/usr/share/ipe/7.2.23/doc/manual.css
/usr/share/ipe/7.2.23/doc/manual.html
/usr/share/ipe/7.2.23/doc/manual_1.html
/usr/share/ipe/7.2.23/doc/manual_10.html
/usr/share/ipe/7.2.23/doc/manual_11.html
/usr/share/ipe/7.2.23/doc/manual_12.html
/usr/share/ipe/7.2.23/doc/manual_13.html
/usr/share/ipe/7.2.23/doc/manual_14.html
/usr/share/ipe/7.2.23/doc/manual_15.html
/usr/share/ipe/7.2.23/doc/manual_16.html
/usr/share/ipe/7.2.23/doc/manual_17.html
/usr/share/ipe/7.2.23/doc/manual_18.html
/usr/share/ipe/7.2.23/doc/manual_19.html
/usr/share/ipe/7.2.23/doc/manual_2.html
/usr/share/ipe/7.2.23/doc/manual_20.html
/usr/share/ipe/7.2.23/doc/manual_21.html
/usr/share/ipe/7.2.23/doc/manual_22.html
/usr/share/ipe/7.2.23/doc/manual_23.html
/usr/share/ipe/7.2.23/doc/manual_24.html
/usr/share/ipe/7.2.23/doc/manual_25.html
/usr/share/ipe/7.2.23/doc/manual_26.html
/usr/share/ipe/7.2.23/doc/manual_27.html
/usr/share/ipe/7.2.23/doc/manual_3.html
/usr/share/ipe/7.2.23/doc/manual_30.html
/usr/share/ipe/7.2.23/doc/manual_31.html
/usr/share/ipe/7.2.23/doc/manual_32.html
/usr/share/ipe/7.2.23/doc/manual_33.html
/usr/share/ipe/7.2.23/doc/manual_35.html
/usr/share/ipe/7.2.23/doc/manual_36.html
/usr/share/ipe/7.2.23/doc/manual_37.html
/usr/share/ipe/7.2.23/doc/manual_38.html
/usr/share/ipe/7.2.23/doc/manual_4.html
/usr/share/ipe/7.2.23/doc/manual_40.html
/usr/share/ipe/7.2.23/doc/manual_42.html
/usr/share/ipe/7.2.23/doc/manual_43.html
/usr/share/ipe/7.2.23/doc/manual_44.html
/usr/share/ipe/7.2.23/doc/manual_45.html
/usr/share/ipe/7.2.23/doc/manual_47.html
/usr/share/ipe/7.2.23/doc/manual_48.html
/usr/share/ipe/7.2.23/doc/manual_49.html
/usr/share/ipe/7.2.23/doc/manual_5.html
/usr/share/ipe/7.2.23/doc/manual_50.html
/usr/share/ipe/7.2.23/doc/manual_51.html
/usr/share/ipe/7.2.23/doc/manual_53.html
/usr/share/ipe/7.2.23/doc/manual_55.html
/usr/share/ipe/7.2.23/doc/manual_56.html
/usr/share/ipe/7.2.23/doc/manual_58.html
/usr/share/ipe/7.2.23/doc/manual_59.html
/usr/share/ipe/7.2.23/doc/manual_6.html
/usr/share/ipe/7.2.23/doc/manual_60.html
/usr/share/ipe/7.2.23/doc/manual_62.html
/usr/share/ipe/7.2.23/doc/manual_63.html
/usr/share/ipe/7.2.23/doc/manual_64.html
/usr/share/ipe/7.2.23/doc/manual_65.html
/usr/share/ipe/7.2.23/doc/manual_66.html
/usr/share/ipe/7.2.23/doc/manual_67.html
/usr/share/ipe/7.2.23/doc/manual_68.html
/usr/share/ipe/7.2.23/doc/manual_69.html
/usr/share/ipe/7.2.23/doc/manual_7.html
/usr/share/ipe/7.2.23/doc/manual_70.html
/usr/share/ipe/7.2.23/doc/manual_71.html
/usr/share/ipe/7.2.23/doc/manual_73.html
/usr/share/ipe/7.2.23/doc/manual_74.html
/usr/share/ipe/7.2.23/doc/manual_8.html
/usr/share/ipe/7.2.23/doc/manual_9.html
/usr/share/ipe/7.2.23/doc/manual_customize.html
/usr/share/ipe/7.2.23/doc/manual_fileformat.html
/usr/share/ipe/7.2.23/doc/manual_ipe_copyright.html
/usr/share/ipe/7.2.23/doc/manual_ipestyle.html
/usr/share/ipe/7.2.23/doc/manual_makestyle.html
/usr/share/ipe/7.2.23/doc/manual_presentations.html
/usr/share/ipe/7.2.23/doc/manual_scripts.html
/usr/share/ipe/7.2.23/doc/manual_stylesheets.html
/usr/share/ipe/7.2.23/doc/manual_usb_stick.html
/usr/share/ipe/7.2.23/doc/manual_views.html
/usr/share/ipe/7.2.23/doc/next.png
/usr/share/ipe/7.2.23/doc/onepage.html
/usr/share/ipe/7.2.23/doc/onepage_2.html
/usr/share/ipe/7.2.23/doc/polygon.pdf
/usr/share/ipe/7.2.23/doc/previous.png
/usr/share/ipe/7.2.23/doc/radgrad1.svg
/usr/share/ipe/7.2.23/doc/radgrad2.svg
/usr/share/ipe/7.2.23/doc/snaplines.svg
/usr/share/ipe/7.2.23/doc/up.png
/usr/share/ipe/7.2.23/icons/icon_128x128.png
/usr/share/ipe/7.2.23/icons/icons.ipe
/usr/share/ipe/7.2.23/lua/actions.lua
/usr/share/ipe/7.2.23/lua/editpath.lua
/usr/share/ipe/7.2.23/lua/main.lua
/usr/share/ipe/7.2.23/lua/model.lua
/usr/share/ipe/7.2.23/lua/mouse.lua
/usr/share/ipe/7.2.23/lua/prefs.lua
/usr/share/ipe/7.2.23/lua/properties.lua
/usr/share/ipe/7.2.23/lua/shortcuts.lua
/usr/share/ipe/7.2.23/lua/tools.lua
/usr/share/ipe/7.2.23/scripts/add-style.lua
/usr/share/ipe/7.2.23/scripts/onepage.lua
/usr/share/ipe/7.2.23/scripts/page-labels.lua
/usr/share/ipe/7.2.23/scripts/update-master.lua
/usr/share/ipe/7.2.23/scripts/update-styles.lua
/usr/share/ipe/7.2.23/styles/arabic.isy
/usr/share/ipe/7.2.23/styles/basic.isy
/usr/share/ipe/7.2.23/styles/beamer.isy
/usr/share/ipe/7.2.23/styles/colors.isy
/usr/share/ipe/7.2.23/styles/decorations.isy
/usr/share/ipe/7.2.23/styles/imperial.isy
/usr/share/ipe/7.2.23/styles/note-paper.isy
/usr/share/ipe/7.2.23/styles/presentation.isy
/usr/share/ipe/7.2.23/styles/right-to-left.isy
/usr/share/ipe/7.2.23/styles/tikz-shapes.isy

%files dev
%defattr(-,root,root,-)
/usr/include/ipeattributes.h
/usr/include/ipebase.h
/usr/include/ipebitmap.h
/usr/include/ipecanvas.h
/usr/include/ipecanvas_cocoa.h
/usr/include/ipecanvas_gtk.h
/usr/include/ipecanvas_qt.h
/usr/include/ipecanvas_win.h
/usr/include/ipedoc.h
/usr/include/ipefactory.h
/usr/include/ipegeo.h
/usr/include/ipegroup.h
/usr/include/ipeimage.h
/usr/include/ipeiml.h
/usr/include/ipelatex.h
/usr/include/ipelet.h
/usr/include/ipelib.h
/usr/include/ipeobject.h
/usr/include/ipeosx.h
/usr/include/ipepage.h
/usr/include/ipepainter.h
/usr/include/ipepath.h
/usr/include/ipepdfparser.h
/usr/include/ipepdfview.h
/usr/include/ipepdfview_cocoa.h
/usr/include/ipepdfview_qt.h
/usr/include/ipepdfview_win.h
/usr/include/ipepdfwriter.h
/usr/include/ipepswriter.h
/usr/include/ipereference.h
/usr/include/iperesources.h
/usr/include/ipeselector_cocoa.h
/usr/include/ipeselector_qt.h
/usr/include/ipeshape.h
/usr/include/ipesnap.h
/usr/include/ipestyle.h
/usr/include/ipetext.h
/usr/include/ipetool.h
/usr/include/ipetoolbase.h
/usr/include/ipeutils.h
/usr/include/ipexml.h
/usr/lib64/libipe.so
/usr/lib64/libipecairo.so
/usr/lib64/libipecanvas.so
/usr/lib64/libipelua.so
/usr/lib64/libipeui.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libipe.so.7.2.23
/usr/lib64/libipecairo.so.7.2.23
/usr/lib64/libipecanvas.so.7.2.23
/usr/lib64/libipelua.so.7.2.23
/usr/lib64/libipeui.so.7.2.23

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipe/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ipe.1
/usr/share/man/man1/ipe6upgrade.1
/usr/share/man/man1/ipeextract.1
/usr/share/man/man1/iperender.1
/usr/share/man/man1/ipescript.1
/usr/share/man/man1/ipetoipe.1
