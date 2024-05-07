"""dummy

Revision ID: 78187d2337be
Revises: 95a42a180623
Create Date: 2024-05-07 20:25:24.518762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78187d2337be'
down_revision: Union[str, None] = '95a42a180623'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        "dummy",
        sa.Column("name", sa.VARCHAR(255)),
        sa.Column("author", sa.VARCHAR(255))
    )
    pass


def downgrade() -> None:
    op.drop_table("dummy")
    pass