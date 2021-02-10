%{!?upstream_version: %global upstream_version %{version}}
%define upstream_name puppet-certmonger


Name:           puppet-certmonger
Version:        2.6.0
Release:        1%{?dist}
Summary:        Certmonger Puppet Module
License:        ASL 2.0

URL:            https://github.com/saltedsignal/puppet-certmonger

Source0:        http://github.com/saltedsignal/%{upstream_name}/archive/v%{upstream_version}.tar.gz#/%{upstream_name}-%{upstream_version}.tar.gz

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
* Wed Feb 10 2021 RDO <dev@lists.rdoproject.org> 2.6.0-1
- Update to 2.6.0

* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.4.0-1.a198870git
- Update to post 2.4.0 (a19887066c4978ad2567c881d60c14fcf0737bb2)


