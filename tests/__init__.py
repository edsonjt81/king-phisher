#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tests/__init__.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import logging
logging.getLogger('KingPhisher').addHandler(logging.NullHandler)
logging.getLogger('').setLevel(logging.CRITICAL)
logging.captureWarnings(True)

from .client import *
from .server import *

from .color import ColorConversionTests
from .find import FindTests
from .find import JSONSchemaDataTests
from .geoip import GeoIPTests
from .geoip import GeoIPRPCTests
from .ics import ICSTests
from .ipaddress import IPAddressTests
from .pipfile import PipfileLockTests
from .plugins import PluginRequirementsTests
from .security_keys import SecurityKeysTests
from .security_keys import SigningKeyTests
from .serializers import ElementTreeTests
from .serializers import JSONSerializerTests
from .serializers import MsgPackSerializerTests
from .sms import SMSTests
from .spf import SPFTests
from .templates import TemplatesTests
from .ua_parser import UserAgentParserTests
from .utilities import UtilitiesTests
from .version import VersionTests
from .xor import XORTests
