# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .role_ticket_access import RoleTicketAccess
from .role_ticket_actions_item import RoleTicketActionsItem

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Role(pydantic.BaseModel):
    """
    # The Role Object
    ### Description
    The `Role` object is used to represent the set of actions & access that a user with this role is allowed to perform.

    ### Usage Example
    TODO
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The name of the Role.")
    ticket_actions: typing.Optional[typing.List[typing.Optional[RoleTicketActionsItem]]] = pydantic.Field(
        description="The set of actions that a User with this Role can perform. Possible enum values include: `VIEW`, `CREATE`, `EDIT`, `DELETE`, `CLOSE`, and `ASSIGN`."
    )
    ticket_access: typing.Optional[RoleTicketAccess] = pydantic.Field(
        description=(
            "The level of Ticket access that a User with this Role can perform.\n"
            "\n"
            "* `ALL` - ALL\n"
            "* `ASSIGNED_ONLY` - ASSIGNED_ONLY\n"
            "* `TEAM_ONLY` - TEAM_ONLY\n"
        )
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
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
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}