r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EventTypeInstance(InstanceResource):
    """
    :ivar type: A string that uniquely identifies this Event Type.
    :ivar schema_id: A string that uniquely identifies the Schema this Event Type adheres to.
    :ivar date_created: The date that this Event Type was created, given in ISO 8601 format.
    :ivar date_updated: The date that this Event Type was updated, given in ISO 8601 format.
    :ivar description: A human readable description for this Event Type.
    :ivar url: The URL of this resource.
    :ivar links:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], type: Optional[str] = None
    ):
        super().__init__(version)

        self.type: Optional[str] = payload.get("type")
        self.schema_id: Optional[str] = payload.get("schema_id")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.description: Optional[str] = payload.get("description")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "type": type or self.type,
        }
        self._context: Optional[EventTypeContext] = None

    @property
    def _proxy(self) -> "EventTypeContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EventTypeContext for this EventTypeInstance
        """
        if self._context is None:
            self._context = EventTypeContext(
                self._version,
                type=self._solution["type"],
            )
        return self._context

    def fetch(self) -> "EventTypeInstance":
        """
        Fetch the EventTypeInstance


        :returns: The fetched EventTypeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EventTypeInstance":
        """
        Asynchronous coroutine to fetch the EventTypeInstance


        :returns: The fetched EventTypeInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.EventTypeInstance {}>".format(context)


class EventTypeContext(InstanceContext):

    def __init__(self, version: Version, type: str):
        """
        Initialize the EventTypeContext

        :param version: Version that contains the resource
        :param type: A string that uniquely identifies this Event Type.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "type": type,
        }
        self._uri = "/Types/{type}".format(**self._solution)

    def fetch(self) -> EventTypeInstance:
        """
        Fetch the EventTypeInstance


        :returns: The fetched EventTypeInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EventTypeInstance(
            self._version,
            payload,
            type=self._solution["type"],
        )

    async def fetch_async(self) -> EventTypeInstance:
        """
        Asynchronous coroutine to fetch the EventTypeInstance


        :returns: The fetched EventTypeInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EventTypeInstance(
            self._version,
            payload,
            type=self._solution["type"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.EventTypeContext {}>".format(context)


class EventTypePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> EventTypeInstance:
        """
        Build an instance of EventTypeInstance

        :param payload: Payload response from the API
        """
        return EventTypeInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.EventTypePage>"


class EventTypeList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the EventTypeList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Types"

    def stream(
        self,
        schema_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[EventTypeInstance]:
        """
        Streams EventTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(schema_id=schema_id, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        schema_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[EventTypeInstance]:
        """
        Asynchronously streams EventTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(schema_id=schema_id, page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        schema_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EventTypeInstance]:
        """
        Lists EventTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                schema_id=schema_id,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        schema_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EventTypeInstance]:
        """
        Asynchronously lists EventTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                schema_id=schema_id,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        schema_id: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EventTypePage:
        """
        Retrieve a single page of EventTypeInstance records from the API.
        Request is executed immediately

        :param schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EventTypeInstance
        """
        data = values.of(
            {
                "SchemaId": schema_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EventTypePage(self._version, response)

    async def page_async(
        self,
        schema_id: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EventTypePage:
        """
        Asynchronously retrieve a single page of EventTypeInstance records from the API.
        Request is executed immediately

        :param schema_id: A string parameter filtering the results to return only the Event Types using a given schema.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EventTypeInstance
        """
        data = values.of(
            {
                "SchemaId": schema_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return EventTypePage(self._version, response)

    def get_page(self, target_url: str) -> EventTypePage:
        """
        Retrieve a specific page of EventTypeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EventTypeInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EventTypePage(self._version, response)

    async def get_page_async(self, target_url: str) -> EventTypePage:
        """
        Asynchronously retrieve a specific page of EventTypeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EventTypeInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EventTypePage(self._version, response)

    def get(self, type: str) -> EventTypeContext:
        """
        Constructs a EventTypeContext

        :param type: A string that uniquely identifies this Event Type.
        """
        return EventTypeContext(self._version, type=type)

    def __call__(self, type: str) -> EventTypeContext:
        """
        Constructs a EventTypeContext

        :param type: A string that uniquely identifies this Event Type.
        """
        return EventTypeContext(self._version, type=type)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.EventTypeList>"
