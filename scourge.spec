Summary:	Rogue-like game with a 3D user interface
Summary(pl):	Tekstowa gra RPG z trójwymiarowym interfejsem u¿ytkownika
Name:		scourge
Version:	0.15
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scourge/%{name}-%{version}.tar.gz
# Source0-md5:	026b91d015865455a3dde7643ae74098
Source1:	%{name}.desktop
Patch0:		%{name}-configure.patch
URL:		http://scourge.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	wxGTK2-devel
Requires:	SDL >= 1.2.7
Requires:	SDL_mixer >= 1.2
Requires:	SDL_net >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S.C.O.U.R.G.E. is a Rogue-like game with a 3D user interface in fine
tradition of NetHack and Moria. The game allows a group of four
characters to search for treasure, kill enemies, gain levels, etc.

%description -l pl
S.C.O.U.R.G.E. jest gr± roguelike z trójwymiarowym interfejsem
u¿ytkownika, utrzyman± w tradycji NetHacka i Morii. Gra pozwala grupie
czterech osób na poszukiwanie skarbu, zabijanie przeciwników,
zdobywanie poziomów do¶wiadczenia, itp.

%prep
%setup -q
%patch0 -p1

%build
cd %{name}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure WXWIDGET=wx-gtk2-ansi-config \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} -C %{name} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf %{name}_data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name}/assets/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc scourge/{AUTHORS,README,ChangeLog}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
