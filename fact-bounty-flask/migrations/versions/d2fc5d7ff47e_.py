"""empty message

Revision ID: d2fc5d7ff47e
Revises:
Create Date: 2019-07-02 18:28:34.801535

"""
from __future__ import annotations
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d2fc5d7ff47e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vote",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("story_id", sa.String(length=128), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("value", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("vote")
    # ### end Alembic commands ###
