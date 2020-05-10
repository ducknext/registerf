


from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator
from peewee import SqliteDatabase, Model, CharField, DateField, fn
import json

import pandas

from question import (
    style,
    continue_confirm,
    general_question,
    get_query_type,
    get_tags,
    get_month,
    get_year,
)

from model import (
    db,
    Balance,
    query_tag,
    query_month_year,
    query_month_year_tag,
)



def print_table():
    print("{:<15} {:<8} {:<40} {:<}".format(i['tag'], i['amount'],i['comment'],str(i['date'])))

""" What do you want to do? """
general = general_question()

if (general == 'Query DB'):
    answer = get_query_type()

    if answer == 'tag':
        tags = get_tags()
        tag_sum = 0
        print("{:<15} {:<8} {:<40} {:<}".format('Tag', 'Amount', 'Comment', 'Date')) 
        for tag in tags:
            result = query_tag(tag)  
            for i in result:
                print_table()
            tsum = (Balance
                .select(fn.Sum(Balance.amount))
                .where(Balance.tag == tag)
                .scalar()
            )
            tag_sum = tag_sum + tsum
        print('Sum for choosen is {}'.format(tag_sum))

    elif answer == 'month-year':
        months = get_month()
        years = get_year()
        my_sum = 0
        print("{:<15} {:<8} {:<40} {:<}".format('Tag', 'Amount', 'Comment', 'Date')) 
        for year in years:
            for month in months:
                result = query_month_year(int(month), int(year))  
                for i in result:
                    print_table()
                mysum = (Balance
                    .select(fn.Sum(Balance.amount))
                    .where(Balance.date.month == int(month), 
                        Balance.date.year == int(year))
                    .scalar()
                )
                my_sum = my_sum + mysum
        print('Sum for choosen is {}'.format(my_sum))
    else:
        tags = get_tags()
        months = get_month()
        years = get_year()
        my_sum = 0
        for year in years:
            for month in months:
                for tag in tags:
                    result = query_month_year_tag(int(month), int(year), tag)  
                    for i in result:
                        print_table()
                    mysum = (Balance
                        .select(fn.Sum(Balance.amount))
                        .where(Balance.date.month == int(month), 
                            Balance.date.year == int(year), 
                            Balance.tag == tag)
                        .scalar()
                    )
                    my_sum = my_sum + mysum
        print('Sum for choosen is {}'.format(my_sum))


    