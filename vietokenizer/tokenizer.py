import os 
import re 
import unicodedata as ud 
from typing import Type
import pickle as pkl 
import tensorflow as tf
from vietokenizer.preprocess_load import download, model_save, vocab_save
os.environ['TF_CPP_MIN_LOG_LEVEL']= '1'

def word_tokenizer(text: Type[str]): 
    text = ud.normalize('NFC', text)
    specials = ["==>", "->", "\.\.\.", ">>",'\n']
    digit = "\d+([\.,_]\d+)+"
    email = "([a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.)+[a-zA-Z0-9-]+)"
    #web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    web = "\w+://[^\s]+"
    #datetime = [
    #    "\d{1,2}\/\d{1,2}(\/\d{1,4})(^\dw. )+",
    #    "\d{1,2}-\d{1,2}(-\d+)?",
    #]
    word = "\w+"
    non_word = "[^\w\s]"
    abbreviations = [
        "[A-ZĐ]+\.",
        "Tp\.",
        "Mr\.", "Mrs\.", "Ms\.",
        "Dr\.", "ThS\."
    ]

    patterns = []
    patterns.extend(abbreviations)
    patterns.extend(specials)
    patterns.extend([web, email])
    patterns.extend([digit, non_word, word])

    patterns = "(" + "|".join(patterns) + ")"
    tokens = re.findall(patterns, text, re.UNICODE)
    return [token[0] for token in tokens]

def load_pretrained():
    pretrained_model= tf.keras.models.load_model(model_save + 'pretrained.h5',
                    compile= False)
    word_index= pkl.load(open(vocab_save + 'word_index.pkl', 'rb'))
    return pretrained_model, word_index

class vntokenizer:
    def __init__(self) -> None:
        download()
        self.pretrained_model, self.word_index= load_pretrained()
    def word2index(self, word):
        try:
            value= self.word_index[word]
        except:
            value= self.word_index['[UNK]']
        return value 

    def __call__(self, text: Type[str], device: Type['str']= 'cpu'):
        sequence= word_tokenizer(text)
        ids= list(map(lambda x: self.word2index(x), sequence))
        with tf.device(device): 
            output= self.pretrained_model.predict([ids])
        output= tf.math.greater_equal(output, 0.5)

        new_str= sequence[0]
        for i in range(1, len(output[0])):
            word, state= sequence[i], output[0].numpy()[i]
            if state:
                new_str += '_' + word
            else:
                new_str += ' ' + word
        return new_str 
        
if __name__ == '__main__':
    text1= 'Tôi tên là Nguyễn Tiến Đạt, hiện là sinh viên Đại học CN GTVT tại Hà Nội.'
    text2= 'Kim loại nặng thường được định nghĩa là kim loại có khối lượng riêng, khối lượng nguyên tử hoặc số hiệu nguyên tử lớn.  \\\
        Tiêu chí phân loại cụ thể, cũng như việc liệu có thể xếp á kim vào nhóm kim loại nặng hay không, khác nhau tùy thuộc vào tác giả và phạm vi áp dụng.'
    tokenizer= vntokenizer()
    print(tokenizer(text1))
