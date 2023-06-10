"""add last few columns to posts table

Revision ID: 104af9469efc
Revises: 8ed090c45d3d
Create Date: 2023-06-10 12:28:57.397395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104af9469efc'
down_revision = '8ed090c45d3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='1'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
