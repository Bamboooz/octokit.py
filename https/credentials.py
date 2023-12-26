# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from auth.authenticator import AuthType

from exceptions import (
    OctokitAuthUnexpectedArguments,
    OctokitAuthExpectedArguments
)


credentials_params = {
    AuthType.ANONYMOUS: [],
    AuthType.BASIC: ["user", "password"],
    AuthType.OAUTH: ["client_id", "client_secret"],
    AuthType.BEARER: ["token"]
}


class Credentials:
    def __init__(self, auth_type: AuthType, **kwargs):
        self.auth_type = auth_type
        self.provided_credentials = kwargs

        self._validate_credentials()

    def _validate_credentials(self):
        required_kwargs = credentials_params.get(self.auth_type)
        provided_kwargs = self.provided_credentials

        unexpected_keys = set(provided_kwargs.keys()) - set(required_kwargs)
        missing_keys = [key for key in required_kwargs if key not in provided_kwargs]

        if unexpected_keys:
            raise OctokitAuthUnexpectedArguments(f"Unexpected parameter(s) for {self.auth_type}: {', '.join(unexpected_keys)}")

        if missing_keys:
            raise OctokitAuthExpectedArguments(f"Missing required parameter(s) for {self.auth_type}: {', '.join(missing_keys)}")
