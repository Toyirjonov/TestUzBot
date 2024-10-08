from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

API_TOKEN = '7640744802:AAFVZj1GFKoln23IYJ5uZy4qnTJzWuJ_3a8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

subjects_uz = {
    'algebra': 'Algebra',
    'geometry': 'Geometriya',
    'uzbek_history': 'Oʻzbekiston tarixi',  
    'world_history': 'Jahon tarixi',         
    'chemistry': 'Kimyo',
    'physics': 'Fizika',
    'biology': 'Biologiya',
    'informatics': 'Informatika',
    'onatili': 'Ona tili',
    'tarbiya': 'Tarbiya',
    'russian': 'Rus tili',
    'literature': 'Adabiyot',
    'geografiya': 'Geografiya',
    'english': 'Ingliz tili',
    'french': 'Fransuz tili',
    'german': 'Nemis tili',
    'law': 'Konstitutsiyaviy huquq asoslari'
}

subjects_ru = {
    'algebra': 'Алгебра',
    'geometry': 'Геометрия',
    'uzbek_history': 'История Узбекистана',  
    'world_history': 'Всемирная история',      
    'chemistry': 'Химия',
    'physics': 'Физика',
    'biology': 'Биология',
    'informatics': 'Информатика',
    'russian': 'Русский язык',
    'literature': 'Литература',
    'english': 'Английский язык',
    'french': 'Французский язык',
    'german': 'Немецкий язык',
    'law': 'Основы конституционного права',
    'onatili': 'Узбекский язык',  
    'tarbiya': 'Воспитание',      
    'geografiya': 'География'   
}

languages = {
    'uzbek': 'Ozbek sinfi 📚',
    'russian': 'Русский класс 📚'
}

