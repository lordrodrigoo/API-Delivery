"""create table users

Revision ID: a5413f30bce3
Revises: 
Create Date: 2026-01-09 18:04:46.228598

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op



# revision identifiers, used by Alembic.
revision: str = 'a5413f30bce3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', #pylint: disable=no-member
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table('users') #pylint: disable=no-member
    # ### end Alembic commands ###
