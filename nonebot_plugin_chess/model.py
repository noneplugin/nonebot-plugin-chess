from datetime import datetime

from nonebot_plugin_orm import Model
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class GameRecord(Model):
    """对局记录"""

    __tablename__ = "nonebot_plugin_chess_gamerecord"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    game_id: Mapped[str] = mapped_column(String(128))
    session_id: Mapped[str] = mapped_column(String(128))
    start_time: Mapped[datetime] = mapped_column(default=datetime.now())
    """ 游戏开始时间 """
    update_time: Mapped[datetime] = mapped_column(default=datetime.now())
    """ 游戏更新时间 """
    player_white_id: Mapped[str] = mapped_column(String(64), default="")
    """ 白方id """
    player_white_name: Mapped[str] = mapped_column(Text, default="")
    """ 白方名字 """
    player_white_is_ai: Mapped[bool] = mapped_column(default=False)
    """ 白方是否为AI """
    player_white_level: Mapped[int] = mapped_column(default=0)
    """ 白方等级 """
    player_black_id: Mapped[str] = mapped_column(String(64), default="")
    """ 黑方id """
    player_black_name: Mapped[str] = mapped_column(Text, default="")
    """ 黑方名字 """
    player_black_is_ai: Mapped[bool] = mapped_column(default=False)
    """ 黑方是否为AI """
    player_black_level: Mapped[int] = mapped_column(default=0)
    """ 黑方等级 """
    start_fen: Mapped[str] = mapped_column(Text, default="")
    """ 起始局面FEN字符串 """
    moves: Mapped[str] = mapped_column(Text, default="")
    """ 所有移动，uci形式，以空格分隔 """
    is_game_over: Mapped[bool] = mapped_column(default=False)
    """ 游戏是否已结束 """
