# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateIntent
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2beta1_generated_Intents_CreateIntent_async]
from google.cloud import dialogflow_v2beta1


async def sample_create_intent():
    # Create a client
    client = dialogflow_v2beta1.IntentsAsyncClient()

    # Initialize request argument(s)
    intent = dialogflow_v2beta1.Intent()
    intent.display_name = "display_name_value"

    request = dialogflow_v2beta1.CreateIntentRequest(
        parent="parent_value",
        intent=intent,
    )

    # Make the request
    response = await client.create_intent(request=request)

    # Handle the response
    print(response)

# [END dialogflow_v2beta1_generated_Intents_CreateIntent_async]
