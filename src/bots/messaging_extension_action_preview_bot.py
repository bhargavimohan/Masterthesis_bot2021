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
    create_ad_adaptive_card_editor,
    create_dc_adaptive_card_editor,
    create_imp_adaptive_card_editor,
    create_adaptive_card_preview,
    create_error_card_editor,
    create_vphase_card_editor,

)

from tinydb import TinyDB, Query, where
from tinydb.operations import delete

from bots import database

class TeamsMessagingExtensionsActionPreviewBot(TeamsActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
         
        if turn_context.activity.conversation.conversation_type != 'personal':
            text_command = turn_context.activity.text        
            D3driverinitcommand = '<at>D3driver</at> init \n'
            D3driverdelcommand = '<at>D3driver</at> del \n' 
            value = turn_context.activity.value
            channel_name = turn_context.activity.conversation.name
            if channel_name is None:
                channel_name = 'General'
            channel_id = turn_context.activity.channel_data['channel']['id']
            conversation_id = turn_context.activity.conversation.id #to distinguish 'Generals' of different teams
            if value is not None:
                vphase = value["Choices"] if "Choices" in value else ""
                member = turn_context.activity.from_property.name
                year = str(turn_context.activity.local_timestamp.year)
                month = str(turn_context.activity.local_timestamp.month)
                day = str(turn_context.activity.local_timestamp.day)
                cardsentdate = year + "-" + month + "-" + day
                result = database.find_channel_exists(channel_id)
                if(len(result) == 0):
                    # database.insert_channel()
                    database.insert_channel(channel_id,channel_name,vphase,member,cardsentdate)
                    reply = MessageFactory.text(
                        f"{turn_context.activity.from_property.name} chose '{vphase}' phase for this channel."
                    )
                    await turn_context.send_activity(reply)
                else:
                    reply = MessageFactory.text(
                        "The phase - '{}' in a V-model has been selected for Channel '{}', please use command '@D3driver del' and reset if required.".format(
                            result[0]["channel"]["vphase"],
                            channel_name)
                    )
                    await turn_context.send_activity(reply)

            elif text_command == D3driverinitcommand:
                        #vphase = 'Model-based'
                result = database.find_channel_exists(channel_id)
                if(len(result) == 0):
                    card = create_vphase_card_editor()
                    task_info = TaskModuleTaskInfo(
                    card=card, height=450, title="Design decision card", width=500
                        )
                    message = MessageFactory.attachment(card)
                    response_id = await turn_context.send_activity(message)
                else:
                    reply = MessageFactory.text(
                        "The phase - '{}' in a V-Model has been selected for Channel '{}', please use command '@D3driver del' and reset if required.".format(
                            result[0]["channel"]["vphase"],
                            channel_name)
                    )
                    await turn_context.send_activity(reply)
                # new_activity = MessageFactory.text("This card has been disable")
                # new_activity.id = response_id.id
                # update_result = await turn_context.update_activity(new_activity)



            elif text_command == D3driverdelcommand:
                database.delete_channel(channel_id)
                database.delete_decision(channel_id)
                reply = MessageFactory.text(
                "This channel is no more initialized. All the design decsions(if discussed) has been deleted from the database. To re-initialize the channel, please enter "
                "@D3driver init"
                )
                await turn_context.send_activity(reply)

            else:
                reply = MessageFactory.text(
                "Hello from ***D3driver!*** Congratulations on choosing one of the best practices of clean "
                "documentation. Please follow apropriate instructions: "
                "***'@D3driver init' - To start accessing decision cards*** and "
                "***'@D3driver del'  - To reset the phase in which you would like to document your design decisions***"
                )
                await turn_context.send_activity(reply)
        else:
            reply = MessageFactory.text(
            "Hi there! Welcome to ***D3driver***. Congratulations on choosing one of the best practices of clean "
            "documentation. Please follow apropriate instructions: "
            "***'@D3driver init' - To start accessing decision cards*** and "
            "***'@D3driver del'  - To reset the phase in which you would like to document your design decisions***"
            )
            await turn_context.send_activity(reply)
            
        

    async def on_teams_messaging_extension_fetch_task(
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:
        channel_id = turn_context.activity.channel_data['channel']['id']
        conversation_id = turn_context.activity.conversation.id #to distinguish 'Generals' of different teams
        # TODO: If channel in initialzed table, then continue with normal card, else show error card
        channel_name = turn_context.activity.conversation.name
        if channel_name is None:
            channel_name = 'General'
        #vphase = value["Choices"]
        result = database.find_channel_exists(channel_id)
        if(len(result) == 1):
            if(result[0]["channel"]["vphase"] == 'Architecture Design'):
                card = create_ad_adaptive_card_editor()
                task_info = TaskModuleTaskInfo(
                    card=card, height=450, title="Design decision card", width=500
                )
                continue_response = TaskModuleContinueResponse(value=task_info)
                return MessagingExtensionActionResponse(task=continue_response)
            elif(result[0]["channel"]["vphase"] == 'Design/concept'):
                card = create_dc_adaptive_card_editor()
                task_info = TaskModuleTaskInfo(
                    card=card, height=450, title="Design decision card", width=500
                )
                continue_response = TaskModuleContinueResponse(value=task_info)
                return MessagingExtensionActionResponse(task=continue_response)
            elif(result[0]["channel"]["vphase"] == 'Implementation'):
                card = create_imp_adaptive_card_editor()
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

        text_command = turn_context.activity.text        
        D3driverdelcommand = '<at>D3driver</at> del \n'  




        channel_id = turn_context.activity.channel_data['channel']['id']
        year = str(turn_context.activity.local_timestamp.year)
        month = str(turn_context.activity.local_timestamp.month)
        day = str(turn_context.activity.local_timestamp.day)
        decisiondate = year + "-" + month + "-" + day
        channel_name = turn_context._activity.conversation.name
        if channel_name is None:
            channel_name = 'General'
        # result = table.search(ch['channel']['name'] == channel_name)
        result = database.find_channel_exists(channel_id)
        if(result[0]["channel"]["vphase"] == 'Architecture Design'):
            a="Functional design decision"
            b="Logical design decision"
            c="Physical design decision"
        elif(result[0]["channel"]["vphase"] == 'Design/concept'):
            a="Design definition desisions"
            b="Design characteristics and enablers desicions"
            c="Design alterantives decisions"
        elif(result[0]["channel"]["vphase"] == 'Implementation'):
            a="Mechanical design decisions"
            b="Electrical design decisions"
            c="Software design decisions"


        user_text1 = action.data["Question1"],
        user_text2 = action.data["Question2"],
        user_text3 = action.data["Question3"],

        

        
        # activity_preview = action.bot_activity_preview[0]
        # content = activity_preview.attachments[0].content
        # data = self._get_example_data(content)
        if(user_text1[0] == ''):
            a = ''
        if(user_text2[0] == ''):
            b = ''
        if(user_text3[0] == ''):
            c = ''
        



   
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

        # db entries
        if(result[0]["channel"]["vphase"] == 'Architecture Design'):
            database.insert_decision(channel_id,channel_name,memberid,decisiondate,a,user_text1,b,user_text2,c,user_text3)
        elif(result[0]["channel"]["vphase"] == 'Design/concept'):
            database.insert_decision(channel_id,channel_name,memberid,decisiondate,a,user_text1,b,user_text2,c,user_text3)
        elif(result[0]["channel"]["vphase"] == 'Implementation'):
            database.insert_decision(channel_id,channel_name,memberid,decisiondate,a,user_text1,b,user_text2,c,user_text3)
        

        if (user_text1[0] or user_text2[0] or user_text3[0] != ''):
            message = MessageFactory.attachment(card)
            await turn_context.send_activity(message)
    
            return MessagingExtensionActionResponse()
        else:  
            reply = MessageFactory.text(
            "Error. No decision made"
            )
            await turn_context.send_activity(reply) 
            
        

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
