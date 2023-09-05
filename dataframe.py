import pandas as pd
import os
from translate_common import translation, detokenize_translation
from translate_from_transliteration import translate_transliteration_base


data_frame = pd.read_csv('/Users/christiankarren/FG/fg.csv')
print(data_frame['Akkadian_transliteration'])

def translate_transliteration(sentence):
    output = ""
    for line in data_frame['Akkadian_transliteration'].str.split('\n'):
        if translation(line):
            output += detokenize_translation(line, "/Users/christiankarren/FG/translation_bpe.model")
    return output


if __name__ == '__main__':
    x = data_frame['Akkadian_transliteration'][1]
    y = translate_transliteration(x)
    print(y)
    #sentence = input("Please enter a transliteration sentence for translation\n")
    # print(translate_transliteration(sentence))

import pandas as pd

def translate_column_to_english(data_frame, column_name):
    def translate_transliteration(text):
        # Replace this with your translation logic
        # For example, you can use the translate_transliteration function here
        return translate_transliteration(text)
    data_frame['English Translation'] = data_frame[column_name].apply(translate_transliteration)
    return data_frame

