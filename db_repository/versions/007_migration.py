from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
submission = Table('submission', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('time', DateTime),
    Column('submission_type', Enum('local', 'external')),
    Column('url', String(length=1024)),
    Column('author_id', Integer),
    Column('country', String(length=120)),
    Column('city', String(length=120)),
    Column('relation', Enum('erased_mom')),
    Column('ip', String(length=128)),
    Column('tags', String(length=1024)),
    Column('other', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['submission'].columns['tags'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['submission'].columns['tags'].drop()
