#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "5a0f653d-152c-4a78-ab1a-d199ad22312e")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "kiX0v85-.z9x3O~lD5l9_SatgCez.r8HVi")
