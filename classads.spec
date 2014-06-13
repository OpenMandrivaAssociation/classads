%define major	1
%define libname	%mklibname classads %{major}
%define libns	%mklibname classads_ns %{major}
%define devname	%mklibname classads -d

Summary:	Condor's classified advertisement language
Name:		classads
Version:	1.0.10
Release:	6
License:	ASLv2.0
Group:		System/Libraries
Url:		http://www.cs.wisc.edu/condor/classad/
Source0:	ftp://ftp.cs.wisc.edu/condor/classad/c++/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libpcre)

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
Summary:	Library for creating ISO disc images
Group:		System/Libraries
Obsoletes:	%{_lib}classads0

%description -n %{libname}
Classified Advertisements (classads) are the lingua franca of
Condor. They are used for describing jobs, workstations, and other
resources. They are exchanged by Condor processes to schedule
jobs. They are logged to files for statistical and debugging
purposes. They are used to enquire about current state of the system.

%package -n %{libns}
Summary:	Library for creating ISO disc images
Group:		System/Libraries
Conflicts:	%{_lib}classads0

%description -n %{libns}
Classified Advertisements (classads) are the lingua franca of
Condor. They are used for describing jobs, workstations, and other
resources. They are exchanged by Condor processes to schedule
jobs. They are logged to files for statistical and debugging
purposes. They are used to enquire about current state of the system.

%package -n %{devname}
Summary:	Headers for Condor's classified advertisement language
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libns} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}classads-static-devel

%description -n %{devname}
Header files for Condor's ClassAd Library, a powerful and flexible,
semi-structured representation of data.

%prep
%setup -q
#autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-namespace \
	--enable-flexible-member

%make

%install
%makeinstall_std

%check
make check

%files -n %{libname}
%{_libdir}/libclassad.so.%{major}*

%files -n %{libns}
%{_libdir}/libclassad_ns.so.%{major}*

%files -n %{devname}
%doc LICENSE-2.0.txt README CHANGELOG
%{_bindir}/classad_version
%{_bindir}/classad_version_ns
%{_bindir}/classad_functional_tester
%{_bindir}/classad_functional_tester_ns
%{_bindir}/cxi
%{_bindir}/cxi_ns
%{_libdir}/libclassad.so
%{_libdir}/libclassad_ns.so
%dir %{_includedir}/classad/
%{_includedir}/classad/*.h

