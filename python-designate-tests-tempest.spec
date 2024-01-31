%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x815afec729392386480e076dcc0dfe2d21c023c9
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

%global common_desc \
This package contains Tempest tests to cover the designate project.\
Additionally it provides a plugin to automatically load these tests into tempest.

Name:       python-%{service}-tests-tempest
Version:    0.20.0
Release:    1%{?dist}
Summary:    Tempest Integration of Designate
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-dns >= 1.15.0
Requires:   python3-ddt >= 1.0.1
Requires:   python3-testtools >= 2.2.0

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.egg-info

%changelog
* Wed Jan 31 2024 RDO <dev@lists.rdoproject.org> 0.20.0-1
- Update to 0.20.0

* Wed Mar 15 2023 RDO <dev@lists.rdoproject.org> 0.17.0-1
- Update to 0.17.0

