%define name	plasma-applet-kbirthdayreminder
%define srcname birthday-plasmoid
%define version	 0.9.73
%define release	4
%define Summary	 A reminder for birthdays and anniversaries


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://kde-look.org/CONTENT/content-files/91641-%srcname-%version.tar.bz2
Patch0:		plasma-applet-kbirthdayreminder-0.9.73-mdv-fix-icon-and-category.patch
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://kde-look.org/content/show.php/K+Birthday+Reminder?content=91641
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdepimlibs4-devel
Requires:	kdebase4-runtime => 4.3
Requires:	plasma-dataengine-kbirthdayreminder
Provides:	plasma-applet


%description
Plasmoid reminds you of birthdays and anniversaries of contacts[¹] in the
(standard) KDE address book.
Inspired by the KDE3 kicker applet KBirthday from Jan Hambrecht.
As the version number indicates, the plasmoid isn't quite ready yet. Also there
are a few issues I know of. You will find the list in the TODO file.
The popup displayed when clicking on the plasmoid's icon is supposed to show
only when living in a panel. This popup dialog is not ready yet!
Hope you will enjoy using it anyway.


%files  -f plasma_applet_kbirthdayapplet.lang
%defattr(-,root,root)
%doc	ChangeLog LICENSE.GPL README
%_kde_libdir/kde4/plasma_applet_kbirthdayapplet.so
%_kde_services/plasma-applet-kbirthday.desktop
%_kde_datadir/apps/desktoptheme/default/widgets/birthdaycake.svg
%_iconsdir/hicolor/scalable/apps/birthdaycake.svgz

#-----------------------------------------------------------------------
%package -n plasma-dataengine-kbirthdayreminder
Summary:	Data engine for %{name}
Group:		Graphical desktop/KDE
%description -n plasma-dataengine-kbirthdayreminder
This package provides the dataengine for %{name}

%files -n plasma-dataengine-kbirthdayreminder
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_engine_kabc.so
%_kde_services/plasma-dataengine-kabc.desktop

#-----------------------------------------------------------------------

%prep
%setup -q -n KBirthdayPlasma_0_9_73
%patch0 -p 0

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang plasma_applet_kbirthdayapplet

%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 30 2010 John Balcaen <mikala@mandriva.org> 0.9.73-3mdv2011.0
+ Revision: 563774
- Add a plasma-dataengine subpackage
- add description on patch0

* Fri Apr 23 2010 John Balcaen <mikala@mandriva.org> 0.9.73-2mdv2010.1
+ Revision: 538387
- Add a patch to fix icon & category

* Mon Feb 15 2010 John Balcaen <mikala@mandriva.org> 0.9.73-1mdv2010.1
+ Revision: 506133
- import plasma-applet-kbirthdayreminder


