"""Update deaths_malaysia, deaths_state, vax_malaysia and vax_state

Revision ID: a5ef24527ae3
Revises: 4b8b75967bb4
Create Date: 2021-09-26 07:52:42.438826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5ef24527ae3'
down_revision = '4b8b75967bb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('deaths_malaysia', sa.Column('deaths_pvax', sa.Integer(), nullable=True, comment='Number of deaths with partial vaccination'))
    op.add_column('deaths_malaysia', sa.Column('deaths_fvax', sa.Integer(), nullable=True, comment='Number of deaths with full vaccination'))
    op.add_column('deaths_state', sa.Column('deaths_pvax', sa.Integer(), nullable=True, comment='Number of deaths with partial vaccination'))
    op.add_column('deaths_state', sa.Column('deaths_fvax', sa.Integer(), nullable=True, comment='Number of deaths with full vaccination'))
    op.add_column('vax_malaysia', sa.Column('daily_partial_child', sa.Integer(), nullable=True, comment='1st doses (for double-dose vaccines) delivered for children between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('daily_full_child', sa.Integer(), nullable=True, comment='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered for children between 0000 and 2359 on date.'))
    op.add_column('vax_state', sa.Column('daily_partial_child', sa.Integer(), nullable=True, comment='1st doses (for double-dose vaccines) delivered for children between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('daily_full_child', sa.Integer(), nullable=True, comment='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered for children between 0000 and 2359 on date'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vax_state', 'daily_full_child')
    op.drop_column('vax_state', 'daily_partial_child')
    op.drop_column('vax_malaysia', 'daily_full_child')
    op.drop_column('vax_malaysia', 'daily_partial_child')
    op.drop_column('deaths_state', 'deaths_fvax')
    op.drop_column('deaths_state', 'deaths_pvax')
    op.drop_column('deaths_malaysia', 'deaths_fvax')
    op.drop_column('deaths_malaysia', 'deaths_pvax')
    # ### end Alembic commands ###