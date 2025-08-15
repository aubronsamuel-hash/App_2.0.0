from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("role", sa.String, nullable=False),
        sa.Column("prefs", sa.JSON, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=True),
        sa.Column("updated_at", sa.DateTime, nullable=True),
        sa.Column("deleted_at", sa.DateTime, nullable=True),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "missions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("start", sa.DateTime, nullable=False),
        sa.Column("end", sa.DateTime, nullable=False),
        sa.Column("location", sa.String, nullable=False),
        sa.Column("call_time", sa.DateTime, nullable=True),
        sa.Column("positions", sa.JSON, nullable=True),
        sa.Column("documents", sa.JSON, nullable=True),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("created_by", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=True),
        sa.Column("updated_at", sa.DateTime, nullable=True),
    )
    op.create_index("ix_missions_start", "missions", ["start"])
    op.create_index("ix_missions_end", "missions", ["end"])

    op.create_table(
        "assignments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("mission_id", sa.Integer, sa.ForeignKey("missions.id"), nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=True),
        sa.Column("role_label", sa.String, nullable=False),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("channel", sa.String, nullable=True),
        sa.Column("responded_at", sa.DateTime, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=True),
        sa.Column("updated_at", sa.DateTime, nullable=True),
    )
    op.create_index("ix_assignments_user_id", "assignments", ["user_id"])

    op.create_table(
        "files",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("path", sa.String, nullable=False),
        sa.Column("mission_id", sa.Integer, sa.ForeignKey("missions.id"), nullable=True),
        sa.Column("uploaded_at", sa.DateTime, nullable=True),
    )

    op.create_table(
        "audit_logs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=True),
        sa.Column("action", sa.String, nullable=False),
        sa.Column("payload", sa.JSON, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("audit_logs")
    op.drop_table("files")
    op.drop_index("ix_assignments_user_id", table_name="assignments")
    op.drop_table("assignments")
    op.drop_index("ix_missions_end", table_name="missions")
    op.drop_index("ix_missions_start", table_name="missions")
    op.drop_table("missions")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
