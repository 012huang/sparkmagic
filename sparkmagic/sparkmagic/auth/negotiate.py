"""Class for implementing a Negotiate authenticator for SparkMagic"""

from requests_negotiate import HTTPNegotiateAuth
from .customauth import Authenticator


class Negotiate(HTTPNegotiateAuth, Authenticator):
    """Negotiate authenticator for SparkMagic"""

    def __init__(self, parsed_attributes=None):
        """Initializes the Authenticator with the attributes in the attributes
        parsed from a %spark magic command if applicable, or with default values
        otherwise.

        Args:
            self,
            parsed_attributes (IPython.core.magics.namespace): The namespace object that
            is created from parsing %spark magic command.
        """
        HTTPNegotiateAuth.__init__(self)
        Authenticator.__init__(self, parsed_attributes)

    def __call__(self, request):
        return HTTPNegotiateAuth.__call__(self, request)

    def __hash__(self):
        return hash((self.url, self.__class__.__name__))
