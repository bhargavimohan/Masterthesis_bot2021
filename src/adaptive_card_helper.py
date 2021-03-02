# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import CardFactory
from botbuilder.schema import Attachment

def create_ad_adaptive_card_editor(
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
                    "text": "Here you can discuss Architectural Design decisions",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "selectAction": {
                        "type": "Action.ToggleVisibility",
                        "targetElements": [
                            "cardContent4",
                            "showInfo",
                            "hideInfo"
                        ]
                    },
                    "verticalContentAlignment": "Center",
                    "items": [
                        {
                            "type": "TextBlock",
                            "id": "showInfo",
                            "horizontalAlignment": "Right",
                            "color": "Accent",
                            "text": "Show Info",
                            "wrap": True
                        },
                        {
                            "type": "TextBlock",
                            "id": "hideInfo",
                            "horizontalAlignment": "Right",
                            "color": "Accent",
                            "text": "Hide Info",
                            "wrap": True,
                            "isVisible": False
                        }
                    ],
                    "width": 1
                }
            ]
        },
        {
            "type": "Container",
            "id": "cardContent4",
            "isVisible": False,
            "items": [
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            "isSubtle": True,
                            "wrap": True
                        }
                    ]
                }
            ]
        },
                {"type": "TextBlock", "text": "Functional design decisions:"},
                {
                    "id": "Question1",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "value": user_text1,
                    "isRequired": True,
                    "errorMessage": "Any one feild is required"
                },
                
                {"type": "TextBlock", "text": "Logical design decisions:"},
                {
                    "id": "Question2",
                    "placeholder": " Input text here",
                    "type": "Input.Text",
                    "value": user_text2,
                },
                {"type": "TextBlock", "text": "Physical design decisions:"},
                {
                    "id": "Question3",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "value": user_text3,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )



def create_dc_adaptive_card_editor(
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
                    "text": "Here you can discuss Design/conceptual decisions",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "selectAction": {
                        "type": "Action.ToggleVisibility",
                        "targetElements": [
                            "cardContent4",
                            "showInfo",
                            "hideInfo"
                        ]
                    },
                    "verticalContentAlignment": "Center",
                    "items": [
                        {
                            "type": "TextBlock",
                            "id": "showInfo",
                            "horizontalAlignment": "Right",
                            "color": "Accent",
                            "text": "Show Info",
                            "wrap": True
                        },
                        {
                            "type": "TextBlock",
                            "id": "hideInfo",
                            "horizontalAlignment": "Right",
                            "color": "Accent",
                            "text": "Hide Info",
                            "wrap": True,
                            "isVisible": False
                        }
                    ],
                    "width": 1
                }
            ]
        },
        {
            "type": "Container",
            "id": "cardContent4",
            "isVisible": False,
            "items": [
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            "isSubtle": True,
                            "wrap": True
                        }
                    ]
                }
            ]
        },
                {"type": "TextBlock", "text": " Design definition decisions:"},
                {
                    "id": "Question1",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "isMultiline": True,
                    "value": user_text1,
                },
                {"type": "TextBlock", "text": "Design characteristics & Enablers decisions:"},
                {
                    "id": "Question2",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "isMultiline": True,
                    "value": user_text2,
                },
                {"type": "TextBlock", "text": " Design Alternatives decisions:"},
                {
                    "id": "Question3",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "isMultiline": True,
                    "value": user_text3,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )



def create_imp_adaptive_card_editor(
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
                    "text": "Here you can discuss Implementational design decisions",
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "selectAction": {
                        "type": "Action.ToggleVisibility",
                        "targetElements": [
                            "cardContent4",
                            "showInfo",
                            "hideInfo"
                        ]
                    },
                    "verticalContentAlignment": "Center",
                    "items": [
                        {
                            "type": "TextBlock",
                            "id": "showInfo",
                            "horizontalAlignment": "Right",
                            "color": "Accent",
                            "text": "Show Info",
                            "wrap": True
                        },
                        {
                            "type": "TextBlock",
                            "id": "hideInfo",
                            "horizontalAlignment": "Right",
                            "color": "Accent",
                            "text": "Hide Info",
                            "wrap": True,
                            "isVisible": False
                        }
                    ],
                    "width": 1
                }
            ]
        },
        {
            "type": "Container",
            "id": "cardContent4",
            "isVisible": False,
            "items": [
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                            "isSubtle": True,
                            "wrap": True
                        }
                    ]
                }
            ]
        },
                {"type": "TextBlock", "text": "Mechanical design decisions:"},
                {
                    "id": "Question1",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "isMultiline": True,
                    "value": user_text1,
                },
                {"type": "TextBlock", "text": "Electrical design decisions:"},
                {
                    "id": "Question2",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "isMultiline": True,
                    "value": user_text2,
                },
                {"type": "TextBlock", "text": "Software design decisions:"},
                {
                    "id": "Question3",
                    "placeholder": "Input text here",
                    "type": "Input.Text",
                    "isMultiline": True,
                    "value": user_text3,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )


def create_vphase_card_editor(
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
                    "text": "Which phase in the V-model would you like to document decisions?",
                    "type": "TextBlock",
                    "weight": "bolder",
                    "wrap": True,
                },
                    {
                        "choices": [
                            {
                                "title": "Architecture Design",
                                "value": "Architecture Design"
                            },
                            {
                                "title": "Design/concept",
                                "value": "Design/concept"
                            },
                            {
                                "title": "Implementation",
                                "value": "Implementation"
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
            "body": [
                {
                    "text": "Decision maker: {}".format(memberid),
                    "type": "TextBlock",
                    "weight": "bolder",
                },
                {
                    "text": "{}".format(a), 
                    "type": "TextBlock", 
                    "id": "Question1",
                    "color": "Accent",
                    "size": "Large"
                },
                {
                    "text": "{}".format(user_text1), 
                    "type": "TextBlock", 
                    "id": "Question1",
                    "weight": "bolder"
                },


                {
                    "text": "{}".format(b),
                    "type": "TextBlock", 
                    "id": "Question2",
                    "color": "Accent",
                    "size": "Large"
                },
                {
                    "text": "{}".format(user_text2), 
                    "type": "TextBlock", 
                    "id": "Question1",
                    "weight": "bolder"
                },
                { 
                    "text": "{}".format(c), 
                    "type": "TextBlock", 
                    "id": "Question3",
                    "color": "Accent",
                    "size": "Large"
                },
                {
                    "text": "{}".format(user_text3), 
                    "type": "TextBlock", 
                    "id": "Question1",
                    "weight": "bolder"
                },

            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )
    

