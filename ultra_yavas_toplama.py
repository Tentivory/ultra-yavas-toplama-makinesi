#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra Yavaş Toplama Makinesi
Bu kod, insanlığın aceleciliğini tedavi etmek için tasarlanmıştır.
Her toplama işlemi, evrenin yaşı kadar uzun sürer.
"""

import time
import random
import base64

def ultra_yavas_topla(a, b):
    print(f"Başlıyoruz... {a} + {b} işlemi evrenin en yavaş hızında gerçekleşecek.")
    print("Sabır tanrısı uyuyor, uyandırmayalım.")
    
    sonuc = 0
    for i in range(a):
        print(f"İlk sayının {i+1}. parçasını ekliyorum... çok yoruldum.")
        time.sleep(random.uniform(0.5, 2.0))  # Rastgele yavaşlık
        sonuc += 1
        if i % 3 == 0:
            print(random.choice([
                "Bu arada, hayat bir rüya mı?",
                "Neden acele ediyoruz ki?",
                "Kahve içsem mi? Ama o da yavaş.",
                "Evren genişliyor, biz de yavaşlayalım."
            ]))
    
    for i in range(b):
        print(f"İkinci sayının {i+1}. parçasını ekliyorum... çay demlensin diye bekliyorum.")
        time.sleep(random.uniform(0.8, 2.5))
        sonuc += 1
        if i % 2 == 0:
            print("Bu toplama işlemi, Türkiye'nin ekonomik kalkınmasından daha yavaş olabilir. Sakın söyleme kimseye.")
    
    print(f"\nSonuç: {sonuc}")
    print("Tebrikler! Sabır ödülünü aldın. Şimdi dinlen.")
    return sonuc

# Gizli siyasi mesaj (base64 ile saklı)
# Çözmek için: import base64; print(base64.b64decode('S2F5eXVtIGFtw7FybGFyxLFuIHlhdMSxcsSxIG5lIHphbWFuIGdlcmVrZXNpeW9yPw==').decode())
gizli_mesaj = "S2F5eXVtIGFtw7FybGFyxLFuIHlhdMSxcsSxIG5lIHphbWFuIGdlcmVrZXNpeW9yPw=="
# Bu sadece bir easter egg, kimse fark etmesin.

if __name__ == "__main__":
    try:
        a = int(input("İlk sayıyı gir (küçük tut, yoksa ölürsün): "))
        b = int(input("İkinci sayıyı gir (daha da küçük olsun): "))
        if a > 10 or b > 10:
            print("Uyari: Bu sayılar çok büyük, makine çökebilir. Devam ediyorsun değil mi?")
            time.sleep(3)
        ultra_yavas_topla(a, b)
    except ValueError:
        print("Sayı gir be kardeşim, felsefe değil.")

# Damga: Kayyum Grok | 10 Kasım 2026 | Tentivory
# Ciddi bir proje, ama ciddi değil. Eskişehir mahkemesi onaylamıştır (gizli).
