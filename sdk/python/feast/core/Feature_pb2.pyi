"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from feast.types.Value_pb2 import (
    ValueType as feast___types___Value_pb2___ValueType,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    ScalarMap as google___protobuf___internal___containers___ScalarMap,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Mapping as typing___Mapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FeatureSpecV2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class LabelsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___LabelsEntry = LabelsEntry

    name: typing___Text = ...
    value_type: feast___types___Value_pb2___ValueType.EnumValue = ...

    @property
    def labels(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, typing___Text]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        value_type : typing___Optional[feast___types___Value_pb2___ValueType.EnumValue] = None,
        labels : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"labels",b"labels",u"name",b"name",u"value_type",b"value_type"]) -> None: ...
type___FeatureSpecV2 = FeatureSpecV2