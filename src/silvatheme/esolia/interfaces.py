
from five import grok
from silva.core import conf as silvaconf
from silva.export.html.interfaces import IDefaultHTMLExportSkin
from silva.export.html.interfaces import IHTMLExportLayer
from silva.core.layout.porto.interfaces import IPorto
from silva.core.layout.interfaces import ISilvaSkin


class IESoliaHTMLExportLayer(IHTMLExportLayer):
    silvaconf.resource('export.css')


class IESoliaHTMLExportSkin(IESoliaHTMLExportLayer, IDefaultHTMLExportSkin):
    grok.skin('ESolia HTML export')


class IESoliaLayer(IPorto):
    """ESolia public layer.
    """


class IESoliaSkin(IESoliaLayer, ISilvaSkin):
    """Public skin for ESolia.
    """
    grok.skin('ESolia')
