# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: csv.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='csv.proto',
  package='csv',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\tcsv.proto\x12\x03\x63sv\"\xc8\x02\n\nCsvRequest\x12\x45\n\x1auploadConfigurationRequest\x18\x01 \x01(\x0b\x32\x1f.csv.UploadConfigurationRequestH\x00\x12\x39\n\x14getDataFormatRequest\x18\x02 \x01(\x0b\x32\x19.csv.GetDataFormatRequestH\x00\x12\x33\n\x11submitDataRequest\x18\x03 \x01(\x0b\x32\x16.csv.SubmitDataRequestH\x00\x12?\n\x17triggerExecutionRequest\x18\x04 \x01(\x0b\x32\x1c.csv.TriggerExecutionRequestH\x00\x12\x33\n\x11getResultsRequest\x18\x05 \x01(\x0b\x32\x16.csv.GetResultsRequestH\x00\x42\r\n\x0b\x63sv_request\"\xe7\x02\n\x0b\x43svResponse\x12\x11\n\x07\x66\x61ilure\x18\x01 \x01(\tH\x00\x12G\n\x1buploadConfigurationResponse\x18\x02 \x01(\x0b\x32 .csv.UploadConfigurationResponseH\x00\x12;\n\x15getDataFormatResponse\x18\x03 \x01(\x0b\x32\x1a.csv.GetDataFormatResponseH\x00\x12\x35\n\x12submitDataResponse\x18\x04 \x01(\x0b\x32\x17.csv.SubmitDataResponseH\x00\x12\x41\n\x18triggerExecutionResponse\x18\x05 \x01(\x0b\x32\x1d.csv.TriggerExecutionResponseH\x00\x12\x35\n\x12getResultsResponse\x18\x06 \x01(\x0b\x32\x17.csv.GetResultsResponseH\x00\x42\x0e\n\x0c\x63sv_response\"<\n\nDataFormat\x12\x19\n\x11\x63\x61tegoriesColumns\x18\x01 \x03(\t\x12\x13\n\x0bvalueColumn\x18\x02 \x02(\t\"S\n\x1aUploadConfigurationRequest\x12#\n\ndataFormat\x18\x01 \x02(\x0b\x32\x0f.csv.DataFormat\x12\x10\n\x08***REMOVED***\x18\x02 \x02(\t\"\x1d\n\x1bUploadConfigurationResponse\"\x16\n\x14GetDataFormatRequest\"<\n\x15GetDataFormatResponse\x12#\n\ndataFormat\x18\x01 \x02(\x0b\x32\x0f.csv.DataFormat\"!\n\x11SubmitDataRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"N\n\x12SubmitDataResponse\x12\x14\n\x0cingestedRows\x18\x01 \x02(\x05\x12\"\n\nfailedRows\x18\x02 \x03(\x0b\x32\x0e.csv.FailedRow\"0\n\tFailedRow\x12\x12\n\nlineNumber\x18\x01 \x02(\x05\x12\x0f\n\x07\x66\x61ilure\x18\x02 \x02(\t\"R\n\x17TriggerExecutionRequest\x12\x10\n\x08***REMOVED***\x18\x01 \x02(\t\x12%\n\x1dserializedExecutionParameters\x18\x02 \x01(\x0c\"\x1a\n\x18TriggerExecutionResponse\"%\n\x11GetResultsRequest\x12\x10\n\x08***REMOVED***\x18\x01 \x01(\t\".\n\x12GetResultsResponse\x12\x18\n\x10serializedResult\x18\x01 \x02(\x0c'
)




_CSVREQUEST = _descriptor.Descriptor(
  name='CsvRequest',
  full_name='csv.CsvRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uploadConfigurationRequest', full_name='csv.CsvRequest.uploadConfigurationRequest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getDataFormatRequest', full_name='csv.CsvRequest.getDataFormatRequest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submitDataRequest', full_name='csv.CsvRequest.submitDataRequest', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggerExecutionRequest', full_name='csv.CsvRequest.triggerExecutionRequest', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getResultsRequest', full_name='csv.CsvRequest.getResultsRequest', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='csv_request', full_name='csv.CsvRequest.csv_request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=19,
  serialized_end=347,
)


