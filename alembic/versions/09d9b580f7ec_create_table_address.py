"""create table address 

Revision ID: 09d9b580f7ec
Revises: 6ebc966ec598
Create Date: 2026-01-13 16:13:02.246609

"""
#pylint: disable=no-member
from typing import Sequence, Union
import sqlalchemy as sa
from alembic import op

revision: str = '09d9b580f7ec'
down_revision: Union[str, Sequence[str], None] = '6ebc966ec598'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=100), nullable=False),
    sa.Column('number', sa.String(length=10), nullable=False),
    sa.Column('complement', sa.String(length=50), nullable=True),
    sa.Column('neighborhood', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('zip_code', sa.String(length=10), nullable=False),
    sa.Column('is_default', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('products', 'created_at',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.DateTime(),
               existing_nullable=False,
               postgresql_using="created_at::timestamp without time zone")
    op.alter_column('products', 'updated_at',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.DateTime(),
               existing_nullable=True,
               postgresql_using="updated_at::timestamp without time zone")
    op.alter_column('users', 'created_at',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.DateTime(),
               existing_nullable=False,
               postgresql_using="created_at::timestamp without time zone")
    op.alter_column('users', 'updated_at',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.DateTime(),
               existing_nullable=True,
               postgresql_using="updated_at::timestamp without time zone")


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('users', 'updated_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(length=30),
               existing_nullable=True)
    op.alter_column('users', 'created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('products', 'updated_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(length=30),
               existing_nullable=True)
    op.alter_column('products', 'created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.drop_table('addresses')
