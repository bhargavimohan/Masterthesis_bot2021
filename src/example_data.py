# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class ExampleData(object):
    def __init__(
        self,
        question1: str = None,
        question2: str = None,
        question3: str = None,
        memberid: str = None,
    ):
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.memberid = memberid