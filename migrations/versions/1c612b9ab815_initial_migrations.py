"""initial migrations

Revision ID: 1c612b9ab815
Revises: a4368d618283
Create Date: 2022-09-25 17:29:51.102575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c612b9ab815'
down_revision = 'a4368d618283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('register', schema=None) as batch_op:
        batch_op.drop_column('f_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('register', schema=None) as batch_op:
        batch_op.add_column(sa.Column('f_name', sa.VARCHAR(length=50), nullable=True))

    # ### end Alembic commands ###
