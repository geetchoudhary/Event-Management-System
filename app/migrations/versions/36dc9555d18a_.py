"""empty message

Revision ID: 36dc9555d18a
Revises: 2890f1e9e65a
Create Date: 2019-11-27 23:23:02.877536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36dc9555d18a'
down_revision = '2890f1e9e65a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('host', sa.Column('vis_name', sa.String(length=64), nullable=True))
    op.drop_column('visitor', 'username')
    op.drop_column('visitor', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visitor', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.add_column('visitor', sa.Column('username', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('host', 'vis_name')
    # ### end Alembic commands ###
