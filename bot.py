from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
 
API_TOKEN = '5871226026:AAFf1BVg3kr2dgwviQf8cnlMACeV_7tRTdE'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

# Главные занчения

class Form(StatesGroup):
    balli = State()

button_return = KeyboardButton("Назад")

# Главный раздел
button_algebra = KeyboardButton("Раздел по Алгебре")
button_geometry = KeyboardButton("Раздел по Геометрии")
button_stereometry = KeyboardButton("Раздел по Стереометрии")
button_trigonometry = KeyboardButton("Раздел по Тригонометрии")
button_balli = KeyboardButton("Перевод первичных баллов в 100 бальную систему")

nachalo_knopki = ReplyKeyboardMarkup(resize_keyboard = True).add(button_algebra).add(button_geometry).add(button_stereometry).add(button_trigonometry).add(button_balli)

#Раздел Алгебры
button_yravnenia = KeyboardButton("Уравнения")
button_graphics = KeyboardButton("Графики функций")
button_proizvodnaya = KeyboardButton("Производная")
button_logr = KeyboardButton("Логарифмические формулы")

algebra_knopki = ReplyKeyboardMarkup(resize_keyboard = True).add(button_yravnenia).add(button_graphics).add(button_proizvodnaya).add(button_logr).add(button_return)

# Раздел Геометрии
button_ploshadfig = KeyboardButton("Площадь фигур")
button_svoistvafig = KeyboardButton("Свойства фигур")
button_okrysh = KeyboardButton("Вписанная и описанная окружность формулы")

geom_knopki = ReplyKeyboardMarkup(resize_keyboard = True).add(button_ploshadfig).add(button_svoistvafig).add(button_okrysh).add(button_return)

# Раздел Стереометрии
button_formylimnogogr = KeyboardButton("Формулы многогранников")
button_formylitelvr = KeyboardButton("Формулы тел фращений")

stereometry_knopki = ReplyKeyboardMarkup(resize_keyboard = True).add(button_formylimnogogr).add(button_formylitelvr).add(button_return)

# Раздел Тригонометрия
button_trigonomform = KeyboardButton("Тригонометрические формулы")
button_trigonomgraf = KeyboardButton("Тригонометрические графики")
#button_primeriresheniatrigyr = KeyboardButton("Нахождение неизвестного под тригонометрической функцией")

trigonom_knopki = ReplyKeyboardMarkup(resize_keyboard = True).add(button_trigonomform).add(button_trigonomgraf).add(button_return)#.add(button_primeriresheniatrigyr)

# Функция для подсчетов баллов
def perevod(balli):
        balli100 = 0
        for i in range(1, balli+1):
            if i <= 5:
                if i < 4 and i % 2 == 0 or i == 1:
                    balli100 += 6
                elif i <= 5:
                    balli100 += 5
            if i == 6:
                balli100 += 7
            if i > 6 and i <= 11:
                balli100 += 6
            if i > 11 and i < 29:
                balli100 += 2
            if i >= 29:
                balli100 = 100
                return balli100
        return balli100

# комманды бота

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ специальный бот, который хранит нужную теорию для ЕГЭ по профильной математике!\nНиже кликни на кнопки, что бы выбрать теорию по нужному тебе разделу.", reply_markup = nachalo_knopki)

@dp.message_handler(lambda message: message.text == "Раздел по Алгебре")
async def teory_alg(message: types.Message):
    await message.reply("Алгебра!", reply_markup = algebra_knopki)

@dp.message_handler(lambda message: message.text == "Раздел по Геометрии")
async def teory_geom(message: types.Message):
    await message.reply("Геометрия!", reply_markup = geom_knopki)

@dp.message_handler(lambda message: message.text == "Раздел по Стереометрии")
async def teory_stere(message: types.Message):
    await message.reply("Стереометрия!", reply_markup = stereometry_knopki)

@dp.message_handler(lambda message: message.text == "Раздел по Тригонометрии")
async def teory_stere(message: types.Message):
    await message.reply("Тригонометрия!",reply_markup = trigonom_knopki)

