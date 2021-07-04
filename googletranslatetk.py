#import needed lib
from tkinter import *
from tkinter import ttk
from google_trans_new import google_translator

#make screen
tk = Tk()
tk.title('mohammadmahdi Eyni')
tk.geometry('1300x100')

fr = Frame(tk, bg='pink')
fr.grid(row=3, column=1)



tk.config(bg='pink')

#create input box
e = Entry(tk, width=100, bg='light green')
e.grid(row=1, column=1)
#translate def
translator = google_translator()
#create intvar for int input
radvar1 = IntVar()







n = StringVar()
languages = ttk.Combobox(fr, width=27, textvariable=n, state='readonly')
languages['values'] = (
    'afrikaans',
    'albanian',
    'amharic',
    'arabic',
    'armenian',
    'azerbaijani',
    'basque',
    'belarusian',
    'bengali',
    'bosnian',
    'bulgarian',
    'catalan',
    'cebuano',
    'chichewa',
    'chinese (simplified)',
    'chinese (traditional)',
    'corsican',
    'croatian',
    'czech',
    'danish',
    'dutch',
    'english',
    'esperanto',
    'estonian',
    'filipino',
    'finnish',
    'french',
    'frisian',
    'galician',
    'georgian',
    'german',
    'greek',
    'gujarati',
    'haitian creole',
    'hausa',
    'hawaiian',
    'hebrew',
    'hebrew',
    'hindi',
    'hmong',
    'hungarian',
    'icelandic',
    'igbo',
    'indonesian',
    'irish',
    'italian',
    'japanese',
    'javanese',
    'kannada',
    'kazakh',
    'khmer',
    'korean',
    'kurdish (kurmanji)',
    'kyrgyz',
    'lao',
    'latin',
    'latvian',
    'lithuanian',
    'luxembourgish',
    'macedonian',
    'malagasy',
    'malay',
    'malayalam',
    'maltese',
    'maori',
    'marathi',
    'mongolian',
    'myanmar (burmese)',
    'nepali',
    'norwegian',
    'odia',
    'pashto',
    'persian',
    'polish',
    'portuguese',
    'punjabi',
    'romanian',
    'russian',
    'samoan',
    'scots gaelic',
    'serbian',
    'sesotho',
    'shona',
    'sindhi',
    'sinhala',
    'slovak',
    'slovenian',
    'somali',
    'spanish',
    'sundanese',
    'swahili',
    'swedish',
    'tajik',
    'tamil',
    'telugu',
    'thai',
    'turkish',
    'ukrainian',
    'urdu',
    'uyghur',
    'uzbek',
    'vietnamese',
    'welsh',
    'xhosa',
    'yiddish',
    'yoruba',
    'zulu',)
languages.grid(row=1, column=4)
languages.current(21)

