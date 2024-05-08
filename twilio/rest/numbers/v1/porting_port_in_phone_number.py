r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.instance_context import InstanceContext

from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PortingPortInPhoneNumberContext(InstanceContext):

    def __init__(
        self, version: Version, port_in_request_sid: str, phone_number_sid: str
    ):
        """
        Initialize the PortingPortInPhoneNumberContext

        :param version: Version that contains the resource
        :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
        :param phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone number.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "port_in_request_sid": port_in_request_sid,
            "phone_number_sid": phone_number_sid,
        }
        self._uri = "/Porting/PortIn/{port_in_request_sid}/PhoneNumber/{phone_number_sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the PortingPortInPhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the PortingPortInPhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V1.PortingPortInPhoneNumberContext {}>".format(context)


class PortingPortInPhoneNumberList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PortingPortInPhoneNumberList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(
        self, port_in_request_sid: str, phone_number_sid: str
    ) -> PortingPortInPhoneNumberContext:
        """
        Constructs a PortingPortInPhoneNumberContext

        :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
        :param phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone number.
        """
        return PortingPortInPhoneNumberContext(
            self._version,
            port_in_request_sid=port_in_request_sid,
            phone_number_sid=phone_number_sid,
        )

    def __call__(
        self, port_in_request_sid: str, phone_number_sid: str
    ) -> PortingPortInPhoneNumberContext:
        """
        Constructs a PortingPortInPhoneNumberContext

        :param port_in_request_sid: The SID of the Port In request. This is a unique identifier of the port in request.
        :param phone_number_sid: The SID of the Port In request phone number. This is a unique identifier of the phone number.
        """
        return PortingPortInPhoneNumberContext(
            self._version,
            port_in_request_sid=port_in_request_sid,
            phone_number_sid=phone_number_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.PortingPortInPhoneNumberList>"
