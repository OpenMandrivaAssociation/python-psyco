%define oname psyco

Summary:	Python Specializing Compiler
Name:		python-%{oname}
Version:	1.6
Release:	16
License:	MIT
Group:		Development/Python
Url:		http://psyco.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{oname}/%{oname}-%{version}-src.tar.gz
Source1:	psyco-1.1.1-docs.tar.bz2
Patch0:		python-psyco_python27.patch
Patch1:		psyco-1.6-fix-linking.patch
BuildRequires:	pkgconfig(python2)
Provides:	psyco = %{EVRD}
Exclusivearch:	%ix86

%description
Psyco is a Python extension module which can massively speed up the
execution of any Python code.

%package docs
Group:		Development/Python
Summary:	Programmer's documentation for Psyco

%description docs
Psyco is a Python extension module which can massively speed up the
execution of any Python code.

This package contains the developer's documentation for %{name} in HTML
and PostScript formats.

%prep
%setup -qn %{oname}-%{version} -a 1
%apply_patches

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --optimize=2

%files 
%doc *.txt
%{py2_platsitedir}/*psyco*

%files docs 
%doc Documentation/*

