"""remove picture date

Revision ID: 514dbe7a8d7d
Revises: 6b73a6101638
Create Date: 2021-05-01 22:28:38.879744

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import AcleaneTypes


# revision identifiers, used by Alembic.
revision = '514dbe7a8d7d'
down_revision = '6b73a6101638'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pictures', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pictures', sa.Column('date', sa.DATE(), nullable=True))
    # ### end Alembic commands ###
