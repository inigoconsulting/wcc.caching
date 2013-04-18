from five import grok
from Products.CMFCore.interfaces import IContentish
from zope.event import notify
from z3c.caching.purge import Purge
from wcc.caching.interfaces import IProductSpecific
grok.templatedir('templates')

class PurgeView(grok.View):
    grok.name('cachepurge')
    grok.require('cmf.ManagePortal')
    grok.template('purge_view')
    grok.context(IContentish)
    grok.layer(IProductSpecific)

    def update(self):
        if (self.request.method == 'POST' and 
            'purge' in self.request.keys()):
            
            notify(Purge(self.context))
