#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 2.9.1
Release  : 54
URL      : https://pypi.debian.net/tox/tox-2.9.1.tar.gz
Source0  : https://pypi.debian.net/tox/tox-2.9.1.tar.gz
Summary  : virtualenv-based automation of test activities
Group    : Development/Tools
License  : MIT
Requires: tox-bin
Requires: tox-legacypython
Requires: tox-python3
Requires: tox-python
Requires: argparse
Requires: pluggy
Requires: py
Requires: six
Requires: virtualenv
BuildRequires : argparse
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py
BuildRequires : pytest
BuildRequires : pytest-timeout
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/tox.svg
:target: https://pypi.org/project/tox/
.. image:: https://img.shields.io/pypi/pyversions/tox.svg
:target: https://pypi.org/project/tox/
.. image:: https://travis-ci.org/tox-dev/tox.svg?branch=master
:target: https://travis-ci.org/tox-dev/tox
.. image:: https://img.shields.io/appveyor/ci/RonnyPfannschmidt/tox/master.svg
:target: https://ci.appveyor.com/project/RonnyPfannschmidt/tox
.. image:: https://codecov.io/gh/tox-dev/tox/branch/master/graph/badge.svg
:target: https://codecov.io/gh/tox-dev/tox
.. image:: https://readthedocs.org/projects/tox/badge/?version=latest
:target: http://tox.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

%package bin
Summary: bin components for the tox package.
Group: Binaries

%description bin
bin components for the tox package.


%package legacypython
Summary: legacypython components for the tox package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the tox package.


%package python
Summary: python components for the tox package.
Group: Default
Requires: tox-python3

%description python
python components for the tox package.


%package python3
Summary: python3 components for the tox package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tox package.


%prep
%setup -q -n tox-2.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520971711
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1520971711
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tox
/usr/bin/tox-quickstart

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
