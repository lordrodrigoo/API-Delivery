#pylint: disable=no-member
"""ajusted entity account (field username unique ) 

Revision ID: 0d9bbab453b2
Revises: fa490857cea9
Create Date: 2026-01-22 17:52:13.691704

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op


revision: str = '0d9bbab453b2'
down_revision: Union[str, Sequence[str], None] = 'fa490857cea9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(None, 'accounts', ['username'])
    op.drop_constraint(op.f('orders_address_id_fkey'), 'orders', type_='foreignkey')
    op.drop_column('orders', 'address_id')


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column('orders', sa.Column('address_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key(op.f('orders_address_id_fkey'), 'orders', 'addresses', ['address_id'], ['id'])
    op.drop_constraint(None, 'accounts', type_='unique')
