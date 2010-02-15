%define name	plasma-applet-kbirthdayreminder
%define srcname birthday-plasmoid
%define version	 0.9.73
%define release	%mkrel 1
%define Summary	 A reminder for birthdays and anniversaries


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://kde-look.org/CONTENT/content-files/91641-%srcname-%version.tar.bz2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://kde-look.org/content/show.php/K+Birthday+Reminder?content=91641
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdepimlibs4-devel
Requires:	kdebase4-runtime => 4.3
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
%_kde_libdir/kde4/plasma_engine_kabc.so
%_kde_services/plasma-applet-kbirthday.desktop
%_kde_services/plasma-dataengine-kabc.desktop
%_kde_datadir/apps/desktoptheme/default/widgets/birthdaycake.svg
%_iconsdir/hicolor/scalable/apps/birthdaycake.svgz

#------------------------------------------------------------------------------

%prep
%setup -q -n KBirthdayPlasma_0_9_73

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang plasma_applet_kbirthdayapplet
%clean
%__rm -rf %{buildroot}
