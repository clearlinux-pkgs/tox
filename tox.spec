#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 3.4.0
Release  : 72
URL      : https://files.pythonhosted.org/packages/45/a6/c35e27a2c81b17b3af3043161671eaff3a0449937d534a6e1baaa3756bdb/tox-3.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/a6/c35e27a2c81b17b3af3043161671eaff3a0449937d534a6e1baaa3756bdb/tox-3.4.0.tar.gz
Summary  : virtualenv-based automation of test activities
Group    : Development/Tools
License  : MIT
Requires: tox-bin
Requires: tox-python3
Requires: tox-license
Requires: tox-python
Requires: Sphinx
Requires: pluggy
Requires: py
Requires: python-toml
Requires: setuptools
Requires: six
Requires: virtualenv
BuildRequires : buildreq-distutils3
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
:alt: Latest version on PyPi
.. image:: https://img.shields.io/pypi/pyversions/tox.svg
:target: https://pypi.org/project/tox/
:alt: Supported Python versions
.. image:: https://dev.azure.com/toxdev/tox/_apis/build/status/tox%20ci?branchName=master
:target: https://dev.azure.com/toxdev/tox/_build/latest?definitionId=9&branchName=master
:alt: Azure Pipelines build status
.. image:: https://travis-ci.org/tox-dev/tox.svg?branch=master
:target: https://travis-ci.org/tox-dev/tox
:alt: Travis-CI build status
.. image:: https://codecov.io/gh/tox-dev/tox/branch/master/graph/badge.svg
:target: https://codecov.io/gh/tox-dev/tox
:alt: Code coverage Status
.. image:: https://readthedocs.org/projects/tox/badge/?version=latest
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
%setup -q -n tox-3.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538839693
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/tox
cp LICENSE %{buildroot}/usr/share/doc/tox/LICENSE
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
/usr/share/doc/tox/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
