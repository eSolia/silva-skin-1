
from five import grok
import os

from silvatheme.esolia.interfaces import IESoliaHTMLExportLayer
from silva.export.html.interfaces import IHTMLExportSettings
from silva.core.views import views as silvaviews
from silva.core.views.interfaces import IVirtualSite
from silva.core.layout.porto.porto import Navigation


class ExportLayout(silvaviews.Layout):
    grok.template('exportlayout')
    grok.layer(IESoliaHTMLExportLayer)

    def update(self):
        settings = IHTMLExportSettings(self.request)
        settings.add_resource('.static', where=globals())
        self.resources_url = os.path.join(
            os.path.dirname(IVirtualSite(self.request).get_root_url()),
            '.static')


# We reuse the standard navigation code.
class ExportNavigation(Navigation):
    grok.layer(IESoliaHTMLExportLayer)

    navigation_depth = -1

    def get_root(self):
        return IVirtualSite(self.request).get_root()

