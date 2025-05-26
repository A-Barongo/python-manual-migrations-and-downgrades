"""Renaming students to scholars

Revision ID: c2641c3f5c7b
Revises: 791279dd0760
Create Date: 2025-05-26 19:30:17.639195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2641c3f5c7b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
