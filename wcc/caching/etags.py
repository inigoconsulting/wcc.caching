from zope.interface import implements
from zope.interface import Interface

from zope.component import adapts
from plone.app.caching.interfaces import IETagValue

from five import grok
import time

class HourlyETag(grok.MultiAdapter):

    grok.name('hoursSinceEpoch')
    grok.implements(IETagValue)
    grok.adapts(Interface, Interface)

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def __call__(self):
        return str(int(time.time()/60/60))
