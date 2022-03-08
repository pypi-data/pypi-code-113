import logging
from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional

from scriptable.abstract_engine import ScriptableEngine
from scriptable.hypothesis_engine import HypothesisEngine
from scriptable.typescript_engine import TypescriptEngine

from arrow_bpmn.__spi__.execution.script_factory import ScriptFactory


@dataclass
class LRUCache(OrderedDict):
    cache_size: int

    def __getitem__(self, item: str) -> Optional[ScriptableEngine]:
        if item in self:
            logging.info(f"cache hit for {item}")
            self.move_to_end(item, last=True)
            return super().__getitem__(item)
        return None

    def __setitem__(self, key: str, value: ScriptableEngine):
        super().__setitem__(key, value)
        if len(self) > self.cache_size:
            evict_key, evict_val = self.popitem(last=False)
            logging.info(f"evict item from LRU cache {evict_key}={evict_val}")


class CacheableScriptFactory(ScriptFactory):

    def __init__(self, cache_size: int):
        self.cache = LRUCache(cache_size)

    def parse(self, language: str, script: str) -> ScriptableEngine:
        key = str(hash(language + ":" + script))

        cached_item = self.cache[key]
        if cached_item is not None:
            return cached_item

        if language == "typescript" or language == "javascript":
            engine = TypescriptEngine.parse(script)
            self.cache[key] = engine
            return engine
        if language == "hypothesis":
            engine = HypothesisEngine.parse(script)
            self.cache[key] = engine
            return engine
        else:
            raise ValueError(f"cannot initialize script engine for {language}")
