class HTTPConnectorException(Exception):
    pass


class HTTPConnectorHTTPError(HTTPConnectorException):
    pass


class HTTPConnectorTimeoutError(HTTPConnectorException):
    pass

class HTTPResponseConverterError(HTTPConnectorException):
    pass
