"""Update vax_malaysia and vax_state schema

Revision ID: 198ec092d8ca
Revises: 21432605da1f
Create Date: 2021-08-18 06:36:03.249261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '198ec092d8ca'
down_revision = '21432605da1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vax_malaysia', sa.Column('daily_partial', sa.Integer(), nullable=True, comment='1st doses (for double-dose vaccines) delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('daily_full', sa.Integer(), nullable=True, comment='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered between 0000 and 2359 on date.'))
    op.add_column('vax_malaysia', sa.Column('daily', sa.Integer(), nullable=True, comment='Total daily delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('cumul_partial', sa.Integer(), nullable=True, comment='Sum of cumulative partial doses delivered until row date'))
    op.add_column('vax_malaysia', sa.Column('cumul_full', sa.Integer(), nullable=True, comment='Sum of cumulative full doses delivered until row date'))
    op.add_column('vax_malaysia', sa.Column('cumul', sa.Integer(), nullable=True, comment='Total cumulative doses delivered until row date'))
    op.add_column('vax_malaysia', sa.Column('pfizer1', sa.Integer(), nullable=True, comment='1st dose of PFizer vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('pfizer2', sa.Integer(), nullable=True, comment='2nd dose of PFizer vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('sinovac1', sa.Integer(), nullable=True, comment='1st dose of SinoVac vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('sinovac2', sa.Integer(), nullable=True, comment='2nd dose of SinoVac vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('astra1', sa.Integer(), nullable=True, comment='1st dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('astra2', sa.Integer(), nullable=True, comment='2nd dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('pending', sa.Integer(), nullable=True, comment='Doses delivered that are quarantined in VMS (Vaccine Management System)'))
    op.drop_column('vax_malaysia', 'dose1_daily')
    op.drop_column('vax_malaysia', 'total_daily')
    op.drop_column('vax_malaysia', 'dose2_cumul')
    op.drop_column('vax_malaysia', 'dose1_cumul')
    op.drop_column('vax_malaysia', 'dose2_daily')
    op.drop_column('vax_malaysia', 'total_cumul')
    op.add_column('vax_state', sa.Column('daily_partial', sa.Integer(), nullable=True, comment='1st doses (for double-dose vaccines) delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('daily_full', sa.Integer(), nullable=True, comment='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered between 0000 and 2359 on date.'))
    op.add_column('vax_state', sa.Column('daily', sa.Integer(), nullable=True, comment='Total daily delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('cumul_partial', sa.Integer(), nullable=True, comment='Sum of cumulative partial doses delivered until row date'))
    op.add_column('vax_state', sa.Column('cumul_full', sa.Integer(), nullable=True, comment='Sum of cumulative full doses delivered until row date'))
    op.add_column('vax_state', sa.Column('cumul', sa.Integer(), nullable=True, comment='Total cumulative doses delivered until row date'))
    op.add_column('vax_state', sa.Column('pfizer1', sa.Integer(), nullable=True, comment='1st dose of PFizer vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('pfizer2', sa.Integer(), nullable=True, comment='2nd dose of PFizer vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('sinovac1', sa.Integer(), nullable=True, comment='1st dose of SinoVac vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('sinovac2', sa.Integer(), nullable=True, comment='2nd dose of SinoVac vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('astra1', sa.Integer(), nullable=True, comment='1st dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('astra2', sa.Integer(), nullable=True, comment='2nd dose of AstraZeneca vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('pending', sa.Integer(), nullable=True, comment='Doses delivered that are quarantined in VMS (Vaccine Management System)'))
    op.drop_column('vax_state', 'dose1_daily')
    op.drop_column('vax_state', 'total_daily')
    op.drop_column('vax_state', 'dose2_cumul')
    op.drop_column('vax_state', 'dose1_cumul')
    op.drop_column('vax_state', 'dose2_daily')
    op.drop_column('vax_state', 'total_cumul')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vax_state', sa.Column('total_cumul', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of dose1_daily and dose2_daily until row date'))
    op.add_column('vax_state', sa.Column('dose2_daily', sa.INTEGER(), autoincrement=False, nullable=True, comment='2nd doses delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('dose1_cumul', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of dose1_daily from first day of programme until row date'))
    op.add_column('vax_state', sa.Column('dose2_cumul', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of dose2_daily from first day of programme until row date'))
    op.add_column('vax_state', sa.Column('total_daily', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of 1st and 2nd dose delivered between 00000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('dose1_daily', sa.INTEGER(), autoincrement=False, nullable=True, comment='1st doses delivered between 0000 and 2359 on date'))
    op.drop_column('vax_state', 'pending')
    op.drop_column('vax_state', 'astra2')
    op.drop_column('vax_state', 'astra1')
    op.drop_column('vax_state', 'sinovac2')
    op.drop_column('vax_state', 'sinovac1')
    op.drop_column('vax_state', 'pfizer2')
    op.drop_column('vax_state', 'pfizer1')
    op.drop_column('vax_state', 'cumul')
    op.drop_column('vax_state', 'cumul_full')
    op.drop_column('vax_state', 'cumul_partial')
    op.drop_column('vax_state', 'daily')
    op.drop_column('vax_state', 'daily_full')
    op.drop_column('vax_state', 'daily_partial')
    op.add_column('vax_malaysia', sa.Column('total_cumul', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of dose1_daily and dose2_daily until row date'))
    op.add_column('vax_malaysia', sa.Column('dose2_daily', sa.INTEGER(), autoincrement=False, nullable=True, comment='2nd doses delivered between 0000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('dose1_cumul', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of dose1_daily from first day of programme until row date'))
    op.add_column('vax_malaysia', sa.Column('dose2_cumul', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of dose2_daily from first day of programme until row date'))
    op.add_column('vax_malaysia', sa.Column('total_daily', sa.INTEGER(), autoincrement=False, nullable=True, comment='Sum of 1st and 2nd dose delivered between 00000 and 2359 on date'))
    op.add_column('vax_malaysia', sa.Column('dose1_daily', sa.INTEGER(), autoincrement=False, nullable=True, comment='1st doses delivered between 0000 and 2359 on date'))
    op.drop_column('vax_malaysia', 'pending')
    op.drop_column('vax_malaysia', 'astra2')
    op.drop_column('vax_malaysia', 'astra1')
    op.drop_column('vax_malaysia', 'sinovac2')
    op.drop_column('vax_malaysia', 'sinovac1')
    op.drop_column('vax_malaysia', 'pfizer2')
    op.drop_column('vax_malaysia', 'pfizer1')
    op.drop_column('vax_malaysia', 'cumul')
    op.drop_column('vax_malaysia', 'cumul_full')
    op.drop_column('vax_malaysia', 'cumul_partial')
    op.drop_column('vax_malaysia', 'daily')
    op.drop_column('vax_malaysia', 'daily_full')
    op.drop_column('vax_malaysia', 'daily_partial')
    # ### end Alembic commands ###