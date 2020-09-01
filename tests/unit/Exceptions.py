# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#              _____                    _   _
#  _ __  _   _| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___
# | '_ \| | | |  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __|
# | |_) | |_| | |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \
# | .__/ \__, |_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/
# |_|    |___/                   |_|
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Testing the pyExceptions module
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2020 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
"""
pyAttributes
############

:copyright: Copyright 2007-2020 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyExceptions import EnvironmentException, PlatformNotSupportedException, NotConfiguredException


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)

def raise_EnvironmentExecption():
	raise EnvironmentException()

def raise_PlatformNotSupportedException():
	raise PlatformNotSupportedException()

def raise_NotConfiguredException():
	raise NotConfiguredException()


class CallByReference_AnyParam(TestCase):
	def test_EnvironmentException(self):
		with self.assertRaises(EnvironmentException):
			raise_EnvironmentExecption()

	def test_PlatformNotSupportedException(self):
		with self.assertRaises(PlatformNotSupportedException):
			raise_PlatformNotSupportedException()

	def test_NotConfiguredException(self):
		with self.assertRaises(NotConfiguredException):
			raise_NotConfiguredException()
