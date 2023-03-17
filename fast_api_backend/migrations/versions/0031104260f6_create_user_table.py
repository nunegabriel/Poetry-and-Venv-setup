"""create user table

Revision ID: 0031104260f6
Revises: 
Create Date: 2023-03-16 10:32:08.727371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0031104260f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('hashed_password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True),
       
    )


def downgrade():
    op.drop_table('users')
