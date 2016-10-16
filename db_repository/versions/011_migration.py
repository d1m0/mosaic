from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
submission = Table('submission', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('time', DATETIME),
    Column('lastChildVisit', DATETIME),
    Column('childVisitFrequency', INTEGER),
    Column('numChildren', INTEGER),
    Column('submission_type', VARCHAR(length=8)),
    Column('url', VARCHAR(length=1024)),
    Column('author_id', INTEGER),
    Column('homeCountry', VARCHAR(length=120)),
    Column('homeCity', VARCHAR(length=120)),
    Column('courtCountry', VARCHAR(length=120)),
    Column('courtCity', VARCHAR(length=120)),
    Column('courtCosts', INTEGER),
    Column('relation', VARCHAR(length=20)),
    Column('ip', VARCHAR(length=128)),
    Column('tags', VARCHAR(length=1024)),
    Column('other', VARCHAR(length=1000)),
    Column('milestone', VARCHAR(length=1024)),
    Column('related', VARCHAR(length=512)),
)

submission = Table('submission', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('time', DateTime),
    Column('lastChildVisit', DateTime),
    Column('childVisitFrequency', Integer),
    Column('numChildren', Integer),
    Column('submission_type', Enum('local', 'external')),
    Column('url', String(length=1024)),
    Column('author_id', Integer),
    Column('homeCountry', String(length=120)),
    Column('homeCity', String(length=120)),
    Column('courtCountry', String(length=120)),
    Column('courtCity', String(length=120)),
    Column('courtCosts', Integer),
    Column('relation', Enum('erased_mom', 'erased_dad', 'erased_sister', 'erased_brother', 'erased_grandparent', 'erased_aunt_or_uncle', 'erased_cousin', 'erased_other_family', 'erased_step_family', 'erased_friend')),
    Column('ip', String(length=128)),
    Column('tags', String(length=1024)),
    Column('milestone', String(length=1024)),
    Column('related_submission', String(length=512)),
    Column('other', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['submission'].columns['related'].drop()
    post_meta.tables['submission'].columns['related_submission'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['submission'].columns['related'].create()
    post_meta.tables['submission'].columns['related_submission'].drop()
