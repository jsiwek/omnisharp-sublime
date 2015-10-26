import os
import sublime
import sublime_plugin
import logging

from ..lib import helpers
from ..lib import omnisharp

log = logging.getLogger(__name__)

class OmniSharpRemoveFromProject(sublime_plugin.WindowCommand):
    def run(self):
        omnisharp.get_response(sublime.active_window().active_view(), '/removefromproject', self._handle_removetoproject)

    def is_enabled(self):
        return helpers.is_csharp(sublime.active_window().active_view())

    def _handle_removetoproject(self, data):
        log.debug('file removed from project')
