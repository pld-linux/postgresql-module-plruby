#
%define		postgresql_version	8.0.1
%define		postgresql_release	2
%define    ruby_archdir            %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')


Summary:	PL/Ruby - PostgreSQL procedural language
Summary(pl):	PL/Ruby j�zyk proceduralny bazy danych PostgreSQL
Name:	postgresql-module-plruby
Version:	0.4.3
Release:	1
License:	Ruby's
Group:		Applications/Databases
Source0:	ftp://moulon.inra.fr/pub/ruby/plruby.tar.gz
# Source0-md5:	0711a9da6154942ed898ccf67f5dd6c7
BuildRequires:	ruby-devel
BuildRequires:	postgresql-devel
Requires:	postgresql = %{postgresql_version}-%{postgresql_release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
From PostgreSQL documentation.

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
F
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/Ruby procedural language for your database you have to
run createlang command.

%prep
%setup -q -n plruby-%{version}

%build
ruby extconf.rb \
	--with-pgsql-include=/usr/include \
	--with-pgsql-lib=/usr/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_libdir}/postgresql
%{__make} install \
	archdir=$RPM_BUILD_ROOT/%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT/%{ruby_archdir}

mv $RPM_BUILD_ROOT/%{ruby_archdir}/plruby.so $RPM_BUILD_ROOT/%{_libdir}/postgresql

%files
%defattr(644,root,root,755)
%doc README.en
%attr(755,root,root) %{_libdir}/postgresql/plruby.so
%dir %{ruby_archdir}/plruby
%attr(755,root,root) %{ruby_archdir}/plruby/*.so

%changelog
* %{date} PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: postgresql-module-plruby.spec,v $
Revision 1.1  2005-03-16 20:56:01  aredridel
- added
- STBR