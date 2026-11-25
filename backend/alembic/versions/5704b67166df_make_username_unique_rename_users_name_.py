"""make username unique

Rename users.name -> users.username;
Make users.username unique field.

Revision ID: 5704b67166df
Revises: 252199303e2b
Create Date: 2026-11-25 22:46:08.370096

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5704b67166df"
down_revision: str | Sequence[str] | None = "252199303e2b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.alter_column(
            "name",
            new_column_name="username",
            existing_type=sa.VARCHAR(length=32),
            existing_nullable=False,
        )

        batch_op.create_unique_constraint(
            "uq_users_username",
            ["username"],
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_constraint(
            "uq_users_username",
            type_="unique",
        )

        batch_op.alter_column(
            "username",
            new_column_name="name",
            existing_type=sa.VARCHAR(length=32),
            existing_nullable=False,
        )
