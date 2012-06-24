Summary:	Rogue-like game with a 3D user interface
Summary(pl):	Tekstowa gra RPG z tr�jwymiarowym interfejsem u�ytkownika
Name:		scourge
Version:	0.17
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scourge/%{name}-%{version}.src.tar.gz
# Source0-md5:	2ff3dac4b5b8bdc1af526fb5917ad383
Source1:	http://dl.sourceforge.net/scourge/%{name}-%{version}.data.tar.gz
# Source1-md5:	5f41657ec0593a5994b21ae01705b5fb
Patch0:		%{name}-configure.patch
Patch1:		%{name}-desktop.patch
URL:		http://scourge.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	wxGTK2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S.C.O.U.R.G.E. is a Rogue-like game with a 3D user interface in fine
tradition of NetHack and Moria. The game allows a group of four
characters to search for treasure, kill enemies, gain levels, etc.

%description -l pl
S.C.O.U.R.G.E. jest gr� roguelike z tr�jwymiarowym interfejsem
u�ytkownika, utrzyman� w tradycji NetHacka i Morii. Gra pozwala grupie
czterech os�b na poszukiwanie skarbu, zabijanie przeciwnik�w,
zdobywanie poziom�w do�wiadczenia, itp.

%prep
%setup -q -n %{name} -a 1
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	WXWIDGET=wx-gtk2-ansi-config \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf %{name}_data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install assets/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install assets/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
