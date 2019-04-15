from pysnmp.hlapi import *
import sys


def walk(host, oid):
    t = []

    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public'),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lookupMib=False,
                              lexicographicMode=False):


        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break

        else:

            for varBind in varBinds:
                 print(varBind)
                 t.append(varBind)
    return t




x=walk('10.1.8.101', '1.0.8802.1.1.2.1.4.2')  # 1.0.8802.1.1.2.1.4.2 Remote MGMT IP addresses

neighbor_mac=[]




test = pat.findall(str(x[1]))

print (str(test))

print ('X1: ' + str(x[1]))




print (x)


