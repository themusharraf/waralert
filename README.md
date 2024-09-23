# Waralert
- Bu loyiha `Sentry` kabi xatolarni kuzatish va bildirish tizimining juda soddalashtirilgan versiyasidir.
Haqiqiy loyiha uchun yuqoridagi kodlarni yanada kengaytirishingiz, qo'shimcha xavfsizlik choralari qo'shishingiz, va ma'lumotlarni to'g'ri boshqarish uchun optimallashtirishingiz kerak bo'ladi. 
Agar bu misolni yanada rivojlantirmoqchi bo'lsangiz `pull requests `qiling yoki qo'shimcha yordam kerak bo'lsa, savollarni bemalol so'rashingiz mumkin. [Gmail](https://mail.google.com/mail/u/0/?tab=rm&ogbl#search/meibrohimov%40gmail.com?compose=new), [Telegram](https://t.me/Musharraaf) 

## Email alert 
![image](https://github.com/user-attachments/assets/6c6fa290-1bbb-40c4-a59e-ee80cbeca110)

## Uni qanday ishlatish kerak 
- create `.env` file
```commandline
EMAIL= 
PASSWORD=
TO=
```
## example 
```python
from waralert.alert import send_exception


@send_exception
def div():
    a = 3 // 0
    print(a)
div()
```
