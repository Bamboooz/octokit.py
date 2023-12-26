# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from auth.authenticator import Authenticator, AuthType


github_api_url = "https://api.github.com/"
github_url = "https://github.com/"


class GitHubClient:
    def __init__(self):
        self.authenticator = None
