"""added category

Revision ID: 7b6a93bc3cfa
Revises: 50e29a23dd2e
Create Date: 2019-05-28 15:37:34.182232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b6a93bc3cfa'
down_revision = '50e29a23dd2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'category')
    # ### end Alembic commands ###