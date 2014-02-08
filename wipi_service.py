import select
import sys
import pybonjour

def register_callback(sdRef, flags, errorCode, name, regtype, domain):
    if errorCode == pybonjour.kDNSServiceErr_NoError:
        started = 1

sdRef = pybonjour.DNSServiceRegister(name = 'WipiService',
                                     regtype = '_wipi._tcp',
                                     port = 3210)
                                     callBack = register_callback)

try:
    try:
        while True:
            ready = select.select([sdRef], [], [])
            if sdRef in ready[0]:
                pybonjour.DNSServiceProcessResult(sdRef)
    except KeyboardInterrupt:
        pass
finally:
    sdRef.close()
