#pylint: disable=no-member
"""Ajusted account(status)

Revision ID: fa4da43a2fa5
Revises: 1c6a41981099
Create Date: 2026-01-19 22:48:55.974259

"""
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'fa4da43a2fa5'
down_revision: Union[str, Sequence[str], None] = '1c6a41981099'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('accounts', 'status',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(length=20),
               existing_nullable=True)


def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column('accounts', 'status',
               existing_type=sa.String(length=20),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
