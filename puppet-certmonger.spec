%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-certmonger
%global commit d09f0f2bfb60f72f4843801f845383576c8afbc2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-certmonger
Version:        1.1.1
Release:        2%{?alphatag}%{?dist}
Summary:        Certmonger Puppet Module
License:        ASL 2.0

URL:            https://github.com/earsdown/puppet-certmonger

Source0:        http://github.com/earsdown/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Certmonger puppet module for integration with IPA CAs.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/certmonger/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/certmonger/



%files
%{_datadir}/openstack-puppet/modules/certmonger/


%changelog
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 1.1.1-2.d09f0f2git
- Pike update 1.1.1 (d09f0f2bfb60f72f4843801f845383576c8afbc2)


