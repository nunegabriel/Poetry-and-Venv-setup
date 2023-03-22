"""CREATE TABLE

Revision ID: 3706c66cbd39
Revises: 
Create Date: 2023-03-22 10:05:57.350018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3706c66cbd39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('event', sa.Unicode(200)),
        sa.Column('creation_date', sa.DateTime(), nullable=False, server_default=sa.func.now()),
        sa.Column('modified_date', sa.DateTime(), nullable=False, server_default=sa.func.now())
    )



def downgrade() -> None:
    pass
