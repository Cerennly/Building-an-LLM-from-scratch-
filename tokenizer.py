import json

class Tokenizer:
    def __init__(self, vocab_file):
        with open(vocab_file, "r", encoding="utf-8") as f:
            self.vocab = json.load(f)
            self.reverser_vocab = {v: k for k, v in self.vocab.items()}
            
    def encode(self, text):
        tokens = []
        
        for word in text.split():
            i=0
            #states ilk sözlükte states var mı diye bakacak sonrasında geriye dogru gelecek state var mı diye bakacak
            #yani states yok s bakacak 58 sonra state var mı bakacak 4 unk düşmesi olmayacak (unk 62 sözlük numarası)
            while i < len(word):
                found_match = False
                for j in range(len(word), i, -1):
                    sub_word = word[i:j]
                    if sub_word in self.vocab:
                        tokens.append(self.vocab[sub_word])
                        i = j
                        found_match = True
                        break
                if not found_match:
                    tokens.append(self.vocab.get("<unk>", 0))
                    i += 1
            tokens.append(self.vocab[" "])  # Boşluk tokeni ekle
            
        tokens.pop()  # Son boşluk tokenini kaldır
        return tokens
                    
                    
    def decode(self, ids):
        text = ""
        for id in ids:
            text += self.reverser_vocab[id]
        return text
    
    #def encode kısmı bunun için farklı olacak -state, states "s" farklı iki farklı tokenle temsil etmemiz lazım -encode alacak sub tokenizer olacak