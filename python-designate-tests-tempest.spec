%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

%if 0%{?fedora}
%global with_python3 1
%endif

%global common_desc \
This package contains Tempest tests to cover the designate project.\
Additionally it provides a plugin to automatically load these tests into tempest.

Name:       python-%{service}-tests-tempest
Version:    0.4.0
Release:    1%{?dist}
Summary:    Tempest Integration of Designate
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python2-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python2-%{service}-tests-tempest}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

Requires:   python2-tempest >= 1:17.1.0
Requires:   python2-dns >= 1.12.0
Requires:   python2-ddt >= 1.0.1
Requires:   python2-testtools >= 1.8.0

%description -n python2-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:17.1.0
Requires:   python3-dns >= 1.12.0
Requires:   python3-ddt >= 1.0.1
Requires:   python3-testtools >= 1.8.0

%description -n python3-%{service}-tests-tempest
%{common_desc}
%endif

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{service}-tests-tempest
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*.egg-info

%if 0%{?with_python3}
%files -n python3-%{service}-tests-tempest
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info
%endif

%changelog
* Mon Feb 19 2017 Chandan Kumar <chkumar@redhat.com> 0.4.0-1
- Update to 0.4.0
