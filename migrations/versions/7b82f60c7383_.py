"""empty message

Revision ID: 7b82f60c7383
Revises: e883f0e68954
Create Date: 2022-07-22 11:28:00.879162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b82f60c7383'
down_revision = 'e883f0e68954'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('course_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'question', 'course', ['course_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'course_id')
    # ### end Alembic commands ###
