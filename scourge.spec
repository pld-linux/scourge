Summary:	Rogue-like game with a 3D user interface
Summary(pl.UTF-8):	Tekstowa gra RPG z trójwymiarowym interfejsem użytkownika
Name:		scourge
Version:	0.19
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scourge/%{name}-%{version}.src.tar.gz
# Source0-md5:	03126a6e8edeecb8fb53165570921834
Source1:	http://dl.sourceforge.net/scourge/%{name}-%{version}.data.tar.gz
# Source1-md5:	fb0b18654f4e00a5bee3be25bf1a9c7f
Patch0:		%{name}-configure.patch
Patch1:		%{name}-desktop.patch
URL:		http://scourgeweb.org/
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

%description -l pl.UTF-8
S.C.O.U.R.G.E. jest grą roguelike z trójwymiarowym interfejsem
użytkownika, utrzymaną w tradycji NetHacka i Morii. Gra pozwala grupie
czterech osób na poszukiwanie skarbu, zabijanie przeciwników,
zdobywanie poziomów doświadczenia, itp.

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

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
