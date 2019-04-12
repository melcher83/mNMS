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
                 print('%s = %s' % varBind)
                 t.append('%s = %s' % varBind)
    return t



x=walk('10.1.8.101', '1.0.8802.1.1.2.1.4.1.1.5')



n = len(x)-1
print (n)
while n != -1:
    x[n]=x[n].split('.')
    n=n-1


n=len(x)-1

print (x)

while n != -1:
    x[n] = x[n][13]
    n = n - 1





print (x)


