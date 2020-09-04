

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))


def general_question():
    question = [
        {
            'type': 'list',
            'name': 'general',
            'message': 'What do you want to do?',
            'choices': [
                'Register income/expense',
                'Month overview',
                'Year overview',
                'Query DB',
                'Search in comments',
                'Edit an entry',
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['general']


# TODO find a way to repeate until confirm = False
def continue_confirm():
    confirm = [
        {
            'type': 'confirm',
            'message': 'Do you want to continue?',
            'name': 'continue',
            'default': True,
        },
    ]

    answer = prompt(confirm, style=style)
    return answer['continue']


def confirm_entry():
    confirm = [
        {
            'type': 'confirm',
            'message': 'Do you want to save this entry?',
            'name': 'save_entry',
            'default': True,
        },
    ]

    answer = prompt(confirm, style=style)
    return answer['save_entry']


def confirm_delete():
    delete = [
        {
            'type': 'confirm',
            'message': 'Do you want to edit (Yes) or delete (no) this entry?',
            'name': 'delete_entry',
            'default': True,
        },
    ]

    answer = prompt(delete, style=style)
    return answer['delete_entry']


def get_query_type():
    question = [
        {
            'type': 'list',
            'name': 'tagdate',
            'message': 'tag or date?',
            'choices': [
                'tag',
                'month-year',
                'tag-month-year',
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['tagdate']


def get_tags():
    question = [
        {
            'type': 'checkbox',
            'name': 'taglist',
            'message': 'Pick tag',
            'choices': [
                {'name': 'consumable'},
                {'name': 'experience'},
                {'name': 'food'},
                {'name': 'income'},
                {'name': 'regular'},
                {'name': 'things'},
                {'name': 'transport'},
                {'name': 'other'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['taglist']


def get_tag_one():
    question = [
        {
            'type': 'list',
            'name': 'tag',
            'message': 'Pick a tag',
            'choices': [
                {'name': 'consumable'},
                {'name': 'experience'},
                {'name': 'food'},
                {'name': 'income'},
                {'name': 'regular'},
                {'name': 'things'},
                {'name': 'transport'},
                {'name': 'other'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['tag']


def get_month():
    question = [
        {
            'type': 'checkbox',
            'name': 'monthlist',
            'message': 'Pick the month',
            'choices': [
                {'name': '1'},
                {'name': '2'},
                {'name': '3'},
                {'name': '4'},
                {'name': '5'},
                {'name': '6'},
                {'name': '7'},
                {'name': '8'},
                {'name': '9'},
                {'name': '10'},
                {'name': '11'},
                {'name': '12'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['monthlist']


def get_one_month():
    question = [
        {
            'type': 'list',
            'name': 'onemonthlist',
            'message': 'Pick the month',
            'choices': [
                {'name': '1'},
                {'name': '2'},
                {'name': '3'},
                {'name': '4'},
                {'name': '5'},
                {'name': '6'},
                {'name': '7'},
                {'name': '8'},
                {'name': '9'},
                {'name': '10'},
                {'name': '11'},
                {'name': '12'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['onemonthlist']


def get_year():
    question = [
        {
            'type': 'checkbox',
            'name': 'yearlist',
            'message': 'Pick the year',
            'choices': [
                {'name': '2020'},
                {'name': '2021'},
                {'name': '2022'},
                {'name': '2023'},
                {'name': '2024'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['yearlist']


def get_one_year():
    question = [
        {
            'type': 'list',
            'name': 'oneyearlist',
            'message': 'Pick the year',
            'choices': [
                {'name': '2020'},
                {'name': '2021'},
                {'name': '2022'},
                {'name': '2023'},
                {'name': '2024'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['oneyearlist']


def get_amount():
    question = [
        {
            'type': 'input',
            'name': 'amount',
            'message': 'Input amount +/-',
            'validate': NumberValidator,
            'filter': lambda val: int(val)
        }
    ]

    answer = prompt(question, style=style)
    return answer['amount']


def get_comment():
    question = [
        {
            'type': 'input',
            'name': 'comment',
            'message': 'Write a comment',
        }
    ]

    answer = prompt(question, style=style)
    return answer['comment']


def get_month_save():
    question = [
        {
            'type': 'list',
            'name': 'month',
            'message': 'Pick the year',
            'choices': [
                {'name': 'this month'},
                {'name': 'last month'},
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['month']


def get_phrase():
    question = [
        {
            'type': 'input',
            'name': 'phrase',
            'message': 'Phrase to search for',
        }
    ]

    answer = prompt(question, style=style)
    return answer['phrase']


def get_entry_id():
    question = [
        {
            'type': 'input',
            'name': 'entry_id',
            'message': 'Write the entry id',
        }
    ]

    answer = prompt(question, style=style)
    return answer['entry_id']
