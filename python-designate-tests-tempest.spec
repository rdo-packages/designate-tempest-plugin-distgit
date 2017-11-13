%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global service designate
%global plugin designate-tempest-plugin
%global module designate_tempest_plugin

Name:       python-%{service}-tests-tempest
Version:    0.3.0
Release:    1%{?dist}
Summary:    Tempest Integration of Designate
License:    ASL 2.0
URL:        https://github.com/openstack/%{plugin}/

Source0:     https://github.com/openstack/%{plugin}/archive/%{commit}.tar.gz#/%{plugin}-%{shortcommit}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:   python-tempest >= 12.1.0
Requires:   python-dns >= 1.12.0
Requires:   python-ddt >= 1.0.1
Requires:   python-testtools

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
* Mon Nov 13 2017 Chandan Kumar <chkumar@redhat.com> 0.3.0-1
- Bumped to 0.3.0 for Pike

* Thu Nov 09 2017 Chandan Kumar <chkumar@redhat.com> 0.2.0-3.4c094d17git
- Bumped release to fix the package upgrade from ocata to pike

* Wed Aug 30 2017 Chandan Kumar <chkumar@redhat.com> 0.2.0-0.1.4c094d17git
- Update to 0.2.0 (4c094d17769a1fc1fef78c4c8d7626a4a11205e2)
