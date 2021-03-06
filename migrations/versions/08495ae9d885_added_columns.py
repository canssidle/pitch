"""added columns

Revision ID: 08495ae9d885
Revises: 410c054413f3
Create Date: 2019-05-28 14:30:20.468562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08495ae9d885'
down_revision = '410c054413f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_body', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('comment_title', sa.String(), nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment_title')
    op.drop_column('comments', 'comment_body')
    # ### end Alembic commands ###
