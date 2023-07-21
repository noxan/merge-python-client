# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.remove_none_from_dict import remove_none_from_dict
from .....environment import MergeEnvironment
from ...types.paginated_transaction_list import PaginatedTransactionList
from ...types.transaction import Transaction
from ...types.transactions_list_request_expand import TransactionsListRequestExpand
from ...types.transactions_retrieve_request_expand import TransactionsRetrieveRequestExpand


class TransactionsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[TransactionsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        transaction_date_after: typing.Optional[str] = None,
        transaction_date_before: typing.Optional[str] = None,
    ) -> PaginatedTransactionList:
        """
        Returns a list of `Transaction` objects.

        Parameters:
            - company_id: typing.Optional[str]. If provided, will only return accounting transactions for this company.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[TransactionsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - transaction_date_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - transaction_date_before: typing.Optional[str]. If provided, will only return objects created before this datetime.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "transactions"),
            params=remove_none_from_dict(
                {
                    "company_id": company_id,
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "page_size": page_size,
                    "remote_id": remote_id,
                    "transaction_date_after": transaction_date_after,
                    "transaction_date_before": transaction_date_before,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTransactionList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[TransactionsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
    ) -> Transaction:
        """
        Returns a `Transaction` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[TransactionsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"transactions/{id}"),
            params=remove_none_from_dict({"expand": expand, "include_remote_data": include_remote_data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Transaction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTransactionsClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[TransactionsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[str] = None,
        modified_before: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        transaction_date_after: typing.Optional[str] = None,
        transaction_date_before: typing.Optional[str] = None,
    ) -> PaginatedTransactionList:
        """
        Returns a list of `Transaction` objects.

        Parameters:
            - company_id: typing.Optional[str]. If provided, will only return accounting transactions for this company.

            - created_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[str]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[TransactionsListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[str]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[str]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - transaction_date_after: typing.Optional[str]. If provided, will only return objects created after this datetime.

            - transaction_date_before: typing.Optional[str]. If provided, will only return objects created before this datetime.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "transactions"),
            params=remove_none_from_dict(
                {
                    "company_id": company_id,
                    "created_after": created_after,
                    "created_before": created_before,
                    "cursor": cursor,
                    "expand": expand,
                    "include_deleted_data": include_deleted_data,
                    "include_remote_data": include_remote_data,
                    "modified_after": modified_after,
                    "modified_before": modified_before,
                    "page_size": page_size,
                    "remote_id": remote_id,
                    "transaction_date_after": transaction_date_after,
                    "transaction_date_before": transaction_date_before,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedTransactionList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[TransactionsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
    ) -> Transaction:
        """
        Returns a `Transaction` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[TransactionsRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"transactions/{id}"),
            params=remove_none_from_dict({"expand": expand, "include_remote_data": include_remote_data}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Transaction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)