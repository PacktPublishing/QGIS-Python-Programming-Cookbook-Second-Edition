# Changing the QGIS Web Proxy

from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import QNetworkRequest, QNetworkProxy

settings={"Proxy enabled": u'proxy/proxyEnabled', "Proxy Host ": u'proxy/proxyHost', "Proxy Port": u'proxy/proxyPort'}

home={"Proxy enabled": True, "Proxy Host ": "localhost", "Proxy Port": 8888}
office={"Proxy enabled": True, "Proxy Host ": "192.168.168.165", "Proxy Port": 8080}
cafe={"Proxy enabled": False, "Proxy Host ": "192.168.168.107", "Proxy Port": 8080}

current=home

s = QSettings() 

for key, val in settings.iteritems():
    settings_key=key
    for key2, val2 in current.iteritems():
        if key2==settings_key:
            settings_val=val2
    current_setting = s.value(str(val).decode('unicode-escape'))
    s.setValue(unicode(str(val)), settings_val)
s.sync()

proxyEnabled = s.value("proxy/proxyEnabled", "")
proxyType = s.value("proxy/proxyType", "" )
proxyHost = s.value("proxy/proxyHost", "" )
proxyPort = s.value("proxy/proxyPort", "" )
proxyUser = s.value("proxy/proxyUser", "" )
proxyPassword = s.value("proxy/proxyPassword", "" )
proxy = QNetworkProxy()
proxy.setType(QNetworkProxy.HttpProxy)
proxy.setHostName(proxyHost)
proxy.setPort(int(proxyPort))
proxy.setUser(proxyUser)
proxy.setPassword(proxyPassword)
QNetworkProxy.setApplicationProxy(proxy)
net_man=QgsNetworkAccessManager.instance()
stringlist= ""
net_man.setupDefaultProxyAndCache ()
net_man.setFallbackProxyAndExcludes(proxy, stringlist)