grade_links = {
    'uzbek': {
        'algebra': {
            7: 'https://www.test-uz.ru/sor_uz.php?cat=214',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=145',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=132',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=122',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=107'
        },
        'geometry': {
            7: 'https://www.test-uz.ru/sor_uz.php?cat=165',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=151',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=209',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=210',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=112'
        },
        'uzbek_history': {
            7: 'https://www.test-uz.ru/sor_uz.php?cat=167',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=152',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=138',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=126',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=114'
        },
        'world_history': {
            7: 'https://www.test-uz.ru/sor_uz.php?cat=163',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=149',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=136',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=125',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=111'
        },
        'chemistry': {
           7: 'https://www.test-uz.ru/sor_uz.php?cat=172',
           8: 'https://www.test-uz.ru/sor_uz.php?cat=157',
           9: 'https://www.test-uz.ru/sor_uz.php?cat=143',
           10: 'https://www.test-uz.ru/sor_uz.php?cat=219',
           11: 'https://www.test-uz.ru/sor_uz.php?cat=120'
        },
        'physics':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=170',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=155',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=141',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=129',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=222'
        },
        'biology':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=161',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=147',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=134',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=123',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=109'
        },
        'informatics':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=205',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=208',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=227',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=226',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=113'
        },
        'russian':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=230',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=231',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=232',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=233',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=268'
        },
        'literature':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=158',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=144',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=131',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=194',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=118'
        },
        'english':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=160',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=146',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=133',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=216',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=108'
        },
        'french':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=245',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=246',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=247',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=248',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=249'
        },
        'german':{
            7: 'https://www.test-uz.ru/sor_uz.php?cat=259',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=260',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=261',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=262',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=263'
        },
        'Huquq':{
            8: 'https://www.test-uz.ru/sor_uz.php?cat=153',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=139',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=128',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=116'
                
        },
        'onatili': {
            7: 'https://www.test-uz.ru/sor_uz.php?cat=264',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=265',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=266',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=267',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=267'
        },
        'tarbiya': {
            7: 'https://www.test-uz.ru/sor_uz.php?cat=162',
            8: 'https://www.test-uz.ru/sor_uz.php?cat=148',
            9: 'https://www.test-uz.ru/sor_uz.php?cat=135',
            10: 'https://www.test-uz.ru/sor_uz.php?cat=124',
            11: 'https://www.test-uz.ru/sor_uz.php?cat=110'
        },
        'geografiya': {
          7: 'https://www.test-uz.ru/sor_uz.php?cat=164',
          8: 'https://www.test-uz.ru/sor_uz.php?cat=150',
          9: 'https://www.test-uz.ru/sor_uz.php?cat=137',
          10: 'https://www.test-uz.ru/sor_uz.php?cat=236'  
        },
    },
    'russian': {
       'algebra': {
           7: 'https://www.test-uz.ru/sor.php?cat=213',
           8: 'https://www.test-uz.ru/sor.php?cat=9',
           9: 'https://www.test-uz.ru/sor.php?cat=13',
           10: 'https://www.test-uz.ru/sor.php?cat=96',
           11: 'https://www.test-uz.ru/sor.php?cat=8'
       },
       'geometry': {
           8: 'https://www.test-uz.ru/sor.php?cat=4',
           9: 'https://www.test-uz.ru/sor.php?cat=3',
           10: 'https://www.test-uz.ru/sor.php?cat=2',
           11: 'https://www.test-uz.ru/sor.php?cat=1'
       },
       'uzbek_history': {
           7: 'https://www.test-uz.ru/sor.php?cat=45',
           8: 'https://www.test-uz.ru/sor.php?cat=60',
           9: 'https://www.test-uz.ru/sor.php?cat=74',
           10: 'https://www.test-uz.ru/sor.php?cat=105',
           11: 'https://www.test-uz.ru/sor.php?cat=87'
       },
       'world_history': { 
           7: 'https://www.test-uz.ru/sor.php?cat=41',
           8: 'https://www.test-uz.ru/sor.php?cat=58',
           9: 'https://www.test-uz.ru/sor.php?cat=72',
           10: 'https://www.test-uz.ru/sor.php?cat=100',
           11: 'https://www.test-uz.ru/sor.php?cat=86'
       },
       'chemistry': {
           7: 'https://www.test-uz.ru/sor.php?cat=53',
           8: 'https://www.test-uz.ru/sor.php?cat=67',
           9: 'https://www.test-uz.ru/sor.php?cat=81',
           10: 'https://www.test-uz.ru/sor.php?cat=218',
           11: 'https://www.test-uz.ru/sor.php?cat=94'
       },
       'physics': {
           7: 'https://www.test-uz.ru/sor.php?cat=51',
           8: 'https://www.test-uz.ru/sor.php?cat=65',
           9: 'https://www.test-uz.ru/sor.php?cat=79',
           10: 'https://www.test-uz.ru/sor.php?cat=101',
           11: 'https://www.test-uz.ru/sor.php?cat=221'
       },
       'biology': {
           7: 'https://www.test-uz.ru/sor.php?cat=39',
           8: 'https://www.test-uz.ru/sor.php?cat=56',
           9: 'https://www.test-uz.ru/sor.php?cat=70',
           10: 'https://www.test-uz.ru/sor.php?cat=99',
           11: 'https://www.test-uz.ru/sor.php?cat=84'
       },
       'informatics': {
           7: 'https://www.test-uz.ru/sor.php?cat=206',
           8: 'https://www.test-uz.ru/sor.php?cat=207',
           9: 'https://www.test-uz.ru/sor.php?cat=223',
           10: 'https://www.test-uz.ru/sor.php?cat=224',
           11: 'https://www.test-uz.ru/sor.php?cat=225'
       },
        'russian': {
            7: 'https://www.test-uz.ru/sor.php?cat=202',
            8: 'https://www.test-uz.ru/sor.php?cat=199',
            9: 'https://www.test-uz.ru/sor.php?cat=201',
            10: 'https://www.test-uz.ru/sor.php?cat=217',
            11: 'https://www.test-uz.ru/sor.php?cat=200'
        },
        'literature': {
            7: 'https://www.test-uz.ru/sor.php?cat=46',
            8: 'https://www.test-uz.ru/sor.php?cat=61',
            9: 'https://www.test-uz.ru/sor.php?cat=75',
            10: 'https://www.test-uz.ru/sor.php?cat=220',
            11: 'https://www.test-uz.ru/sor.php?cat=88'
        },
        'english': {
            7: 'https://www.test-uz.ru/sor.php?cat=38',
            8: 'https://www.test-uz.ru/sor.php?cat=55',
            9: 'https://www.test-uz.ru/sor.php?cat=69',
            10: 'https://www.test-uz.ru/sor.php?cat=215',
            11: 'https://www.test-uz.ru/sor.php?cat=83'
        },
        'french': {
            7: 'https://www.test-uz.ru/sor.php?cat=240',
            8: 'https://www.test-uz.ru/sor.php?cat=55',
            9: 'https://www.test-uz.ru/sor.php?cat=242',
            10: 'https://www.test-uz.ru/sor.php?cat=243',
            11: 'https://www.test-uz.ru/sor.php?cat=83'
        },
        'german': {
            7: 'https://www.test-uz.ru/sor.php?cat=252',
            8: 'https://www.test-uz.ru/sor.php?cat=253',
            9: 'https://www.test-uz.ru/sor.php?cat=254',
            10: 'https://www.test-uz.ru/sor.php?cat=255',
            11: 'https://www.test-uz.ru/sor.php?cat=256'
        },
        'law': {
            8: 'https://www.test-uz.ru/sor.php?cat=62',
            9: 'https://www.test-uz.ru/sor.php?cat=238',
            10: 'https://www.test-uz.ru/sor.php?cat=104',
            11: 'https://www.test-uz.ru/sor.php?cat=90'
        },
        'onatili': {
            7: 'https://www.test-uz.ru/sor.php?cat=50',
            8: 'https://www.test-uz.ru/sor.php?cat=64',
            9: 'https://www.test-uz.ru/sor.php?cat=78',
            10: 'https://www.test-uz.ru/sor.php?cat=102',
            11: 'https://www.test-uz.ru/sor.php?cat=92'
        },
        'tarbiya': {
            7: 'https://www.test-uz.ru/sor.php?cat=40',
            8: 'https://www.test-uz.ru/sor.php?cat=57',
            9: 'https://www.test-uz.ru/sor.php?cat=71',
            10: 'https://www.test-uz.ru/sor.php?cat=98',
            11: 'https://www.test-uz.ru/sor.php?cat=85'
        },
        'geografiya': {
            7: 'https://www.test-uz.ru/sor.php?cat=42',
            8: 'https://www.test-uz.ru/sor.php?cat=59',
            9: 'https://www.test-uz.ru/sor.php?cat=73',
            10: 'https://www.test-uz.ru/sor.php?cat=235'
        },
    },
}

