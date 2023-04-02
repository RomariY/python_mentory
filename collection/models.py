import datetime
from typing import Optional, Dict, List, Union

from pydantic.networks import HttpUrl
from pydantic.types import constr

from utils.base import UUIDModel, PermalinkField, SlugField


class Tag(UUIDModel, SlugField):
    pass


class Author(UUIDModel, PermalinkField):
    location: Optional[constr(max_length=50)]
    name: Optional[constr(max_length=50)]
    username: Optional[constr(max_length=50)]


class Collection(UUIDModel, PermalinkField):
    author: Author
    description: str = ""
    date_created: datetime.datetime = datetime.datetime.now()
    date_updated: datetime.datetime = datetime.datetime.now()
    is_collaborative: bool = False
    is_featured: bool = False
    is_published: bool = False
    is_store_item: bool = False
    name: Optional[constr(max_length=50)]
    sponsor: Dict[str, str] = {}
    sponsor_campaign_link: Union[HttpUrl, str]
    sponsor_id: str
    tags: List[Tag] = []
    template: Optional[constr(max_length=5)]
