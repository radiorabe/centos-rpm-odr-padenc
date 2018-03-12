#
# spec file for package odr-padenc
#
# Copyright (c) 2016 - 2018 Radio Bern RaBe
#                           http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-odr-padenc
#

# Name of the GitHub repository
%define reponame ODR-PadEnc

%define service_user odr-padenc
%define service_group odr

# Conditional build support
# add --without imagemagick option, i.e. enable imagemagick by default
%bcond_without imagemagick


Name:           odr-padenc
Version:        2.3.0
Release:        1%{?dist}
Summary:        Opendigitalradio Programme Associated Data encoder 

License:        GPLv3+
URL:            https://github.com/Opendigitalradio/%{reponame}
Source0:        https://github.com/Opendigitalradio/%{reponame}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}@.service
Source2:        %{name}.conf

%{?systemd_requires}
BuildRequires: systemd

%if %{with imagemagick}
BuildRequires:  ImageMagick-devel
%endif

%description
ODR-PadEnc is an encoder for Programme Associated Data, and includes support
for DAB MOT Slideshow and DLS.
To encode DLS and Slideshow data, the odr-padenc tool reads images from a
folder and DLS text from a file, and generates the PAD data for the encoder.

%prep
%setup -q -n %{reponame}-%{version}


%build
autoreconf -fi
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

# Install the systemd service unit
install -d %{buildroot}/%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}
install -d %{buildroot}/%{_tmpfilesdir}
install -m 644 %{SOURCE2} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

# Temporary directory for DLS texts, MOT slideshow slides and FIFOs
install -d %{buildroot}/var/tmp/odr/padenc


%pre
getent group %{service_group} >/dev/null || groupadd -r %{service_group}
getent passwd %{service_user} >/dev/null || \
    useradd -r -g %{service_group} -d /dev/null -m -s /sbin/nologin \
    -c "%{name} system user account" %{service_user}
exit 0


%files
%doc ChangeLog README.md
%{_bindir}/*
%{_unitdir}/%{name}@.service
%{_tmpfilesdir}/%{name}.conf

# Install the temporary directory owned by the odr-padenc user/group
%dir %attr(0755, %{name}, %{name}) /var/tmp/odr/padenc



%changelog
* Sun Mar 11 2018 Christian Affolter <c.affolter@purplehaze.ch> - 2.3.0-1
- Bump to upstream version 2.3.0

* Sat Aug 26 2017 Christian Affolter <c.affolter@purplehaze.ch> - 2.2.0-2
- Use a shared system odr group to play nicely together with odr-audioenc
- systemd service unit template fixes and enhancements.

* Tue Aug 22 2017 Christian Affolter <c.affolter@purplehaze.ch> - 2.2.0-1
- Bump to upstream version 2.2.0

* Fri Mar 24 2017 Lucas Bickel <hairmare@rabe.ch> - 2.1.0-2
- Bump to upstream version 2.1.1
- Add systemd-tmpfiles config for /var/tmp/odr

* Sun Feb 19 2017 Christian Affolter <c.affolter@purplehaze.ch> - 2.1.0-1
- Bump to upstream version 2.1.0

* Tue Nov 01 2016 Christian Affolter <c.affolter@purplehaze.ch> - 2.0.1-1
- Switched from specific Git commit to upstream release
- Added a dedicated system user/group and systemd service unit template for
  starting odr-padenc

* Sat Sep 24 2016 Christian Affolter <c.affolter@purplehaze.ch> - 1.2.0.fa1cd36-1
- Initial release
