"""empty message

<<<<<<<< HEAD:app/migrations/versions/3cc4908510de_.py
Revision ID: 3cc4908510de
Revises: 
Create Date: 2024-03-05 11:46:06.384914
========
Revision ID: f5bbe8256281
Revises: 
Create Date: 2024-05-10 01:52:10.559405
>>>>>>>> bb8bfb8 (issue: checking bad request):app/migrations/versions/f5bbe8256281_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:app/migrations/versions/3cc4908510de_.py
revision = '3cc4908510de'
========
revision = 'f5bbe8256281'
>>>>>>>> bb8bfb8 (issue: checking bad request):app/migrations/versions/f5bbe8256281_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('login', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('avatar', sa.String(length=256), nullable=True),
<<<<<<<< HEAD:app/migrations/versions/3cc4908510de_.py
    sa.Column('google_id', sa.String(), nullable=False),
========
    sa.Column('google_id', sa.String(), nullable=True),
>>>>>>>> bb8bfb8 (issue: checking bad request):app/migrations/versions/f5bbe8256281_.py
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('google_id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
