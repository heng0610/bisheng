from terminus.services.factory import ServiceFactory
from terminus.services.session.service import SessionService

# if TYPE_CHECKING:
#     from terminus.services.cache.service import BaseCacheService


class SessionServiceFactory(ServiceFactory):

    def __init__(self):
        super().__init__(SessionService)

    def create(self):
        return SessionService()
