#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tests/templates.py
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

import unittest

from king_phisher import testing
from king_phisher.templates import *
from king_phisher.utilities import random_string

class TemplatesTests(testing.KingPhisherTestCase):
	def test_global_variables(self):
		# prepend an alphabetic character so the result is a valid identifier
		test_key = 'a' + random_string(10)
		test_value = random_string(20)
		global_vars = {test_key: test_value}
		env = TemplateEnvironmentBase(global_vars=global_vars)
		test_string = '<html>{{ ' + test_key + ' }}</html>'
		template = env.from_string(test_string)
		result = template.render()
		self.assertIn(test_value, result)
		self.assertNotIn(test_key, result)

	def test_strings_are_not_escaped(self):
		env = TemplateEnvironmentBase()
		test_string = '<html>{{ link }}</html>'
		link = '<a href="http://king-phisher.com/">Click Me</a>'
		template = env.from_string(test_string)
		result = template.render(link=link)
		self.assertIn(link, result)

	def test_decoding_filters(self):
		env = TemplateEnvironmentBase()
		tests = {
			'base16': '6B696E672D70686973686572',
			'base32': 'NNUW4ZZNOBUGS43IMVZA====',
			'base64': 'a2luZy1waGlzaGVy',
			'rot-13': 'xvat-cuvfure',
			'rot13': 'xvat-cuvfure',
			'hex': '6B696E672D70686973686572'
		}
		for encoding, value in tests.items():
			test_string = '{{ value | decode(encoding) }}'
			template = env.from_string(test_string)
			self.assertEqual(template.render(encoding=encoding, value=value), 'king-phisher')

	def test_encoding_filters(self):
		env = TemplateEnvironmentBase()
		tests = {
			'base16': '6B696E672D70686973686572',
			'base32': 'NNUW4ZZNOBUGS43IMVZA====',
			'base64': 'a2luZy1waGlzaGVy',
			'rot-13': 'xvat-cuvfure',
			'rot13': 'xvat-cuvfure',
			'hex': '6B696E672D70686973686572'
		}
		for encoding, value in tests.items():
			test_string = '{{ value | encode(encoding) }}'
			template = env.from_string(test_string)
			self.assertEqual(template.render(encoding=encoding, value='king-phisher'), value)

	def test_hash_filters(self):
		env = TemplateEnvironmentBase()
		tests = {
			'md5': 'C16B310ED4DF16EFE6FC788B3ED20F0A',
			'sha1': '2946F7BDE8D99F2B1B1C61D91EE8735F4D8F1B8F',
			'sha256': '214D38858B9816404C1465E77E0576D9DC1C8543D433D6581E91394D965F2CD2'
		}
		for algorithm, value in tests.items():
			test_string = '{{ value | hash(algorithm) | encode(\'hex\')}}'
			template = env.from_string(test_string)
			self.assertEqual(template.render(algorithm=algorithm, value='king-phisher'), value)

if __name__ == '__main__':
	unittest.main()
