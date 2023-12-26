# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from enum import Enum


class AuthType(Enum):
    ANONYMOUS = 0
    BASIC = 1
    OAUTH = 2
    BEARER = 3
