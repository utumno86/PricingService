import uuid
import re
from dataclasses import dataclass, field
from typing import Dict
from models.model import Model

@dataclass
class Store(Model):
    collection: str = field(init=False, default="stores")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
      return {
        "_id": self._id,
        "url_prefix": self.url_prefix,
        "tag_name": self.tag_name,
        "query": self.query,
        "name": self.name
      }

    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
      return cls.find_one_by("name", store_name)

    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
      return cls.find_one_by("url_prefix", url_prefix)

    @classmethod
    def find_by_url(cls, url: str) -> "Store":
      pattern = re.compile(r"(https?://.*?/)")
      match = pattern.search(url)
      url_prefix = match.group(1)
      return cls.get_by_url_prefix(url_prefix)