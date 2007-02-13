# TODO
# - doesn't build
Summary:	PL/Ruby - PostgreSQL procedural language
Summary(pl.UTF-8):	PL/Ruby - język proceduralny bazy danych PostgreSQL
Name:		postgresql-module-plruby
Version:	0.4.3
Release:	0.1
License:	Ruby's
Group:		Applications/Databases
Source0:	ftp://moulon.inra.fr/pub/ruby/plruby.tar.gz
# Source0-md5:	0711a9da6154942ed898ccf67f5dd6c7
BuildRequires:	postgresql-backend-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%requires_eq_to postgresql postgresql-backend-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
From PostgreSQL documentation:

Postgres supports the definition of procedural languages. In the case
of a function or trigger procedure defined in a procedural language,
the database has no built-in knowledge about how to interpret the
function's source text. Instead, the task is passed to a handler that
knows the details of the language. The handler itself is a special
programming language function compiled into a shared object and loaded
on demand.

To enable PL/Ruby procedural language for your database you have to
run createlang command.

%description -l pl.UTF-8
Z dokumentacji PostgreSQL:

Postgres ma wsparcie dla języków proceduralnych. W przypadku, kiedy
programista zdefiniuje procedurę wyzwalacza lub funkcję w języku
proceduralnym, baza danych nie ma pojęcia jak interpretować tego typu
funkcję. Funkcja lub procedura ta jest przekazywana do interpretera,
który wie jak ją wykonać. Interpreter jest odpowiednią, specjalną
funkcją, która jest skompilowana w obiekt dzielony i ładowany w razie
potrzeby.

Za pomocą polecenia createlang można dodać obsługę języka
proceduralnego PL/Ruby dla swojej bazy danych.

%prep
%setup -q -n plruby-%{version}

%build
ruby extconf.rb \
	--with-pgsql-include=/usr/include/postgresql \
	--with-pgsql-lib=/usr/%{_lib} \
	--with-pgsql-version=80

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/postgresql

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir}

mv -f $RPM_BUILD_ROOT%{ruby_archdir}/plruby.so $RPM_BUILD_ROOT%{_libdir}/postgresql

%files
%defattr(644,root,root,755)
%doc README.en
%attr(755,root,root) %{_libdir}/postgresql/plruby.so
%dir %{ruby_archdir}/plruby
%attr(755,root,root) %{ruby_archdir}/plruby/*.so
