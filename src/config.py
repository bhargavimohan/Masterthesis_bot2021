#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

os.environ["D3_DATABASE_PATH"] = '/home/bhargavi/Documents/Masterthesis_bot2021/src/database.json'

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "5a0f653d-152c-4a78-ab1a-d199ad22312e")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "YVSn~K-fn_59V6TgNPpWyeDa56kz7.JFfT")

    #bhargavi@mstbotdev.onmicrosoft.com
