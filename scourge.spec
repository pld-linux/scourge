Summary:	Rogue-like game with a 3D user interface
Summary(pl):	Tekstowa gra RPG z trójwymiarowym interfejsem u¿ytkownika
Name:		scourge
Version:	0.7
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scourge/%{name}-%{version}.tar.gz
# Source0-md5:	ec3c89aebe0a2c6302261ba04d4e3080
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://scourge.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S.C.O.U.R.G.E. is a Rogue-like game with a 3D user interface in fine
tradition of NetHack and Moria. The game allows a group of four
characters to search for treasure, kill enemies, gain levels, etc.

%description -l pl
S.C.O.U.R.G.E. jest tekstow± gr± RPG z trójwymiarowym interfejsem
u¿ytkownika utrzyman± w tradycji NetHacka i Morii. Gra pozwala grupie
czterech osób na poszukiwanie skarbu, zabijanie przeciwników,
zdobywanie poziomów, itp.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
