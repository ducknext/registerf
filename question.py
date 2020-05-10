

from PyInquirer import style_from_dict, Token, prompt, Separator

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})




def general_question():
    question = [
        {
            'type': 'list',
            'name': 'general',
            'message': 'What do you want to do?',
            'choices': [
                'Register income/expense',
                'Current month overview',
                'Current year overview',
                'Query DB',
                'Search in comments',
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
    if answer.get('continue') == True:
        general_question()


def get_query_type():
    question = [
        {
            'type': 'list',
            'name': 'tagdate',
            'message': 'tag or date?',
            'choices': [
                'tag',
                'month-year',
                'tag-month-year'
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
            'message': 'Pick tags',
            'choices': [
                {'name': 'consumable'},
                {'name': 'experience'},
                {'name': 'food'},
                {'name': 'income'},
                {'name': 'regular'},
                {'name': 'things'},
                {'name': 'transport'},
                {'name': 'other'}
            ]
        },
    ]
    answer = prompt(question, style=style)
    return answer['taglist']


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