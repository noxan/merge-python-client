# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .vendor_credit_apply_line_invoice import VendorCreditApplyLineInvoice


class VendorCreditApplyLine(pydantic.BaseModel):
    """
    # The VendorCreditApplyLine Object
    ### Description
    The `VendorCreditApplyLine` object is used to represent a applied vendor credit.

    ### Usage Example
    Fetch from the `GET VendorCredit` endpoint and view the vendor credit's applied to lines.
    """

    invoice: typing.Optional[VendorCreditApplyLineInvoice]
    applied_date: typing.Optional[dt.datetime] = pydantic.Field(
        description="Date that the vendor credit is applied to the invoice."
    )
    applied_amount: typing.Optional[str] = pydantic.Field(
        description="The amount of the VendorCredit applied to the invoice."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}