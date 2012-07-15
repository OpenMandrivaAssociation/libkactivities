%define oname kactivities

Name:		lib%{oname}
Summary:	API for using and interacting with Activities
Version:	4.8.97
Release:	1
Epoch:		6
License:	GPLv2+ and LGPLv2+
URL:		https://projects.kde.org/projects/kde/kdelibs/kactivities
Source0:	ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/%{oname}-%{version}.tar.xz
Group:		System/Libraries
BuildRequires:	kdelibs4-devel >= 5:4.8.80

# libkactivities moved from kdelibs, but turns out there's no actual conflicts
# kactivitymanagerd moved here from kde-runtime
Conflicts:	kdebase4-runtime < 1:4.7.3-10

%description
API for using and interacting with Activities as a consumer,
application adding information to them or as an activity manager.

%files
%{_kde_bindir}/kactivitymanagerd
%{_kde_libdir}/kde4/activitymanager_plugin_dummy.so
%{_kde_libdir}/kde4/activitymanager_plugin_globalshortcuts.so
%{_kde_libdir}/kde4/activitymanager_plugin_nepomuk.so
%{_kde_libdir}/kde4/activitymanager_plugin_slc.so
%{_kde_libdir}/kde4/activitymanager_plugin_sqlite.so
%{_kde_libdir}/kde4/activitymanager_uihandler_declarative.so
%{_kde_libdir}/kde4/activitymanager_uihandler_kdialog.so
%{_kde_libdir}/kde4/kactivitymanagerd_fileitem_linking_plugin.so
%{_kde_libdir}/kde4/kio_activities.so
%{_kde_datadir}/kde4/services/activities.protocol
%{_kde_datadir}/kde4/services/activitymanager-plugin-dummy.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-sqlite.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-globalshortcuts.desktop
%{_kde_datadir}/kde4/services/kactivitymanagerd.desktop
%{_kde_datadir}/kde4/services/kactivitymanagerd_fileitem_linking_plugin.desktop
%{_kde_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%{_kde_appsdir}/plasma/packages/org.kde.ActivityManager.UiHandler
%{_datadir}/ontology/kde/kao.*

#-----------------------------------------------------------------------

%define libkactivities_major 6
%define libkactivities %mklibname kactivities %{libkactivities_major}

%package -n %{libkactivities}
Summary:	Runtime library for %{name}

%description -n %{libkactivities}
Library file needed by %{name}

%files -n %{libkactivities}
%{_kde_libdir}/libkactivities.so.%{libkactivities_major}*

#-----------------------------------------------------------------------

%package devel
Summary:	Developer files for %{name}
Requires:	kdelibs4-devel
Requires:	%{libkactivities} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description devel
%{summary}.

%files devel
%{_kde_libdir}/libkactivities.so
%{_libdir}/cmake/KActivities
%{_libdir}/pkgconfig/libkactivities.pc
%{_kde_includedir}/KDE/KActivities
%{_kde_includedir}/kactivities

#-----------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}

%build
%cmake_kde4 \
	-DKACTIVITIES_BUILD_NEPOMUK_PLUGIN:bool=ON \
	-DKACTIVITIES_BUILD_DUMMY_PLUGIN:bool=ON
%make

%install
%makeinstall_std -C build

