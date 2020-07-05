

from peewee import SqliteDatabase, Model, CharField, DateField

db = SqliteDatabase('balance.db')


class Balance(Model):
    amount = CharField()
    tag = CharField()
    comment = CharField()
    date = DateField()

    class Meta:
        database = db  # This model uses the "balance.db" database.


db.connect()


def query_tag(tag):
    result = []
    for r in Balance.select().where(Balance.tag == tag):
        result.append(dict(
            amount=r.amount,
            tag=r.tag,
            comment=r.comment,
            date=r.date,
        ))
    return result


def query_month_year(month, year):
    result = []
    for r in Balance.select().where(Balance.date.month == month,
                                    Balance.date.year == year):
        result.append(dict(
            amount=r.amount,
            tag=r.tag,
            comment=r.comment,
            date=r.date,
        ))
    return result


def query_month_year_tag(month, year, tag):
    result = []
    for r in Balance.select().where(Balance.date.month == month,
                                    Balance.date.year == year,
                                    Balance.tag == tag):
        result.append(dict(
            amount=r.amount,
            tag=r.tag,
            comment=r.comment,
            date=r.date,
        ))
    return result


def query_comments(phrase):
    result = []
    for query in Balance.select():

        if query.comment.find(phrase) != -1:
            result.append(dict(
                amount=query.amount,
                tag=query.tag,
                comment=query.comment,
                date=query.date,
            ))

    return result
