%global framework kbookmarks

Name:           kf5-%{framework}
Version: 5.55.0
Release: 1
Summary:        KDE Frameworks 5 Tier 3 addon for bookmarks manipulation

License:        LGPLv2+
URL:            https://cgit.kde.org/%{framework}.git

%global majmin %(echo %{version} | cut -d. -f1-2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcodecs-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       kf5-kwidgetsaddons-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang_kf5 kbookmarks5_qt


%ldconfig_scriptlets

%files -f kbookmarks5_qt.lang
%doc README.md
%license COPYING.LIB
%{_kf5_sysconfdir}/xdg/%{framework}.*
%{_kf5_libdir}/libKF5Bookmarks.so.*

%files devel
%{_kf5_includedir}/kbookmarks_version.h
%{_kf5_includedir}/KBookmarks/
%{_kf5_libdir}/libKF5Bookmarks.so
%{_kf5_libdir}/cmake/KF5Bookmarks/
%{_kf5_archdatadir}/mkspecs/modules/qt_KBookmarks.pri


%changelog
* Mon Aug 17 2020 yeqinglong <yeqinglong@uniontech.com> - 5.55.0-1
- Initial release for OpenEuler
