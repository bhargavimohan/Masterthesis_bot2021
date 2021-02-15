def create_modelbased_adaptive_card_editor(
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
                    "id": "Question",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text,
                },
                {"type": "TextBlock", "text": "Logical design decisions:"},
                {
                    "id": "Question",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text,
                },
                {"type": "TextBlock", "text": "Physical design decisions:"},
                {
                    "id": "Question",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )



    def create_incose_adaptive_card_editor(
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
                    "id": "Question",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text,
                },
                {"type": "TextBlock", "text": "Design characteristics & Enablers decisions:"},
                {
                    "id": "Question",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text,
                },
                {"type": "TextBlock", "text": " Design Alternatives decisions:"},
                {
                    "id": "Question",
                    "placeholder": "text here",
                    "type": "Input.Text",
                    "value": user_text,
                },  
            ],
            "type": "AdaptiveCard",
            "version": "1.0",
        }
    )
