Summary:	BloGTK - a weblog client
Summary(pl):	BloGTK - klient dla weblogów
Name:		BloGTK
Version:	1.1
Release:	1
License:	GPL v2
Group:		Development
Source0:	http://dl.sourceforge.net/blogtk/blogtk_%{version}.tar.bz2
# Source0-md5:	cd2d2521a261867cd9c830a81d3d4408
URL:		http://blogtk.sourceforge.net/
BuildRequires:	python
BuildRequires:	python-pygtk-gtk >= 2.0
BuildRequires:	python-pygtk-glade
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BloGTK is a weblog client that allows you to post to your weblog from
Linux without the need for a separate browser window. BloGTK allows
you to connect with many weblog systems such as Blogger, Movable Type,
WordPress, and more. BloGTK Main WindowBloGTK is written using Python
and PyGTK, and is designed to be fast and simple to use.

%description -l pl
BloGTK jest klientem dla weblogów, który pozwala umieszczaæ notatki
na blogach bez konieczno¶ci korzystania z przegl±darki internetowej.
BloGTK pozwala na korzystanie z wielu systemu weblogów, takich jak:
Blogger, Moveable Type, WordPress i innych. BloGTK jest napisany z
u¿yciem Pythona i PyGTK i ma byæ szybkim i prostym w u¿yciu.

%prep
%setup -q -n BloGTK-1.1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        BINDIR=$RPM_BUILD_ROOT%{_bindir} \
        DATADIR=$RPM_BUILD_ROOT/share/blogtk \
	LIBDIR=$RPM_BUILD_ROOT/lib/blogtk \
        APPLICATIONSDIR=$RPM_BUILD_ROOT/share/applications \
	ICONDIR=$RPM_BUILD_ROOT/share/pixmaps
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
