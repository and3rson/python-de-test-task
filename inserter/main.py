#!/usr/bin/env python3
import os
import sys
import uuid
import time
import random

from essential_generators import DocumentGenerator
import psycopg2


def main():
    gen = DocumentGenerator()
    conn = None
    while conn is None:
        try:
            conn = psycopg2.connect(
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST')
            )
        except Exception as e:
            print(f'PostgreSQL does not seem to be ready yet: {e}')
            time.sleep(1)
    print('Connected to PostgreSQL')
    while True:
        time.sleep(random.random() / 5)
        key = gen.slug()
        value = gen.sentence()
        pk = uuid.uuid1()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO events(id, name, info) VALUES(%s, %s, %s)',
            (
                str(pk),
                key,
                value
            )
        )
        conn.commit()
        print('New event:')
        print('  pk:', pk)
        print('  key:', key)
        print('  value:', value)

    return 0


if __name__ == '__main__':
    sys.exit(main())
