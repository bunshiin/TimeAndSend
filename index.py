import pywhatkit
import pywhatkit

number = "" #Telefon Numarası (Başına alan kodu koyulmalıdır.) Örn: "+90"
message = "" #Mesaj Örn: Doğum Günün Kutlu Olsun. ❤
hours = "" #Saat, Not: hours= "13" 13 saat anlamına gelmez Saat 1 de anlamına gelir.
minutes = "" #Dakika


# Mesaj Gönderme Fonksiyonu
pywhatkit.sendwhatmsg(number, message, hours, minutes)