_CSVRESPONSE = _descriptor.Descriptor(
  name='CsvResponse',
  full_name='csv.CsvResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failure', full_name='csv.CsvResponse.failure', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uploadConfigurationResponse', full_name='csv.CsvResponse.uploadConfigurationResponse', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getDataFormatResponse', full_name='csv.CsvResponse.getDataFormatResponse', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submitDataResponse', full_name='csv.CsvResponse.submitDataResponse', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggerExecutionResponse', full_name='csv.CsvResponse.triggerExecutionResponse', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='getResultsResponse', full_name='csv.CsvResponse.getResultsResponse', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='csv_response', full_name='csv.CsvResponse.csv_response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=350,
  serialized_end=709,
)


_DATAFORMAT = _descriptor.Descriptor(
  name='DataFormat',
  full_name='csv.DataFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categoriesColumns', full_name='csv.DataFormat.categoriesColumns', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valueColumn', full_name='csv.DataFormat.valueColumn', index=1,
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
  serialized_start=711,
  serialized_end=771,
)


_UPLOADCONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='UploadConfigurationRequest',
  full_name='csv.UploadConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataFormat', full_name='csv.UploadConfigurationRequest.dataFormat', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='***REMOVED***', full_name='csv.UploadConfigurationRequest.***REMOVED***', index=1,
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
  serialized_start=773,
  serialized_end=856,
)


_UPLOADCONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='UploadConfigurationResponse',
  full_name='csv.UploadConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=858,
  serialized_end=887,
)


_GETDATAFORMATREQUEST = _descriptor.Descriptor(
  name='GetDataFormatRequest',
  full_name='csv.GetDataFormatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=889,
  serialized_end=911,
)


_GETDATAFORMATRESPONSE = _descriptor.Descriptor(
  name='GetDataFormatResponse',
  full_name='csv.GetDataFormatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataFormat', full_name='csv.GetDataFormatResponse.dataFormat', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=913,
  serialized_end=973,
)


_SUBMITDATAREQUEST = _descriptor.Descriptor(
  name='SubmitDataRequest',
  full_name='csv.SubmitDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='csv.SubmitDataRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  serialized_start=975,
  serialized_end=1008,
)


_SUBMITDATARESPONSE = _descriptor.Descriptor(
  name='SubmitDataResponse',
  full_name='csv.SubmitDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingestedRows', full_name='csv.SubmitDataResponse.ingestedRows', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failedRows', full_name='csv.SubmitDataResponse.failedRows', index=1,
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
  serialized_start=1010,
  serialized_end=1088,
)


_FAILEDROW = _descriptor.Descriptor(
  name='FailedRow',
  full_name='csv.FailedRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lineNumber', full_name='csv.FailedRow.lineNumber', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure', full_name='csv.FailedRow.failure', index=1,
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
  serialized_start=1090,
  serialized_end=1138,
)


_TRIGGEREXECUTIONREQUEST = _descriptor.Descriptor(
  name='TriggerExecutionRequest',
  full_name='csv.TriggerExecutionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='***REMOVED***', full_name='csv.TriggerExecutionRequest.***REMOVED***', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serializedExecutionParameters', full_name='csv.TriggerExecutionRequest.serializedExecutionParameters', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=1140,
  serialized_end=1222,
)


_TRIGGEREXECUTIONRESPONSE = _descriptor.Descriptor(
  name='TriggerExecutionResponse',
  full_name='csv.TriggerExecutionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1224,
  serialized_end=1250,
)


_GETRESULTSREQUEST = _descriptor.Descriptor(
  name='GetResultsRequest',
  full_name='csv.GetResultsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='***REMOVED***', full_name='csv.GetResultsRequest.***REMOVED***', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1252,
  serialized_end=1289,
)


_GETRESULTSRESPONSE = _descriptor.Descriptor(
  name='GetResultsResponse',
  full_name='csv.GetResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serializedResult', full_name='csv.GetResultsResponse.serializedResult', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  serialized_start=1291,
  serialized_end=1337,
)

_CSVREQUEST.fields_by_name['uploadConfigurationRequest'].message_type = _UPLOADCONFIGURATIONREQUEST
_CSVREQUEST.fields_by_name['getDataFormatRequest'].message_type = _GETDATAFORMATREQUEST
_CSVREQUEST.fields_by_name['submitDataRequest'].message_type = _SUBMITDATAREQUEST
_CSVREQUEST.fields_by_name['triggerExecutionRequest'].message_type = _TRIGGEREXECUTIONREQUEST
_CSVREQUEST.fields_by_name['getResultsRequest'].message_type = _GETRESULTSREQUEST
_CSVREQUEST.oneofs_by_name['csv_request'].fields.append(
  _CSVREQUEST.fields_by_name['uploadConfigurationRequest'])
