Summary:	Frontend to PWN Oxford 2003 dictionary
Summary(pl):	Interfejs do s³ownika PWN Oxford 2003
Name:		kpwndict
Version:	0.1.3
Release:	0.1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://members.elysium.pl/ytm/src/%{name}-%{version}.tar.bz2
# Source0-md5:	62a70a6a4435983a5b66cae96981f2b5
#Source1:	%{name}.desktop
#Source2:	%{name}.png
URL:		http://members.elysium.pl/ytm/html/kpwndict.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kpwndict is a Qt frontend for PWN Oxford 2003 English-Polish
dictionary.

%description -l pl
Kpwndict to interfejs do s³ownika angielsko-polskiego PWN Oxford 2003.

%prep
%setup -q

%build
%{__aclocal} --acdir=config
%{__autoconf}
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_datadir}/%{name}}

install src/kpwndict $RPM_BUILD_ROOT%{_bindir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install src/kpwndict_pl.qm $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
