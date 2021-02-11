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
    create_adaptive_card_editor,
    create_adaptive_card_preview,
    create_error_card_editor,
    create_vmodel_card_editor,

)

from tinydb import TinyDB, Query, where
db = TinyDB('database.json')
table = db.table('Initializedchanels')
ch = Query()



class TeamsMessagingExtensionsActionPreviewBot(TeamsActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        text_command = turn_context._activity.text
        channel_name = turn_context._activity.recipient.name
        
        D3driverinitcommand = '<at>Preview Messaging Extension</at> initialize\n'
        D3driverdelcommand = '<at>Preview Messaging Extension</at> delete\n'         
        value = turn_context.activity.value

        if value is not None:
            vmodelname = value["Choices"] if "Choices" in value else ""

            result = table.search(ch[channel_name].exists())
            if(len(result) == 0):
                table.insert({channel_name: vmodelname})
                reply = MessageFactory.text(
                    f"{turn_context.activity.from_property.name} chose '{vmodelname}'."
                )
                await turn_context.send_activity(reply)
            else:
                reply = MessageFactory.text(
                    "Model '{}' already exists for Channel '{}', please delete and reset if required.".format(
                        result[0][channel_name],
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
            table.remove(where(channel_name) == 'Domain-specific')
            reply = MessageFactory.text(
            "This channel is no more initialized. To re-initialize the channel, please enter "
            "@Preview Messaging Extension initialize"
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
        channel_name = turn_context._activity.recipient.name
        # vmodelname = 'Model-based'
        result = table.search(ch[channel_name] == vmodelname)
        if(len(result) >= 1):
                #table.remove(where(channel_name) == vmodelname)
            card = create_adaptive_card_editor()
            task_info = TaskModuleTaskInfo(
                card=card, height=450, title="Design decision card", width=500
            )
            continue_response = TaskModuleContinueResponse(value=task_info)
            return MessagingExtensionActionResponse(task=continue_response)
        else:
            reply = MessageFactory.text(
            "Hi there! Please initialize your channel before accessing the cards. The command to intialize your current channel is " 
            "@Preview Messaging Extension initialize"
            )
            await turn_context.send_activity(reply)

    async def on_teams_messaging_extension_submit_action(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:
        preview_card = create_adaptive_card_preview(
            user_text=action.data["Question"],
            is_multi_select=action.data["MultiSelect"],
            option1=action.data["Option1"],
            option2=action.data["Option2"],
            option3=action.data["Option3"],
        )

        extension_result = MessagingExtensionResult(
            type="botMessagePreview",
            activity_preview=MessageFactory.attachment(preview_card),
        )
        return MessagingExtensionActionResponse(compose_extension=extension_result)

    async def on_teams_messaging_extension_bot_message_preview_edit(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:
        activity_preview = action.bot_activity_preview[0]
        content = activity_preview.attachments[0].content
        data = self._get_example_data(content)
        card = create_adaptive_card_editor(
            data.question,
            data.is_multi_select,
            data.option1,
            data.option2,
            data.option3,
        )
        task_info = TaskModuleTaskInfo(
            card=card, height=450, title="Task Module Fetch Example", width=500
        )
        continue_response = TaskModuleContinueResponse(value=task_info)
        return MessagingExtensionActionResponse(task=continue_response)

    async def on_teams_messaging_extension_bot_message_preview_send(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:
        activity_preview = action.bot_activity_preview[0]
        content = activity_preview.attachments[0].content
        data = self._get_example_data(content)
        card = create_adaptive_card_preview(
            data.question,
            data.is_multi_select,
            data.option1,
            data.option2,
            data.option3,
        )
        message = MessageFactory.attachment(card)
        await turn_context.send_activity(message)

    def _get_example_data(self, content: dict) -> ExampleData:
        body = content["body"]
        question = body[1]["text"]
        choice_set = body[3]
        multi_select = "isMultiSelect" in choice_set
        option1 = choice_set["choices"][0]["value"]
        option2 = choice_set["choices"][1]["value"]
        option3 = choice_set["choices"][2]["value"]
        return ExampleData(question, multi_select, option1, option2, option3)
