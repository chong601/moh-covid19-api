"""Update cases_malaysia, cases_state, deaths_malaysia, deaths_state, icu_by_state, vax_malaysia and vax_state schema

Revision ID: 7c85c1c7765b
Revises: 198ec092d8ca
Create Date: 2021-09-19 04:50:05.620497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c85c1c7765b'
down_revision = '198ec092d8ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cases_malaysia', sa.Column('cases_import', sa.Integer(), nullable=True, comment='New import cases'))
    op.add_column('cases_malaysia', sa.Column('cases_recovered', sa.Integer(), nullable=True, comment='Recovered cases'))
    op.alter_column('cases_malaysia', 'cases_new',
               existing_type=sa.INTEGER(),
               comment='New local cases',
               existing_comment='New cases',
               existing_nullable=True)
    op.add_column('cases_state', sa.Column('cases_import', sa.Integer(), nullable=True, comment='New import cases'))
    op.add_column('cases_state', sa.Column('cases_recovered', sa.Integer(), nullable=True, comment='Recovered cases'))
    op.alter_column('cases_state', 'cases_new',
               existing_type=sa.INTEGER(),
               comment='New local cases',
               existing_comment='New cases',
               existing_nullable=True)
    op.add_column('deaths_malaysia', sa.Column('deaths_bid', sa.Integer(), nullable=True, comment='New deaths for the reported date'))
    op.add_column('deaths_malaysia', sa.Column('deaths_new_dod', sa.Integer(), nullable=True, comment='New deaths for the reported date'))
    op.add_column('deaths_state', sa.Column('deaths_bid', sa.Integer(), nullable=True, comment='New deaths for the reported date'))
    op.add_column('deaths_state', sa.Column('deaths_new_dod', sa.Integer(), nullable=True, comment='New deaths for the reported date'))
    op.add_column('icu_by_state', sa.Column('vent_used', sa.Integer(), nullable=True, comment='Total ventilators in use'))
    op.add_column('icu_by_state', sa.Column('vent_port_used', sa.Integer(), nullable=True, comment='Total portable ventilator in use'))
    op.add_column('vax_malaysia', sa.Column('cansino', sa.Integer(), nullable=True, comment='Single-dose CanSino vaccine delivered between 0000 and 2359 on date'))
    op.add_column('vax_state', sa.Column('cansino', sa.Integer(), nullable=True, comment='Single-dose CanSino vaccine delivered between 0000 and 2359 on date'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vax_state', 'cansino')
    op.drop_column('vax_malaysia', 'cansino')
    op.drop_column('icu_by_state', 'vent_port_used')
    op.drop_column('icu_by_state', 'vent_used')
    op.drop_column('deaths_state', 'deaths_new_dod')
    op.drop_column('deaths_state', 'deaths_bid')
    op.drop_column('deaths_malaysia', 'deaths_new_dod')
    op.drop_column('deaths_malaysia', 'deaths_bid')
    op.alter_column('cases_state', 'cases_new',
               existing_type=sa.INTEGER(),
               comment='New cases',
               existing_comment='New local cases',
               existing_nullable=True)
    op.drop_column('cases_state', 'cases_recovered')
    op.drop_column('cases_state', 'cases_import')
    op.alter_column('cases_malaysia', 'cases_new',
               existing_type=sa.INTEGER(),
               comment='New cases',
               existing_comment='New local cases',
               existing_nullable=True)
    op.drop_column('cases_malaysia', 'cases_recovered')
    op.drop_column('cases_malaysia', 'cases_import')
    # ### end Alembic commands ###
