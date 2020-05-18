


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
    # get_amount,
)

from model import (
    db,
    Balance,
    query_tag,
    query_month_year,
    query_month_year_tag,
)


def p_table():
        print("{:<15} {:<8} {:<40} {:<}".format(i['tag'], i['amount'],i['comment'],str(i['date'])))


def print_table(result):
    j = 0
    while j < len(result):
        for i in result[j]:
            print("{:<15} {:<8} {:<40} {:<}".format(i['tag'], i['amount'],i['comment'],str(i['date'])))
        j = j + 1


def get_month_year_query(years, months):
    result = []
    for year in years:
        for month in months:
            result.append(query_month_year(int(month), int(year)))
    return result 


def get_month_year_sum(years, months):
    my_sum = 0
    for year in years:
        for month in months:
            mysum = (Balance
                .select(fn.Sum(Balance.amount))
                .where(Balance.date.month == int(month), 
                    Balance.date.year == int(year))
                .scalar()
            )
            my_sum = my_sum + mysum
    return my_sum


def get_month_year_tag_query(years, months, tags):
    result = []
    for year in years:
        for month in months:
            for tag in tags:
                result.append(query_month_year_tag(int(month), int(year), tag))
    return result 

def get_month_year_tag_sum(years, months, tags):
    my_sum = 0
    for year in years:
        for month in months:
            for tag in tags:
                mysum = (Balance
                    .select(fn.Sum(Balance.amount))
                    .where(Balance.date.month == int(month), 
                        Balance.date.year == int(year),
                        Balance.tag == tag)
                    .scalar()
                )
                my_sum = my_sum + mysum
    return my_sum


""" What do you want to do? """
general = general_question()

if general != 'Query DB':
    exit(0)

answer = get_query_type()

if answer == 'tag':
    tags = get_tags()
    tag_sum = 0
    print("{:<15} {:<8} {:<40} {:<}".format('Tag', 'Amount', 'Comment', 'Date')) 
    for tag in tags:
        result = query_tag(tag)  
        for i in result:
            p_table()
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

    print("{:<15} {:<8} {:<40} {:<}".format('Tag', 'Amount', 'Comment', 'Date')) 

    result = get_month_year_query(years, months)
    print_table(result)

    print('Sum for choosen is {}'.format(get_month_year_sum(years, months)))

else:
    tags = get_tags()
    months = get_month()
    years = get_year()

    print("{:<15} {:<8} {:<40} {:<}".format('Tag', 'Amount', 'Comment', 'Date')) 

    result = get_month_year_tag_query(years, months, tags)
    print_table(result)

    print('Sum for choosen is {}'.format(get_month_year_tag_sum(years, months, tags)))


    

# if (general == 'Register income/expense'):
#     tag = get_tags()
#     amount = int(get_amount())

