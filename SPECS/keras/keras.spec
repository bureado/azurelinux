%define _enable_debug_package 0
%global debug_package %{nil}
Summary:        Keras is a high-level neural networks API.
Name:           keras
Version:        2.11.0
Release:        3%{?dist}
License:        ASL 2.0
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
Group:          Development/Languages/Python
URL:            https://keras.io/
Source0:        https://github.com/keras-team/keras/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-cache.tar.gz
BuildRequires:  bazel
BuildRequires:  build-essential
BuildRequires:  git
BuildRequires:  libstdc++-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  python3-requests
BuildRequires:  python3-wheel
BuildRequires:  tar
BuildRequires:  which
BuildRequires:  python3-tf-nightly
ExclusiveArch:  x86_64

%description
Keras is a deep learning API written in Python, running on top of the machine learning platform TensorFlow.

%package -n     python3-keras
Summary:        python-keras


%description -n python3-keras
Python 3 version.

%prep
%autosetup -p1


%build
MD5_HASH=$(echo -n $PWD | md5sum | awk '{print $1}')
mkdir -p /root/.cache/bazel/_bazel_$USER/$MD5_HASH/external
tar -xvf %{SOURCE1} -C /root/.cache/bazel/_bazel_$USER/$MD5_HASH/external

ln -s %{_bindir}/python3 %{_bindir}/python

bazel --batch build  --verbose_explanations //keras/tools/pip_package:build_pip_package

./bazel-bin/keras/tools/pip_package/build_pip_package pyproject-wheeldir/
# --------


%install
%{pyproject_install}


%files -n python3-keras
%license LICENSE
%{python3_sitelib}/*


%changelog
* Fri Feb 16 2024 Andrew Phelps <anphel@microsoft.com> - 2.11.0-3
- Relax requirement for python3-tf-nightly BR

* Tue Aug 01 2023 Riken Maharjan <rmaharjan@microsoft.com> - 2.11.0-2
- Remove bazel version.

* Mon Dec 12 2022 Riken Maharjan <rmaharjan@microsoft> - 2.11.0-1
- License verified
- Original version for CBL-Mariner
