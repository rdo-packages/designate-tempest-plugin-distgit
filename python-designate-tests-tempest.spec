%{!?upstream_version: %global upstream_version %{commit}}
%global commit 5fde0854fcf6eb2455d4028ade186ade20d6bbf9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

Name:       python-%{service}-tests-tempest
Version:    0.1.1
Release:    0.1%{?alphatag}%{?dist}
Summary:    Tempest Integration of Designate
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:    https://github.com/openstack/%{plugin}/archive/%{commit}.tar.gz#/%{plugin}-%{shortcommit}.tar.gz

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
%autosetup -n %{plugin}-%{upstream_version} -S git

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
* Thu Sep 22 2016 Alan Pevec <apevec AT redhat.com> 0.1.1-0.1.5fde085git
- Update to post 0.1.0 (5fde0854fcf6eb2455d4028ade186ade20d6bbf9)
