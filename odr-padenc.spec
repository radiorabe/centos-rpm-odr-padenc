#
# spec file for package odr-padenc
#
# Copyright (c) 2016 Radio Bern RaBe
#                    http://www.rabe.ch
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

# Note, that at the time of writing there was no official release available.
# To get a stable reproducable build, a specific Git commit is used instead.
%global commit0 fa1cd36ab9e7395fb3aacf98e89de2aa08b82527
%global shortcommit0 fa1cd36

# Conditional build support
# add --without imagemagick option, i.e. enable imagemagick by default
%bcond_without imagemagick


Name:           odr-padenc
# Version according to the last ChangeLog entry with short commit hash appended
Version:        1.2.0.%{shortcommit0}
Release:        1%{?dist}
Summary:        Opendigitalradio Programme Associated Data encoder 

License:        GPLv3+
URL:            https://github.com/Opendigitalradio/%{reponame}
Source0:        https://github.com/Opendigitalradio/%{reponame}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

%if %{with imagemagick}
BuildRequires:  ImageMagick-devel
%endif

%description
ODR-PadEnc is an encoder for Programme Associated Data, and includes support
for DAB MOT Slideshow and DLS.
To encode DLS and Slideshow data, the odr-padenc tool reads images from a
folder and DLS text from a file, and generates the PAD data for the encoder.

%prep
%setup -q -n %{reponame}-%{commit0}


%build
autoreconf -fi
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc ChangeLog README.md
%{_bindir}/*



%changelog
* Sat Sep 24 2016 Christian Affolter <c.affolter@purplehaze.ch> - 1.2.0.fa1cd36-1
- Initial release
