"""modified requirements class

Revision ID: 087b42d54bd5
Revises: 615ba1b91a2f
Create Date: 2023-12-01 19:35:48.506323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '087b42d54bd5'
down_revision: Union[str, None] = '615ba1b91a2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funding_requirements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_funding_requirements_data'), 'funding_requirements', ['data'], unique=False)
    op.create_index(op.f('ix_funding_requirements_id'), 'funding_requirements', ['id'], unique=False)
    op.create_index(op.f('ix_funding_requirements_title'), 'funding_requirements', ['title'], unique=False)
    op.create_table('funding_opp_requirements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fund_id', sa.Integer(), nullable=True),
    sa.Column('requirement_id', sa.Integer(), nullable=True),
    sa.Column('data', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['fund_id'], ['funding_opportunity.id'], ),
    sa.ForeignKeyConstraint(['requirement_id'], ['funding_requirements.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_funding_opp_requirements_data'), 'funding_opp_requirements', ['data'], unique=False)
    op.create_index(op.f('ix_funding_opp_requirements_id'), 'funding_opp_requirements', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_funding_opp_requirements_id'), table_name='funding_opp_requirements')
    op.drop_index(op.f('ix_funding_opp_requirements_data'), table_name='funding_opp_requirements')
    op.drop_table('funding_opp_requirements')
    op.drop_index(op.f('ix_funding_requirements_title'), table_name='funding_requirements')
    op.drop_index(op.f('ix_funding_requirements_id'), table_name='funding_requirements')
    op.drop_index(op.f('ix_funding_requirements_data'), table_name='funding_requirements')
    op.drop_table('funding_requirements')
    # ### end Alembic commands ###
