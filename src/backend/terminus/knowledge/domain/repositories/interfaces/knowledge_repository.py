from abc import ABC

from terminus.common.repositories.interfaces.base_repository import BaseRepository
from terminus.knowledge.domain.models.knowledge import Knowledge


class KnowledgeRepository(BaseRepository[Knowledge, int], ABC):
    """知识库仓库接口"""
    pass
