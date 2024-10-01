"""Add admin and faculty validation to Bibliography

Revision ID: 95409c0a7e8c
Revises: 
Create Date: 2024-09-30 15:42:38.260666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95409c0a7e8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bibliography', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_validated_by_admin', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('is_validated_by_faculty', sa.Boolean(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    with op.batch_alter_table('bibliography', schema=None) as batch_op:
        batch_op.drop_column('is_validated_by_faculty')
        batch_op.drop_column('is_validated_by_admin')

    # ### end Alembic commands ###
