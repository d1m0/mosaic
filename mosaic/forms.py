from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Length, regexp, URL, Email
from .validators import YoutubeURL

countries = [
    ('US',  'United States'),
    ('AD',  'Andorra'),
    ('AE',  'United Arab Emirates'),
    ('AF',  'Afghanistan'),
    ('AG',  'Antigua and Barbuda'),
    ('AI',  'Anguilla'),
    ('AL',  'Albania'),
    ('AM',  'Armenia'),
    ('AO',  'Angola'),
    ('AQ',  'Antarctica'),
    ('AR',  'Argentina'),
    ('AS',  'American Samoa'),
    ('AT',  'Austria'),
    ('AU',  'Australia'),
    ('AW',  'Aruba'),
    ('AZ',  'Azerbaijan'),
    ('BA',  'Bosnia and Herzegovina'),
    ('BB',  'Barbados'),
    ('BD',  'Bangladesh'),
    ('BE',  'Belgium'),
    ('BF',  'Burkina Faso'),
    ('BG',  'Bulgaria'),
    ('BH',  'Bahrain'),
    ('BI',  'Burundi'),
    ('BJ',  'Benin'),
    ('BL',  'Saint Barthelemy'),
    ('BM',  'Bermuda'),
    ('BN',  'Brunei'),
    ('BO',  'Bolivia'),
    ('BR',  'Brazil'),
    ('BS',  'Bahamas, The'),
    ('BT',  'Bhutan'),
    ('BV',  'Bouvet Island'),
    ('BW',  'Botswana'),
    ('BY',  'Belarus'),
    ('BZ',  'Belize'),
    ('CA',  'Canada'),
    ('CC',  'Cocos (Keeling) Islands'),
    ('CD',  'Congo, Democratic Republic of the'),
    ('CF',  'Central African Republic'),
    ('CG',  'Congo, Republic of the'),
    ('CH',  'Switzerland'),
    ('CI',  'Cote d\'Ivoire'),
    ('CK',  'Cook Islands'),
    ('CL',  'Chile'),
    ('CM',  'Cameroon'),
    ('CN',  'China'),
    ('CO',  'Colombia'),
    ('CR',  'Costa Rica'),
    ('CU',  'Cuba'),
    ('CV',  'Cape Verde'),
    ('CW',  'Curacao'),
    ('CX',  'Christmas Island'),
    ('CY',  'Cyprus'),
    ('CZ',  'Czech Republic'),
    ('DE',  'Germany'),
    ('DJ',  'Djibouti'),
    ('DK',  'Denmark'),
    ('DM',  'Dominica'),
    ('DO',  'Dominican Republic'),
    ('DZ',  'Algeria'),
    ('EC',  'Ecuador'),
    ('EE',  'Estonia'),
    ('EG',  'Egypt'),
    ('EH',  'Western Sahara'),
    ('ER',  'Eritrea'),
    ('ES',  'Spain'),
    ('ET',  'Ethiopia'),
    ('FI',  'Finland'),
    ('FJ',  'Fiji'),
    ('FM',  'Micronesia, Federated States of'),
    ('FO',  'Faroe Islands'),
    ('FR',  'France'),
    ('FX',  'France, Metropolitan'),
    ('GA',  'Gabon'),
    ('GB',  'United Kingdom'),
    ('GD',  'Grenada'),
    ('GE',  'Georgia'),
    ('GF',  'French Guiana'),
    ('GG',  'Guernsey'),
    ('GH',  'Ghana'),
    ('GI',  'Gibraltar'),
    ('GL',  'Greenland'),
    ('GM',  'Gambia, The'),
    ('GN',  'Guinea'),
    ('GP',  'Guadeloupe'),
    ('GQ',  'Equatorial Guinea'),
    ('GR',  'Greece'),
    ('GT',  'Guatemala'),
    ('GU',  'Guam'),
    ('GW',  'Guinea-Bissau'),
    ('GY',  'Guyana'),
    ('HK',  'Hong Kong'),
    ('HN',  'Honduras'),
    ('HR',  'Croatia'),
    ('HT',  'Haiti'),
    ('HU',  'Hungary'),
    ('ID',  'Indonesia'),
    ('IE',  'Ireland'),
    ('IL',  'Israel'),
    ('IM',  'Isle of Man'),
    ('IN',  'India'),
    ('IQ',  'Iraq'),
    ('IR',  'Iran'),
    ('IS',  'Iceland'),
    ('IT',  'Italy'),
    ('JE',  'Jersey'),
    ('JM',  'Jamaica'),
    ('JO',  'Jordan'),
    ('JP',  'Japan'),
    ('KE',  'Kenya'),
    ('KG',  'Kyrgyzstan'),
    ('KH',  'Cambodia'),
    ('KI',  'Kiribati'),
    ('KM',  'Comoros'),
    ('KP',  'Korea, North'),
    ('KR',  'Korea, South'),
    ('KW',  'Kuwait'),
    ('KY',  'Cayman Islands'),
    ('KZ',  'Kazakhstan'),
    ('LA',  'Laos'),
    ('LB',  'Lebanon'),
    ('LC',  'Saint Lucia'),
    ('LI',  'Liechtenstein'),
    ('LK',  'Sri Lanka'),
    ('LR',  'Liberia'),
    ('LS',  'Lesotho'),
    ('LT',  'Lithuania'),
    ('LU',  'Luxembourg'),
    ('LV',  'Latvia'),
    ('LY',  'Libya'),
    ('MA',  'Morocco'),
    ('MC',  'Monaco'),
    ('MD',  'Moldova'),
    ('ME',  'Montenegro'),
    ('MF',  'Saint Martin'),
    ('MG',  'Madagascar'),
    ('MH',  'Marshall Islands'),
    ('MK',  'Macedonia'),
    ('ML',  'Mali'),
    ('MM',  'Burma'),
    ('MN',  'Mongolia'),
    ('MO',  'Macau'),
    ('MP',  'Northern Mariana Islands'),
    ('MQ',  'Martinique'),
    ('MR',  'Mauritania'),
    ('MS',  'Montserrat'),
    ('MT',  'Malta'),
    ('MU',  'Mauritius'),
    ('MV',  'Maldives'),
    ('MW',  'Malawi'),
    ('MX',  'Mexico'),
    ('MY',  'Malaysia'),
    ('MZ',  'Mozambique'),
    ('NA',  'Namibia'),
    ('NC',  'New Caledonia'),
    ('NE',  'Niger'),
    ('NF',  'Norfolk Island'),
    ('NG',  'Nigeria'),
    ('NI',  'Nicaragua'),
    ('NL',  'Netherlands'),
    ('NO',  'Norway'),
    ('NP',  'Nepal'),
    ('NR',  'Nauru'),
    ('NU',  'Niue'),
    ('NZ',  'New Zealand'),
    ('OM',  'Oman'),
    ('PA',  'Panama'),
    ('PE',  'Peru'),
    ('PF',  'French Polynesia'),
    ('PG',  'Papua New Guinea'),
    ('PH',  'Philippines'),
    ('PK',  'Pakistan'),
    ('PL',  'Poland'),
    ('PM',  'Saint Pierre and Miquelon'),
    ('PN',  'Pitcairn Islands'),
    ('PR',  'Puerto Rico'),
    ('PS',  'Gaza Strip'),
    ('PS',  'West Bank'),
    ('PT',  'Portugal'),
    ('PW',  'Palau'),
    ('PY',  'Paraguay'),
    ('QA',  'Qatar'),
    ('RE',  'Reunion'),
    ('RO',  'Romania'),
    ('RS',  'Serbia'),
    ('RU',  'Russia'),
    ('RW',  'Rwanda'),
    ('SA',  'Saudi Arabia'),
    ('SB',  'Solomon Islands'),
    ('SC',  'Seychelles'),
    ('SD',  'Sudan'),
    ('SE',  'Sweden'),
    ('SG',  'Singapore'),
    ('SI',  'Slovenia'),
    ('SJ',  'Svalbard'),
    ('SK',  'Slovakia'),
    ('SL',  'Sierra Leone'),
    ('SM',  'San Marino'),
    ('SN',  'Senegal'),
    ('SO',  'Somalia'),
    ('SR',  'Suriname'),
    ('SS',  'South Sudan'),
    ('ST',  'Sao Tome and Principe'),
    ('SV',  'El Salvador'),
    ('SX',  'Sint Maarten'),
    ('SY',  'Syria'),
    ('SZ',  'Swaziland'),
    ('TC',  'Turks and Caicos Islands'),
    ('TD',  'Chad'),
    ('TG',  'Togo'),
    ('TH',  'Thailand'),
    ('TJ',  'Tajikistan'),
    ('TK',  'Tokelau'),
    ('TL',  'Timor-Leste'),
    ('TM',  'Turkmenistan'),
    ('TN',  'Tunisia'),
    ('TO',  'Tonga'),
    ('TR',  'Turkey'),
    ('TT',  'Trinidad and Tobago'),
    ('TV',  'Tuvalu'),
    ('TW',  'Taiwan'),
    ('TZ',  'Tanzania'),
    ('UA',  'Ukraine'),
    ('UG',  'Uganda'),
    ('US',  'United States'),
    ('UY',  'Uruguay'),
    ('UZ',  'Uzbekistan'),
    ('VE',  'Venezuela'),
    ('VG',  'British Virgin Islands'),
    ('VI',  'Virgin Islands'),
    ('VN',  'Vietnam'),
    ('VU',  'Vanuatu'),
    ('WF',  'Wallis and Futuna'),
    ('WS',  'Samoa'),
    ('XK',  'Kosovo'),
    ('YE',  'Yemen'),
    ('YT',  'Mayotte'),
    ('ZA',  'South Africa'),
    ('ZM',  'Zambia'),
    ('ZW',  'Zimbabwe'),
    ('ZZ',  'Other')
]

class UploadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    country = SelectField('Country', choices=countries, validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    video_url = StringField('Video File Link', validators=[DataRequired(), URL(), YoutubeURL()])
    tags = StringField('Tags', default="")
    relationship = SelectField('Relationship', choices=[('erased_mom', 'erased mom')])
    release = BooleanField('Release', default=False, validators=[DataRequired()])
