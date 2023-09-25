
#Sözlük uygulaması!

#Kelimeleri ve anlamlarını nasıl saklayacağız? Ne tür bir değişken bize yardımcı olur?
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            #Ek çlaışma: Daha fazla keliime ekleyin. Örnek kelimeler en altta...
            }
#Sözlük yapısı bir anahtar ve bir değerden oluşur. { key : value , ... }

#Kullanıcının isteğini nasıl alacağız?
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

#Kullanıcının talebini nasıl işleyeceğiz ve açıklamayı nasıl döndüreceğiz?
if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız? 

else:
    # Kelime eşleşmiyorsa ne yapmalıyız?

#Ek Çalışma 1: 
#Programı tek seferde 5 kelime soracak şekilde döngüye sokalım.

#Ek Çalışma 2:
#Bir selamlama mesajı ve bazı talimatlar ekleyeliim.

#Örnek Kelimeler: 
# LOL - komik bir şeye verilen cevap
# CRINGE - garip ya da utandırıcı bir şey
# ROFL - bir şakaya karşılık cevap
# SHEESH - onaylamamak
# CREEPY - korkunç
# AGGRO - agresifleşmek/sinirlenmek