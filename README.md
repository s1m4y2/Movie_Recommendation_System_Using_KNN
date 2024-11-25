[# Movie_Recommendation_System_Using_KNN]

# 🎬 **Film Öneri Sistemi**

Bu proje, kullanıcıların kişiselleştirilmiş film önerileri almasını, filmleri puanlamasını ve çeşitli filtreleme seçenekleriyle arama yapmasını sağlayan bir **Film Öneri Sistemi**dir. Flask tabanlı bir web uygulaması olarak geliştirilmiştir ve KNN algoritmasını kullanır.

---

## 🚀 **Özellikler**
- 🔍 **Kullanıcı ID'sine göre öneri**: Girilen kullanıcı ID'sine özel öneriler.
- 🎞️ **Benzer filmleri bulma**: Girilen film adına benzeyen filmler önerilir.
- 🎭 **Film filtreleme**: Tür, çıkış yılı ve puana göre arama yapılabilir.
- ⭐ **Film puanlama**: Kullanıcılar filmleri değerlendirebilir.
- 📊 **Görselleştirme**: Kullanıcı aktivite grafiği oluşturma.

---

## 🛠️ **Kurulum Talimatları**

### 1. **Gereksinimler**
Bu projeyi çalıştırmak için aşağıdaki araçların sisteminizde kurulu olması gereklidir:
- Python 3.8 veya üstü
- Flask
- Pandas
- Matplotlib

### 2. **Projenin Klonlanması**
```bash
git clone https://github.com/kullaniciadi/film-oneri-sistemi.git
cd film-oneri-sistemi
```

### 3. **Gerekli Kütüphanelerin Yüklenmesi**
Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:

pip install -r requirements.txt

### 4. **Uygulamanın Çalıştırılması**
Projeyi çalıştırmak için aşağıdaki komutu kullanın:

python app.py

Ardından tarayıcınızda http://127.0.0.1:5000 adresine gidin.


## 🗂️ **Proje Yapısı**
film-oneri-sistemi/
├── app.py                   # Flask ana uygulaması
├── recommendation.py        # Öneri fonksiyonlarını içeren dosya
├── visualization.py         # Görselleştirme için kodlar
├── templates/               # HTML şablonları
│   ├── index.html
│   ├── recommendations.html
│   ├── error.html
│   ├── success.html
│   └── visualization.html
├── static/                  # Statik dosyalar (CSS, JS, resimler)
├── data/                    # Kullanılan veri setleri
│   └── movies.csv
├── README.md                # Proje açıklama dosyası
└── requirements.txt         # Gerekli Python paketleri
---

## 🌟 **Kullanım**
- **Film Önerisi Almak**: Ana sayfada Kullanıcı ID girerek öneri alın.
- **Benzer Filmler**: Bir film adı girerek benzer filmleri bulun.
- **Film Filtreleme**: Tür, yıl ve puan kriterlerini girerek arama yapın.
- **Film Puanlama**: Kullanıcı ve film bilgilerini girerek değerlendirme yapın.
- **Görselleştirme**: Kullanıcı aktiviteleri için grafik oluşturun.

---

## 📂 **Veri Seti**
Bu proje, [MovieLens](https://grouplens.org/datasets/movielens/) veri setini kullanır. Veri setindeki sütunlar:
- **userId**: Kullanıcı ID'si
- **movieId**: Film ID'si
- **rating**: Kullanıcı değerlendirme puanı
- **timestamp**: Puanlama tarihi
- **title**: Film adı
- **genres**: Film türleri

---

## 🧪 **Kullanılan Teknolojiler**
- **Flask** : Web geliştirme için.
- **Pandas** : Veri işleme ve analizi.
- **Matplotlib** : Veri görselleştirme.
- **KNN algoritması** : Film önerileri için.

---

## 🤝 **Katkıda Bulunmak**
Proje üzerinde geliştirme yapmak için:
1. Bu projeyi forklayın.
2. Yeni bir dal oluşturun: git checkout -b feature/ozellik.
3. Değişikliklerinizi ekleyin ve commit yapın: git commit -m "Yeni özellik eklendi".
4. Değişikliklerinizi ittirin: git push origin feature/ozellik.
5. Bir pull request oluşturun.

---

## 📧 **İletişim**
Eğer bir sorunla karşılaşırsanız veya bir öneriniz varsa simaynglu@gmail.com adresinden bana ulaşabilirsiniz.

---

İyi eğlenceler! 😊
)
