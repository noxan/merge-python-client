# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivityTypeEnum(str, enum.Enum):
    """
    * `CALL` - CALL
    * `MEETING` - MEETING
    * `EMAIL` - EMAIL
    """

    CALL = "CALL"
    MEETING = "MEETING"
    EMAIL = "EMAIL"

    def visit(
        self,
        call: typing.Callable[[], T_Result],
        meeting: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActivityTypeEnum.CALL:
            return call()
        if self is ActivityTypeEnum.MEETING:
            return meeting()
        if self is ActivityTypeEnum.EMAIL:
            return email()