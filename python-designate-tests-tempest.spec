%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x22284f69d9eccdf3df7819791c711af193ff8e54
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{?dlrn: %global tarsources %{plugin}}
%{!?dlrn: %global tarsources %{module}}
%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

%global common_desc \
This package contains Tempest tests to cover the designate project.\
Additionally it provides a plugin to automatically load these tests into tempest.

Name:       python-%{service}-tests-tempest
Version:    0.25.0
Release:    1%{?dist}
Summary:    Tempest Integration of Designate
License:    Apache-2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{tarsources}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{plugin}/%{tarsources}-%{upstream_version}.tar.gz.asc
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

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{tarsources}-%{upstream_version} -S git

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{service}-tests-tempest
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.dist-info

%changelog
* Tue Mar 25 2025 RDO <dev@lists.rdoproject.org> 0.25.0-1
- Update to 0.25.0


