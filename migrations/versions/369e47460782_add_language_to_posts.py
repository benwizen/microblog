"""add language to posts

Revision ID: 369e47460782
Revises: 9748a8535b4c
Create Date: 2020-04-18 14:58:08.455080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '369e47460782'
down_revision = '9748a8535b4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
