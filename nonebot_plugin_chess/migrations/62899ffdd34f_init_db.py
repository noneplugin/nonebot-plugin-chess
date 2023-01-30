"""init_db

Revision ID: 62899ffdd34f
Revises: 
Create Date: 2023-01-30 22:45:31.948438

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "62899ffdd34f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nonebot_plugin_chess_gamerecord",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("game_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("session_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("update_time", sa.DateTime(), nullable=False),
        sa.Column(
            "player_white_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "player_white_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("player_white_is_ai", sa.Boolean(), nullable=False),
        sa.Column("player_white_level", sa.Integer(), nullable=False),
        sa.Column(
            "player_black_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "player_black_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("player_black_is_ai", sa.Boolean(), nullable=False),
        sa.Column("player_black_level", sa.Integer(), nullable=False),
        sa.Column("start_fen", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("moves", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("is_game_over", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nonebot_plugin_chess_gamerecord")
    # ### end Alembic commands ###
