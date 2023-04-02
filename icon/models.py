import datetime
from typing import Optional, List, Union, Dict

from pydantic.class_validators import validator
from pydantic.networks import AnyHttpUrl
from pydantic.types import constr
from collection.models import Collection as CollectionModel, Tag

from utils.base import UUIDModel, PermalinkField, SlugField


class Icon(UUIDModel, PermalinkField, SlugField):
    attribution: Optional[constr(max_length=50)]
    attribution_preview_url: AnyHttpUrl
    collections: List[CollectionModel]
    date_uploaded: Union[datetime.datetime, str]
    icon_url: AnyHttpUrl
    is_active: bool = False
    license_description: str
    preview_url: AnyHttpUrl
    preview_url_42: AnyHttpUrl
    attribution_preview_url: AnyHttpUrl
    sponsor: Dict[str, str] = {}
    sponsor_campaign_link: AnyHttpUrl = None
    sponsor_id: str
    tags: List[Tag] = []
    term: Optional[constr(max_length=50)]
    term_id: int
    term_slug: str
    uploader: Optional[constr(max_length=50)]
    uploader_id: str
    year: int

    @validator("year")
    def check_year(cls, value):
        today = datetime.datetime.now().year
        past_50_years = today - 50
        assert past_50_years <= value <= today, f"Your date must be in at least {past_50_years}-{today}"
        return value
