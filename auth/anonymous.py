# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Session
    from https.credentials import Credentials


class AnonymousAuthentication:
    @staticmethod
    def authenticate(session: Session, credentials: Credentials):
        return  # Do nothing, retain anonymity.
