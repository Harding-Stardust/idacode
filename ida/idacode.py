#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r''' This is fork of https://github.com/ioncodes/idacode that works with Cursor (Visual Stuido Fork with AI support) '''

__version__ = "2025-12-15 14:40:13"
__author__ = "Harding"
__description__ = __doc__
__copyright__ = "Copyright 2025"
__credits__ = ["https://github.com/ioncodes/idacode/"]
__license__ = "GPL 3.0"
__maintainer__ = "Harding"
__email__ = "not.at.the.moment@example.com"
__status__ = "Development"
__url__ = "https://github.com/Harding-Stardust/idacode"

import idacode_utils.plugin as plugin

def PLUGIN_ENTRY():
    return plugin.IDACode()