@dp.message_handler(lambda message: message.text == "Перевод первичных баллов в 100 бальную систему", state = None)
async def perevod_ballov(message: types.Message):
    await message.reply("Отправь свое количество первичных баллов для перевода")
    await Form.balli.set()

@dp.message_handler(state = Form.balli)
async def start(message: types.Message, state: FSMContext):
    msg = message.text
    if msg.isdigit():
        balli = message.text
        await bot.send_message(message.from_user.id, text = f'При переводе у вас получилось {perevod(int(balli))} конечных баллов.')
        await state.finish()
    else:
        await message.reply("Баллы это целые числа, а не текст или десятичные числа!")
        await state.finish()

# Ответы на комманды

@dp.message_handler(lambda message: message.text == "Уравнения")
async def yravn(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/yravnenia.png?raw=true')
    await bot.send_message(call.from_user.id, text = "Основными способами решения уравнений являются:\n\nМетод разложения на множители уравнений - применяется для представления их в виде произведения нескольких менее сложных уравнений. Разложение основывается на свойстве произведения нескольких множителей равняться нулю тогда и только тогда, когда хотя бы один из этих множителей также равен нулю.\n\nМетод переноса слагаемых - любую часть уравнения можно перенести в другую сторону, за знак равенства, прибавив её к другой части уравнения и только поменяв знак на противоположный.\n\nПрибавление или вычитание выражения - к обеим частям уравнения можно прибавить одно и то же число или выражение с числовой функцией, ОДЗ которой не уже, чем ОДЗ функций в исходном уравнении. Перенос слагаемых является просто частным случаем прибавления (вычитания) выражений. В частности, 'взаимоуничтожение' одинаковых слагаемых по разные стороны знака равенства.\n\nЗамена выражений - Тождественная замена переменной другим выражением, содержащим функции от переменной, ОДЗ которых не уже, чем ОДЗ функций исходного уравнения, также всегда приводит к равносильному уравнению.\n\nВозведение в степень - частный случай умножения при идентичности множителей.Однако, возведение в степень строго определено лишь для неотрицательных чисел.")


@dp.message_handler(lambda message: message.text == "Графики функций")
async def graphici(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/graphici.jpg?raw=true', caption='Всего есть 5 типов элементарных функций:\n Степенные - к ним относятсялинейные, квадратичные, кубические, с корнями\n Показательные - неизвестная величина находится в показателе степени\т Логарифмические - неизвестная величина под знаком логарифма или в основании.\n Тригонометрические и обратные тригонометрическим.')

@dp.message_handler(lambda message: message.text == "Производная")
async def proizvod(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/tablicaproizvod.png?raw=true')

@dp.message_handler(lambda message: message.text == "Логарифмические формулы")
async def primeriresh(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/logrform.png?raw=true')

@dp.message_handler(lambda message: message.text == "Площадь фигур")
async def ploshadfigur(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://github.com/happinaith/pngfiles/blob/main/ploshadi.JPG?raw=true')

@dp.message_handler(lambda message: message.text == "Свойства фигур")
async def svoistvafigur(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/svoistva.png?raw=true')

@dp.message_handler(lambda message: message.text == "Вписанная и описанная окружность формулы")
async def vpisokr(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/radiusi.jpg?raw=true')

@dp.message_handler(lambda message: message.text == "Формулы многогранников")
async def formmnogogr(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/41.jpg?raw=true', caption="Самые часто встерчающиеся формулы в ЕГЭ по многогранникам")

@dp.message_handler(lambda message: message.text == "Формулы тел фращений")
async def formtelvr(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/telvrash.jpg?raw=true')

@dp.message_handler(lambda message: message.text == "Тригонометрические формулы")
async def trignformuli(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/trigformuli.jpg?raw=true')

@dp.message_handler(lambda message: message.text == "Тригонометрические графики")
async def logrform(call: types.CallbackQuery):
    await call.answer_photo('https://github.com/happinaith/pngfiles/blob/main/trigonomfunc.png?raw=true')

@dp.message_handler(lambda message: message.text == "Назад")
async def vozvr(message: types.Message):
    await message.reply("Возвращаю",reply_markup = nachalo_knopki)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)