import os
import openai
import math
import numpy as np
import pandas as pd
from aiogram import Bot, Dispatcher, executor, types
from keep_alive import keep_alive
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = InlineKeyboardMarkup([
  [
    InlineKeyboardButton("𝐂𝐡𝐚𝐧𝐧𝐞𝐥🧿", url="https://t.me/tigraicode"),
    InlineKeyboardButton("𝐆𝐫𝐨𝐮𝐩💬", url="https://t.me/tigraicodeg")
  ],
  [
    InlineKeyboardButton("𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫👨‍💻", url="https://t.me/hipersoul"),
    InlineKeyboardButton("𝐌𝐨𝐭𝐢𝐯𝐚𝐭𝐢𝐨𝐧⚡️", url="https://t.me/hiperbrain")
  ],
])
bot = Bot(token=os.getenv("tg_token"))
dp = Dispatcher(bot)

openai.api_key = os.getenv("ai_token")

keep_alive()

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('𝐇𝐞𝐲👋𝐃𝐞𝐚𝐫, 𝐇𝐨𝐰 𝐂𝐚𝐧 𝐈 𝐚𝐬𝐬𝐢𝐬𝐭 𝐲𝐨𝐮 𝐭𝐨𝐝𝐚𝐲?', reply_markup=start_btn)


@dp.message_handler(commands=['start', 'channel'])
async def welcome(message: types.Message):
  await message.reply('https://t.me/tigraicode')


# Create a numpy array
a = np.array([1, 2, 3])

# Create a pandas DataFrame
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]})

# Use math functions
print(math.sqrt(4))
print(math.pi)

#Import the necessary libraries \nimport math \nimport numpy as np \nimport pandas as pd \n\n
#Define the subjects \nsubjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'Civics', 'SAT', 'English', 'History', 'Geography', 'Economics']\n\n
#Define the formulas for each subject \nformulas = {\n    'Math': [\n        'Area of a triangle: A = 1/2 * b * h', \n        'Circumference of a circle: C = 2 * pi * r',\n        'Pythagorean Theorem: a^2 + b^2 = c^2'\n    ],\n    'Physics': [\n        'Force = mass * acceleration',\n        'Work = force * distance',\n        'Power = work / time'\n    ],\n    'Chemistry': [\n        'Molar mass of a substance: m = n * M',\n        'Avogadro’s number: N_A = 6.022 * 10^23',\n        'Ideal gas law: PV = nRT'\n    ],\n    'Biology': [\n        'Cell theory: cells are the basic unit of life',\n        'Cell structure: cells have a nucleus, cytoplasm, and cell membrane',\n        'Cell division: mitosis and meiosis'\n    ],\n    'Civics': [\n        'Rule of law: laws should be applied equally to everyone',\n        'Separation of powers: power is divided between the executive, legislative, and judicial branches',\n        'Checks and balances: each branch of government has the power to limit the actions of the other branches'\n    ],\n    'SAT': [\n        'Sentence completion: fill in the blank with the best answer',\n        'Reading comprehension: answer questions based on a given passage',\n        'Writing: make an argument and support it with evidence'\n    ],\n    'English': [\n        'Parts of speech: noun, verb, adjective, adverb, pronoun, preposition, conjunction, interjection',\n        'Grammar: subject-verb agreement, verb tense, sentence structure',\n        'Vocabulary: synonyms, antonyms, idioms, homophones'\n    ],\n    'History': [\n        'Causes of World War I: militarism, alliances, imperialism, nationalism',\n        'Great Depression: stock market crash of 1929, bank failures, overproduction',\n        'Civil Rights Movement: Rosa Parks, Martin Luther King Jr., Selma march'\n    ],\n    'Geography': [\n        'Physical features: mountains, rivers, deserts, oceans',\n        'Political features: countries, capitals, borders',\n        'Cultural features: languages, religions, customs'\n    ],\n    'Economics': [\n        'Supply and demand: price and quantity are determined by the interaction of buyers and sellers',\n        'Scarcity: limited resources and infinite wants',\n        'Opportunity cost: the cost of an action is the next best alternative forgone'\n    ]\n}\n\n#Define the examples for each subject \nexamples = {\n    'Math': [\n        'Example 1: Find the area of a triangle with a base of 5 cm and a height of 3 cm. A = 1/2 * 5 cm * 3 cm = 7.5 cm^2',\n        'Example 2: Find the circumference of a circle with a radius of 4 cm. C = 2 * pi * 4 cm = 25.13 cm',\n        'Example 3: Find the length of the hypotenuse of a right triangle with sides of 3 cm and 4 cm. c^2 = 3 cm^2 + 4 cm^2 = 25 cm'\n    ],\n    'Physics': [\n        'Example 1: Find the force on an object with a mass of 10 kg and an acceleration of 2 m/s^2. F = 10 kg * 2 m/s^2 = 20 N',\n        'Example 2: Find the work done on an object with a force of 10 N and a distance of 5 m. W = 10 N * 5 m = 50 J',\n        'Example 3: Find the power of an object that does work of 30 J in 2 seconds. P = 30 J / 2 s = 15 W'\n    ],\n


@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=message.text,
                                      temperature=0.5,
                                      max_tokens=1024,
                                      top_p=1,
                                      frequency_penalty=0.0,
                                      presence_penalty=0.0,
                                      stop=[" Human:", " AI:"])
  await message.reply(response.choices[0].text)


if __name__ == "__main__":
  executor.start_polling(dp)