#add language for use
def trans():

    if n.get() == 'english':
        a = 'en'
    elif n.get() == 'persian':
        a = 'fa'
    elif n.get() == 'arabic':
        a = 'ar'
    elif n.get() == 'french':
        a = 'fr'
    elif n.get() == 'german':
        a = 'de'
    elif n.get() == 'italian':
        a = 'it'
    elif n.get() == 'hindi':
        a = 'hi'
    elif n.get() == 'japanese':
        a = 'ja'
    elif n.get() == 'chinese (simplified)':
        a = 'zh-cn'
    elif n.get() == 'turkish':
        a = 'tr'
    elif n.get() == 'albanian':
        a = 'sq'
    elif n.get() == 'amharic':
        a = 'am'
    elif n.get() == 'armenian':
        a = 'hy'
    elif n.get() == 'azerbaijani':
        a = 'az'
    elif n.get() == 'basque':
        a = 'eu'
    elif n.get() == 'belarusian':
        a = 'be'
    elif n.get() == 'bengali':
        a = 'bn'
    elif n.get() == 'bosnian':
        a = 'bs'
    elif n.get() == 'bulgarian':
        a = 'bg'
    elif n.get() == 'catalan':
        a = 'ca'
    elif n.get() == 'cebuano':
        a = 'ceb'
    elif n.get() == 'chichewa':
        a = 'ny'
    elif n.get() == 'chinese (traditional)':
        a = 'zh-tw'
    elif n.get() == 'corsican':
        a = 'co'
    elif n.get() == 'croatian':
        a = 'hr'
    elif n.get() == 'czech':
        a = 'cs'
    elif n.get() == 'danish':
        a = 'da'
    elif n.get() == 'dutch':
        a = 'nl'
    elif n.get() == 'esperanto':
        a = 'eo'
    elif n.get() == 'estonian':
        a = 'et'
    elif n.get() == 'filipino':
        a = 'tl'
    elif n.get() == 'finnish':
        a = 'fi'
    elif n.get() == 'frisian':
        a = 'fy'
    elif n.get() == 'galician':
        a = 'gl'
    elif n.get() == 'georgian':
        a = 'ka'
    elif n.get() == 'greek':
        a = 'el'
    elif n.get() == 'gujarati':
        a = 'gu'
    elif n.get() == 'haitian creole':
        a = 'ht'
    elif n.get() == 'hausa':
        a = 'ha'
    elif n.get() == 'hawaiian':
        a = 'haw'
    elif n.get() == 'hebrew':
        a = 'iw'
    elif n.get() == 'hebrew':
        a = 'he'
    elif n.get() == 'hmong':
        a = 'hmn'
    elif n.get() == 'hungarian':
        a = 'hu'
    elif n.get() == 'icelandic':
        a = 'is'
    elif n.get() == 'igbo':
        a = 'ig'
    elif n.get() == 'indonesian':
        a = 'id'
    elif n.get() == 'irish':
        a = 'ga'
    elif n.get() == 'javanese':
        a = 'jw'
    elif n.get() == 'kannada':
        a = 'kn'
    elif n.get() == 'kazakh':
        a = 'kk'
    elif n.get() == 'khmer':
        a = 'km'
    elif n.get() == 'korean':
        a = 'ko'
    elif n.get() == 'kurdish (kurmanji)':
        a = 'ku'
    elif n.get() == 'kyrgyz':
        a = 'ky'
    elif n.get() == 'lao':
        a = 'lo'
    elif n.get() == 'latin':
        a = 'la'
    elif n.get() == 'latvian':
        a = 'lv'
    elif n.get() == 'lithuanian':
        a = 'lt'
    elif n.get() == 'luxembourgish':
        a = 'lb'
    elif n.get() == 'macedonian':
        a = 'mk'
    elif n.get() == 'malagasy':
        a = 'mg'
    elif n.get() == 'malay':
        a = 'ms'
    elif n.get() == 'malayalam':
        a = 'ml'
    elif n.get() == 'maltese':
        a = 'mt'
    elif n.get() == 'maori':
        a = 'mi'
    elif n.get() == 'marathi':
        a = 'mr'
    elif n.get() == 'mongolian':
        a = 'mn'
    elif n.get() == 'myanmar (burmese)':
        a = 'my'
    elif n.get() == 'nepali':
        a = 'ne'
    elif n.get() == 'norwegian':
        a = 'no'
    elif n.get() == 'odia':
        a = 'or'
    elif n.get() == 'pashto':
        a = 'ps'
    elif n.get() == 'polish':
        a = 'pl'
    elif n.get() == 'portuguese':
        a = 'pt'
    elif n.get() == 'punjabi':
        a = 'pa'
    elif n.get() == 'romanian':
        a = 'ro'
    elif n.get() == 'russian':
        a = 'ru'
    elif n.get() == 'samoan':
        a = 'sm'
    elif n.get() == 'scots gaelic':
        a = 'gd'
    elif n.get() == 'serbian':
        a = 'sr'
    elif n.get() == 'sesotho':
        a = 'st'
    elif n.get() == 'shona':
        a = 'sn'
    elif n.get() == 'sindhi':
        a = 'sd'
    elif n.get() == 'sinhala':
        a = 'si'
    elif n.get() == 'slovak':
        a = 'sk'
    elif n.get() == 'slovenian':
        a = 'sl'
    elif n.get() == 'somali':
        a = 'so'
    elif n.get() == 'spanish':
        a = 'es'
    elif n.get() == 'sundanese':
        a = 'su'
    elif n.get() == 'swahili':
        a = 'sw'
    elif n.get() == 'swedish':
        a = 'sv'
    elif n.get() == 'tajik':
        a = 'tg'
    elif n.get() == 'tamil':
        a = 'ta'
    elif n.get() == 'telugu':
        a = 'te'
    elif n.get() == 'thai':
        a = 'th'
    elif n.get() == 'ukrainian':
        a = 'uk'
    elif n.get() == 'urdu':
        a = 'ur'
    elif n.get() == 'uyghur':
        a = 'ug'
    elif n.get() == 'uzbek':
        a = 'uz'
    elif n.get() == 'vietnamese':
        a = 'vi'
    elif n.get() == 'welsh':
        a = 'cy'
    elif n.get() == 'xhosa':
        a = 'xh'
    elif n.get() == 'yiddish':
        a = 'yi'
    elif n.get() == 'yoruba':
        a = 'yo'
    elif n.get() == 'zulu':
        a = 'zu'
    elif n.get() == 'afrikaans':
        a = 'af'

