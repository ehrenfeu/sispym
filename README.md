SisPyM
======

Python based web interface for Gembird SIS-PM controllable power outlets.

Requirements
============

Requires the sispm Python module available from the `extra` section of the
sispmctl package (e.g. available from http://github.com/anlumo/sispmctl.git).

Installation
============

This can be used for example with mini-httpd by linking to this repository with
a speaking name (e.g. `power`) and adjusting the cgi path in
`/etc/mini-httpd.conf` like this:

```
cgipat=cgi/*|power/*
```
