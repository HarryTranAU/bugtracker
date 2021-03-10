"""added user.tickets

Revision ID: 95ec3157304a
Revises: 3d0b8bea1604
Create Date: 2021-03-10 15:28:42.691255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95ec3157304a'
down_revision = '3d0b8bea1604'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickets', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tickets', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tickets', type_='foreignkey')
    op.drop_column('tickets', 'user_id')
    # ### end Alembic commands ###