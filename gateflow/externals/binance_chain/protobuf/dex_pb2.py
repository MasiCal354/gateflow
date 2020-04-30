# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dex.proto

from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='dex.proto',
    package='transaction',
    syntax='proto3',
    serialized_options=_b(
        '\n\031com.binance.dex.api.protoB\013TransactionP\001'),
    serialized_pb=_b('\n\tdex.proto\x12\x0btransaction\"U\n\x05StdTx\x12\x0c\n\x04msgs\x18\x01 \x03(\x0c\x12\x12\n\nsignatures\x18\x02 \x03(\x0c\x12\x0c\n\x04memo\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\"f\n\x0cStdSignature\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x03 \x01(\x03\x12\x10\n\x08sequence\x18\x04 \x01(\x03\x1a\x08\n\x06PubKey\"\x8d\x01\n\x08NewOrder\x12\x0e\n\x06sender\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x11\n\tordertype\x18\x04 \x01(\x03\x12\x0c\n\x04side\x18\x05 \x01(\x03\x12\r\n\x05price\x18\x06 \x01(\x03\x12\x10\n\x08quantity\x18\x07 \x01(\x03\x12\x13\n\x0btimeinforce\x18\x08 \x01(\x03\"<\n\x0b\x43\x61ncelOrder\x12\x0e\n\x06sender\x18\x01 \x01(\x0c\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\r\n\x05refid\x18\x03 \x01(\t\";\n\x0bTokenFreeze\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"=\n\rTokenUnfreeze\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"&\n\x05Token\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\";\n\x05Input\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12!\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x12.transaction.Token\"<\n\x06Output\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12!\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x12.transaction.Token\"P\n\x04Send\x12\"\n\x06inputs\x18\x01 \x03(\x0b\x32\x12.transaction.Input\x12$\n\x07outputs\x18\x02 \x03(\x0b\x32\x13.transaction.Output\":\n\x04Vote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x03\x12\r\n\x05voter\x18\x02 \x01(\x0c\x12\x0e\n\x06option\x18\x03 \x01(\x03\x42*\n\x19\x63om.binance.dex.api.protoB\x0bTransactionP\x01\x62\x06proto3')
)


_STDTX = _descriptor.Descriptor(
    name='StdTx',
    full_name='transaction.StdTx',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='msgs', full_name='transaction.StdTx.msgs', index=0,
            number=1, type=12, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='signatures', full_name='transaction.StdTx.signatures', index=1,
            number=2, type=12, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='memo', full_name='transaction.StdTx.memo', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='source', full_name='transaction.StdTx.source', index=3,
            number=4, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='transaction.StdTx.data', index=4,
            number=5, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=26,
    serialized_end=111,
)


_STDSIGNATURE_PUBKEY = _descriptor.Descriptor(
    name='PubKey',
    full_name='transaction.StdSignature.PubKey',
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=207,
    serialized_end=215,
)

_STDSIGNATURE = _descriptor.Descriptor(
    name='StdSignature',
    full_name='transaction.StdSignature',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='pub_key', full_name='transaction.StdSignature.pub_key', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='signature', full_name='transaction.StdSignature.signature', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='account_number', full_name='transaction.StdSignature.account_number', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sequence', full_name='transaction.StdSignature.sequence', index=3,
            number=4, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_STDSIGNATURE_PUBKEY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=113,
    serialized_end=215,
)


_NEWORDER = _descriptor.Descriptor(
    name='NewOrder',
    full_name='transaction.NewOrder',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='sender', full_name='transaction.NewOrder.sender', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='id', full_name='transaction.NewOrder.id', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='symbol', full_name='transaction.NewOrder.symbol', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='ordertype', full_name='transaction.NewOrder.ordertype', index=3,
            number=4, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='side', full_name='transaction.NewOrder.side', index=4,
            number=5, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='price', full_name='transaction.NewOrder.price', index=5,
            number=6, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='quantity', full_name='transaction.NewOrder.quantity', index=6,
            number=7, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timeinforce', full_name='transaction.NewOrder.timeinforce', index=7,
            number=8, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=218,
    serialized_end=359,
)


_CANCELORDER = _descriptor.Descriptor(
    name='CancelOrder',
    full_name='transaction.CancelOrder',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='sender', full_name='transaction.CancelOrder.sender', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='symbol', full_name='transaction.CancelOrder.symbol', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='refid', full_name='transaction.CancelOrder.refid', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=361,
    serialized_end=421,
)


_TOKENFREEZE = _descriptor.Descriptor(
    name='TokenFreeze',
    full_name='transaction.TokenFreeze',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='from', full_name='transaction.TokenFreeze.from', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='symbol', full_name='transaction.TokenFreeze.symbol', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='amount', full_name='transaction.TokenFreeze.amount', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=423,
    serialized_end=482,
)


_TOKENUNFREEZE = _descriptor.Descriptor(
    name='TokenUnfreeze',
    full_name='transaction.TokenUnfreeze',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='from', full_name='transaction.TokenUnfreeze.from', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='symbol', full_name='transaction.TokenUnfreeze.symbol', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='amount', full_name='transaction.TokenUnfreeze.amount', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=484,
    serialized_end=545,
)


