# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Session
    from https.credentials import Credentials


class OAuthAuthentication:
    @staticmethod
    def authenticate(session: Session, credentials: Credentials):
        client_id = credentials.provided_credentials.get("client_id")
        client_secret = credentials.provided_credentials.get("client_secret")

        assert client_id, "OAuth auth client id cannot be empty or None."
        assert client_secret, "OAuth auth client secret cannot be empty or None."

        # todo: implement setting the request authorization to oauth app, currently idk how to do that
