# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logregr.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logregr.proto',
  package='logregr',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\rlogregr.proto\x12\x07logregr\"w\n\rLogregrResult\x12\x30\n\rlogregrResult\x18\x01 \x03(\x0b\x32\x19.logregr.LogregrResultRow\x12\x34\n\x0flogregrMetadata\x18\x02 \x03(\x0b\x32\x1b.logregr.LogregrMetadataRow\"A\n\x10LogregrResultRow\x12\x15\n\rparameterName\x18\x01 \x02(\t\x12\x16\n\x0eparameterValue\x18\x02 \x02(\x02\"0\n\x12LogregrMetadataRow\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\x88\x01\n\x1fLogregrStartExecutionParameters\x12\x15\n\rlearning_rate\x18\x01 \x02(\x02\x12\x12\n\nnum_splits\x18\x02 \x02(\r\x12\x12\n\nnum_epochs\x18\x03 \x02(\r\x12\x12\n\nl2_penalty\x18\x04 \x02(\x02\x12\x12\n\nl1_penalty\x18\x05 \x02(\x02'
)




_LOGREGRRESULT = _descriptor.Descriptor(
  name='LogregrResult',
  full_name='logregr.LogregrResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logregrResult', full_name='logregr.LogregrResult.logregrResult', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logregrMetadata', full_name='logregr.LogregrResult.logregrMetadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=145,
)


_LOGREGRRESULTROW = _descriptor.Descriptor(
  name='LogregrResultRow',
  full_name='logregr.LogregrResultRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameterName', full_name='logregr.LogregrResultRow.parameterName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameterValue', full_name='logregr.LogregrResultRow.parameterValue', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=212,
)


_LOGREGRMETADATAROW = _descriptor.Descriptor(
  name='LogregrMetadataRow',
  full_name='logregr.LogregrMetadataRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='logregr.LogregrMetadataRow.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='logregr.LogregrMetadataRow.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=262,
)


_LOGREGRSTARTEXECUTIONPARAMETERS = _descriptor.Descriptor(
  name='LogregrStartExecutionParameters',
  full_name='logregr.LogregrStartExecutionParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='logregr.LogregrStartExecutionParameters.learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_splits', full_name='logregr.LogregrStartExecutionParameters.num_splits', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_epochs', full_name='logregr.LogregrStartExecutionParameters.num_epochs', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_penalty', full_name='logregr.LogregrStartExecutionParameters.l2_penalty', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l1_penalty', full_name='logregr.LogregrStartExecutionParameters.l1_penalty', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=401,
)

_LOGREGRRESULT.fields_by_name['logregrResult'].message_type = _LOGREGRRESULTROW
_LOGREGRRESULT.fields_by_name['logregrMetadata'].message_type = _LOGREGRMETADATAROW
DESCRIPTOR.message_types_by_name['LogregrResult'] = _LOGREGRRESULT
DESCRIPTOR.message_types_by_name['LogregrResultRow'] = _LOGREGRRESULTROW
DESCRIPTOR.message_types_by_name['LogregrMetadataRow'] = _LOGREGRMETADATAROW
DESCRIPTOR.message_types_by_name['LogregrStartExecutionParameters'] = _LOGREGRSTARTEXECUTIONPARAMETERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogregrResult = _reflection.GeneratedProtocolMessageType('LogregrResult', (_message.Message,), {
  'DESCRIPTOR' : _LOGREGRRESULT,
  '__module__' : 'logregr_pb2'
  # @@protoc_insertion_point(class_scope:logregr.LogregrResult)
  })
_sym_db.RegisterMessage(LogregrResult)

LogregrResultRow = _reflection.GeneratedProtocolMessageType('LogregrResultRow', (_message.Message,), {
  'DESCRIPTOR' : _LOGREGRRESULTROW,
  '__module__' : 'logregr_pb2'
  # @@protoc_insertion_point(class_scope:logregr.LogregrResultRow)
  })
_sym_db.RegisterMessage(LogregrResultRow)

LogregrMetadataRow = _reflection.GeneratedProtocolMessageType('LogregrMetadataRow', (_message.Message,), {
  'DESCRIPTOR' : _LOGREGRMETADATAROW,
  '__module__' : 'logregr_pb2'
  # @@protoc_insertion_point(class_scope:logregr.LogregrMetadataRow)
  })
_sym_db.RegisterMessage(LogregrMetadataRow)

LogregrStartExecutionParameters = _reflection.GeneratedProtocolMessageType('LogregrStartExecutionParameters', (_message.Message,), {
  'DESCRIPTOR' : _LOGREGRSTARTEXECUTIONPARAMETERS,
  '__module__' : 'logregr_pb2'
  # @@protoc_insertion_point(class_scope:logregr.LogregrStartExecutionParameters)
  })
_sym_db.RegisterMessage(LogregrStartExecutionParameters)


# @@protoc_insertion_point(module_scope)
