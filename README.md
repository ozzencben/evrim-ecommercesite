
# Evrim Köy Ürünleri - E-Ticaret Sitesi

Evrim Köy Ürünleri, köy ürünlerini online ortamda satmayı amaçlayan bir e-ticaret sitesidir. Zeytinyağı, salça, zeytin, baharatlar ve diğer doğal köy ürünleri ile kullanıcıların sağlıklı ve organik ürünlere kolay erişimini sağlamayı hedefler.

## Proje Hakkında

Bu proje, Django framework'u kullanarak geliştirilmiş bir e-ticaret sitesidir. Kullanıcılar, ürünleri görüntüleyebilir, sepete ekleyebilir, ve satın alabilirler. Proje, veritabanı yönetimi, kullanıcı yönetimi ve ödeme entegrasyonu gibi temel özellikleri içerir.

### Projede Kullanılan Teknolojiler:
- **Django**: Web framework'ü olarak Django kullanıldı.
- **SQLite**: Veritabanı olarak SQLite kullanıldı (geliştirme ve test amaçlı).
- **HTML/CSS**: Temel sayfa yapısı ve stilizasyon için kullanıldı.
- **JavaScript**: Dinamik içerik ve kullanıcı etkileşimleri için kullanıldı.
- **Git**: Proje sürüm kontrolü için Git kullanıldı.
- **Heroku**: Uygulamanın online platformda çalıştırılması ve sunulması için kullanılması planlanıyor.

### Proje Özellikleri:
- Kullanıcı Kaydı ve Girişi: Kullanıcılar, siteye üye olabilir ve giriş yapabilirler.
- Ürün Yönetimi: Yönetici, ürünleri ekleyip düzenleyebilir.
- Sepet Sistemi: Kullanıcılar ürünleri sepete ekleyebilir ve satın alabilir.
- Ödeme Entegrasyonu: Ödeme entegrasyonu (henüz entegre edilmemiş olabilir).
- İletişim: Kullanıcılar, site ile iletişim kurabilirler.

### Kurulum Talimatları:
Projeyi çalıştırabilmek için aşağıdaki adımları izleyebilirsiniz.

#### 1. Proje Klasörüne Git:
Terminal veya komut satırını açın ve proje klasörüne gidin.
```bash
cd /path/to/evrim-ecommercesite
```

#### 2. Sanal Ortamı Kurun (Opsiyonel):
Python sanal ortamı oluşturun ve etkinleştirin.
```bash
python -m venv myenv
source myenv/bin/activate  # Linux/MacOS
myenv\Scriptsctivate     # Windows
```

#### 3. Bağımlılıkları Yükleyin:
Gerekli paketleri yüklemek için:
```bash
pip install -r requirements.txt
```

#### 4. Veritabanı Migrasyonlarını Uygulayın:
Veritabanı migrasyonlarını uygulayın:
```bash
python manage.py migrate
```

#### 5. Sunucuyu Başlatın:
Django geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

### Katkı Yapma:
Eğer projeye katkı sağlamak isterseniz, aşağıdaki adımları izleyebilirsiniz:
1. Bu projeyi fork'layın.
2. Yeni bir feature branch oluşturun.
3. Yapmak istediğiniz değişiklikleri yapın.
4. Değişikliklerinizi commit ve push edin.
5. Pull request açın.

### Lisans:
Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.

---

Evrim Köy Ürünleri, doğal köy ürünlerinin dijital ortamda satışı için geliştirilmiş, kullanıcı dostu ve güvenli bir platformdur.
