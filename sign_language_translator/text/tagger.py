from typing import Callable, List, Tuple
import re

import enum


class Tags(enum.Enum):
    WORD = "WORD"
    DATE = "DATE"
    NAME = "NAME"
    SPACE = "SPACE"
    NUMBER = "NUMBER"
    ACRONYM = "ACRONYM"
    PUNCTUATION = "PUNCTUATION"
    DEFAULT = ""
    # CONTEXT = "(something)"


class Rule:
    def __init__(self, matcher: Callable[[str], bool], tag: str, priority: int):
        self.matcher = matcher
        self.tag = tag
        self.priority = priority

    def is_match(self, token: str):
        return self.matcher(token)

    def get_tag(self):
        return self.tag

    def get_priority(self):
        return self.priority

    @staticmethod
    def from_pattern(pattern: str, tag: str, priority: int):
        def match(text: str):
            return bool(re.match(pattern, text))

        return Rule(match, tag, priority)


class Tagger:
    def __init__(self, rules: List[Rule], default=Tags.DEFAULT):
        self.rules = rules
        self.default = default

    def tag(self, tokens: List[str]) -> List[Tuple[str, str]]:
        tagged_tokens = list(zip(tokens, self.get_tags(tokens)))

        return tagged_tokens

    def get_tags(self, tokens: List[str]) -> List[str]:
        return [self._apply_rules(token) for token in tokens]

    def _apply_rules(self, token: str) -> str:
        tag = self.default
        priority = float("inf")

        for rule in self.rules:
            if rule.is_match(token):
                if rule.get_priority() < priority:
                    tag = rule.get_tag()
                    priority = rule.get_priority()

        return tag