#show translate
    tran = translator.translate(e.get(), lang_tgt=a, pronounce=False)
    label = Label(tk, text=tran, bg='cyan', width=100)
    label.grid(row=1, column=4)
def transevent(event):
    if n.get() == 'english':
        a = 'en'
    elif n.get() == 'persian':
        a = 'fa'
    elif n.get() == 'arabic':
        a = 'ar'
    elif n.get() == 'french':
        a = 'fr'
    elif n.get() == 'german':
        a = 'de'
    elif n.get() == 'italian':
        a = 'it'
    elif n.get() == 'hindi':
        a = 'hi'
    elif n.get() == 'japanese':
        a = 'ja'
    elif n.get() == 'chinese (simplified)':
        a = 'zh-cn'
    elif n.get() == 'turkish':
        a = 'tr'
    elif n.get() == 'albanian':
        a = 'sq'
    elif n.get() == 'amharic':
        a = 'am'
    elif n.get() == 'armenian':
        a = 'hy'
    elif n.get() == 'azerbaijani':
        a = 'az'
    elif n.get() == 'basque':
        a = 'eu'
    elif n.get() == 'belarusian':
        a = 'be'
    elif n.get() == 'bengali':
        a = 'bn'
    elif n.get() == 'bosnian':
        a = 'bs'
    elif n.get() == 'bulgarian':
        a = 'bg'
    elif n.get() == 'catalan':
        a = 'ca'
    elif n.get() == 'cebuano':
        a = 'ceb'
    elif n.get() == 'chichewa':
        a = 'ny'
    elif n.get() == 'chinese (traditional)':
        a = 'zh-tw'
    elif n.get() == 'corsican':
        a = 'co'
    elif n.get() == 'croatian':
        a = 'hr'
    elif n.get() == 'czech':
        a = 'cs'
    elif n.get() == 'danish':
        a = 'da'
    elif n.get() == 'dutch':
        a = 'nl'
    elif n.get() == 'esperanto':
        a = 'eo'
    elif n.get() == 'estonian':
        a = 'et'
    elif n.get() == 'filipino':
        a = 'tl'
    elif n.get() == 'finnish':
        a = 'fi'
    elif n.get() == 'frisian':
        a = 'fy'
    elif n.get() == 'galician':
        a = 'gl'
    elif n.get() == 'georgian':
        a = 'ka'
    elif n.get() == 'greek':
        a = 'el'
    elif n.get() == 'gujarati':
        a = 'gu'
    elif n.get() == 'haitian creole':
        a = 'ht'
    elif n.get() == 'hausa':
        a = 'ha'
    elif n.get() == 'hawaiian':
        a = 'haw'
    elif n.get() == 'hebrew':
        a = 'iw'
    elif n.get() == 'hebrew':
        a = 'he'
    elif n.get() == 'hmong':
        a = 'hmn'
    elif n.get() == 'hungarian':
        a = 'hu'
    elif n.get() == 'icelandic':
        a = 'is'
    elif n.get() == 'igbo':
        a = 'ig'
    elif n.get() == 'indonesian':
        a = 'id'
    elif n.get() == 'irish':
        a = 'ga'
    elif n.get() == 'javanese':
        a = 'jw'
    elif n.get() == 'kannada':
        a = 'kn'
    elif n.get() == 'kazakh':
        a = 'kk'
    elif n.get() == 'khmer':
        a = 'km'
    elif n.get() == 'korean':
        a = 'ko'
    elif n.get() == 'kurdish (kurmanji)':
        a = 'ku'
    elif n.get() == 'kyrgyz':
        a = 'ky'
    elif n.get() == 'lao':
        a = 'lo'
    elif n.get() == 'latin':
        a = 'la'
    elif n.get() == 'latvian':
        a = 'lv'
    elif n.get() == 'lithuanian':
        a = 'lt'
    elif n.get() == 'luxembourgish':
        a = 'lb'
    elif n.get() == 'macedonian':
        a = 'mk'
    elif n.get() == 'malagasy':
        a = 'mg'
    elif n.get() == 'malay':
        a = 'ms'
    elif n.get() == 'malayalam':
        a = 'ml'
    elif n.get() == 'maltese':
        a = 'mt'
    elif n.get() == 'maori':
        a = 'mi'
    elif n.get() == 'marathi':
        a = 'mr'
    elif n.get() == 'mongolian':
        a = 'mn'
    elif n.get() == 'myanmar (burmese)':
        a = 'my'
    elif n.get() == 'nepali':
        a = 'ne'
    elif n.get() == 'norwegian':
        a = 'no'
    elif n.get() == 'odia':
        a = 'or'
    elif n.get() == 'pashto':
        a = 'ps'
    elif n.get() == 'polish':
        a = 'pl'
    elif n.get() == 'portuguese':
        a = 'pt'
    elif n.get() == 'punjabi':
        a = 'pa'
    elif n.get() == 'romanian':
        a = 'ro'
    elif n.get() == 'russian':
        a = 'ru'
    elif n.get() == 'samoan':
        a = 'sm'
    elif n.get() == 'scots gaelic':
        a = 'gd'
    elif n.get() == 'serbian':
        a = 'sr'
    elif n.get() == 'sesotho':
        a = 'st'
    elif n.get() == 'shona':
        a = 'sn'
    elif n.get() == 'sindhi':
        a = 'sd'
    elif n.get() == 'sinhala':
        a = 'si'
    elif n.get() == 'slovak':
        a = 'sk'
    elif n.get() == 'slovenian':
        a = 'sl'
    elif n.get() == 'somali':
        a = 'so'
    elif n.get() == 'spanish':
        a = 'es'
    elif n.get() == 'sundanese':
        a = 'su'
    elif n.get() == 'swahili':
        a = 'sw'
    elif n.get() == 'swedish':
        a = 'sv'
    elif n.get() == 'tajik':
        a = 'tg'
    elif n.get() == 'tamil':
        a = 'ta'
    elif n.get() == 'telugu':
        a = 'te'
    elif n.get() == 'thai':
        a = 'th'
    elif n.get() == 'ukrainian':
        a = 'uk'
    elif n.get() == 'urdu':
        a = 'ur'
    elif n.get() == 'uyghur':
        a = 'ug'
    elif n.get() == 'uzbek':
        a = 'uz'
    elif n.get() == 'vietnamese':
        a = 'vi'
    elif n.get() == 'welsh':
        a = 'cy'
    elif n.get() == 'xhosa':
        a = 'xh'
    elif n.get() == 'yiddish':
        a = 'yi'
    elif n.get() == 'yoruba':
        a = 'yo'
    elif n.get() == 'zulu':
        a = 'zu'
    elif n.get() == 'afrikaans':
        a = 'af'

    #show translate
    tran = translator.translate(e.get(), lang_tgt=a, pronounce=False)
    label = Label(tk, text=tran, bg='cyan', width=100)
    label.grid(row=1, column=4)
tk.bind('<Return>', transevent)
#button for translate

b = Button(tk, text='translate', command=trans)
b.grid(row=2, column=1)
tk.mainloop()
