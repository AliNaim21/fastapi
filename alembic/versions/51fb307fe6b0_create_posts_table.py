"""Create posts table

Revision ID: 51fb307fe6b0
Revises: 
Create Date: 2023-06-10 11:50:10.254338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51fb307fe6b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(length=255), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
