"""Update hospital and icu schema

Revision ID: 21432605da1f
Revises: 94b2acb22e6b
Create Date: 2021-08-16 21:34:31.893205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21432605da1f'
down_revision = '94b2acb22e6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hospital_by_state', sa.Column('beds_covid', sa.Integer(), nullable=True, comment='Total available hospital beds dedicated for COVID-19'))
    op.add_column('icu_by_state', sa.Column('beds_icu', sa.Integer(), nullable=True, comment='Gazetted ICU beds'))
    op.add_column('icu_by_state', sa.Column('beds_icu_rep', sa.Integer(), nullable=True, comment='Total ICU beds for Anaesthesiology & Critical Care departments'))
    op.add_column('icu_by_state', sa.Column('beds_icu_total', sa.Integer(), nullable=True, comment='Total ICU beds'))
    op.add_column('icu_by_state', sa.Column('beds_icu_covid', sa.Integer(), nullable=True, comment='Total ICU beds dedicated for COVID-19'))
    op.drop_column('icu_by_state', 'bed_icu_covid')
    op.drop_column('icu_by_state', 'bed_icu')
    op.drop_column('icu_by_state', 'bed_icu_total')
    op.drop_column('icu_by_state', 'bed_icu_rep')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('icu_by_state', sa.Column('bed_icu_rep', sa.INTEGER(), autoincrement=False, nullable=True, comment='Total ICU beds for Anaesthesiology & Critical Care departments'))
    op.add_column('icu_by_state', sa.Column('bed_icu_total', sa.INTEGER(), autoincrement=False, nullable=True, comment='Total ICU beds'))
    op.add_column('icu_by_state', sa.Column('bed_icu', sa.INTEGER(), autoincrement=False, nullable=True, comment='Gazetted ICU beds'))
    op.add_column('icu_by_state', sa.Column('bed_icu_covid', sa.INTEGER(), autoincrement=False, nullable=True, comment='Total ICU beds dedicated for COVID-19'))
    op.drop_column('icu_by_state', 'beds_icu_covid')
    op.drop_column('icu_by_state', 'beds_icu_total')
    op.drop_column('icu_by_state', 'beds_icu_rep')
    op.drop_column('icu_by_state', 'beds_icu')
    op.drop_column('hospital_by_state', 'beds_covid')
    # ### end Alembic commands ###
