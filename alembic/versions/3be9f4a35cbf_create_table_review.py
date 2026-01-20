#pylint: disable=no-member
"""Create table review

Revision ID: 3be9f4a35cbf
Revises: 3f3044fa0b51
Create Date: 2026-01-19 23:43:11.468637

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op


revision: str = '3be9f4a35cbf'
down_revision: Union[str, Sequence[str], None] = '3f3044fa0b51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rating', sa.Numeric(precision=2, scale=1), nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('reviews')
