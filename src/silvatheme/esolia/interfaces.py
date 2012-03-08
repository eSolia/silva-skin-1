
from five import grok
from silva.core import conf as silvaconf
from silva.export.html.interfaces import IDefaultHTMLExportSkin
from silva.export.html.interfaces import IHTMLExportLayer


class IESoliaHTMLExportLayer(IHTMLExportLayer):
    silvaconf.resource('export.css')


class IESoliaHTMLExportSkin(IESoliaHTMLExportLayer, IDefaultHTMLExportSkin):
    grok.skin('ESolia HTML export')

