from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
submission = Table('submission', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('time', DATETIME),
    Column('submission_type', ENUM(u'local', u'external', collation=u'utf8_bin')),
    Column('url', VARCHAR(collation=u'utf8_bin', length=1024)),
    Column('author_id', INTEGER(display_width=11)),
    Column('country', VARCHAR(collation=u'utf8_bin', length=120)),
    Column('city', VARCHAR(collation=u'utf8_bin', length=120)),
    Column('relation', ENUM(u'erased_mom', u'erased_dad', u'erased_sister', u'erased_brother', u'erased_grandparent', u'erased_aunt_or_uncle', u'erased_cousin', u'erased_other_family', u'erased_step_family', u'erased_friend', collation=u'utf8_bin')),
    Column('ip', VARCHAR(collation=u'utf8_bin', length=128)),
    Column('tags', VARCHAR(collation=u'utf8_bin', length=1024)),
    Column('other', VARCHAR(collation=u'utf8_bin', length=1000)),
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
    Column('other', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['submission'].columns['city'].drop()
    pre_meta.tables['submission'].columns['country'].drop()
    post_meta.tables['submission'].columns['childVisitFrequency'].create()
    post_meta.tables['submission'].columns['courtCity'].create()
    post_meta.tables['submission'].columns['courtCosts'].create()
    post_meta.tables['submission'].columns['courtCountry'].create()
    post_meta.tables['submission'].columns['homeCity'].create()
    post_meta.tables['submission'].columns['homeCountry'].create()
    post_meta.tables['submission'].columns['lastChildVisit'].create()
    post_meta.tables['submission'].columns['numChildren'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['submission'].columns['city'].create()
    pre_meta.tables['submission'].columns['country'].create()
    post_meta.tables['submission'].columns['childVisitFrequency'].drop()
    post_meta.tables['submission'].columns['courtCity'].drop()
    post_meta.tables['submission'].columns['courtCosts'].drop()
    post_meta.tables['submission'].columns['courtCountry'].drop()
    post_meta.tables['submission'].columns['homeCity'].drop()
    post_meta.tables['submission'].columns['homeCountry'].drop()
    post_meta.tables['submission'].columns['lastChildVisit'].drop()
    post_meta.tables['submission'].columns['numChildren'].drop()
