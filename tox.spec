#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 2.8.2
Release  : 48
URL      : https://pypi.debian.net/tox/tox-2.8.2.tar.gz
Source0  : https://pypi.debian.net/tox/tox-2.8.2.tar.gz
Summary  : virtualenv-based automation of test activities
Group    : Development/Tools
License  : MIT
Requires: tox-bin
Requires: tox-legacypython
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
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-remove-deps-to-run-tests.patch

%description
What is Tox?
        --------------------

%package bin
Summary: bin components for the tox package.
Group: Binaries

%description bin
bin components for the tox package.


%package legacypython
Summary: legacypython components for the tox package.
Group: Default

%description legacypython
legacypython components for the tox package.


%package python
Summary: python components for the tox package.
Group: Default
Requires: tox-legacypython

%description python
python components for the tox package.


%prep
%setup -q -n tox-2.8.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505696714
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505696714
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
/usr/lib/python3*/*
