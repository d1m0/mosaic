from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('name', VARCHAR(collation=u'utf8_bin', length=120)),
    Column('email', VARCHAR(collation=u'utf8_bin', length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=120)),
    Column('last_name', String(length=120)),
    Column('email', String(length=120)),
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
    Column('milestones', String(length=1024)),
    Column('related_submission', String(length=512)),
    Column('other', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['name'].drop()
    post_meta.tables['user'].columns['first_name'].create()
    post_meta.tables['user'].columns['last_name'].create()
    post_meta.tables['submission'].columns['milestones'].create()
    post_meta.tables['submission'].columns['related_submission'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['name'].create()
    post_meta.tables['user'].columns['first_name'].drop()
    post_meta.tables['user'].columns['last_name'].drop()
    post_meta.tables['submission'].columns['milestones'].drop()
    post_meta.tables['submission'].columns['related_submission'].drop()
