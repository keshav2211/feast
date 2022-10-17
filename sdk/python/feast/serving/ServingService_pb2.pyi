"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from feast.types.Value_pb2 import (
    Value as feast___types___Value_pb2___Value,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    MessageMap as google___protobuf___internal___containers___MessageMap,
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
    ScalarMap as google___protobuf___internal___containers___ScalarMap,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

FieldStatusValue = typing___NewType('FieldStatusValue', builtin___int)
type___FieldStatusValue = FieldStatusValue
FieldStatus: _FieldStatus
class _FieldStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[FieldStatusValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    INVALID = typing___cast(FieldStatusValue, 0)
    PRESENT = typing___cast(FieldStatusValue, 1)
    NULL_VALUE = typing___cast(FieldStatusValue, 2)
    NOT_FOUND = typing___cast(FieldStatusValue, 3)
    OUTSIDE_MAX_AGE = typing___cast(FieldStatusValue, 4)
    INGESTION_FAILURE = typing___cast(FieldStatusValue, 5)
INVALID = typing___cast(FieldStatusValue, 0)
PRESENT = typing___cast(FieldStatusValue, 1)
NULL_VALUE = typing___cast(FieldStatusValue, 2)
NOT_FOUND = typing___cast(FieldStatusValue, 3)
OUTSIDE_MAX_AGE = typing___cast(FieldStatusValue, 4)
INGESTION_FAILURE = typing___cast(FieldStatusValue, 5)

FeastServingTypeValue = typing___NewType('FeastServingTypeValue', builtin___int)
type___FeastServingTypeValue = FeastServingTypeValue
FeastServingType: _FeastServingType
class _FeastServingType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[FeastServingTypeValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    FEAST_SERVING_TYPE_INVALID = typing___cast(FeastServingTypeValue, 0)
    FEAST_SERVING_TYPE_ONLINE = typing___cast(FeastServingTypeValue, 1)
    FEAST_SERVING_TYPE_BATCH = typing___cast(FeastServingTypeValue, 2)
FEAST_SERVING_TYPE_INVALID = typing___cast(FeastServingTypeValue, 0)
FEAST_SERVING_TYPE_ONLINE = typing___cast(FeastServingTypeValue, 1)
FEAST_SERVING_TYPE_BATCH = typing___cast(FeastServingTypeValue, 2)

class GetFeastServingInfoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___GetFeastServingInfoRequest = GetFeastServingInfoRequest

class GetFeastServingInfoResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version: typing___Text = ...
    type: type___FeastServingTypeValue = ...
    job_staging_location: typing___Text = ...

    def __init__(self,
        *,
        version : typing___Optional[typing___Text] = None,
        type : typing___Optional[type___FeastServingTypeValue] = None,
        job_staging_location : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"job_staging_location",b"job_staging_location",u"type",b"type",u"version",b"version"]) -> None: ...
type___GetFeastServingInfoResponse = GetFeastServingInfoResponse

class FeatureReferenceV2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    feature_table: typing___Text = ...
    name: typing___Text = ...

    def __init__(self,
        *,
        feature_table : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"feature_table",b"feature_table",u"name",b"name"]) -> None: ...
type___FeatureReferenceV2 = FeatureReferenceV2

class GetOnlineFeaturesRequestV2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class EntityRow(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class FieldsEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...

            @property
            def value(self) -> feast___types___Value_pb2___Value: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[feast___types___Value_pb2___Value] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___FieldsEntry = FieldsEntry


        @property
        def timestamp(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

        @property
        def fields(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, feast___types___Value_pb2___Value]: ...

        def __init__(self,
            *,
            timestamp : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
            fields : typing___Optional[typing___Mapping[typing___Text, feast___types___Value_pb2___Value]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"timestamp",b"timestamp"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"fields",b"fields",u"timestamp",b"timestamp"]) -> None: ...
    type___EntityRow = EntityRow

    project: typing___Text = ...

    @property
    def features(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___FeatureReferenceV2]: ...

    @property
    def entity_rows(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___GetOnlineFeaturesRequestV2.EntityRow]: ...

    def __init__(self,
        *,
        features : typing___Optional[typing___Iterable[type___FeatureReferenceV2]] = None,
        entity_rows : typing___Optional[typing___Iterable[type___GetOnlineFeaturesRequestV2.EntityRow]] = None,
        project : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"entity_rows",b"entity_rows",u"features",b"features",u"project",b"project"]) -> None: ...
type___GetOnlineFeaturesRequestV2 = GetOnlineFeaturesRequestV2

class GetOnlineFeaturesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FieldValues(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class FieldsEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...

            @property
            def value(self) -> feast___types___Value_pb2___Value: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[feast___types___Value_pb2___Value] = None,
                ) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___FieldsEntry = FieldsEntry

        class StatusesEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...
            value: type___FieldStatusValue = ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[type___FieldStatusValue] = None,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___StatusesEntry = StatusesEntry


        @property
        def fields(self) -> google___protobuf___internal___containers___MessageMap[typing___Text, feast___types___Value_pb2___Value]: ...

        @property
        def statuses(self) -> google___protobuf___internal___containers___ScalarMap[typing___Text, type___FieldStatusValue]: ...

        def __init__(self,
            *,
            fields : typing___Optional[typing___Mapping[typing___Text, feast___types___Value_pb2___Value]] = None,
            statuses : typing___Optional[typing___Mapping[typing___Text, type___FieldStatusValue]] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"fields",b"fields",u"statuses",b"statuses"]) -> None: ...
    type___FieldValues = FieldValues


    @property
    def field_values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___GetOnlineFeaturesResponse.FieldValues]: ...

    def __init__(self,
        *,
        field_values : typing___Optional[typing___Iterable[type___GetOnlineFeaturesResponse.FieldValues]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"field_values",b"field_values"]) -> None: ...
type___GetOnlineFeaturesResponse = GetOnlineFeaturesResponse

class GetOnlineFeaturesResponseV2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FieldVector(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        statuses: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___FieldStatusValue] = ...

        @property
        def values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[feast___types___Value_pb2___Value]: ...

        def __init__(self,
            *,
            values : typing___Optional[typing___Iterable[feast___types___Value_pb2___Value]] = None,
            statuses : typing___Optional[typing___Iterable[type___FieldStatusValue]] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"statuses",b"statuses",u"values",b"values"]) -> None: ...
    type___FieldVector = FieldVector


    @property
    def metadata(self) -> type___GetOnlineFeaturesResponseMetadata: ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___GetOnlineFeaturesResponseV2.FieldVector]: ...

    def __init__(self,
        *,
        metadata : typing___Optional[type___GetOnlineFeaturesResponseMetadata] = None,
        results : typing___Optional[typing___Iterable[type___GetOnlineFeaturesResponseV2.FieldVector]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata",u"results",b"results"]) -> None: ...
type___GetOnlineFeaturesResponseV2 = GetOnlineFeaturesResponseV2

class GetOnlineFeaturesResponseMetadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def field_names(self) -> type___FieldList: ...

    def __init__(self,
        *,
        field_names : typing___Optional[type___FieldList] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"field_names",b"field_names"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"field_names",b"field_names"]) -> None: ...
type___GetOnlineFeaturesResponseMetadata = GetOnlineFeaturesResponseMetadata

class FieldList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
type___FieldList = FieldList