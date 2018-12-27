#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 3.6.1
Release  : 75
URL      : https://files.pythonhosted.org/packages/14/c4/ee073df7f649e2a1977781807c0bb1fcfc691a99ee7b4a7a3cc819841458/tox-3.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/c4/ee073df7f649e2a1977781807c0bb1fcfc691a99ee7b4a7a3cc819841458/tox-3.6.1.tar.gz
Summary  : virtualenv-based automation of test activities
Group    : Development/Tools
License  : MIT
Requires: tox-bin = %{version}-%{release}
Requires: tox-license = %{version}-%{release}
Requires: tox-python = %{version}-%{release}
Requires: tox-python3 = %{version}-%{release}
Requires: filelock
Requires: pluggy
Requires: py
Requires: python-toml
Requires: setuptools
Requires: six
Requires: virtualenv
BuildRequires : buildreq-distutils3
BuildRequires : filelock
BuildRequires : pluggy
BuildRequires : py
BuildRequires : pytest
BuildRequires : pytest-timeout
BuildRequires : python-toml
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://badge.fury.io/py/tox.svg
:target: https://badge.fury.io/py/tox
:alt: Latest version on PyPI
.. image:: https://img.shields.io/pypi/pyversions/tox.svg
:target: https://pypi.org/project/tox/
:alt: Supported Python versions
.. image:: https://dev.azure.com/toxdev/tox/_apis/build/status/tox%20ci?branchName=master
:target: https://dev.azure.com/toxdev/tox/_build/latest?definitionId=9&branchName=master
:alt: Azure Pipelines build status
.. image:: https://api.codeclimate.com/v1/badges/425c19ab2169a35e1c16/test_coverage
:target: https://codeclimate.com/github/tox-dev/tox/code?sort=test_coverage
:alt: Test Coverage
.. image:: https://readthedocs.org/projects/tox/badge/?version=latest&style=flat-square
:target: https://tox.readthedocs.io/en/latest/?badge=latest
:alt: Documentation status
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
:target: https://github.com/ambv/black
:alt: Code style: black

%package bin
Summary: bin components for the tox package.
Group: Binaries
Requires: tox-license = %{version}-%{release}

%description bin
bin components for the tox package.


%package license
Summary: license components for the tox package.
Group: Default

%description license
license components for the tox package.


%package python
Summary: python components for the tox package.
Group: Default
Requires: tox-python3 = %{version}-%{release}

%description python
python components for the tox package.


%package python3
Summary: python3 components for the tox package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tox package.


%prep
%setup -q -n tox-3.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545922165
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tox
cp LICENSE %{buildroot}/usr/share/package-licenses/tox/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tox
/usr/bin/tox-quickstart

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tox/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
