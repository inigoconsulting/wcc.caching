from collective.grok import gs
from wcc.caching import MessageFactory as _

@gs.importstep(
    name=u'wcc.caching', 
    title=_('wcc.caching import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.caching.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
