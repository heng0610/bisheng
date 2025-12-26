from abc import ABC

from terminus.common.models.config import Config
from terminus.common.repositories.interfaces.base_repository import BaseRepository


class ConfigRepository(BaseRepository[Config, str], ABC):
    """配置仓库接口"""
    pass
