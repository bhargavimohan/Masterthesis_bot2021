# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import sys
import traceback
from datetime import datetime
from http import HTTPStatus
import jinja2
import aiohttp_jinja2

from aiohttp import web
import json
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.schema import Activity, ActivityTypes
from bots import TeamsMessagingExtensionsActionPreviewBot, database
from config import DefaultConfig

import logging
import os
#
logging.basicConfig(level=logging.DEBUG)

CONFIG = DefaultConfig()


# Create adapter.
# See https://aka.ms/about-bot-adapter to learn more about how bots work.
SETTINGS = BotFrameworkAdapterSettings(CONFIG.APP_ID, CONFIG.APP_PASSWORD)
ADAPTER = BotFrameworkAdapter(SETTINGS)


# Catch-all for errors.
async def on_error(context: TurnContext, error: Exception):
    # This check writes out errors to console log .vs. app insights.
    # NOTE: In production environment, you should consider logging this to Azure
    #       application insights.
    print(f"\n [on_turn_error] unhandled error: {error}", file=sys.stderr)
    traceback.print_exc()

    # Send a message to the user
    await context.send_activity("The bot encountered an error or bug.")
    await context.send_activity(
        "To continue to run this bot, please fix the bot source code."
    )
    # Send a trace activity if we're talking to the Bot Framework Emulator
    if context.activity.channel_id == "emulator":
        # Create a trace activity that contains the error object
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error Trace",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        # Send a trace activity, which will be displayed in Bot Framework Emulator
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error


# Create the Bot
BOT = TeamsMessagingExtensionsActionPreviewBot()


# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler.

    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    activity = Activity().deserialize(body)

    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    invoke_response = await ADAPTER.process_activity(


        activity, auth_header, BOT.on_turn
    )

    if invoke_response:
        return json_response(
            data=invoke_response.body, status=invoke_response.status
        )

    return Response(status=HTTPStatus.OK)


@aiohttp_jinja2.template("dashboard.html")
async def dashboard(request):
    # return web.Response(
    #     text='<h1>Hello!</h1>',
    #     content_type='text/html')   
    try:
        param = request._rel_url.query_string
        param = param.strip('channelid=')
        response_obj_tables = database.get_channel_details(param)
        response_obj_decisions = database.get_all_decisions(param)
        ## rErroreturn a success json response with status code 200 i.e. 'OK'
        return {"decisions_list": response_obj_decisions,"tables_list":response_obj_tables}
    except Exception as e:
        ## Bad path where name is not set
        return e

@aiohttp_jinja2.template("config.html")
async def config(request):
    # return web.Response(
    #     text='<h1>Hello!</h1>',
    #     content_type='text/html')   
    try:
        return {}
    except Exception as e:
        ## Bad path where name is not set
        return e


def init_func(argv):
    #APP = web.Application()
    APP = web.Application(middlewares=[aiohttp_error_middleware])

    aiohttp_jinja2.setup(
        APP, loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
    )

    APP.router.add_post("/api/messages", messages)
    APP.router.add_get("/dashboard", dashboard)
    APP.router.add_get("/config", config)
    return APP


if __name__ == "__main__":
    APP = init_func(None)
    try:
        web.run_app(APP, host="0.0.0.0", port=CONFIG.PORT)
    except Exception as error:
        raise error
