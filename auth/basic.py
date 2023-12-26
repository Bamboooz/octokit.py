# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

from base64 import b64encode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Session
    from https.credentials import Credentials


class BasicAuthentication:
    @staticmethod
    def authenticate(session: Session, credentials: Credentials):
        user = credentials.provided_credentials.get("user")
        password = credentials.provided_credentials.get("password")

        assert user, "Basic auth username cannot be empty or None."
        assert password, "Basic auth password cannot be empty or None."

        utf_8_credentials = f"{user}:{password}".encode('utf-8')
        base64_credentials = b64encode(utf_8_credentials)
        encoded_credentials = base64_credentials.decode('utf-8')

        header_auth = f"Basic {encoded_credentials}"
        session.headers["Authorization"] = header_auth
