"""fifth

Revision ID: 410c054413f3
Revises: da4431e5867e
Create Date: 2019-05-27 20:55:14.520532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '410c054413f3'
down_revision = 'da4431e5867e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_hash')
    # ### end Alembic commands ###
