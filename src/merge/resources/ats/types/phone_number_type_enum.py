# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PhoneNumberTypeEnum(str, enum.Enum):
    """
    * `HOME` - HOME
    * `WORK` - WORK
    * `MOBILE` - MOBILE
    * `SKYPE` - SKYPE
    * `OTHER` - OTHER
    """

    HOME = "HOME"
    WORK = "WORK"
    MOBILE = "MOBILE"
    SKYPE = "SKYPE"
    OTHER = "OTHER"

    def visit(
        self,
        home: typing.Callable[[], T_Result],
        work: typing.Callable[[], T_Result],
        mobile: typing.Callable[[], T_Result],
        skype: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PhoneNumberTypeEnum.HOME:
            return home()
        if self is PhoneNumberTypeEnum.WORK:
            return work()
        if self is PhoneNumberTypeEnum.MOBILE:
            return mobile()
        if self is PhoneNumberTypeEnum.SKYPE:
            return skype()
        if self is PhoneNumberTypeEnum.OTHER:
            return other()