from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class FileTransferClient(Client):
    """
    The "File Transfer DXL Python client" client wrapper class.
    """

    def my_example_method(self):
        """
        TODO: Example only, should be removed

        This is an example method that demonstrates how DXL service invocations
        can be wrapped by the client. In this particular case we are making a
        service request to the broker the client is currently connected to in
        order to retrieve its health information. The results of the query are
        returned as a Python dictionary. The DXL-specific details (topics,
        message objects, JSON payload format, etc.) are hidden from the users of
        this method.

        :return: The result of the broker health query
        """
        # Create the DXL request message
        request = Request("/mcafee/service/dxl/broker/health")

        # Set the payload on the request message (Python dictionary to JSON payload)
        MessageUtils.dict_to_json_payload(request, {})

        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)

        # Convert the JSON payload in the DXL response message to a Python dictionary
        # and return it.
        return MessageUtils.json_payload_to_dict(response)
