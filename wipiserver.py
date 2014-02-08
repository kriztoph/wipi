from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

import cgi

class FormPage(Resource):
    def render_GET(self, request):
        return '<html><body><form method="POST">SSID: <input name="ssid" type="text" /><br/>PASSWORD: <input type="password" name="password"/><br/><input type="submit" /></form></body></html>'

    def render_POST(self, request):
        ssid = cgi.escape(request.args["ssid"][0])
        password = cgi.escape(request.args["password"][0])
        f = open('/etc/network/interfaces', 'w')
        f.write('auto lo\niface lo inet loopback\niface eth0 inet dhcp\nallow-hotplug wlan0\nauto wlan0\niface wlan0 inet dhcp\nwpa-ssid "{0}"\nwpa-psk "{1}"\n'.format(ssid, password))
        f.close
        return '<html><body>Successfully saved your wifi settings. Please reboot your Pi. :)</body></html>'

root = Resource()
root.putChild("form", FormPage())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
