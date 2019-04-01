# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

%global common_desc \
This package contains Tempest tests to cover the designate project.\
Additionally it provides a plugin to automatically load these tests into tempest.

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Designate
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python%{pyver}-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python%{pyver}-%{service}-tests-tempest}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools

Requires:   python%{pyver}-tempest >= 1:18.0.0
Requires:   python%{pyver}-dns >= 1.15.0
Requires:   python%{pyver}-ddt >= 1.0.1
Requires:   python%{pyver}-testtools >= 1.8.0
Requires:   python-dnspython3 >= 1.12.0

%description -n python%{pyver}-%{service}-tests-tempest
%{common_desc}

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%files -n python%{pyver}-%{service}-tests-tempest
%license LICENSE
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/%{module}-*.egg-info

%changelog
