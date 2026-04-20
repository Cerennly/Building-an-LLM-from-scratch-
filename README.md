Building an LLM from scratch
Module 01 
token örnek bir metin üzerinden en basit hali ile  kelimelere böldük .split()
ve bir sözlük oluşturduk
#vocab = {
#    "The": 0,
#    "cat": 1,
#    "dog": 2,
#    "chased": 3,
#    "capital": 4,
#    "of": 5,
#    "France": 6,
#    "is": 7,
#    "<unk>": 8,
#    "the": 9
#}   
tokenladık metin/cümle artık [0, 1, 3, 9, 2] ifade edebiliyorduk
tiktoken 
encoding-decoding
dışarıdan bir (gemma) model kullanrak istediğimiz bir cümleyi- metni farklı dil modelinde sözlüklerdeki numaralarını görebildiğimiz codlar yazdık
transformers
BPE
sentencepiece library
huggingface - accesstoken
***************Düzeltme********************************
Module 01: Tokenization Fundamentals
Bu modülde, bir Büyük Dil Modeli'nin (LLM) ham metni nasıl anlamlandırdığını keşfederek en temel seviyeden gelişmiş kütüphanelere kadar tokenization süreçlerini ele aldık.

1. Temel Tokenization ve Sözlük (Vocab) Oluşturma
Süreci anlamak adına bir metni en basit haliyle .split() metodunu kullanarak kelimelerine ayırdık ve her kelimeye benzersiz bir sayısal karşılık atadık.

Sözlük Yapısı: Kelimeleri indekslerle eşleştirerek bir vocab oluşturduk.

Sayısal Temsil: Metinleri artık bilgisayarın işleyebileceği [0, 1, 3, 9, 2] gibi vektör formlarına dönüştürebiliyoruz.

Bilinmeyen Kelimeler: Sözlükte yer almayan kelimeler için <unk> (unknown) token kullanımını simüle ettik.

Python
vocab = {
    "The": 0, "cat": 1, "dog": 2, "chased": 3, 
    "capital": 4, "of": 5, "France": 6, "is": 7, 
    "<unk>": 8, "the": 9
}
2. Gelişmiş Tokenization Araçları
Basit bölme işlemlerinden sonra, modern modellerin kullandığı profesyonel kütüphaneleri ve yöntemleri inceledik:

tiktoken: OpenAI tarafından kullanılan hızlı BPE (Byte Pair Encoding) çözümleyicisi üzerinde çalışıldı.

Encoding & Decoding: Metnin sayılara (encode) ve sayıların tekrar metne (decode) dönüştürülme süreçleri uygulandı.

Model Entegrasyonu (Gemma): Harici modellerin (örneğin Gemma) sözlük yapılarını kullanarak, bir metnin farklı dil modellerinde nasıl farklı numaralandırıldığını gözlemleyen kodlar yazıldı.

3. Kütüphaneler ve Algoritmalar
Projenin bu aşamasında aşağıdaki temel kavramlar ve araçlar kullanılmıştır:

BPE (Byte Pair Encoding): Kelime altı (subword) birimlerini temel alan algoritma yapısı.

SentencePiece: Google tarafından geliştirilen, dilden bağımsız tokenization kütüphanesi.

Hugging Face Transformers: access_token kullanarak model ağırlıklarına ve tokenizer yapılarına erişim sağlandı.


