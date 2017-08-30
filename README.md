# soak
This automation covered:

- CPU Usage
- Memory utilization
- Disk utilization
- Log size
- System up time since the last reboot
- Packet sent
- Packet received
- Bytes sent
- Bytes received 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Prerequisite to run this automation is `pip` and `psutil-library` packages installed on your host machine. Follow below steps for the installation of required packages and copy the `stats.py` script to your BPO-host machine. 

## Install pip
#### Install Pip with Curl and Python

Pip is part of Extra Packages for Enterprise Linux (EPEL), which is a community repository of non-standard packages for the RHEL distribution. 

```sh
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
$ python get-pip.py
```
## Verify The Installation

#### View a list of helpful commands

```sh
$ pip --help
```
#### check the version of pip you installed
```sh
$ pip -V
```
## psutil
psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling, limiting process resources and the management of running processes. It implements many functionalities offered by command line tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap.
#### Install 
The easiest way to install psutil is with pip
#### RedHat / CentOS
```sh
$ sudo yum install gcc python-devel python-pip -y
$ pip install psutil
```
#### Ubuntu / Debian
```sh
$ sudo apt-get install gcc python-dev python-pip
$ pip install psutil
```
