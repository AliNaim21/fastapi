"""Add content column to posts table

Revision ID: 7333b4d75dd2
Revises: 51fb307fe6b0
Create Date: 2023-06-10 11:57:44.465629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7333b4d75dd2'
down_revision = '51fb307fe6b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(250), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
