"""host table

Revision ID: 4c704b545cc5
Revises: 5071b3d32b1e
Create Date: 2019-11-26 23:09:43.564256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c704b545cc5'
down_revision = '5071b3d32b1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('host',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_host_email'), 'host', ['email'], unique=True)
    op.create_index(op.f('ix_host_username'), 'host', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_host_username'), table_name='host')
    op.drop_index(op.f('ix_host_email'), table_name='host')
    op.drop_table('host')
    # ### end Alembic commands ###