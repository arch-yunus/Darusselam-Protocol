# Darusselam Protokolü (DP-01) Teknik Şartnamesi

Bu belge, bir projenin "Darusselam Uyumlu" (`DP-Compliant`) sayılabilmesi için gereken teknik detayları açıklar.

## 1. Anti-Dataism (Veri İndirgemeciliğine Ret)
- **Veri Sahipliği:** Veri her zaman kaynağında (uç cihazda) kalmalı, merkezi sunucularda "insan profili" oluşturulmamalıdır.
- **Simülasyon Sınırı:** İnsan duyguları ve iradesi, sistem optimizasyonu için birer "değişken" (variable) olarak görülemez.
- **Yasaklı Gereksinimler:** Davranışsal manipülasyon amaçlı izleme kütüphaneleri (behavioral tracking) kesinlikle yasaktır.

## 2. Zero-Harm Architecture (Hanif Mimari)
- **Ekosistem Uyumu:** Donanım tasarımları geri dönüştürülebilir olmalı, yazılım ise donanımı kasten yoran ("bloatware") yapılar içermemelidir.
- **Dayanıklılık:** Yazılım, donanımın ömrünü kısaltacak yapay kısıtlamalar (`Planned Obsolescence`) içeremez.
- **Enerji Verimliliği:** Algoritmalar, fıtrata en az yük bindirecek şekilde ("carbon-aware") tasarlanmalıdır.

## 3. Cognitive Sovereignty (Bilişsel Özgürlük)
- **Arayüz Ahlakı:** Kullanıcıyı sistemde daha fazla tutmak için tasarlanmış "Infinite Scroll" veya "Ghost Notifications" gibi yapılar yasaktır.
- **Şeffaflık:** Öneri algoritmaları, kullanıcının gerçeklik algısını bozmamalı ve hangi veriye dayanarak öneri yapıldığını şeffafça sunmalıdır.
- **Dikkat Ekonomisi:** Sistem, kullanıcının vaktini çalmak üzerine değil, ihtiyacını en hızlı şekilde giderip onu "fiziksel gerçekliğe" döndürmek üzerine kurgulanmalıdır.

## 4. Ademiyet Çizgisi (Transhümanist Sınır)
- **İradi Devre Dışı Bırakma:** İnsanın ahlaki karar alma sürecini makineye devreden (Autonomous Moral Decision Making) sistemler DP-Uyumsuz kabul edilir.
- **Biyo-Sınır:** İnsanın biyolojik yapısını "geliştirme" adı altında onun insani zaaflarını (onu insan yapan temel unsurları) yok eden donanım entegrasyonları sınırlandırılmalıdır.
- **Kul Hakkı ve Telif:** Yapay zeka modelleri, insan emeğinin karşılığını vermeden ve rıza almadan eğitilemez.

---

## Uyumluluk Denetimi (Audit)
Projelerin uyumluluğu `dp-audit` aracı ile taranır. Bu araç şu kriterlere bakar:
1. `package.json` / `requirements.txt` içindeki yasaklı izleme kütüphaneleri.
2. Kod içindeki karanlık tasarım desenleri (heuristic analysis).
3. Veri işleme fonksiyonlarındaki şeffaflık etiketleri.
