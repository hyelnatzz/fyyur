"""Adjusted types in the artist  model to .string

Revision ID: 841dfc626e2d
Revises: ac05044cd0c3
Create Date: 2022-06-02 14:21:41.236933

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '841dfc626e2d'
down_revision = 'ac05044cd0c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.TEXT()),
               type_=sa.ARRAY(sa.String()),
               existing_nullable=False)
    op.alter_column('venues', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               type_=sa.ARRAY(sa.Text()),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'genres',
               existing_type=sa.ARRAY(sa.Text()),
               type_=postgresql.ARRAY(sa.VARCHAR()),
               existing_nullable=True)
    op.alter_column('artists', 'genres',
               existing_type=sa.ARRAY(sa.String()),
               type_=postgresql.ARRAY(sa.TEXT()),
               existing_nullable=False)
    # ### end Alembic commands ###
