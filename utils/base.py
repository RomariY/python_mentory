import re
from typing import Optional
from uuid import UUID, uuid4

from pydantic.class_validators import validator
from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.types import constr


class UUIDModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)


class PermalinkField(BaseModel):
    permalink: Optional[constr(max_length=50)]

    @validator("permalink")
    def check_permalink(cls, value):
        assert re.match(r"(^/)", value), "It's not look like a permalink."
        return value


class SlugField(BaseModel):
    slug: Optional[constr(max_length=50)]

    @validator("slug")
    def slugify(cls, value):
        assert re.match('^[-\w]+$', value), "Insert the valid slug field."
        return value
