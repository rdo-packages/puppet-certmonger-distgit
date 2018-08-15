%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-certmonger
%global commit ef9457ca650b652547fa99644b8a27de01b3db50
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-certmonger
Version:        2.3.0
Release:        2%{?alphatag}%{?dist}
Summary:        Certmonger Puppet Module
License:        ASL 2.0

URL:            https://github.com/saltedsignal/puppet-certmonger

Source0:        http://github.com/saltedsignal/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.3.0-2.ef9457cgit
- Update to post 2.3.0 (ef9457ca650b652547fa99644b8a27de01b3db50)