_CSVREQUEST.fields_by_name['uploadConfigurationRequest'].containing_oneof = _CSVREQUEST.oneofs_by_name['csv_request']
_CSVREQUEST.oneofs_by_name['csv_request'].fields.append(
  _CSVREQUEST.fields_by_name['getDataFormatRequest'])
_CSVREQUEST.fields_by_name['getDataFormatRequest'].containing_oneof = _CSVREQUEST.oneofs_by_name['csv_request']
_CSVREQUEST.oneofs_by_name['csv_request'].fields.append(
  _CSVREQUEST.fields_by_name['submitDataRequest'])
_CSVREQUEST.fields_by_name['submitDataRequest'].containing_oneof = _CSVREQUEST.oneofs_by_name['csv_request']
_CSVREQUEST.oneofs_by_name['csv_request'].fields.append(
  _CSVREQUEST.fields_by_name['triggerExecutionRequest'])
_CSVREQUEST.fields_by_name['triggerExecutionRequest'].containing_oneof = _CSVREQUEST.oneofs_by_name['csv_request']
_CSVREQUEST.oneofs_by_name['csv_request'].fields.append(
  _CSVREQUEST.fields_by_name['getResultsRequest'])
_CSVREQUEST.fields_by_name['getResultsRequest'].containing_oneof = _CSVREQUEST.oneofs_by_name['csv_request']
_CSVRESPONSE.fields_by_name['uploadConfigurationResponse'].message_type = _UPLOADCONFIGURATIONRESPONSE
_CSVRESPONSE.fields_by_name['getDataFormatResponse'].message_type = _GETDATAFORMATRESPONSE
_CSVRESPONSE.fields_by_name['submitDataResponse'].message_type = _SUBMITDATARESPONSE
_CSVRESPONSE.fields_by_name['triggerExecutionResponse'].message_type = _TRIGGEREXECUTIONRESPONSE
_CSVRESPONSE.fields_by_name['getResultsResponse'].message_type = _GETRESULTSRESPONSE
_CSVRESPONSE.oneofs_by_name['csv_response'].fields.append(
  _CSVRESPONSE.fields_by_name['failure'])
_CSVRESPONSE.fields_by_name['failure'].containing_oneof = _CSVRESPONSE.oneofs_by_name['csv_response']
_CSVRESPONSE.oneofs_by_name['csv_response'].fields.append(
  _CSVRESPONSE.fields_by_name['uploadConfigurationResponse'])
_CSVRESPONSE.fields_by_name['uploadConfigurationResponse'].containing_oneof = _CSVRESPONSE.oneofs_by_name['csv_response']
_CSVRESPONSE.oneofs_by_name['csv_response'].fields.append(
  _CSVRESPONSE.fields_by_name['getDataFormatResponse'])
_CSVRESPONSE.fields_by_name['getDataFormatResponse'].containing_oneof = _CSVRESPONSE.oneofs_by_name['csv_response']
_CSVRESPONSE.oneofs_by_name['csv_response'].fields.append(
  _CSVRESPONSE.fields_by_name['submitDataResponse'])
_CSVRESPONSE.fields_by_name['submitDataResponse'].containing_oneof = _CSVRESPONSE.oneofs_by_name['csv_response']
_CSVRESPONSE.oneofs_by_name['csv_response'].fields.append(
  _CSVRESPONSE.fields_by_name['triggerExecutionResponse'])
_CSVRESPONSE.fields_by_name['triggerExecutionResponse'].containing_oneof = _CSVRESPONSE.oneofs_by_name['csv_response']
_CSVRESPONSE.oneofs_by_name['csv_response'].fields.append(
  _CSVRESPONSE.fields_by_name['getResultsResponse'])
