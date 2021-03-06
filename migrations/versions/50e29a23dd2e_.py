"""empty message

Revision ID: 50e29a23dd2e
Revises: 08495ae9d885
Create Date: 2019-05-28 14:35:18.061422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50e29a23dd2e'
down_revision = '08495ae9d885'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted_by', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'posted_by')
    # ### end Alembic commands ###
