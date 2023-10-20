"""init_db

修订 ID: 32c01e50814d
父修订: 
创建时间: 2023-10-19 15:33:59.636036

"""
from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "32c01e50814d"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = "nonebot_plugin_chess"
depends_on: str | Sequence[str] | None = None


def upgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_chess_gamerecord",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("game_id", sa.String(length=128), nullable=False),
        sa.Column("session_id", sa.String(length=128), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("update_time", sa.DateTime(), nullable=False),
        sa.Column("player_white_id", sa.String(length=64), nullable=False),
        sa.Column("player_white_name", sa.Text(), nullable=False),
        sa.Column("player_white_is_ai", sa.Boolean(), nullable=False),
        sa.Column("player_white_level", sa.Integer(), nullable=False),
        sa.Column("player_black_id", sa.String(length=64), nullable=False),
        sa.Column("player_black_name", sa.Text(), nullable=False),
        sa.Column("player_black_is_ai", sa.Boolean(), nullable=False),
        sa.Column("player_black_level", sa.Integer(), nullable=False),
        sa.Column("start_fen", sa.Text(), nullable=False),
        sa.Column("moves", sa.Text(), nullable=False),
        sa.Column("is_game_over", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_nonebot_plugin_chess_gamerecord")),
    )
    # ### end Alembic commands ###


def downgrade(name: str = "") -> None:
    if name:
        return
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_chess_gamerecord")
    # ### end Alembic commands ###