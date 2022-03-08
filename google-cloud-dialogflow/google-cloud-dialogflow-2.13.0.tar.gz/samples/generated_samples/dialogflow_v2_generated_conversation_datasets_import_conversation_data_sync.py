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
# Snippet for ImportConversationData
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2_generated_ConversationDatasets_ImportConversationData_sync]
from google.cloud import dialogflow_v2


def sample_import_conversation_data():
    # Create a client
    client = dialogflow_v2.ConversationDatasetsClient()

    # Initialize request argument(s)
    input_config = dialogflow_v2.InputConfig()
    input_config.gcs_source.uris = ['uris_value_1', 'uris_value_2']

    request = dialogflow_v2.ImportConversationDataRequest(
        name="name_value",
        input_config=input_config,
    )

    # Make the request
    operation = client.import_conversation_data(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END dialogflow_v2_generated_ConversationDatasets_ImportConversationData_sync]
