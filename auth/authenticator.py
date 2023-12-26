# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

from auth.anonymous import AnonymousAuthentication
from auth.basic import BasicAuthentication
from auth.bearer import BearerAuthentication
from auth.oauth import OAuthAuthentication
from auth.type import AuthType

if TYPE_CHECKING:
    from https.credentials import Credentials
    from requests import Session


authenticators = {
    AuthType.ANONYMOUS: AnonymousAuthentication,
    AuthType.BASIC: BasicAuthentication,
    AuthType.OAUTH: OAuthAuthentication,
    AuthType.BEARER: BearerAuthentication
}


class Authenticator:
    def __init__(self, credentials: Credentials):
        self.credentials = credentials
        self.auth_type = credentials.auth_type

    def apply(self, session: Session):
        authenticators[self.auth_type].authenticate(session, self.credentials)
