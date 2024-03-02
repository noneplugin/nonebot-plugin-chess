from pathlib import Path

from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    chess_engine_path: Path = Path("data/chess/stockfish")


chess_config = get_plugin_config(Config)
