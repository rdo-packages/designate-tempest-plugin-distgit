%{!?upstream_version: %global upstream_version %{commit}}
%global commit 9c3c7a32ab9f13eb6f8773bac5668bce7b83a9de
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

%{?dlrn: %global tarsources %{plugin}}
%{!?dlrn: %global tarsources %{module}}

Name:       python-%{service}-tests-tempest
Version:    0.2.0
Release:    2%{?alphatag}%{?dist}
Summary:    Tempest Integration of Designate
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:   python-tempest >= 12.1.0
Requires:   python-dns >= 1.12.0
Requires:   python-ddt >= 1.0.1

%description
This package contains Tempest tests to cover the designate project.
Additionally it provides a plugin to automatically load these tests into tempest.

%prep
%autosetup -n %{tarsources}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build

%install
%py2_install

%files
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*.egg-info

%changelog
* Thu Nov 09 2017 Chandan Kumar <chkumar@redhat.com> 0.2.0-2.9c3c7a3git
- Update to 0.2.0 (9c3c7a32ab9f13eb6f8773bac5668bce7b83a9de)

* Wed Feb 15 2017 Alfredo Moralejo <amoralej@redhat.com> 0.2.0-1
- Update to 0.2.0