_CSVRESPONSE.fields_by_name['getResultsResponse'].containing_oneof = _CSVRESPONSE.oneofs_by_name['csv_response']
_UPLOADCONFIGURATIONREQUEST.fields_by_name['dataFormat'].message_type = _DATAFORMAT
_GETDATAFORMATRESPONSE.fields_by_name['dataFormat'].message_type = _DATAFORMAT
_SUBMITDATARESPONSE.fields_by_name['failedRows'].message_type = _FAILEDROW
DESCRIPTOR.message_types_by_name['CsvRequest'] = _CSVREQUEST
DESCRIPTOR.message_types_by_name['CsvResponse'] = _CSVRESPONSE
DESCRIPTOR.message_types_by_name['DataFormat'] = _DATAFORMAT
DESCRIPTOR.message_types_by_name['UploadConfigurationRequest'] = _UPLOADCONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['UploadConfigurationResponse'] = _UPLOADCONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetDataFormatRequest'] = _GETDATAFORMATREQUEST
DESCRIPTOR.message_types_by_name['GetDataFormatResponse'] = _GETDATAFORMATRESPONSE
DESCRIPTOR.message_types_by_name['SubmitDataRequest'] = _SUBMITDATAREQUEST
DESCRIPTOR.message_types_by_name['SubmitDataResponse'] = _SUBMITDATARESPONSE
DESCRIPTOR.message_types_by_name['FailedRow'] = _FAILEDROW
DESCRIPTOR.message_types_by_name['TriggerExecutionRequest'] = _TRIGGEREXECUTIONREQUEST
DESCRIPTOR.message_types_by_name['TriggerExecutionResponse'] = _TRIGGEREXECUTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetResultsRequest'] = _GETRESULTSREQUEST
DESCRIPTOR.message_types_by_name['GetResultsResponse'] = _GETRESULTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CsvRequest = _reflection.GeneratedProtocolMessageType('CsvRequest', (_message.Message,), {
  'DESCRIPTOR' : _CSVREQUEST,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.CsvRequest)
  })
_sym_db.RegisterMessage(CsvRequest)

CsvResponse = _reflection.GeneratedProtocolMessageType('CsvResponse', (_message.Message,), {
  'DESCRIPTOR' : _CSVRESPONSE,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.CsvResponse)
  })
_sym_db.RegisterMessage(CsvResponse)

DataFormat = _reflection.GeneratedProtocolMessageType('DataFormat', (_message.Message,), {
  'DESCRIPTOR' : _DATAFORMAT,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.DataFormat)
  })
_sym_db.RegisterMessage(DataFormat)

UploadConfigurationRequest = _reflection.GeneratedProtocolMessageType('UploadConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCONFIGURATIONREQUEST,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.UploadConfigurationRequest)
  })
_sym_db.RegisterMessage(UploadConfigurationRequest)

UploadConfigurationResponse = _reflection.GeneratedProtocolMessageType('UploadConfigurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADCONFIGURATIONRESPONSE,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.UploadConfigurationResponse)
  })
_sym_db.RegisterMessage(UploadConfigurationResponse)

GetDataFormatRequest = _reflection.GeneratedProtocolMessageType('GetDataFormatRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAFORMATREQUEST,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.GetDataFormatRequest)
  })
_sym_db.RegisterMessage(GetDataFormatRequest)

GetDataFormatResponse = _reflection.GeneratedProtocolMessageType('GetDataFormatResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAFORMATRESPONSE,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.GetDataFormatResponse)
  })
_sym_db.RegisterMessage(GetDataFormatResponse)

SubmitDataRequest = _reflection.GeneratedProtocolMessageType('SubmitDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITDATAREQUEST,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.SubmitDataRequest)
  })
_sym_db.RegisterMessage(SubmitDataRequest)

SubmitDataResponse = _reflection.GeneratedProtocolMessageType('SubmitDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITDATARESPONSE,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.SubmitDataResponse)
  })
_sym_db.RegisterMessage(SubmitDataResponse)

FailedRow = _reflection.GeneratedProtocolMessageType('FailedRow', (_message.Message,), {
  'DESCRIPTOR' : _FAILEDROW,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.FailedRow)
  })
_sym_db.RegisterMessage(FailedRow)

TriggerExecutionRequest = _reflection.GeneratedProtocolMessageType('TriggerExecutionRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGEREXECUTIONREQUEST,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.TriggerExecutionRequest)
  })
_sym_db.RegisterMessage(TriggerExecutionRequest)

TriggerExecutionResponse = _reflection.GeneratedProtocolMessageType('TriggerExecutionResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGEREXECUTIONRESPONSE,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.TriggerExecutionResponse)
  })
_sym_db.RegisterMessage(TriggerExecutionResponse)

GetResultsRequest = _reflection.GeneratedProtocolMessageType('GetResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRESULTSREQUEST,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.GetResultsRequest)
  })
_sym_db.RegisterMessage(GetResultsRequest)

GetResultsResponse = _reflection.GeneratedProtocolMessageType('GetResultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRESULTSRESPONSE,
  '__module__' : 'csv_pb2'
  # @@protoc_insertion_point(class_scope:csv.GetResultsResponse)
  })
_sym_db.RegisterMessage(GetResultsResponse)


# @@protoc_insertion_point(module_scope)