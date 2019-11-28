"""empty message

Revision ID: 4e14dac2e9bb
Revises: f339e1a93df4
Create Date: 2019-11-27 14:50:13.585448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e14dac2e9bb'
down_revision = 'f339e1a93df4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('visitor', 'password_hash')
    op.drop_column('visitor', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visitor', sa.Column('username', sa.VARCHAR(length=64), nullable=True))
    op.add_column('visitor', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
