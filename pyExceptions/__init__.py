# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#              _____                    _   _
#  _ __  _   _| ____|_  _____ ___ _ __ | |_(_) ___  _ __  ___
# | '_ \| | | |  _| \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \/ __|
# | |_) | |_| | |___ >  < (_|  __/ |_) | |_| | (_) | | | \__ \
# | .__/ \__, |_____/_/\_\___\___| .__/ \__|_|\___/|_| |_|___/
# |_|    |___/                   |_|
# ==============================================================================
# Authors:            Patrick Lehmann
#
# Python Module:      This module contains exception base classes and common exceptions.
#
# License:
# ==============================================================================
# Copyright 2017-2020 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Technische Universität Dresden - Germany
#                     Chair of VLSI-Design, Diagnostics and Architecture
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
# ==============================================================================
#
from SphinxExtensions import DocumentMemberAttribute


__api__ = [
	'ExceptionBase',
	'EnvironmentException',
	'PlatformNotSupportedException',
	'NotConfiguredException'
]
__all__ = __api__


class ExceptionBase(Exception):
	"""
	Base exception derived from :py:exc:`Exception <python:Exception>` for all
	custom exceptions.
	"""

	@DocumentMemberAttribute()
	def __init__(self, message : str =""):
		"""pyExceptions initializer
		:param message:   The exception message.
		"""
		super().__init__()
		self.message = message

	@DocumentMemberAttribute()
	def __str__(self):
		"""Returns the exception's message text."""
		return self.message

	@DocumentMemberAttribute(False)
	def with_traceback(self, tb):
		super().with_traceback(tb)

	# @DocumentMemberAttribute(False)
	# @MethodAlias(pyExceptions.with_traceback)
	# def with_traceback(self): pass

class EnvironmentException(ExceptionBase):
	"""``EnvironmentException`` is raised when an expected environment variable is
	missing.
	"""

class PlatformNotSupportedException(ExceptionBase):
	"""``PlatformNotSupportedException`` is raise if the platform is not supported.
	"""

class NotConfiguredException(ExceptionBase):
	"""``NotConfiguredException`` is raise if the requested setting is not
	configured.
	"""
