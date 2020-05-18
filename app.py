


from __future__ import print_function, unicode_literals

import json

from question import (
    continue_confirm,
    general_question,
)

from general import (
    query_db,
    register,
    year_overview,
    month_overview,
)


keep_going = True

while keep_going is True:
    """ What do you want to do? """
    general = general_question()

    if general == 'Register income/expense':
        register()

    if general == 'Month overview':
        month_overview()

    if general == 'Year overview':
        year_overview()

    if general == 'Query DB':
        query_db()

    if general == 'Search in comments':
        print('not yet done')

    keep_going = continue_confirm()

print(' See you soon!')