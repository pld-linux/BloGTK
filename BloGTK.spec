Summary:	BloGTK - a weblog client
Summary(pl.UTF-8):   BloGTK - klient dla weblogów
Name:		BloGTK
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/blogtk/blogtk_%{version}.tar.bz2
# Source0-md5:	cd2d2521a261867cd9c830a81d3d4408
URL:		http://blogtk.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-pygtk-glade
BuildRequires:	python-pygtk-gtk >= 2.0
Requires:	python-gnome-extras-gtkhtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BloGTK is a weblog client that allows you to post to your weblog from
Linux without the need for a separate browser window. BloGTK allows
you to connect with many weblog systems such as Blogger, Movable Type,
WordPress, and more. BloGTK Main WindowBloGTK is written using Python
and PyGTK, and is designed to be fast and simple to use.

%description -l pl.UTF-8
BloGTK jest klientem dla weblogów, który pozwala umieszczać notatki
na blogach bez konieczności korzystania z przeglądarki internetowej.
BloGTK pozwala na korzystanie z wielu systemu weblogów, takich jak:
Blogger, Moveable Type, WordPress i innych. BloGTK jest napisany z
użyciem Pythona i PyGTK i ma być szybkim i prostym w użyciu.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

sed -i 's/if test -f.*fi//' Makefile

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/blogtk \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/blogtk \
	APPLICATIONSDIR=$RPM_BUILD_ROOT%{_desktopdir} \
	ICONDIR=$RPM_BUILD_ROOT%{_pixmapsdir}

rm $RPM_BUILD_ROOT%{_bindir}/BloGTK
ln -s %{_libdir}/blogtk/BloGTK.py $RPM_BUILD_ROOT%{_bindir}/BloGTK
rm -f $RPM_BUILD_ROOT%{_datadir}/blogtk/*.bak

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%dir %{_libdir}/blogtk
%attr(755,root,root) %{_libdir}/blogtk/BloGTK.py
%{_libdir}/blogtk/[cps]*.py
%{_datadir}/blogtk