_TOKEN = _descriptor.Descriptor(
    name='Token',
    full_name='transaction.Token',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='denom', full_name='transaction.Token.denom', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='amount', full_name='transaction.Token.amount', index=1,
            number=2, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=547,
    serialized_end=585,
)


_INPUT = _descriptor.Descriptor(
    name='Input',
    full_name='transaction.Input',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='transaction.Input.address', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='coins', full_name='transaction.Input.coins', index=1,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=587,
    serialized_end=646,
)


_OUTPUT = _descriptor.Descriptor(
    name='Output',
    full_name='transaction.Output',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='transaction.Output.address', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='coins', full_name='transaction.Output.coins', index=1,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=648,
    serialized_end=708,
)


_SEND = _descriptor.Descriptor(
    name='Send',
    full_name='transaction.Send',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='inputs', full_name='transaction.Send.inputs', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='outputs', full_name='transaction.Send.outputs', index=1,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=710,
    serialized_end=790,
)


_VOTE = _descriptor.Descriptor(
    name='Vote',
    full_name='transaction.Vote',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='proposal_id', full_name='transaction.Vote.proposal_id', index=0,
            number=1, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='voter', full_name='transaction.Vote.voter', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='option', full_name='transaction.Vote.option', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
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
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=792,
    serialized_end=850,
)

_STDSIGNATURE_PUBKEY.containing_type = _STDSIGNATURE
_INPUT.fields_by_name['coins'].message_type = _TOKEN
_OUTPUT.fields_by_name['coins'].message_type = _TOKEN
_SEND.fields_by_name['inputs'].message_type = _INPUT
_SEND.fields_by_name['outputs'].message_type = _OUTPUT
DESCRIPTOR.message_types_by_name['StdTx'] = _STDTX
DESCRIPTOR.message_types_by_name['StdSignature'] = _STDSIGNATURE
DESCRIPTOR.message_types_by_name['NewOrder'] = _NEWORDER
DESCRIPTOR.message_types_by_name['CancelOrder'] = _CANCELORDER
DESCRIPTOR.message_types_by_name['TokenFreeze'] = _TOKENFREEZE
DESCRIPTOR.message_types_by_name['TokenUnfreeze'] = _TOKENUNFREEZE
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['Send'] = _SEND
DESCRIPTOR.message_types_by_name['Vote'] = _VOTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StdTx = _reflection.GeneratedProtocolMessageType('StdTx', (_message.Message,), dict(
    DESCRIPTOR=_STDTX,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.StdTx)
))
_sym_db.RegisterMessage(StdTx)

StdSignature = _reflection.GeneratedProtocolMessageType('StdSignature', (_message.Message,), dict(

    PubKey=_reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), dict(
        DESCRIPTOR=_STDSIGNATURE_PUBKEY,
        __module__='dex_pb2'
        # @@protoc_insertion_point(class_scope:transaction.StdSignature.PubKey)
    )),
    DESCRIPTOR=_STDSIGNATURE,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.StdSignature)
))
_sym_db.RegisterMessage(StdSignature)
_sym_db.RegisterMessage(StdSignature.PubKey)

NewOrder = _reflection.GeneratedProtocolMessageType('NewOrder', (_message.Message,), dict(
    DESCRIPTOR=_NEWORDER,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.NewOrder)
))
_sym_db.RegisterMessage(NewOrder)

CancelOrder = _reflection.GeneratedProtocolMessageType('CancelOrder', (_message.Message,), dict(
    DESCRIPTOR=_CANCELORDER,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.CancelOrder)
))
_sym_db.RegisterMessage(CancelOrder)

TokenFreeze = _reflection.GeneratedProtocolMessageType('TokenFreeze', (_message.Message,), dict(
    DESCRIPTOR=_TOKENFREEZE,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.TokenFreeze)
))
_sym_db.RegisterMessage(TokenFreeze)

TokenUnfreeze = _reflection.GeneratedProtocolMessageType('TokenUnfreeze', (_message.Message,), dict(
    DESCRIPTOR=_TOKENUNFREEZE,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.TokenUnfreeze)
))
_sym_db.RegisterMessage(TokenUnfreeze)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), dict(
    DESCRIPTOR=_TOKEN,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.Token)
))
_sym_db.RegisterMessage(Token)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), dict(
    DESCRIPTOR=_INPUT,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.Input)
))
_sym_db.RegisterMessage(Input)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), dict(
    DESCRIPTOR=_OUTPUT,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.Output)
))
_sym_db.RegisterMessage(Output)

Send = _reflection.GeneratedProtocolMessageType('Send', (_message.Message,), dict(
    DESCRIPTOR=_SEND,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.Send)
))
_sym_db.RegisterMessage(Send)

Vote = _reflection.GeneratedProtocolMessageType('Vote', (_message.Message,), dict(
    DESCRIPTOR=_VOTE,
    __module__='dex_pb2'
    # @@protoc_insertion_point(class_scope:transaction.Vote)
))
_sym_db.RegisterMessage(Vote)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
