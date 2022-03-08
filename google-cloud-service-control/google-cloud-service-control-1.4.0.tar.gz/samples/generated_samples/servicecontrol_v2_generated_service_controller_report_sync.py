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
# Snippet for Report
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-service-control


# [START servicecontrol_v2_generated_ServiceController_Report_sync]
from google.cloud import servicecontrol_v2


def sample_report():
    # Create a client
    client = servicecontrol_v2.ServiceControllerClient()

    # Initialize request argument(s)
    request = servicecontrol_v2.ReportRequest(
    )

    # Make the request
    response = client.report(request=request)

    # Handle the response
    print(response)

# [END servicecontrol_v2_generated_ServiceController_Report_sync]
