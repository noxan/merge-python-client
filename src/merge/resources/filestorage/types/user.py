# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime


class User(pydantic.BaseModel):
    """
    # The User Object
    ### Description
    The `User` object is used to represent a user within the File Storage account.
    ### Usage Example
    Fetch from the `GET /api/filestorage/v1/users` endpoint and view their users.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The user's name.")
    email_address: typing.Optional[str] = pydantic.Field(
        description="The user's email address. This is typically used to identify a user across linked accounts."
    )
    is_me: typing.Optional[bool] = pydantic.Field(description="Whether the user is the one who linked this account.")
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Any]]]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}