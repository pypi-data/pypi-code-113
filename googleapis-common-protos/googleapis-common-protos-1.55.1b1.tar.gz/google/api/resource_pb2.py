# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/resource.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19google/api/resource.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"\xee\x02\n\x12ResourceDescriptor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07pattern\x18\x02 \x03(\t\x12\x12\n\nname_field\x18\x03 \x01(\t\x12\x37\n\x07history\x18\x04 \x01(\x0e\x32&.google.api.ResourceDescriptor.History\x12\x0e\n\x06plural\x18\x05 \x01(\t\x12\x10\n\x08singular\x18\x06 \x01(\t\x12\x33\n\x05style\x18\n \x03(\x0e\x32$.google.api.ResourceDescriptor.Style"[\n\x07History\x12\x17\n\x13HISTORY_UNSPECIFIED\x10\x00\x12\x1d\n\x19ORIGINALLY_SINGLE_PATTERN\x10\x01\x12\x18\n\x14\x46UTURE_MULTI_PATTERN\x10\x02"8\n\x05Style\x12\x15\n\x11STYLE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x44\x45\x43LARATIVE_FRIENDLY\x10\x01"5\n\x11ResourceReference\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x12\n\nchild_type\x18\x02 \x01(\t:Y\n\x12resource_reference\x12\x1d.google.protobuf.FieldOptions\x18\x9f\x08 \x01(\x0b\x32\x1d.google.api.ResourceReference:Z\n\x13resource_definition\x12\x1c.google.protobuf.FileOptions\x18\x9d\x08 \x03(\x0b\x32\x1e.google.api.ResourceDescriptor:R\n\x08resource\x12\x1f.google.protobuf.MessageOptions\x18\x9d\x08 \x01(\x0b\x32\x1e.google.api.ResourceDescriptorBn\n\x0e\x63om.google.apiB\rResourceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xf8\x01\x01\xa2\x02\x04GAPIb\x06proto3'
)


RESOURCE_REFERENCE_FIELD_NUMBER = 1055
resource_reference = DESCRIPTOR.extensions_by_name["resource_reference"]
RESOURCE_DEFINITION_FIELD_NUMBER = 1053
resource_definition = DESCRIPTOR.extensions_by_name["resource_definition"]
RESOURCE_FIELD_NUMBER = 1053
resource = DESCRIPTOR.extensions_by_name["resource"]

_RESOURCEDESCRIPTOR = DESCRIPTOR.message_types_by_name["ResourceDescriptor"]
_RESOURCEREFERENCE = DESCRIPTOR.message_types_by_name["ResourceReference"]
_RESOURCEDESCRIPTOR_HISTORY = _RESOURCEDESCRIPTOR.enum_types_by_name["History"]
_RESOURCEDESCRIPTOR_STYLE = _RESOURCEDESCRIPTOR.enum_types_by_name["Style"]
ResourceDescriptor = _reflection.GeneratedProtocolMessageType(
    "ResourceDescriptor",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCEDESCRIPTOR,
        "__module__": "google.api.resource_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ResourceDescriptor)
    },
)
_sym_db.RegisterMessage(ResourceDescriptor)

ResourceReference = _reflection.GeneratedProtocolMessageType(
    "ResourceReference",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCEREFERENCE,
        "__module__": "google.api.resource_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ResourceReference)
    },
)
_sym_db.RegisterMessage(ResourceReference)

if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(
        resource_reference
    )
    google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(
        resource_definition
    )
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(resource)

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\rResourceProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\370\001\001\242\002\004GAPI"
    _RESOURCEDESCRIPTOR._serialized_start = 76
    _RESOURCEDESCRIPTOR._serialized_end = 442
    _RESOURCEDESCRIPTOR_HISTORY._serialized_start = 293
    _RESOURCEDESCRIPTOR_HISTORY._serialized_end = 384
    _RESOURCEDESCRIPTOR_STYLE._serialized_start = 386
    _RESOURCEDESCRIPTOR_STYLE._serialized_end = 442
    _RESOURCEREFERENCE._serialized_start = 444
    _RESOURCEREFERENCE._serialized_end = 497
# @@protoc_insertion_point(module_scope)
