%{!?upstream_version: %global upstream_version %{version}}
%define upstream_name puppet-certmonger


Name:           puppet-certmonger
Version:        1.1.1
Release:        2%{?alphatag}%{?dist}
Summary:        Certmonger Puppet Module
License:        ASL 2.0

URL:            https://github.com/saltedsignal/puppet-certmonger

Source0:        http://github.com/saltedsignal/%{upstream_name}/archive/v%{version}.tar.gz

#
# patches_base=v1.1.1
#

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
* Tue Oct 03 2017 Jon Schlueter <jschluet@redhat.com> 1.1.1-2
- Update to v1.1.1 tag official tag

* Thu Oct 27 2016 Jon Schlueter <jschluet@redhat.com> 1.1.1-1
- Update to 1.1.1 (1157a7e552d87696e80ed4ab54bf0608a1c5ffff)

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.1.0-1.e72a78c.git
- Newton update 1.1.0 (e72a78cf7361e7b64facebf42b29351c1a4e96c8)


