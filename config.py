from dataclasses import dataclass


@dataclass(frozen=True)
class _CommonSettings:
    url = 'https://yandex.ru/'
    timeout = 10


@dataclass(frozen=True)
class _News:
    rows_count = 5
    rows_count_after_click_more = 10


@dataclass(frozen=True)
class _Config:
    common_settings = _CommonSettings()
    news = _News()


CONFIG = _Config()
