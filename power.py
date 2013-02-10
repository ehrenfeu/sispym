#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sispm

def process_sispm():
    outlet = None
    action = None
    fs = cgi.FieldStorage()
    if 'outlet' in fs:
        outlet = fs['outlet'].value
    if 'action' in fs:
        action = fs['action'].value

    if not ((outlet is None) or (action is None)):
        status = True
        if (action == 'True'):
            status = True
        if (action == 'False'):
            status = False
        dev.set_outlet_enabled(int(outlet), status)

    for outlet in range(dev.get_num_outlets()):
        status = dev.get_outlet_enabled(outlet)
        status_name = 'OFF';
        if status:
            status_name = 'ON'
        toggle = "<a href='power.py?outlet=%s&action=%s'>%s</a>" % \
            (outlet, not(status), status_name)
        print "Status of outlet %s: %s<br/><br/>" % (outlet, toggle)


print "Content-Type: text/html"
print
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"'
print '"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
print '<html>'
print '<header>'
print '<title>SISPM power manager</title>'
print '</header>'
print '<body>'
print '<div align="center">'
print "<a href='power.py'>sispm power control</a><br/><br/>"

try:
    dev=sispm.Sispm()
    process_sispm()
except sispm.SispmException as e:
    print "error: %s" % e


print '</div>'
print '</body>'
print '</html>'


# from subprocess import call
# from subprocess import Popen, PIPE
# for socket in [1, 2, 3, 4]:
#     p = Popen(["sispmctl", "-q", "-g", str(socket)], stdout=PIPE)
#     out, err = p.communicate()
#     toggle = "<a href='power_toggle_%s.py'>%s</a>" % (socket, out)
#     print "Status of outlet %s: %s<br/><br/>" % (socket, toggle)
