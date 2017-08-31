# centos-rpm-odr-padenc
CentOS 7 RPM Specfile for [Opendigitalradio's ODR-PadEnc](https://github.com/Opendigitalradio/ODR-PadEnc) which is part of [RaBe's DAB / DAB+ broadcasting package collection](https://build.opensuse.org/project/show/home:radiorabe:dab).

## Usage
There are pre-built binary packages for CentOS 7 available on [Radio RaBe's OBS DAB / DAB+ broadcasting package repository](https://build.opensuse.org/project/show/home:radiorabe:dab), which can be installed as follows:

```bash
curl -o /etc/yum.repos.d/home:radiorabe:dab.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/dab/CentOS_7/home:radiorabe:dab.repo
     
yum install odr-padenc
```

### Running odr-padenc through systemd
The odr-padenc can be started via the installed systemd service unit template
(and therefore supports multiple instances):
```bash
systemctl start odr-padenc@<INSTANCE>.service

# To start an instance named "example":
systemctl start odr-padenc@example.service
```

The systemd service will also create the necessary directories and the FIFO,
located within the odr-padnenc temporary instance directory
<code>/var/tmp/odr/padenc/<INSTANCE></code>:
```
/var/tmp/odr/padenc/<INSTANCE>
├── pad.fifo
├── slides/
└── texts/dls-01.txt
```

So you can then point the <code>odr-audioenc</code> to the
`/var/tmp/odr/padenc/<INSTANCE>/pad.fifo` FIFO, insert your DLS text into `/var/tmp/odr/padenc/<INSTANCE>/texts/dls-01.txt` and put your MOT slideshow images into the `/var/tmp/odr/padenc/<INSTANCE>/slides` directory.

#### odr-padenc together with odr-audioenc
 An `odr-padenc`service unit instance plays nicely together with an
[`odr-audioenc`](https://github.com/radiorabe/centos-rpm-odr-audioenc#running-odr-audioenc-through-systemd)
service unit instance. Simply create an `odr-audioenc` and `odr-padenc`
instance with the same instance name and they will use the same PAD data FIFO.
For further details, refere to [odr-audioenc together with
odr-padenc](https://github.com/radiorabe/centos-rpm-odr-audioenc#odr-audioenc-together-with-odr-padenc)
