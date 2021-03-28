import pandas as pd
import numpy as np
from random import randrange
from datetime import timedelta
from datetime import datetime
import random
import string

TOTAL_TEST_COUNT = 100
POSITIVE_CASE_FREQ = 0.21
NUM_PATIENTS = 40

START_DATE = datetime.strptime('10/1/2020', '%m/%d/%Y')
END_DATE = datetime.strptime('4/21/2021', '%m/%d/%Y')


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    d = start + timedelta(seconds=random_second)
    return f"{d.month}/{d.day}/{d.year}"


d = random_date(START_DATE, END_DATE)

sample_results = random.choices(['positive', 'negative'],
                                weights=[POSITIVE_CASE_FREQ, 1 - POSITIVE_CASE_FREQ],
                                k=TOTAL_TEST_COUNT)

test_type = ['RT-PCR'] * TOTAL_TEST_COUNT
test_dates = [random_date(START_DATE, END_DATE) for _ in range(TOTAL_TEST_COUNT)]
collection_site = random.choices(['Kilachand', 'Health Annex', '808 Gallery', 'Agganis Arena Lobby',
                                  'BU Medical Campus'],
                                 k=TOTAL_TEST_COUNT)
users = [''.join(random.choices(string.digits, k=12)) for _ in range(NUM_PATIENTS)]

user_id_col = random.choices(users, k=100)

ct_values = []

df = pd.DataFrame([sample_results, test_type, test_dates, collection_site, user_id_col, ct_values]).T
df.columns = ['sample_result', 'test_type', 'test_date', 'collection_site', 'user_id', 'ct_values']
df.to_csv('example.csv')
