#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 2.4.1
Release  : 30
URL      : http://pypi.debian.net/tox/tox-2.4.1.tar.gz
Source0  : http://pypi.debian.net/tox/tox-2.4.1.tar.gz
Summary  : virtualenv-based automation of test activities
Group    : Development/Tools
License  : MIT
Requires: tox-bin
Requires: tox-python
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
Tox is a generic virtualenv management and test command line tool you can use for:

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
%setup -q -n tox-2.4.1
%patch1 -p1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tox
/usr/bin/tox-quickstart

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
