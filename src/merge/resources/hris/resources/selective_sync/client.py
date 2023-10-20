# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.linked_account_selective_sync_configuration import LinkedAccountSelectiveSyncConfiguration
from ...types.linked_account_selective_sync_configuration_request import LinkedAccountSelectiveSyncConfigurationRequest
from ...types.paginated_condition_schema_list import PaginatedConditionSchemaList

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SelectiveSyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def configurations_list(self) -> typing.List[LinkedAccountSelectiveSyncConfiguration]:
        """
        Get a linked account's selective syncs.

        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.configurations_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/selective-sync/configurations"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LinkedAccountSelectiveSyncConfiguration], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def configurations_update(
        self, *, sync_configurations: typing.List[LinkedAccountSelectiveSyncConfigurationRequest]
    ) -> typing.List[LinkedAccountSelectiveSyncConfiguration]:
        """
        Replace a linked account's selective syncs.

        Parameters:
            - sync_configurations: typing.List[LinkedAccountSelectiveSyncConfigurationRequest]. The selective syncs associated with a linked account.
        ---
        from merge import LinkedAccountSelectiveSyncConfigurationRequest
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.configurations_update(
            sync_configurations=[
                LinkedAccountSelectiveSyncConfigurationRequest(
                    linked_account_conditions=[],
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/selective-sync/configurations"
            ),
            json=jsonable_encoder({"sync_configurations": sync_configurations}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LinkedAccountSelectiveSyncConfiguration], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_list(
        self,
        *,
        common_model: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedConditionSchemaList:
        """
        Get metadata for the conditions available to a linked account.

        Parameters:
            - common_model: typing.Optional[str].

            - cursor: typing.Optional[str]. The pagination cursor value.

            - page_size: typing.Optional[int]. Number of results to return per page.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.meta_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/selective-sync/meta"),
            params=remove_none_from_dict({"common_model": common_model, "cursor": cursor, "page_size": page_size}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedConditionSchemaList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSelectiveSyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def configurations_list(self) -> typing.List[LinkedAccountSelectiveSyncConfiguration]:
        """
        Get a linked account's selective syncs.

        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.configurations_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/selective-sync/configurations"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LinkedAccountSelectiveSyncConfiguration], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def configurations_update(
        self, *, sync_configurations: typing.List[LinkedAccountSelectiveSyncConfigurationRequest]
    ) -> typing.List[LinkedAccountSelectiveSyncConfiguration]:
        """
        Replace a linked account's selective syncs.

        Parameters:
            - sync_configurations: typing.List[LinkedAccountSelectiveSyncConfigurationRequest]. The selective syncs associated with a linked account.
        ---
        from merge import LinkedAccountSelectiveSyncConfigurationRequest
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.configurations_update(
            sync_configurations=[
                LinkedAccountSelectiveSyncConfigurationRequest(
                    linked_account_conditions=[],
                )
            ],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/selective-sync/configurations"
            ),
            json=jsonable_encoder({"sync_configurations": sync_configurations}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[LinkedAccountSelectiveSyncConfiguration], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_list(
        self,
        *,
        common_model: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
    ) -> PaginatedConditionSchemaList:
        """
        Get metadata for the conditions available to a linked account.

        Parameters:
            - common_model: typing.Optional[str].

            - cursor: typing.Optional[str]. The pagination cursor value.

            - page_size: typing.Optional[int]. Number of results to return per page.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.meta_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/selective-sync/meta"),
            params=remove_none_from_dict({"common_model": common_model, "cursor": cursor, "page_size": page_size}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedConditionSchemaList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
