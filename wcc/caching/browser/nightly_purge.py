from five import grok
from Products.CMFCore.interfaces import ISiteRoot
from zope.event import notify
from z3c.caching.purge import Purge
from wcc.homepage.interfaces import IBaseHomepage
from wcc.caching.utils import syncPurge
from wcc.prayercycle.content.prayercycle import IPrayerCycle
from wcc.caching.interfaces import IPurgeNightly

class NightlyPurge(grok.View):
    grok.name('nightly-purge')
    grok.context(ISiteRoot)

    def render(self):
        urls = []
        urls += self.flush_by_iface(IBaseHomepage)
        urls += self.flush_by_iface(IPrayerCycle)
        urls += self.flush_by_iface(IPurgeNightly)
        return u'Flushed\n%s' % ('\n'.join(urls))

    def flush_by_iface(self, iface):
        brains = self.context.portal_catalog(
            object_provides=iface.__identifier__,
            Language='all',
        )

        urls = []
        for brain in brains:
            obj = brain.getObject()
            syncPurge(obj)
            urls.append(obj.absolute_url())
        return urls
