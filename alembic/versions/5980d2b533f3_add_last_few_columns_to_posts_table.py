"""add last few columns to posts table

Revision ID: 5980d2b533f3
Revises: 9b9d50bc8eef
Create Date: 2022-05-05 19:12:56.196216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5980d2b533f3'
down_revision = '9b9d50bc8eef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                                     nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
