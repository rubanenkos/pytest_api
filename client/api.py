from requests import Response, request
from logger_config import setup_logger
logger = setup_logger()


class Api:

    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        The method is a wrapper for the standard request from requests lib
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """

        logger.info(f"{method} request by URL: {url}")
        response = request(method, url, **kwargs)
        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response.text}" if response.text else "Response Body: Empty")
        return response