def get_language_keyboard():
    buttons = [
        [InlineKeyboardButton(text=text, callback_data=f'lang_{code}')]
        for code, text in languages.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_subjects_keyboard(lang):
    subjects = subjects_uz if lang == 'uzbek' else subjects_ru
    buttons = []
    for i in range(0, len(subjects), 2):
        row = []
        for code, text in list(subjects.items())[i:i+2]:
            row.append(InlineKeyboardButton(text=text, callback_data=f'subject_{lang}_{code}'))
        buttons.append(row)
    
    back_text = "Orqaga" if lang == 'uzbek' else "Назад"
    buttons.append([InlineKeyboardButton(text=back_text, callback_data='back_to_lang')])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_grades_keyboard(lang, subject):
    buttons = []
    grades = list(range(7, 12))
    
    for i in range(0, len(grades), 2):
        row = []
        for grade in grades[i:i+2]:
            if lang == 'uzbek':
                text = f"{subject.capitalize()} {grade}-sinf"  # Используем стандартное название предмета
                link = grade_links['uzbek'].get(subject, {}).get(grade, '')
            else:
                text = f"{subject.capitalize()} {grade}-й класс"  # Используем стандартное название предмета
                link = grade_links['russian'].get(subject, {}).get(grade, '')

            if link:
                row.append(InlineKeyboardButton(text=text, url=link))
        buttons.append(row)
    
    back_text = "Orqaga" if lang == 'uzbek' else "Назад"
    buttons.append([InlineKeyboardButton(text=back_text, callback_data=f'back_to_subjects_{lang}')])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(Command('start'))
async def start_cmd(message: Message):
    welcome_text = f"Salom {message.from_user.first_name}! Ushbu bot sizga BSB va CHSB ga javob olishda yordam beradi."
    await message.reply(welcome_text, reply_markup=get_language_keyboard())

@dp.callback_query(F.data.startswith('lang_'))
async def process_language_selection(callback: CallbackQuery):
    lang = callback.data.split('_')[1]
    await callback.answer()
    
    if lang == 'uzbek':
        text = "Javoblar kerak bo'lgan fanni tanlang:"
    else:
        text = "Выберите предмет, по которому нужны ответы:"
    
    await callback.message.edit_text(text=text, reply_markup=get_subjects_keyboard(lang))

@dp.callback_query(F.data.startswith('subject_'))
async def process_subject_selection(callback: CallbackQuery):
    _, lang, subject_code = callback.data.split('_')
    subjects = subjects_uz if lang == 'uzbek' else subjects_ru
    subject_name = subjects.get(subject_code, "Noma'lum fan" if lang == 'uzbek' else "Неизвестный предмет")
    
    await callback.answer()
    
    if lang == 'uzbek':
        text = f"{subject_name}\nSinfni tanlang:"
    else:
        text = f"{subject_name}\nВыберите класс:"
    
    await callback.message.edit_text(
        text=text,
        reply_markup=get_grades_keyboard(lang, subject_code)
    )

@dp.callback_query(F.data == 'back_to_lang')
async def process_back_to_lang(callback: CallbackQuery):
    await callback.answer()
    welcome_text = f"Salom! Ushbu bot sizga BSB va CHSB ga javob olishda yordam beradi."
    await callback.message.edit_text(text=welcome_text, reply_markup=get_language_keyboard())

@dp.callback_query(F.data.startswith('back_to_subjects_'))
async def process_back_to_subjects(callback: CallbackQuery):
    lang = callback.data.split('_')[-1]
    await callback.answer()
    
    if lang == 'uzbek':
        text = "Javoblar kerak bo'lgan fanni tanlang:"
    else:
        text = "Выберите предмет, по которому нужны ответы:"
    
    await callback.message.edit_text(text=text, reply_markup=get_subjects_keyboard(lang))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())