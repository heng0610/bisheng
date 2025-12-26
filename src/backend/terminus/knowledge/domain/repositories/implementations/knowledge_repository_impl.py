from typing import Union

from sqlmodel import Session
from sqlmodel.ext.asyncio.session import AsyncSession

from terminus.common.repositories.implementations.base_repository_impl import BaseRepositoryImpl
from terminus.knowledge.domain.models.knowledge import Knowledge
from terminus.knowledge.domain.repositories.interfaces.knowledge_repository import KnowledgeRepository


class KnowledgeRepositoryImpl(BaseRepositoryImpl[Knowledge, int], KnowledgeRepository):
    """知识库仓库实现类"""

    def __init__(self, session: Union[AsyncSession, Session]):
        super().__init__(session, Knowledge)
