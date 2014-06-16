%define	major	3
%define	libname	%mklibname shine %{major}
%define	devname	%mklibname shine -d

Name:		shine
Version:	3.0.0
Release:	1
Summary:	Fixed-point mp3 encoder
Source0:	http://sourceforge.net/projects/savonet/files/shine/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		System/Libraries
Url:		http://savonet.sourceforge.net/
BuildRequires:	ocaml
BuildRequires:	ocaml-doc
BuildRequires:	ocaml-compiler-libs
BuildRequires:	camlp4-devel
BuildRequires:	ocaml-findlib

%description
Shine is a library for encoding mp3 data which is implemented in fixed-point
arithmetic.
The library can thus be used to implement super fast mp3 encoding on
architectures without a FPU, such as `armel`, etc.. In fact, it is also super
fast on architectures with a FPU!

%package -n	%{libname}
Summary:	Libraries needed by shine mp3 encoder
Group:		System/Libraries

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Provides:	shine-devel = %{EVRD}

%description -n	%{devname}
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure
%make all

%install
%makeinstall_std OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml DLLDIR=%{buildroot}%{_libdir}/ocaml/stublibs

%files
%{_bindir}/shineenc

%files -n %{libname}
%{_libdir}/libshine.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libshine.so
%{_libdir}/pkgconfig/*.pc
