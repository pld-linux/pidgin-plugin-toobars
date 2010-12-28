#
# TODO: BRs
#
%define		short_name pidgin-toobars
Summary:	Adds toolbar and status bar to Pidgin buddy list
Name:		pidgin-plugin-toobars
Version:	1.13
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://vayurik.ru/wordpress/wp-content/uploads/toobars/%{version}/%{short_name}-%{version}.tar.gz
# Source0-md5:	a9678ae59addbe41e7389d72d4cea978
URL:		http://vayurik.ru/wordpress/en/toobars/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	pidgin-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adds toolbar and status bar to Pidgin buddy list.

%prep
%setup -q -n %{short_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang toobars
rm -f $RPM_BUILD_ROOT%{_libdir}/pidgin/toobars.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f toobars.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/pidgin/toobars.so
%{_pixmapsdir}/pidgin/buttons/*.png
