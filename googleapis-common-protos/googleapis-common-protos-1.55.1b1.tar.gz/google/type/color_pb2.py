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
# source: google/type/color.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17google/type/color.proto\x12\x0bgoogle.type\x1a\x1egoogle/protobuf/wrappers.proto"]\n\x05\x43olor\x12\x0b\n\x03red\x18\x01 \x01(\x02\x12\r\n\x05green\x18\x02 \x01(\x02\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x02\x12*\n\x05\x61lpha\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValueB`\n\x0f\x63om.google.typeB\nColorProtoP\x01Z6google.golang.org/genproto/googleapis/type/color;color\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3'
)


_COLOR = DESCRIPTOR.message_types_by_name["Color"]
Color = _reflection.GeneratedProtocolMessageType(
    "Color",
    (_message.Message,),
    {
        "DESCRIPTOR": _COLOR,
        "__module__": "google.type.color_pb2"
        # @@protoc_insertion_point(class_scope:google.type.Color)
    },
)
_sym_db.RegisterMessage(Color)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\017com.google.typeB\nColorProtoP\001Z6google.golang.org/genproto/googleapis/type/color;color\370\001\001\242\002\003GTP"
    _COLOR._serialized_start = 72
    _COLOR._serialized_end = 165
# @@protoc_insertion_point(module_scope)
