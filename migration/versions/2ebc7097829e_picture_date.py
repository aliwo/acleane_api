"""picture date

Revision ID: 2ebc7097829e
Revises: 514dbe7a8d7d
Create Date: 2021-05-03 23:48:35.381581

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import AcleaneTypes


# revision identifiers, used by Alembic.
revision = '2ebc7097829e'
down_revision = '514dbe7a8d7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pictures', sa.Column('date', sa.DATE(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pictures', 'date')
    # ### end Alembic commands ###