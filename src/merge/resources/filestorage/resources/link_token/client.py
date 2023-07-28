# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....environment import MergeEnvironment
from ...types.categories_enum import CategoriesEnum
from ...types.common_model_scopes_body_request import CommonModelScopesBodyRequest
from ...types.link_token import LinkToken

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LinkTokenClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        end_user_email_address: str,
        end_user_organization_name: str,
        end_user_origin_id: str,
        categories: typing.List[CategoriesEnum],
        integration: typing.Optional[str] = OMIT,
        link_expiry_mins: typing.Optional[int] = OMIT,
        should_create_magic_link_url: typing.Optional[bool] = OMIT,
        common_models: typing.Optional[typing.List[CommonModelScopesBodyRequest]] = OMIT,
    ) -> LinkToken:
        """
        Creates a link token to be used when linking a new end user.

        Parameters:
            - end_user_email_address: str. Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent. <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 100 characters`</span>

            - end_user_organization_name: str. Your end user's organization. <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 100 characters`</span>

            - end_user_origin_id: str. This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers. <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 100 characters`</span>

            - categories: typing.List[CategoriesEnum]. The integration categories to show in Merge Link.

            - integration: typing.Optional[str]. The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://www.merge.dev/docs/basics/integration-metadata/.

            - link_expiry_mins: typing.Optional[int]. An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.

            - should_create_magic_link_url: typing.Optional[bool]. Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/integrations-fast-say-hello-to-magic-link.

            - common_models: typing.Optional[typing.List[CommonModelScopesBodyRequest]]. An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.
        """
        _request: typing.Dict[str, typing.Any] = {
            "end_user_email_address": end_user_email_address,
            "end_user_organization_name": end_user_organization_name,
            "end_user_origin_id": end_user_origin_id,
            "categories": categories,
        }
        if integration is not OMIT:
            _request["integration"] = integration
        if link_expiry_mins is not OMIT:
            _request["link_expiry_mins"] = link_expiry_mins
        if should_create_magic_link_url is not OMIT:
            _request["should_create_magic_link_url"] = should_create_magic_link_url
        if common_models is not OMIT:
            _request["common_models"] = common_models
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/link-token"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(LinkToken, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLinkTokenClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        end_user_email_address: str,
        end_user_organization_name: str,
        end_user_origin_id: str,
        categories: typing.List[CategoriesEnum],
        integration: typing.Optional[str] = OMIT,
        link_expiry_mins: typing.Optional[int] = OMIT,
        should_create_magic_link_url: typing.Optional[bool] = OMIT,
        common_models: typing.Optional[typing.List[CommonModelScopesBodyRequest]] = OMIT,
    ) -> LinkToken:
        """
        Creates a link token to be used when linking a new end user.

        Parameters:
            - end_user_email_address: str. Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent. <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 100 characters`</span>

            - end_user_organization_name: str. Your end user's organization. <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 100 characters`</span>

            - end_user_origin_id: str. This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers. <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 100 characters`</span>

            - categories: typing.List[CategoriesEnum]. The integration categories to show in Merge Link.

            - integration: typing.Optional[str]. The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://www.merge.dev/docs/basics/integration-metadata/.

            - link_expiry_mins: typing.Optional[int]. An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.

            - should_create_magic_link_url: typing.Optional[bool]. Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/integrations-fast-say-hello-to-magic-link.

            - common_models: typing.Optional[typing.List[CommonModelScopesBodyRequest]]. An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.
        """
        _request: typing.Dict[str, typing.Any] = {
            "end_user_email_address": end_user_email_address,
            "end_user_organization_name": end_user_organization_name,
            "end_user_origin_id": end_user_origin_id,
            "categories": categories,
        }
        if integration is not OMIT:
            _request["integration"] = integration
        if link_expiry_mins is not OMIT:
            _request["link_expiry_mins"] = link_expiry_mins
        if should_create_magic_link_url is not OMIT:
            _request["should_create_magic_link_url"] = should_create_magic_link_url
        if common_models is not OMIT:
            _request["common_models"] = common_models
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "api/filestorage/v1/link-token"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(LinkToken, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)