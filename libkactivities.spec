%define  oname kactivities
Name:    lib%oname
Summary: API for using and interacting with Activities 
Version: 4.7.90
Release: 1
Epoch:   6
License: GPLv2+ and LGPLv2+
URL:     https://projects.kde.org/projects/kde/kdelibs/kactivities 
Source0: ftp://ftp.kde.org/pub/kde/stable/active/1.0/src/%oname-%{version}.tar.bz2
Group:   System/Libraries
BuildRequires: kdelibs4-devel >= 5:4.7 

# libkactivities moved from kdelibs, but turns out there's no actual conflicts
# kactivitymanagerd moved here from kde-runtime 
Conflicts: kdebase4-runtime < 1:4.7.3-10

%description
API for using and interacting with Activities as a consumer, 
application adding information to them or as an activity manager.

%files
%{_kde_bindir}/kactivitymanagerd
%{_kde_libdir}/kde4/activitymanager_plugin_dummy.so
%{_kde_libdir}/kde4/activitymanager_plugin_nepomuk.so
%{_kde_libdir}/kde4/activitymanager_plugin_slc.so
%{_kde_datadir}/kde4/services/activitymanager-plugin-dummy.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_kde_datadir}/kde4/services/kactivitymanagerd.desktop
%{_kde_datadir}/kde4/services/kded/activitymanager.desktop
%{_kde_datadir}/kde4/servicetypes/activitymanager-plugin.desktop

#-----------------------------------------------------------------------

%define libkactivities_major 6
%define libkactivities %mklibname kactivities %libkactivities_major

%package -n %libkactivities
Summary: Runtime library for %{name}

%description -n %libkactivities
Librairie File needed by %name

%files -n %libkactivities
%{_kde_libdir}/libkactivities.so.%{libkactivities_major}*

#-----------------------------------------------------------------------

%package  devel
Summary:  Developer files for %{name}
Requires: kdelibs4-devel
Requires: %libkactivities = %EVRD
Provides: %name-devel = %EVRD

%description devel
%{summary}.

%files devel
%{_kde_libdir}/libkactivities.so
%{_libdir}/cmake/KActivities
%{_libdir}/pkgconfig/libkactivities.pc
%{_kde_includedir}/KDE/Activities
%{_kde_includedir}/kactivities

#-----------------------------------------------------------------------

%prep
%setup -q -n %oname-%version

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build
