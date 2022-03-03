# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: predictor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='predictor.proto',
  package='predictor',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fpredictor.proto\x12\tpredictor\"\\\n\nAccRequest\x12\r\n\x05sides\x18\x01 \x01(\x02\x12\x0e\n\x06updown\x18\x02 \x01(\x02\x12\x12\n\naboveunder\x18\x03 \x01(\x02\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0c\n\x04user\x18\x05 \x01(\t\"]\n\x0b\x41\x63\x63Response\x12\r\n\x05sides\x18\x01 \x01(\x02\x12\x0e\n\x06updown\x18\x02 \x01(\x02\x12\x12\n\naboveunder\x18\x03 \x01(\x02\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0c\n\x04user\x18\x05 \x01(\t2N\n\x10PredictorService\x12:\n\x07predict\x12\x15.predictor.AccRequest\x1a\x16.predictor.AccResponse\"\x00\x62\x06proto3'
)




_ACCREQUEST = _descriptor.Descriptor(
  name='AccRequest',
  full_name='predictor.AccRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sides', full_name='predictor.AccRequest.sides', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updown', full_name='predictor.AccRequest.updown', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aboveunder', full_name='predictor.AccRequest.aboveunder', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='predictor.AccRequest.image', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='predictor.AccRequest.user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=122,
)


_ACCRESPONSE = _descriptor.Descriptor(
  name='AccResponse',
  full_name='predictor.AccResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sides', full_name='predictor.AccResponse.sides', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updown', full_name='predictor.AccResponse.updown', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aboveunder', full_name='predictor.AccResponse.aboveunder', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='predictor.AccResponse.image', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='predictor.AccResponse.user', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['AccRequest'] = _ACCREQUEST
DESCRIPTOR.message_types_by_name['AccResponse'] = _ACCRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccRequest = _reflection.GeneratedProtocolMessageType('AccRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCREQUEST,
  '__module__' : 'predictor_pb2'
  # @@protoc_insertion_point(class_scope:predictor.AccRequest)
  })
_sym_db.RegisterMessage(AccRequest)

AccResponse = _reflection.GeneratedProtocolMessageType('AccResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCRESPONSE,
  '__module__' : 'predictor_pb2'
  # @@protoc_insertion_point(class_scope:predictor.AccResponse)
  })
_sym_db.RegisterMessage(AccResponse)



_PREDICTORSERVICE = _descriptor.ServiceDescriptor(
  name='PredictorService',
  full_name='predictor.PredictorService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=219,
  serialized_end=297,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict',
    full_name='predictor.PredictorService.predict',
    index=0,
    containing_service=None,
    input_type=_ACCREQUEST,
    output_type=_ACCRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTORSERVICE)

DESCRIPTOR.services_by_name['PredictorService'] = _PREDICTORSERVICE

# @@protoc_insertion_point(module_scope)
