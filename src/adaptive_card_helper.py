# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import CardFactory
from botbuilder.schema import Attachment

def create_modelbased_adaptive_card_editor(
    user_text1: str = None,
    user_text2: str = None,
    user_text3: str = None,
) -> Attachment:
    return CardFactory.adaptive_card(
        {
            "actions": [
                {
                    "data": {"submitLocation": "messagingExtensionFetchTask"},
                    "title": "Submit",
                    "type": "Action.Submit",
                }
            ],
            "body": [
                {
                    "text": "Here you can discuss Model-based design decisions",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {"type": "TextBlock", "text": "Functional design decisions:"},
                {
                    "id": "Question1",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text1,
                },
                {"type": "TextBlock", "text": "Logical design decisions:"},
                {
                    "id": "Question2",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text2,
                },
                {"type": "TextBlock", "text": "Physical design decisions:"},
                {
                    "id": "Question3",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text3,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )



def create_incose_adaptive_card_editor(
    user_text1: str = None,
    user_text2: str = None,
    user_text3: str = None,
) -> Attachment:
    return CardFactory.adaptive_card(
        {
            "actions": [
                {
                    "data": {"submitLocation": "messagingExtensionFetchTask"},
                    "title": "Submit",
                    "type": "Action.Submit",
                }
            ],
            "body": [
                {
                    "text": "Here you can discuss INCOSE design decisions",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {"type": "TextBlock", "text": " Design definition decisions:"},
                {
                    "id": "Question1",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text1,
                },
                {"type": "TextBlock", "text": "Design characteristics & Enablers decisions:"},
                {
                    "id": "Question2",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text2,
                },
                {"type": "TextBlock", "text": " Design Alternatives decisions:"},
                {
                    "id": "Question3",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text3,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )



def create_domainspecific_adaptive_card_editor(
    user_text1: str = None,
    user_text2: str = None,
    user_text3: str = None,
) -> Attachment:
    return CardFactory.adaptive_card(
        {
            "actions": [
                {
                    "data": {"submitLocation": "messagingExtensionFetchTask"},
                    "title": "Submit",
                    "type": "Action.Submit",
                }
            ],
            "body": [
                {
                    "text": "Here you can discuss Domain Specific design decisions",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {"type": "TextBlock", "text": "Mechanical design decisions:"},
                {
                    "id": "Question1",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text1,
                },
                {"type": "TextBlock", "text": "Electrical design decisions:"},
                {
                    "id": "Question2",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text2,
                },
                {"type": "TextBlock", "text": "Software design decisions:"},
                {
                    "id": "Question3",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text3,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )


def create_vmodel_card_editor(
    user_text: str = None,
    is_multi_select: bool = False,
    option1: str = None,
    option2: str = None,
    option3: str = None,
) -> Attachment:
    return CardFactory.adaptive_card(
        {
            "actions": [
                {
                    "data": {"submitLocation": "messagingExtensionFetchTask", "type" : "vmodelinit"},
                    "title": "Submit",
                    "type": "Action.Submit",
                }
            ],

                "body": [
                    {
                    "text": "Which V-model would you like to choose?",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                    {
                        "choices": [
                            {
                                "title": "Model-based standard",
                                "value": "Model-based"
                            },
                            {
                                "title": "INCOSE standard",
                                "value": "INCOSE"
                            },
                            {
                                "title": "Domain-specific standard",
                                "value": "Domain-specific"
                            }   
                        ],
			"id": "Choices",
                    	"isMultiSelect": is_multi_select,
                    	"style": "expanded",
                    	"type": "Input.ChoiceSet",
                    },
                ],
		        "type": "AdaptiveCard",
            	"version": "1.0",
            }
    )

def create_error_card_editor(
    user_text: str = None,
) -> Attachment:
    return CardFactory.error_card(
        {
            "actions": [
                {
                    "title": "Error, Please initialize the channel by typing appropriate command",
                }
            ]
        }
    )


def create_adaptive_card_preview(
    user_text1: str = None,
    user_text2: str = None,
    user_text3: str = None,
    a: str = None,
    b: str = None,
    c: str = None,
    memberid: str = None,
) -> Attachment:
    return CardFactory.adaptive_card(
        {
            # "actions": [
            #     {
            #         
            #         "title": "Submit",
            #         "data": {"submitLocation": "messagingExtensionSubmit"},
            #     }
            #],
            "body": [
                {
                    "text": "Decision maker: {}".format(memberid),
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {
                    "text": "{}: {}".format(a, user_text1), 
                    "type": "TextBlock", 
                    "id": "Question1"
                },


                {
                    "text": "{}: {}".format(b, user_text2),
                    "type": "TextBlock", 
                    "id": "Question2"
                },
                { 
                    "text": "{}: {}".format(c, user_text3), 
                    "type": "TextBlock", 
                    "id": "Question3"
                },

            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )

