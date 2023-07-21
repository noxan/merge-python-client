# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .email_address import EmailAddress
from .phone_number import PhoneNumber
from .remote_data import RemoteData
from .url import Url


class Candidate(pydantic.BaseModel):
    """
    # The Candidate Object
    ### Description
    The `Candidate` object is used to represent profile information about a given Candidate. Because it is specific to a Candidate, this information stays constant across applications.
    ### Usage Example
    Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all candidates.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    first_name: typing.Optional[str] = pydantic.Field(description="The candidate's first name.")
    last_name: typing.Optional[str] = pydantic.Field(description="The candidate's last name.")
    company: typing.Optional[str] = pydantic.Field(description="The candidate's current company.")
    title: typing.Optional[str] = pydantic.Field(description="The candidate's current title.")
    remote_created_at: typing.Optional[str] = pydantic.Field(
        description="When the third party's candidate was created."
    )
    remote_updated_at: typing.Optional[str] = pydantic.Field(
        description="When the third party's candidate was updated."
    )
    last_interaction_at: typing.Optional[str] = pydantic.Field(
        description="When the most recent interaction with the candidate occurred."
    )
    is_private: typing.Optional[bool] = pydantic.Field(description="Whether or not the candidate is private.")
    can_email: typing.Optional[bool] = pydantic.Field(description="Whether or not the candidate can be emailed.")
    locations: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="The candidate's locations."
    )
    phone_numbers: typing.Optional[typing.List[PhoneNumber]]
    email_addresses: typing.Optional[typing.List[EmailAddress]]
    urls: typing.Optional[typing.List[Url]]
    tags: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="Array of `Tag` names as strings."
    )
    applications: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="Array of `Application` object IDs."
    )
    attachments: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="Array of `Attachment` object IDs."
    )
    remote_was_deleted: typing.Optional[bool]
    modified_at: typing.Optional[str] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}