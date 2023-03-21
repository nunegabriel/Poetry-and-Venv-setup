"""create events table

Revision ID: 2645cd5bb949
Revises: 
Create Date: 2023-03-21 10:44:09.116011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2645cd5bb949'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('event', sa.Unicode(200)),
        sa.Column('creation_date', sa.DateTime(), nullable=False, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('events')
