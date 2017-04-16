#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 2.7.0
Release  : 38
URL      : https://pypi.debian.net/tox/tox-2.7.0.tar.gz
Source0  : https://pypi.debian.net/tox/tox-2.7.0.tar.gz
Summary  : virtualenv-based automation of test activities
Group    : Development/Tools
License  : MIT
Requires: tox-bin
Requires: tox-python
Requires: argparse
Requires: pluggy
Requires: py
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
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-remove-deps-to-run-tests.patch

%description
What is Tox?
--------------------
.. image:: https://img.shields.io/pypi/v/tox.svg
:target: https://pypi.org/project/tox/
.. image:: https://img.shields.io/pypi/pyversions/tox.svg
:target: https://pypi.org/project/tox/
.. image:: https://travis-ci.org/tox-dev/tox.svg?branch=master
:target: https://travis-ci.org/tox-dev/tox
.. image:: https://img.shields.io/appveyor/ci/RonnyPfannschmidt/tox/master.svg
:target: https://ci.appveyor.com/project/RonnyPfannschmidt/tox

%package bin
Summary: bin components for the tox package.
Group: Binaries

%description bin
bin components for the tox package.


%package python
Summary: python components for the tox package.
Group: Default

%description python
python components for the tox package.


%prep
%setup -q -n tox-2.7.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492372616
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1492372616
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

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
