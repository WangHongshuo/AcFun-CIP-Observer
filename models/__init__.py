from .article import Base as ArticleBase
from .user import Base as UserBase

__all__ = ['article', 'user']

ModelBaseMetadata= [
  ArticleBase.metadata,
  UserBase.metadata
]



