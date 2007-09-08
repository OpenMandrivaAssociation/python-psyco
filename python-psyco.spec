%define name python-psyco
%define version 1.5.2
%define release %mkrel 3
%define oname psyco

Summary: Python Specializing Compiler
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/%oname/%oname-%version-src.tar.bz2
Source1: psyco-1.1.1-docs.tar.bz2
License: MIT
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libpython-devel
Provides: psyco
Obsoletes: psyco
Url: http://psyco.sourceforge.net
Exclusivearch: %ix86

%description
Psyco is a Python extension module which can massively speed up the
execution of any Python code.

%package docs
Group: Development/Python
Summary: Programmer's documentation for Psyco

%description docs
Psyco is a Python extension module which can massively speed up the
execution of any Python code.

This package contains the developer's documentation for %{name} in HTML
and PostScript formats.

%prep
%setup -q -n %{oname}-%{version} -a 1

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --optimize=2

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt
%py_platsitedir/*psyco*

%files docs 
%defattr(-,root,root)
%doc Documentation/*


