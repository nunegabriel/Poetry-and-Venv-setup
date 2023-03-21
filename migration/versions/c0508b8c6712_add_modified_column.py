"""ADD MODIFIED COLUMN

Revision ID: c0508b8c6712
Revises: 2645cd5bb949
Create Date: 2023-03-21 15:34:45.668869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0508b8c6712'
down_revision = '2645cd5bb949'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column('events', sa.Column('last_modified', sa.DateTime))

def downgrade() -> None:
    pass
