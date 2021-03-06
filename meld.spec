Summary:	Visual diff and merge tool
Summary(pl.UTF-8):	Wizualne narzędzie do oglądania i włączania zmian (diff)
Name:		meld
Version:	3.16.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnome.org/pub/GNOME/sources/meld/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	f1dc544cc46ead1369bb424759bd2c05
Patch0:		%{name}-desktop.patch
URL:		http://meld.sourceforge.net/
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	python-modules >= 2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.34
Requires:	gtk+3 >= 3.6
Requires:	gtksourceview3 >= 3.6
Requires:	hicolor-icon-theme
Requires:	pango >= 1:1.26
Requires:	python-modules >= 2.7
Requires:	python-pycairo
Requires:	python-pygobject3 >= 3.8
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Meld is a GNOME visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy
navigation, and it also features a tabbed interface that allows you to
open many diffs at once.

%description -l pl.UTF-8
Meld to przeznaczone dla GNOME wizualne narzędzie do oglądania i
włączania zmian (w formacie diff). Integruje się szczególnie dobrze z
CVS. Przeglądarka różnic pozwala modyfikować pliki w miejscu
(dynamicznie uaktualniać), a środkowa kolumna pokazuje szczegółowe
zmiany i pozwala na włączanie. Na marginesach jest pokazane położenie
zmian w celu łatwej nawigacji. Jest dostępny także interfejs z
zakładkami, pozwalający na otwieranie wielu plików diff naraz.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
	--no-compile-schemas \
	--no-update-icon-cache \
	build --build-base=build-2 \
	install --skip-build \
	--prefix=%{_prefix} \
	--install-purelib=%{py_sitescriptdir} \
	--install-platlib=%{py_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitescriptdir}/meld-*.egg-info
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%dir %{py_sitescriptdir}/%{name}/ui
%{py_sitescriptdir}/%{name}/ui/*.py[co]
%dir %{py_sitescriptdir}/%{name}/util
%{py_sitescriptdir}/%{name}/util/*.py[co]
%dir %{py_sitescriptdir}/%{name}/vc
%{py_sitescriptdir}/%{name}/vc/*.py[co]
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_iconsdir}/hicolor/*/apps/meld-version-control.png
%{_iconsdir}/HighContrast/scalable/apps/meld.svg
%{_datadir}/%{name}
%{_datadir}/appdata/meld.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.meld.gschema.xml
%{_datadir}/mime/packages/meld.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
