%define oname kactivities

Summary:	API for using and interacting with Activities
Name:		libkactivities
Version:	4.11.4
Release:	3
Epoch:		6
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/kde/kdelibs/kactivities
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{oname}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel >= 5:4.9.80
BuildRequires:	nepomuk-core-devel
BuildRequires:	soprano-devel

# libkactivities moved from kdelibs, but turns out there's no actual conflicts
# kactivitymanagerd moved here from kde-runtime
Conflicts:	kdebase4-runtime < 1:4.7.3-10

%description
API for using and interacting with Activities as a consumer,
application adding information to them or as an activity manager.

%files
%{_kde_bindir}/kactivitymanagerd
%{_kde_libdir}/kde4/activitymanager_plugin_activityranking.so
%{_kde_libdir}/kde4/activitymanager_plugin_globalshortcuts.so
%{_kde_libdir}/kde4/activitymanager_plugin_nepomuk.so
%{_kde_libdir}/kde4/activitymanager_plugin_slc.so
%{_kde_libdir}/kde4/activitymanager_plugin_sqlite.so
%{_kde_libdir}/kde4/activitymanager_plugin_virtualdesktopswitch.so
%{_kde_libdir}/kde4/kactivitymanagerd_fileitem_linking_plugin.so
%{_kde_libdir}/kde4/kio_activities.so
%{_kde_datadir}/kde4/services/activities.protocol
%{_kde_datadir}/kde4/services/activitymanager-plugin-activityranking.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-nepomuk.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-slc.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-sqlite.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-globalshortcuts.desktop
%{_kde_datadir}/kde4/services/kactivitymanagerd.desktop
%{_kde_datadir}/kde4/services/kactivitymanagerd_fileitem_linking_plugin.desktop
%{_kde_datadir}/kde4/services/activitymanager-plugin-virtualdesktopswitch.desktop
%{_kde_datadir}/kde4/services/kcm_activities.desktop
%{_kde_datadir}/kde4/servicetypes/activitymanager-plugin.desktop
%{_datadir}/ontology/kde/kao.*
%{_kde_libdir}/kde4/imports/org/kde/activities
%{_kde_libdir}/kde4/kcm_activities.so
%{_kde_appsdir}/activitymanager


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

%define libkactivities_models_major 1
%define libkactivities_models %mklibname kactivities-models %{libkactivities_models_major}

%package -n %{libkactivities_models}
Summary:	Runtime library for %{name}-models

%description -n %{libkactivities_models}
Library file needed by %{name}-models

%files -n %{libkactivities_models}
%{_kde_libdir}/libkactivities-models.so.%{libkactivities_models_major}*

#-----------------------------------------------------------------------

%package devel
Summary:	Developer files for %{name}
Requires:	kdelibs4-devel
Requires:	%{libkactivities} = %{EVRD}
Requires:	%{libkactivities_models} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description devel
%{summary}.

%files devel
%{_kde_libdir}/libkactivities.so
%{_kde_libdir}/libkactivities-models.so
%{_libdir}/cmake/KActivities
%{_libdir}/cmake/KActivities-Models
%{_libdir}/pkgconfig/*.pc
%{_kde_includedir}/KDE/KActivities
%{_kde_includedir}/kactivities
%{_kde_includedir}/kactivities-models

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

%changelog
* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.11.0-1
- New version 4.11.0
- Updates files list

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.9.1-1
- New version 4.9.1

* Fri Aug 03 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.8.97-1
- New version 4.8.97
- Update files

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.8.95-1
- Update to 4.8.95

* Tue Jun 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 6:4.8.90-1
- Update to 4.8.90
- Add cmake options
- Update file list

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 6:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 6:4.8.3-1
- update to 4.8.3

* Wed Apr 4 2012 Alex Burmashev <alex.burmashev@rosalab.ru>
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 6:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 6:4.8.0-1
+ Revision: 762433
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 6:4.7.97-1
+ Revision: 758048
- New upstream tarball

* Sun Jan 01 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 6:4.7.95-1
+ Revision: 748555
- New version
- New version

* Wed Dec 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 6:4.7.90-1
+ Revision: 740797
- Fix file list
- New version 4.7.90

* Sat Nov 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:6.1-4
+ Revision: 733487
- Fix conflicts

* Fri Nov 18 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:6.1-3
+ Revision: 731559
- Fix use of epoch in provides/requires

* Thu Nov 17 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:6.1-2
+ Revision: 731510
- Add a provide in the devel package

* Thu Nov 17 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 5:6.1-1
+ Revision: 731502
- Import libkactivities

