import os
import sublime
import sublime_plugin
import logging

from ..lib import omnisharp
from ..lib import helpers

log = logging.getLogger(__name__)

class OmniSharpFixCodeIssue(sublime_plugin.TextCommand):
    data = None

    def run(self, edit):
        if self.data is None:
            omnisharp.get_response(
               self.view, '/fixcodeissue', self._handle_fixcodeissue)
        else:
            self._fixcodeissue(edit)

    def _handle_fixcodeissue(self, data):
        log.debug('fixcodeissue response is:')
        log.debug(data)
        if data is None:
            return
        self.data = data
        self.view.run_command('omni_sharp_fix_code_issue')

    def _fixcodeissue(self, edit):
        log.debug('fixcodeissue is :')
        log.debug(self.data)
        if self.data != None:
            region = sublime.Region(0, self.view.size())
            self.view.replace(edit, region, self.data["Text"])
        self.data = None

    def is_enabled(self):
        return helpers.is_csharp(self.view)
