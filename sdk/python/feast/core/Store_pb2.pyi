"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.duration_pb2 import (
    Duration as google___protobuf___duration_pb2___Duration,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
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

class Store(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    StoreTypeValue = typing___NewType('StoreTypeValue', builtin___int)
    type___StoreTypeValue = StoreTypeValue
    StoreType: _StoreType
    class _StoreType(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[Store.StoreTypeValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        INVALID = typing___cast(Store.StoreTypeValue, 0)
        REDIS = typing___cast(Store.StoreTypeValue, 1)
        REDIS_CLUSTER = typing___cast(Store.StoreTypeValue, 4)
    INVALID = typing___cast(Store.StoreTypeValue, 0)
    REDIS = typing___cast(Store.StoreTypeValue, 1)
    REDIS_CLUSTER = typing___cast(Store.StoreTypeValue, 4)

    class RedisConfig(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        host: typing___Text = ...
        port: builtin___int = ...
        initial_backoff_ms: builtin___int = ...
        max_retries: builtin___int = ...
        flush_frequency_seconds: builtin___int = ...
        ssl: builtin___bool = ...

        def __init__(self,
            *,
            host : typing___Optional[typing___Text] = None,
            port : typing___Optional[builtin___int] = None,
            initial_backoff_ms : typing___Optional[builtin___int] = None,
            max_retries : typing___Optional[builtin___int] = None,
            flush_frequency_seconds : typing___Optional[builtin___int] = None,
            ssl : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"flush_frequency_seconds",b"flush_frequency_seconds",u"host",b"host",u"initial_backoff_ms",b"initial_backoff_ms",u"max_retries",b"max_retries",u"port",b"port",u"ssl",b"ssl"]) -> None: ...
    type___RedisConfig = RedisConfig

    class RedisClusterConfig(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        ReadFromValue = typing___NewType('ReadFromValue', builtin___int)
        type___ReadFromValue = ReadFromValue
        ReadFrom: _ReadFrom
        class _ReadFrom(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[Store.RedisClusterConfig.ReadFromValue]):
            DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
            MASTER = typing___cast(Store.RedisClusterConfig.ReadFromValue, 0)
            MASTER_PREFERRED = typing___cast(Store.RedisClusterConfig.ReadFromValue, 1)
            REPLICA = typing___cast(Store.RedisClusterConfig.ReadFromValue, 2)
            REPLICA_PREFERRED = typing___cast(Store.RedisClusterConfig.ReadFromValue, 3)
        MASTER = typing___cast(Store.RedisClusterConfig.ReadFromValue, 0)
        MASTER_PREFERRED = typing___cast(Store.RedisClusterConfig.ReadFromValue, 1)
        REPLICA = typing___cast(Store.RedisClusterConfig.ReadFromValue, 2)
        REPLICA_PREFERRED = typing___cast(Store.RedisClusterConfig.ReadFromValue, 3)

        connection_string: typing___Text = ...
        initial_backoff_ms: builtin___int = ...
        max_retries: builtin___int = ...
        flush_frequency_seconds: builtin___int = ...
        key_prefix: typing___Text = ...
        enable_fallback: builtin___bool = ...
        fallback_prefix: typing___Text = ...
        read_from: type___Store.RedisClusterConfig.ReadFromValue = ...

        @property
        def timeout(self) -> google___protobuf___duration_pb2___Duration: ...

        def __init__(self,
            *,
            connection_string : typing___Optional[typing___Text] = None,
            initial_backoff_ms : typing___Optional[builtin___int] = None,
            max_retries : typing___Optional[builtin___int] = None,
            flush_frequency_seconds : typing___Optional[builtin___int] = None,
            key_prefix : typing___Optional[typing___Text] = None,
            enable_fallback : typing___Optional[builtin___bool] = None,
            fallback_prefix : typing___Optional[typing___Text] = None,
            read_from : typing___Optional[type___Store.RedisClusterConfig.ReadFromValue] = None,
            timeout : typing___Optional[google___protobuf___duration_pb2___Duration] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"timeout",b"timeout"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"connection_string",b"connection_string",u"enable_fallback",b"enable_fallback",u"fallback_prefix",b"fallback_prefix",u"flush_frequency_seconds",b"flush_frequency_seconds",u"initial_backoff_ms",b"initial_backoff_ms",u"key_prefix",b"key_prefix",u"max_retries",b"max_retries",u"read_from",b"read_from",u"timeout",b"timeout"]) -> None: ...
    type___RedisClusterConfig = RedisClusterConfig

    class Subscription(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        project: typing___Text = ...
        name: typing___Text = ...
        exclude: builtin___bool = ...

        def __init__(self,
            *,
            project : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            exclude : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"exclude",b"exclude",u"name",b"name",u"project",b"project"]) -> None: ...
    type___Subscription = Subscription

    name: typing___Text = ...
    type: type___Store.StoreTypeValue = ...

    @property
    def subscriptions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Store.Subscription]: ...

    @property
    def redis_config(self) -> type___Store.RedisConfig: ...

    @property
    def redis_cluster_config(self) -> type___Store.RedisClusterConfig: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[type___Store.StoreTypeValue] = None,
        subscriptions : typing___Optional[typing___Iterable[type___Store.Subscription]] = None,
        redis_config : typing___Optional[type___Store.RedisConfig] = None,
        redis_cluster_config : typing___Optional[type___Store.RedisClusterConfig] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"config",b"config",u"redis_cluster_config",b"redis_cluster_config",u"redis_config",b"redis_config"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"name",b"name",u"redis_cluster_config",b"redis_cluster_config",u"redis_config",b"redis_config",u"subscriptions",b"subscriptions",u"type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"config",b"config"]) -> typing_extensions___Literal["redis_config","redis_cluster_config"]: ...
type___Store = Store