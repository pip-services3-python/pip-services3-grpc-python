# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commandable.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='commandable.proto',
  package='commandable',
  syntax='proto3',
  serialized_options=b'\n\035pip-services.grpc.commandableB\020CommandableProtoP\001Z\006protos\242\002\010GRPC_CMD',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63ommandable.proto\x12\x0b\x63ommandable\"\xfc\x01\n\x10\x45rrorDescription\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\x05\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\r\n\x05\x63\x61use\x18\x06 \x01(\t\x12\x13\n\x0bstack_trace\x18\x07 \x01(\t\x12;\n\x07\x64\x65tails\x18\x08 \x03(\x0b\x32*.commandable.ErrorDescription.DetailsEntry\x1a.\n\x0c\x44\x65tailsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"^\n\rInvokeRequest\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x02 \x01(\t\x12\x12\n\nargs_empty\x18\x03 \x01(\x08\x12\x11\n\targs_json\x18\x04 \x01(\t\"f\n\x0bInvokeReply\x12,\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.commandable.ErrorDescription\x12\x14\n\x0cresult_empty\x18\x02 \x01(\x08\x12\x13\n\x0bresult_json\x18\x03 \x01(\t2O\n\x0b\x43ommandable\x12@\n\x06invoke\x12\x1a.commandable.InvokeRequest\x1a\x18.commandable.InvokeReply\"\x00\x42\x46\n\x1dpip-services.grpc.commandableB\x10\x43ommandableProtoP\x01Z\x06protos\xa2\x02\x08GRPC_CMDb\x06proto3'
)




_ERRORDESCRIPTION_DETAILSENTRY = _descriptor.Descriptor(
  name='DetailsEntry',
  full_name='commandable.ErrorDescription.DetailsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='commandable.ErrorDescription.DetailsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='commandable.ErrorDescription.DetailsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=287,
)

_ERRORDESCRIPTION = _descriptor.Descriptor(
  name='ErrorDescription',
  full_name='commandable.ErrorDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='commandable.ErrorDescription.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='commandable.ErrorDescription.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='correlation_id', full_name='commandable.ErrorDescription.correlation_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='commandable.ErrorDescription.status', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='commandable.ErrorDescription.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cause', full_name='commandable.ErrorDescription.cause', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stack_trace', full_name='commandable.ErrorDescription.stack_trace', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='commandable.ErrorDescription.details', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ERRORDESCRIPTION_DETAILSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=287,
)


_INVOKEREQUEST = _descriptor.Descriptor(
  name='InvokeRequest',
  full_name='commandable.InvokeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='commandable.InvokeRequest.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='correlation_id', full_name='commandable.InvokeRequest.correlation_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args_empty', full_name='commandable.InvokeRequest.args_empty', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args_json', full_name='commandable.InvokeRequest.args_json', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=289,
  serialized_end=383,
)


_INVOKEREPLY = _descriptor.Descriptor(
  name='InvokeReply',
  full_name='commandable.InvokeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='commandable.InvokeReply.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_empty', full_name='commandable.InvokeReply.result_empty', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_json', full_name='commandable.InvokeReply.result_json', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=385,
  serialized_end=487,
)

_ERRORDESCRIPTION_DETAILSENTRY.containing_type = _ERRORDESCRIPTION
_ERRORDESCRIPTION.fields_by_name['details'].message_type = _ERRORDESCRIPTION_DETAILSENTRY
_INVOKEREPLY.fields_by_name['error'].message_type = _ERRORDESCRIPTION
DESCRIPTOR.message_types_by_name['ErrorDescription'] = _ERRORDESCRIPTION
DESCRIPTOR.message_types_by_name['InvokeRequest'] = _INVOKEREQUEST
DESCRIPTOR.message_types_by_name['InvokeReply'] = _INVOKEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ErrorDescription = _reflection.GeneratedProtocolMessageType('ErrorDescription', (_message.Message,), {

  'DetailsEntry' : _reflection.GeneratedProtocolMessageType('DetailsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ERRORDESCRIPTION_DETAILSENTRY,
    '__module__' : 'commandable_pb2'
    # @@protoc_insertion_point(class_scope:commandable.ErrorDescription.DetailsEntry)
    })
  ,
  'DESCRIPTOR' : _ERRORDESCRIPTION,
  '__module__' : 'commandable_pb2'
  # @@protoc_insertion_point(class_scope:commandable.ErrorDescription)
  })
_sym_db.RegisterMessage(ErrorDescription)
_sym_db.RegisterMessage(ErrorDescription.DetailsEntry)

InvokeRequest = _reflection.GeneratedProtocolMessageType('InvokeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEREQUEST,
  '__module__' : 'commandable_pb2'
  # @@protoc_insertion_point(class_scope:commandable.InvokeRequest)
  })
_sym_db.RegisterMessage(InvokeRequest)

InvokeReply = _reflection.GeneratedProtocolMessageType('InvokeReply', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEREPLY,
  '__module__' : 'commandable_pb2'
  # @@protoc_insertion_point(class_scope:commandable.InvokeReply)
  })
_sym_db.RegisterMessage(InvokeReply)


DESCRIPTOR._options = None
_ERRORDESCRIPTION_DETAILSENTRY._options = None

_COMMANDABLE = _descriptor.ServiceDescriptor(
  name='Commandable',
  full_name='commandable.Commandable',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=489,
  serialized_end=568,
  methods=[
  _descriptor.MethodDescriptor(
    name='invoke',
    full_name='commandable.Commandable.invoke',
    index=0,
    containing_service=None,
    input_type=_INVOKEREQUEST,
    output_type=_INVOKEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMANDABLE)

DESCRIPTOR.services_by_name['Commandable'] = _COMMANDABLE

# @@protoc_insertion_point(module_scope)
