"""Add columns

Revision ID: 8ccc74cd8d1a
Revises: 92adc8bc099e
Create Date: 2023-03-16 11:56:04.309660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ccc74cd8d1a'
down_revision = '92adc8bc099e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',sa.Column('dept', sa.String(50), nullable=False)),
    


def downgrade():
    op.drop_column('users','dept')
