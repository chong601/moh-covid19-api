"""Fix missing column name

Revision ID: 4b8b75967bb4
Revises: 9fde3d4af686
Create Date: 2021-09-19 10:49:26.216517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b8b75967bb4'
down_revision = '9fde3d4af686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deaths_malaysia', sa.Column('deaths_bid_dod', sa.Integer(), nullable=True, comment='New deaths for the reported date'))
    op.add_column('deaths_state', sa.Column('deaths_bid_dod', sa.Integer(), nullable=True, comment='New deaths for the reported date'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('deaths_state', 'deaths_bid_dod')
    op.drop_column('deaths_malaysia', 'deaths_bid_dod')
    # ### end Alembic commands ###