

from __future__ import print_function, unicode_literals

from peewee import fn

from datetime import date, timedelta

from question import (
    get_query_type,
    get_tags,
    get_tag_one,
    get_month,
    get_one_month,
    get_year,
    get_one_year,
    get_amount,
    get_month_save,
    get_comment,
    get_entry_id,
    confirm_entry,
    confirm_delete,
    get_phrase,
)

from model import (
    Balance,
    query_tag,
    query_month_year,
    query_month_year_tag,
    query_comments,
)


def print_table(result):
    print('length is =', len(result))
    j = 0
    while j < len(result):
        for i in result[j]:
            print("{:<15} {:<15} {:<8} {:<40} {:<}"
                  .format(i['id'], i['tag'], i['amount'], i['comment'], str(i['date'])))
        j = j + 1


def print_table_2(result):
    j = 0
    while j < len(result):
        print("{:<15} {:<15} {:<8} {:<40} {:<}"
              .format(result[j]['id'], result[j]['tag'], result[j]['amount'],
                      result[j]['comment'], str(result[j]['date'])))
        j = j + 1


def get_tag_query(tags):
    result = []
    for tag in tags:
        result.append(query_tag(tag))
    return result


def get_tag_sum(tags):
    tag_sum = 0
    for tag in tags:
        tsum = (Balance
                .select(fn.Sum(Balance.amount))
                .where(Balance.tag == tag)
                .scalar()
                )
        tag_sum = tag_sum + tsum
    return tag_sum


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
            if mysum is not None:
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
                if mysum is not None:
                    my_sum = my_sum + mysum
    return my_sum

# 4 branches of the general question


def month_overview():
    month = get_one_month()
    year = get_one_year()

    msum = (Balance
            .select(fn.Sum(Balance.amount))
            .where(Balance.date.month == int(month),
                   Balance.date.year == int(year))
            .scalar()
            )

    msum_in = (Balance
               .select(fn.Sum(Balance.amount))
               .where(Balance.date.month == int(month),
                      Balance.date.year == int(year),
                      Balance.tag == 'income')
               .scalar()
               )

    msum_out = msum_in - msum

    print('--- {}/{} ---'.format(month, year))
    print('Income   = {}'.format(msum_in))
    print('Expenses = {}'.format(msum_out))
    print('Left     = {}'.format(msum))


def year_overview():
    year = get_one_year()

    ysum = (Balance
            .select(fn.Sum(Balance.amount))
            .where(Balance.date.year == int(year))
            .scalar()
            )

    ysum_in = (Balance
               .select(fn.Sum(Balance.amount))
               .where(Balance.date.year == int(year), Balance.tag == 'income')
               .scalar()
               )

    ysum_out = ysum_in - ysum

    print('--- {} ---'.format(year))
    print('Income   = {}'.format(ysum_in))
    print('Expenses = {}'.format(ysum_out))
    print('Left     = {}'.format(ysum))


def query_db():
    answer = get_query_type()

    if answer == 'tag':
        tags = get_tags()

        print("{:<15} {:<15} {:<8} {:<40} {:<}"
              .format('ID', 'Tag', 'Amount', 'Comment', 'Date'))

        result = get_tag_query(tags)
        print_table(result)

        print('Sum for choosen is {}'.format(get_tag_sum(tags)))

    elif answer == 'month-year':
        months = get_month()
        years = get_year()

        print("{:<15} {:<15} {:<8} {:<40} {:<}"
              .format('ID', 'Tag', 'Amount', 'Comment', 'Date'))

        result = get_month_year_query(years, months)
        print_table(result)

        print('Sum for choosen is {}'
              .format(get_month_year_sum(years, months)))

    else:
        tags = get_tags()
        months = get_month()
        years = get_year()

        print("{:<15} {:<15} {:<8} {:<40} {:<}"
              .format('ID', 'Tag', 'Amount', 'Comment', 'Date'))

        result = get_month_year_tag_query(years, months, tags)
        print_table(result)

        print('Sum for choosen is {}'
              .format(get_month_year_tag_sum(years, months, tags)))


def register():
    tag = get_tag_one()
    amount = get_amount()
    comment = get_comment()
    month = get_month_save()

    input_date = date.today()
    if month == 'last month':
        input_date = date.today().replace(day=1) - timedelta(1)

    register = confirm_entry()

    if register is True:
        Balance(
            amount=amount,
            tag=tag,
            comment=comment,
            date=input_date
        ).save()


def search_comment():
    phrase = get_phrase()

    print("{:<15} {:<15} {:<8} {:<40} {:<}"
          .format('ID', 'Tag', 'Amount', 'Comment', 'Date'))

    result = query_comments(phrase)
    print_table_2(result)

    print('Sum for choosen is {}'
          .format(get_comment_sum(result)))


def get_comment_sum(result):
    comment_sum = 0
    j = 0
    while j < len(result):
        comment_sum = comment_sum + int(result[j]['amount'])
        j = j + 1
    return comment_sum


def edit_entry():
    entry_id = get_entry_id()

    entry = Balance.get_or_none(Balance.id == entry_id)
    if entry is None:
        print("Not an entry")
    else:
        result = []
        result.append(dict(
            id=entry.id,
            amount=entry.amount,
            tag=entry.tag,
            comment=entry.comment,
            date=entry.date,
        ))

        print("{:<15} {:<15} {:<8} {:<40} {:<}"
              .format('ID', 'Tag', 'Amount', 'Comment', 'Date'))
        print_table_2(result)

        delete = confirm_delete()
        if delete is not True:
            entry.delete_instance()
        else:
            tag = get_tag_one()
            amount = get_amount()
            comment = get_comment()

            register = confirm_entry()

            if register is True:
                entry.amount = amount
                entry.tag = tag
                entry.comment = comment
                entry.date = entry.date
                entry.save()
