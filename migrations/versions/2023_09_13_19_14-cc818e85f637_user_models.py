"""user models

Revision ID: cc818e85f637
Revises:
Create Date: 2023-09-13 19:14:15.579524

"""
import sqlalchemy as sa
from alembic import op

import src

# revision identifiers, used by Alembic.
revision = "cc818e85f637"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users_social_network",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("icon", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users_user",
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("password", src.users.utils.password_hash.Password(length=128), nullable=False),
        sa.Column("first_name", sa.String(length=30), nullable=False),
        sa.Column("last_name", sa.String(length=30), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("avatar", sa.String(), nullable=True),
        sa.Column("is_banned", sa.Boolean(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_user_created_at"), "users_user", ["created_at"], unique=False)
    op.create_index(op.f("ix_users_user_email"), "users_user", ["email"], unique=True)
    op.create_index(op.f("ix_users_user_username"), "users_user", ["username"], unique=True)
    op.create_table(
        "users_personal_info",
        sa.Column("site", sa.String(), nullable=True),
        sa.Column("about", sa.Text(), nullable=True),
        sa.Column("time_zone", sa.DateTime(timezone=True), nullable=False),
        sa.Column("dev_exp", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("language", sa.String(length=100), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "users_social_accounts",
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("user_metadata", sa.JSON(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users_user_social",
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("social_network_id", sa.UUID(), nullable=False),
        sa.Column("link", sa.String(length=100), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["social_network_id"],
            ["users_social_network.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users_competence",
        sa.Column("competence", sa.String(length=100), nullable=False),
        sa.Column("personal_info", sa.UUID(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["personal_info"],
            ["users_personal_info.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users_competence_group",
        sa.Column("competence_id", sa.UUID(), nullable=False),
        sa.Column("personal_info_id", sa.UUID(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["competence_id"],
            ["users_competence.id"],
        ),
        sa.ForeignKeyConstraint(
            ["personal_info_id"],
            ["users_personal_info.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("competence_id", "personal_info_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users_competence_group")
    op.drop_table("users_competence")
    op.drop_table("users_user_social")
    op.drop_table("users_social_accounts")
    op.drop_table("users_personal_info")
    op.drop_index(op.f("ix_users_user_username"), table_name="users_user")
    op.drop_index(op.f("ix_users_user_email"), table_name="users_user")
    op.drop_index(op.f("ix_users_user_created_at"), table_name="users_user")
    op.drop_table("users_user")
    op.drop_table("users_social_network")
    # ### end Alembic commands ###