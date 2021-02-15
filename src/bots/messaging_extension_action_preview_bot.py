# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import (
    MessageFactory,
    TurnContext,
)
from botbuilder.schema.teams import (
    MessagingExtensionAction,
    MessagingExtensionActionResponse,
    TaskModuleContinueResponse,
    MessagingExtensionResult,
    TaskModuleTaskInfo,
)
from botbuilder.core.teams import TeamsActivityHandler
from example_data import ExampleData
from adaptive_card_helper import (
    create_domainspecific_adaptive_card_editor,
    create_incose_adaptive_card_editor,
    create_modelbased_adaptive_card_editor,
    create_adaptive_card_preview,
    create_error_card_editor,
    create_vmodel_card_editor,

)

from tinydb import TinyDB, Query, where
from tinydb.operations import delete
db = TinyDB('database.json')
table = db.table('Initializedchannelsanddata')
ch = Query()



class TeamsMessagingExtensionsActionPreviewBot(TeamsActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        text_command = turn_context._activity.text        
        D3driverinitcommand = '<at>D3driver</at> init\n'
        D3driverdelcommand = '<at>D3driver</at> del\n'         
        value = turn_context.activity.value
        channel_name = turn_context._activity.conversation.name
        if channel_name is None:
            channel_name = 'General'

        if value is not None:
            vmodelname = value["Choices"] if "Choices" in value else ""
            member = turn_context._activity.from_property.name
            year = str(turn_context._activity.local_timestamp.year)
            month = str(turn_context._activity.local_timestamp.month)
            day = str(turn_context._activity.local_timestamp.day)
            cardsentdate = year + "-" + month + "-" + day
            result = table.search(ch['channel']['name'] == channel_name)
            if(len(result) == 0):
                table.insert({'channel': {'name' : channel_name ,'vmodel' : vmodelname, 'membername' : member, 'date' : cardsentdate}})
                reply = MessageFactory.text(
                    f"{turn_context.activity.from_property.name} chose '{vmodelname}' V-model process for this channel."
                )
                await turn_context.send_activity(reply)
            else:
                reply = MessageFactory.text(
                    "V-Model process - '{}' has been selected for Channel '{}', please use command '@D3driver del' and reset if required.".format(
                        result[0]["channel"]["vmodel"],
                        channel_name)
                )
                await turn_context.send_activity(reply)

        elif text_command == D3driverinitcommand:
                    #vmodelname = 'Model-based'
            
            card = create_vmodel_card_editor()
            task_info = TaskModuleTaskInfo(
            card=card, height=450, title="Design decision card", width=500
                )
            message = MessageFactory.attachment(card)
            await turn_context.send_activity(message)
            
                        

        elif text_command == D3driverdelcommand:
            table.remove(where('channel').name == channel_name)
            reply = MessageFactory.text(
            "This channel is no more initialized. To re-initialize the channel, please enter "
            "@D3driver init"
            )
            await turn_context.send_activity(reply)
                    
        else:
            reply = MessageFactory.text(
            "Hello from D3driver! Please follow apropriate instructions."
            )
            await turn_context.send_activity(reply)
        

    async def on_teams_messaging_extension_fetch_task(
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:

        # TODO: If channel in initialzed table, then continue with normal card, else show error card
        channel_name = turn_context._activity.conversation.name
        if channel_name is None:
            channel_name = 'General'
        #vmodelname = value["Choices"]
        result = table.search(ch['channel']['name'] == channel_name)
        if(len(result) == 1):
            if(result[0]["channel"]["vmodel"] == 'Model-based'):
                card = create_modelbased_adaptive_card_editor()
                task_info = TaskModuleTaskInfo(
                    card=card, height=450, title="Design decision card", width=500
                )
                continue_response = TaskModuleContinueResponse(value=task_info)
                return MessagingExtensionActionResponse(task=continue_response)
            elif(result[0]["channel"]["vmodel"] == 'INCOSE'):
                card = create_incose_adaptive_card_editor()
                task_info = TaskModuleTaskInfo(
                    card=card, height=450, title="Design decision card", width=500
                )
                continue_response = TaskModuleContinueResponse(value=task_info)
                return MessagingExtensionActionResponse(task=continue_response)
            elif(result[0]["channel"]["vmodel"] == 'Domain-specific'):
                card = create_domainspecific_adaptive_card_editor()
                task_info = TaskModuleTaskInfo(
                    card=card, height=450, title="Design decision card", width=500
                )
                continue_response = TaskModuleContinueResponse(value=task_info)
                return MessagingExtensionActionResponse(task=continue_response)
        else: 
            reply = MessageFactory.text(
            "Hi there! Please initialize your channel before accessing the cards. The command to intialize your current channel is " 
            "@D3driver init"
            )
            await turn_context.send_activity(reply)

    async def on_teams_messaging_extension_submit_action(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:
    
        channel_name = turn_context._activity.conversation.name
        if channel_name is None:
            channel_name = 'General'
        result = table.search(ch['channel']['name'] == channel_name)
        if(result[0]["channel"]["vmodel"] == 'Model-based'):
            a="Functional design decision"
            b="Logical design decision"
            c="Physical design decision"
        elif(result[0]["channel"]["vmodel"] == 'INCOSE'):
            a="Design definition desisions"
            b="Design characteristics and enablers desicions"
            c="Design alterantives decisions"
        elif(result[0]["channel"]["vmodel"] == 'Domain-specific'):
            a="Mechanical design decisions"
            b="Electrical design decisions"
            c="Software design decisions"


        user_text1 = action.data["Question1"],
        user_text2 = action.data["Question2"],
        user_text3 = action.data["Question3"],

        # db entries
        # activity_preview = action.bot_activity_preview[0]
        # content = activity_preview.attachments[0].content
        # data = self._get_example_data(content)

   
        memberid = turn_context._activity.from_property.name
        card = create_adaptive_card_preview(
             user_text1[0],
             user_text2[0],
             user_text3[0],
             a,
             b,
             c,
             memberid,
        )
          
        message = MessageFactory.attachment(card)
        await turn_context.send_activity(message)

        return MessagingExtensionActionResponse()
        

    # async def on_teams_messaging_extension_bot_message_preview_edit(  # pylint: disable=unused-argument
    #     self, turn_context: TurnContext, action: MessagingExtensionAction
    # ) -> MessagingExtensionActionResponse:
    #     activity_preview = action.bot_activity_preview[0]
    #     content = activity_preview.attachments[0].content
    #     data = self._get_example_data(content)
    #     card = create_adaptive_card_editor(
    #         data.question,
    #         data.is_multi_select,
    #         data.option1,
    #         data.option2,
    #         data.option3,
    #     )
    #     task_info = TaskModuleTaskInfo(
    #         card=card, height=450, title="Task Module Fetch Example", width=500
    #     )
    #     continue_response = TaskModuleContinueResponse(value=task_info)
    #     return MessagingExtensionActionResponse(task=continue_response)

    # async def on_teams_messaging_extension_bot_message_preview_send(  # pylint: disable=unused-argument
    #     self, turn_context: TurnContext, action: MessagingExtensionAction
    # ) -> MessagingExtensionActionResponse:
    #     activity_preview = action.bot_activity_preview[0]
    #     content = activity_preview.attachments[0].content
    #     data = self._get_example_data(content)
    #     card = create_adaptive_card_preview(
    #         data.question,
    #         data.is_multi_select,
    #         data.option1,
    #         data.option2,
    #         data.option3,
    #     )
    #     message = MessageFactory.attachment(card)
    #     await turn_context.send_activity(message)

    def _get_example_data(self, content: dict) -> ExampleData:
        body = content["body"]
        question1 = body[1]["text"]
        question2 = body[2]["text"]
        question3 = body[3]["text"]
        return ExampleData(question1,question2, question3)
