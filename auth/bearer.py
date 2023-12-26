# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Session
    from https.credentials import Credentials


class BearerAuthentication:
    @staticmethod
    def authenticate(session: Session, credentials: Credentials):
        token = credentials.provided_credentials.get("token")

        assert token, "Bearer auth token cannot be empty or None."

        header_auth = f"Bearer {token}"
        session.headers["Authorization"] = header_auth
