# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreditNotesRetrieveRequestExpand(str, enum.Enum):
    APPLIED_TO_LINES = "applied_to_lines"
    LINE_ITEMS = "line_items"
    LINE_ITEMS_APPLIED_TO_LINES = "line_items,applied_to_lines"
    LINE_ITEMS_TRACKING_CATEGORIES = "line_items,tracking_categories"
    LINE_ITEMS_TRACKING_CATEGORIES_APPLIED_TO_LINES = "line_items,tracking_categories,applied_to_lines"
    PAYMENTS = "payments"
    PAYMENTS_APPLIED_TO_LINES = "payments,applied_to_lines"
    PAYMENTS_LINE_ITEMS = "payments,line_items"
    PAYMENTS_LINE_ITEMS_APPLIED_TO_LINES = "payments,line_items,applied_to_lines"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES = "payments,line_items,tracking_categories"
    PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_APPLIED_TO_LINES = (
        "payments,line_items,tracking_categories,applied_to_lines"
    )
    PAYMENTS_TRACKING_CATEGORIES = "payments,tracking_categories"
    PAYMENTS_TRACKING_CATEGORIES_APPLIED_TO_LINES = "payments,tracking_categories,applied_to_lines"
    TRACKING_CATEGORIES = "tracking_categories"
    TRACKING_CATEGORIES_APPLIED_TO_LINES = "tracking_categories,applied_to_lines"

    def visit(
        self,
        applied_to_lines: typing.Callable[[], T_Result],
        line_items: typing.Callable[[], T_Result],
        line_items_applied_to_lines: typing.Callable[[], T_Result],
        line_items_tracking_categories: typing.Callable[[], T_Result],
        line_items_tracking_categories_applied_to_lines: typing.Callable[[], T_Result],
        payments: typing.Callable[[], T_Result],
        payments_applied_to_lines: typing.Callable[[], T_Result],
        payments_line_items: typing.Callable[[], T_Result],
        payments_line_items_applied_to_lines: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories: typing.Callable[[], T_Result],
        payments_line_items_tracking_categories_applied_to_lines: typing.Callable[[], T_Result],
        payments_tracking_categories: typing.Callable[[], T_Result],
        payments_tracking_categories_applied_to_lines: typing.Callable[[], T_Result],
        tracking_categories: typing.Callable[[], T_Result],
        tracking_categories_applied_to_lines: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditNotesRetrieveRequestExpand.APPLIED_TO_LINES:
            return applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS:
            return line_items()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_APPLIED_TO_LINES:
            return line_items_applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES:
            return line_items_tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.LINE_ITEMS_TRACKING_CATEGORIES_APPLIED_TO_LINES:
            return line_items_tracking_categories_applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS:
            return payments()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_APPLIED_TO_LINES:
            return payments_applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS:
            return payments_line_items()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_APPLIED_TO_LINES:
            return payments_line_items_applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES:
            return payments_line_items_tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_LINE_ITEMS_TRACKING_CATEGORIES_APPLIED_TO_LINES:
            return payments_line_items_tracking_categories_applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES:
            return payments_tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.PAYMENTS_TRACKING_CATEGORIES_APPLIED_TO_LINES:
            return payments_tracking_categories_applied_to_lines()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES:
            return tracking_categories()
        if self is CreditNotesRetrieveRequestExpand.TRACKING_CATEGORIES_APPLIED_TO_LINES:
            return tracking_categories_applied_to_lines()
