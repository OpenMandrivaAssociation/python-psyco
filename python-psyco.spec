%define oname psyco

Summary:	Python Specializing Compiler
Name:		python-%{oname}
Version:	1.6
Release:	9
Source0:	http://downloads.sourceforge.net/%oname/%oname-%version-src.tar.gz
Source1:	psyco-1.1.1-docs.tar.bz2
Patch0:		python-psyco_python27.patch
Patch1:		psyco-1.6-fix-linking.patch
License:	MIT
Group:		Development/Python
BuildRequires:	python-devel
Provides:	psyco = %{EVRD}
Obsoletes:	psyco < %{EVRD}
Url:		http://psyco.sourceforge.net
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
%setup -q -n %{oname}-%{version} -a 1
%patch0 -p0 
%patch1 -p1

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --root=%{buildroot} --optimize=2

%files 
%doc *.txt
%py_platsitedir/*psyco*

%files docs 
%doc Documentation/*




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6-7mdv2011.0
+ Revision: 668022
- mass rebuild

* Fri Mar 18 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.6-6
+ Revision: 646481
- fix linking

  + Matthew Dawkins <mattydaw@mandriva.org>
    - added p0 to fix python2.7 build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-4mdv2010.1
+ Revision: 523854
- rebuilt for 2010.1

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.6-3mdv2009.1
+ Revision: 319602
- rebuild with python 2.6

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.6-2mdv2009.0
+ Revision: 225138
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.6-1mdv2008.1
+ Revision: 120729
- new version

* Sat Sep 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.2-3mdv2008.0
+ Revision: 82454
- rebuild with optflags


* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5.2-2mdv2007.0
+ Revision: 88165
- update file list

* Tue Nov 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5.2-1mdv2007.1
+ Revision: 85949
- Import python-psyco

* Tue Nov 21 2006 Götz Waschk <waschk@mandriva.org> 1.5.2-1mdv2007.1
- new version

* Fri Apr 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.5.1-1mdk
- New release 1.5.1
- use mkrel

* Sun Oct 30 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.5-1mdk
- New release 1.5

* Fri Feb 18 2005 Götz Waschk <waschk@linux-mandrake.com> 1.4-1mdk
- provide and obsolete psyco
- New release 1.4

* Tue Dec 07 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3-2mdk
- update description

* Mon Dec 06 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3-1mdk
- New release 1.3

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.2-2mdk
- Rebuild for new python

* Thu Mar 04 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2-1mdk
- new version

