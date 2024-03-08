import streamlit as st

import pandas as pd
from io import StringIO


'''
# S.U.R.G.E - Sustainable Usage Research for Green Energy
A project by Ankit Jha

'''
with st.sidebar:
        

    option = st.selectbox(
    'Select the country for Analysis',
    ('Afghanistan', 'Africa', 'Africa (EI)', 'Africa (Ember)',
       'Africa (Shift)', 'Albania', 'Algeria', 'American Samoa', 'Angola',
       'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia',
       'Aruba', 'Asia', 'Asia & Oceania (EIA)', 'Asia (Ember)',
       'Asia Pacific (EI)', 'Asia and Oceania (Shift)', 'Australia',
       'Australia and New Zealand (EIA)', 'Austria', 'Azerbaijan',
       'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
       'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
       'Bosnia and Herzegovina', 'Botswana', 'Brazil',
       'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso',
       'Burundi', 'CIS (EI)', 'Cambodia', 'Cameroon', 'Canada',
       'Cape Verde', 'Cayman Islands', 'Central & South America (EIA)',
       'Central African Republic', 'Central America (EI)',
       'Central and South America (Shift)', 'Chad', 'Chile', 'China',
       'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica',
       "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia',
       'Czechoslovakia', 'Democratic Republic of Congo', 'Denmark',
       'Djibouti', 'Dominica', 'Dominican Republic', 'EU28 (Shift)',
       'East Germany (EIA)', 'East Timor', 'Eastern Africa (EI)',
       'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
       'Estonia', 'Eswatini', 'Ethiopia', 'Eurasia (EIA)',
       'Eurasia (Shift)', 'Europe', 'Europe (EI)', 'Europe (Ember)',
       'Europe (Shift)', 'European Union (27)', 'European Union (EIA)',
       'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France',
       'French Guiana', 'French Polynesia', 'G20 (Ember)', 'G7 (Ember)',
       'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar',
       'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
       'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
       'Hawaiian Trade Zone (EIA)', 'High-income countries', 'Honduras',
       'Hong Kong', 'Hungary', 'IEO - Africa (EIA)',
       'IEO - Middle East (EIA)', 'IEO OECD - Europe (EIA)', 'Iceland',
       'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
       'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
       'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos',
       'Latin America and Caribbean (Ember)', 'Latvia', 'Lebanon',
       'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Low-income countries',
       'Lower-middle-income countries', 'Luxembourg', 'Macao',
       'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Martinique', 'Mauritania', 'Mauritius', 'Mexico',
       'Mexico, Chile, and other OECD Americas (EIA)',
       'Micronesia (country)', 'Middle Africa (EI)', 'Middle East (EI)',
       'Middle East (EIA)', 'Middle East (Ember)', 'Middle East (Shift)',
       'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco',
       'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
       'Netherlands', 'Netherlands Antilles', 'New Caledonia',
       'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue',
       'Non-OECD (EI)', 'Non-OECD (EIA)', 'Non-OPEC (EI)',
       'Non-OPEC (EIA)', 'North America', 'North America (EI)',
       'North America (Ember)', 'North America (Shift)', 'North Korea',
       'North Macedonia', 'Northern Mariana Islands', 'Norway',
       'OECD (EI)', 'OECD (EIA)', 'OECD (Ember)', 'OECD (Shift)',
       'OECD - Asia And Oceania (EIA)', 'OECD - Europe (EIA)',
       'OECD - North America (EIA)', 'OPEC (EI)', 'OPEC (EIA)',
       'OPEC (Shift)', 'OPEC - Africa (EIA)',
       'OPEC - South America (EIA)', 'Oceania', 'Oceania (Ember)', 'Oman',
       'Other Non-OECD - America (EIA)', 'Other Non-OECD - Asia (EIA)',
       'Other Non-OECD - Europe and Eurasia (EIA)', 'Pakistan',
       'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay',
       'Persian Gulf (EIA)', 'Persian Gulf (Shift)', 'Peru',
       'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
       'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines',
       'Samoa', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
       'Serbia', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone',
       'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
       'South Africa', 'South America', 'South Korea',
       'South Korea and other OECD Asia (EIA)', 'South Sudan',
       'South and Central America (EI)', 'Spain', 'Sri Lanka', 'Sudan',
       'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
       'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
       'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
       'Turks and Caicos Islands', 'Tuvalu', 'U.S. Pacific Islands (EIA)',
       'U.S. Territories (EIA)', 'USSR', 'Uganda', 'Ukraine',
       'United Arab Emirates', 'United Kingdom', 'United States',
       'United States Pacific Islands (Shift)',
       'United States Territories (Shift)',
       'United States Virgin Islands', 'Upper-middle-income countries',
       'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam',
       'Wake Island (EIA)', 'Wake Island (Shift)', 'West Germany (EIA)',
       'Western Africa (EI)', 'Western Sahara', 'World', 'Yemen',
       'Yugoslavia', 'Zambia', 'Zimbabwe'))

    st.write('You selected:', option)

st.write(option, "Energy Analysis till 2022")