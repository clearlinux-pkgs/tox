#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tox
Version  : 3.20.0
Release  : 110
URL      : https://files.pythonhosted.org/packages/b2/2c/579c4ad3d0c050770ee3b3bf42305606107ea42abb88ec8c5ce24c055a3f/tox-3.20.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b2/2c/579c4ad3d0c050770ee3b3bf42305606107ea42abb88ec8c5ce24c055a3f/tox-3.20.0.tar.gz
Summary  : tox is a generic virtualenv management and test command line tool
Group    : Development/Tools
License  : MIT
Requires: tox-bin = %{version}-%{release}
Requires: tox-license = %{version}-%{release}
Requires: tox-python = %{version}-%{release}
Requires: tox-python3 = %{version}-%{release}
Requires: filelock
Requires: importlib_metadata
Requires: packaging
Requires: pluggy
Requires: py
Requires: six
Requires: toml
Requires: virtualenv
BuildRequires : buildreq-distutils3
BuildRequires : filelock
BuildRequires : importlib_metadata
BuildRequires : packaging
BuildRequires : pluggy
BuildRequires : py
BuildRequires : pytest
BuildRequires : pytest-timeout
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : toml
BuildRequires : virtualenv

%description
[![Latest version on
PyPi](https://badge.fury.io/py/tox.svg)](https://badge.fury.io/py/tox)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/tox.svg)](https://pypi.org/project/tox/)
[![Azure Pipelines build
status](https://dev.azure.com/toxdev/tox/_apis/build/status/tox%20ci?branchName=master)](https://dev.azure.com/toxdev/tox/_build/latest?definitionId=9&branchName=master)
[![Documentation
status](https://readthedocs.org/projects/tox/badge/?version=latest&style=flat-square)](https://tox.readthedocs.io/en/latest/?badge=latest)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/tox/month)](https://pepy.tech/project/tox/month)

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
Provides: pypi(tox)
Requires: pypi(filelock)
Requires: pypi(packaging)
Requires: pypi(pluggy)
Requires: pypi(py)
Requires: pypi(six)
Requires: pypi(toml)
Requires: pypi(virtualenv)

%description python3
python3 components for the tox package.


%prep
%setup -q -n tox-3.20.0
cd %{_builddir}/tox-3.20.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598997079
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tox
cp %{_builddir}/tox-3.20.0/LICENSE %{buildroot}/usr/share/package-licenses/tox/e7fd7c458df3ba9633d648e0d666e348689f3559
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
/usr/share/package-licenses/tox/e7fd7c458df3ba9633d648e0d666e348689f3559

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
