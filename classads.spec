%define major 0
%define libname %mklibname classads %{major}
%define develname %mklibname classads -d


Summary: Condor's classified advertisement language
Name: classads
Version: 1.0.10
Release: 1
License: ASL 2.0
Group: System/Libraries
URL: http://www.cs.wisc.edu/condor/classad/
Source0: http://parrot.cs.wisc.edu/externals/classads-%{version}.tar.gz
BuildRequires: pcre-devel

%description
Classified Advertisements (classads) are the lingua franca of
Condor. They are used for describing jobs, workstations, and other
resources. They are exchanged by Condor processes to schedule
jobs. They are logged to files for statistical and debugging
purposes. They are used to enquire about current state of the system.

A classad is a mapping from attribute names to expressions. In the
simplest cases, the expressions are simple constants (integer,
floating point, or string). A classad is thus a form of property
list. Attribute expressions can also be more complicated. There is a
protocol for evaluating an attribute expression of a classad vis a vis
another ad. For example, the expression "other.size > 3" in one ad
evaluates to true if the other ad has an attribute named size and the
value of that attribute is (or evaluates to) an integer greater than
three. Two classads match if each ad has an attribute requirements
that evaluates to true in the context of the other ad. Classad
matching is used by the Condor central manager to determine the
compatibility of jobs and workstations where they may be run.


%package -n %{libname}
Summary: Library for creating ISO disc images
Group:   System/Libraries

%description -n %{libname}
Classified Advertisements (classads) are the lingua franca of
Condor. They are used for describing jobs, workstations, and other
resources. They are exchanged by Condor processes to schedule
jobs. They are logged to files for statistical and debugging
purposes. They are used to enquire about current state of the system.


%package -n %{develname}
Summary: Headers for Condor's classified advertisement language
Group: Development/C++
Requires: %{libname} = %{version}-%{release}
Requires: pcre-devel
Provides: %{name}-devel = %{version}-%{release}


%description -n %{develname}
Header files for Condor's ClassAd Library, a powerful and flexible,
semi-structured representation of data.

%package static
Summary: Condor's classified advertisement language's static libraries
Group: Development/C++
Requires: %{libname} = %{version}-%{release}

%description static
Static versions of Condor's ClassAd Library's libraries, a powerful
and flexible, semi-structured representation of data.

%prep
%setup -q -n %name-%version

%build
autoreconf -fi
%configure --enable-namespace --enable-flexible-member CC=g++
%make

%install
%makeinstall_std
rm -rf %{buildroot}%_libdir/*.la

%check
make check

%files -n %libname
%doc LICENSE-2.0.txt README CHANGELOG
%_libdir/libclassad.so.*
%_libdir/libclassad_ns.so.*


%files -n %develname
%doc LICENSE-2.0.txt README CHANGELOG
%_bindir/classad_version
%_bindir/classad_version_ns
%_bindir/classad_functional_tester
%_bindir/classad_functional_tester_ns
%_bindir/cxi
%_bindir/cxi_ns
%_libdir/libclassad.so
%_libdir/libclassad_ns.so
%dir %_includedir/classad/
%_includedir/classad/attrrefs.h
%_includedir/classad/cclassad.h
%_includedir/classad/classad_distribution.h
%_includedir/classad/classadErrno.h
%_includedir/classad/classad.h
%_includedir/classad/classadItor.h
%_includedir/classad/classad_stl.h
%_includedir/classad/collectionBase.h
%_includedir/classad/collection.h
%_includedir/classad/common.h
%_includedir/classad/debug.h
%_includedir/classad/exprList.h
%_includedir/classad/exprTree.h
%_includedir/classad/fnCall.h
%_includedir/classad/indexfile.h
%_includedir/classad/lexer.h
%_includedir/classad/lexerSource.h
%_includedir/classad/literals.h
%_includedir/classad/matchClassad.h
%_includedir/classad/operators.h
%_includedir/classad/query.h
%_includedir/classad/sink.h
%_includedir/classad/source.h
%_includedir/classad/transaction.h
%_includedir/classad/util.h
%_includedir/classad/value.h
%_includedir/classad/view.h
%_includedir/classad/xmlLexer.h
%_includedir/classad/xmlSink.h
%_includedir/classad/xmlSource.h

%files static
%doc LICENSE-2.0.txt README CHANGELOG
%_libdir/libclassad.a
%_libdir/libclassad_ns.a
