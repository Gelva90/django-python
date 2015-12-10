import xml.etree.ElementTree as ET
import sys
import getopt
try: 
    nmapresult = sys.argv[1]
except:
    print "XML doc"
if nmapresult:
    #print nmapresult
    tree = ET.parse(nmapresult)
    #print nmapresult
    #output = []
    doc = tree.getroot()
    print doc
    hostname = doc.find('name')
    #hostname = ''
    #ip = ''
    #ports = ''
    print hostname
    #addresses = host.getElementsByTagName("address")
    #ip = addresses[0].getAttribute("addr")
    #print ip
    #manyports = host.getElementsByTagName("port")
    #print ports
    """for p in manyports:
        try:
            if p.getAttribute("key") == 'portid':
                if portid == '':
                    portid = p.childNodes[0].nodeValue
        except:
            pass
    print p#"".join([str(x) for x in p] )
    output.append(ip + ',' + ports)
for i in output:
    print i"""