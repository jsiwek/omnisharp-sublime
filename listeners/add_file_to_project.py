import os
import sublime
import sublime_plugin
import logging

from ..lib import helpers
from ..lib import omnisharp

log = logging.getLogger(__name__)

class OmniSharpAddFileToProjectEventListener(sublime_plugin.EventListener):

    def on_post_save(self, view):
        if not helpers.is_csharp(view):
            return
        omnisharp.get_response(view, '/addtoproject', self._handle_addtoproject)


    def _handle_addtoproject(self, data):
        log.debug('file added to project')
        log.debug(data)


