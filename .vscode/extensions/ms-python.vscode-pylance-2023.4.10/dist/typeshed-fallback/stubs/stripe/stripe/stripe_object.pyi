import json
from _typeshed import Incomplete
from typing import Any
from typing_extensions import Self

from stripe import api_requestor as api_requestor

class StripeObject(dict[Any, Any]):
    class ReprJSONEncoder(json.JSONEncoder):
        def default(self, obj): ...

    def __init__(
        self,
        id: Incomplete | None = ...,
        api_key: Incomplete | None = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        last_response: Incomplete | None = ...,
        **params,
    ) -> None: ...
    @property
    def last_response(self): ...
    def update(self, update_dict): ...
    def __setattr__(self, k: str, v) -> None: ...
    def __getattr__(self, k: str): ...
    def __delattr__(self, k: str) -> None: ...
    def __setitem__(self, k, v) -> None: ...
    def __getitem__(self, k): ...
    def __delitem__(self, k) -> None: ...
    def __reduce__(self): ...
    @classmethod
    def construct_from(
        cls,
        values: Any,
        key: str | None,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        last_response: Incomplete | None = ...,
    ) -> Self: ...
    api_key: Any
    stripe_version: Any
    stripe_account: Any
    def refresh_from(
        self,
        values: Any,
        api_key: Incomplete | None = ...,
        partial: bool = ...,
        stripe_version: Incomplete | None = ...,
        stripe_account: Incomplete | None = ...,
        last_response: Incomplete | None = ...,
    ) -> None: ...
    @classmethod
    def api_base(cls) -> None: ...
    def request(self, method, url, params: Incomplete | None = ..., headers: Incomplete | None = ...): ...
    def request_stream(self, method, url, params: Incomplete | None = ..., headers: Incomplete | None = ...): ...
    def to_dict(self): ...
    def to_dict_recursive(self): ...
    @property
    def stripe_id(self): ...
    def serialize(self, previous): ...
    def __copy__(self) -> StripeObject: ...
    def __deepcopy__(self, memo: Any) -> StripeObject: ...
