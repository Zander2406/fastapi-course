"""Add content column to posts table

Revision ID: af8737722e0b
Revises: 713bef6fa782
Create Date: 2022-05-05 18:39:44.589802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8737722e0b'
down_revision = '713bef6fa782'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
