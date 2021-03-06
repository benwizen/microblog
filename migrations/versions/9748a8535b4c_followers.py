"""followers

Revision ID: 9748a8535b4c
Revises: c29791050733
Create Date: 2020-04-17 16:56:49.274813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9748a8535b4c'
down_revision = 'c29791050733'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
