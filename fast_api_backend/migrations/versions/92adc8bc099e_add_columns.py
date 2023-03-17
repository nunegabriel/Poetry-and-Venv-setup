"""Add columns

Revision ID: 92adc8bc099e
Revises: 36b181894ad0
Create Date: 2023-03-16 11:30:18.896130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92adc8bc099e'
down_revision = '36b181894ad0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',sa.Column('first_na', sa.String(50), nullable=False)),
    op.add_column('users',sa.Column('last_name', sa.String(50), nullable=False))

       
    


def downgrade():
    op.drop_column('users','first_name')
    op.drop_column('users','last_name')

