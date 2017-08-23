%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
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
Requires:   python-testtools
Requires:   python-dnspython3 >= 1.12.0

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
