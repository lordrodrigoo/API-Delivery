#pylint: disable=no-member
"""ajusted relationship bettwen with back_populate

Revision ID: fa490857cea9
Revises: 4ace5a091546
Create Date: 2026-01-21 17:54:50.359883

"""
from typing import Sequence, Union


revision: str = 'fa490857cea9'
down_revision: Union[str, Sequence[str], None] = '4ace5a091546'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
