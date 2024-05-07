"""user

Revision ID: 04cbf4217efa
Revises: 
Create Date: 2024-05-07 19:35:41.885239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04cbf4217efa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("name", sa.VARCHAR(255)),
        sa.Column("l_name", sa.VARCHAR(255))
    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
