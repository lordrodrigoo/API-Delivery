#pylint: disable=no-member
"""Created table orders_item

Revision ID: 3f3044fa0b51
Revises: fa4da43a2fa5
Create Date: 2026-01-19 23:19:55.134462

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op


revision: str = '3f3044fa0b51'
down_revision: Union[str, Sequence[str], None] = 'fa4da43a2fa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('subtotal', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('order_items')
