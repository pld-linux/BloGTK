Summary:	BloGTK - a weblog client
Summary(pl):	BloGTK - klient dla weblog�w
Name:		BloGTK
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/blogtk/blogtk_%{version}.tar.bz2
# Source0-md5:	cd2d2521a261867cd9c830a81d3d4408
URL:		http://blogtk.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-pygtk-gtk >= 2.0
BuildRequires:	python-pygtk-glade
Requires:	python-gnome-extras-gtkhtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BloGTK is a weblog client that allows you to post to your weblog from
Linux without the need for a separate browser window. BloGTK allows
you to connect with many weblog systems such as Blogger, Movable Type,
WordPress, and more. BloGTK Main WindowBloGTK is written using Python
and PyGTK, and is designed to be fast and simple to use.

%description -l pl
BloGTK jest klientem dla weblog�w, kt�ry pozwala umieszcza� notatki
na blogach bez konieczno�ci korzystania z przegl�darki internetowej.
BloGTK pozwala na korzystanie z wielu systemu weblog�w, takich jak:
Blogger, Moveable Type, WordPress i innych. BloGTK jest napisany z
u�yciem Pythona i PyGTK i ma by� szybkim i prostym w u�yciu.

%prep
%setup -q -n BloGTK-1.1

%install
rm -rf $RPM_BUILD_ROOT

sed -i 's/if test -f.*fi//' Makefile

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/blogtk \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/blogtk \
	APPLICATIONSDIR=$RPM_BUILD_ROOT%{_desktopdir} \
	ICONDIR=$RPM_BUILD_ROOT%{_iconsdir}

rm $RPM_BUILD_ROOT%{_bindir}/BloGTK
ln -s %{_libdir}/blogtk/BloGTK.py $RPM_BUILD_ROOT%{_bindir}/BloGTK

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_desktopdir}/*
%attr(644,root,root) %{_iconsdir}/*
%attr(755,root,root) %{_libdir}/blogtk/BloGTK.py
%{_datadir}/blogtk
%{_libdir}/blogtk
