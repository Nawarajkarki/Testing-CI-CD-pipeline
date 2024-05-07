"""book

Revision ID: 95a42a180623
Revises: 04cbf4217efa
Create Date: 2024-05-07 20:02:56.187462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95a42a180623'
down_revision: Union[str, None] = '04cbf4217efa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "book",
        sa.Column("name", sa.VARCHAR(255)),
        sa.Column("author", sa.VARCHAR(255))
    )
    pass


def downgrade() -> None:
    op.drop_table("book")
    pass
