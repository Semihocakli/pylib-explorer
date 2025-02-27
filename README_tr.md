# PyLib Explorer

PyLib Explorer, Python kütüphanelerini keşfetmek için LLM (Dil Modeli) destekli bir araçtır. Bu kütüphane, rastgele seçilen veya belirtilen Python paketleri hakkında kapsamlı README.md dosyaları oluşturarak, geliştiricilerin yeni kütüphaneleri anlamalarına ve uygulamalarına yardımcı olur.

## Özellikler

- 🔍 Rastgele Python kütüphanesi keşfi
- 🤖 OpenAI ve Claude LLM entegrasyonları
- 📚 Detaylı README.md dosyaları oluşturma
- 🔧 Kod örnekleri ve kullanım senaryoları
- 📊 Popülerlik bazlı filtreleme
- 🧩 Kullanımı kolay API ve CLI
- 🌍 Çoklu dil desteği (istediğiniz dilde README oluşturma)

## Kurulum

```bash
pip install pylib-explorer
```

## Hızlı Başlangıç

### Python Kodu İçinde Kullanım

```python
from pylib_explorer.core import LibExplorer

# API anahtarınızı doğrudan sağlayabilir veya çevre değişkeni kullanabilirsiniz
# Varsayılan dil İngilizce'dir (language="en")
explorer = LibExplorer(api_key="your_api_key_here", provider="openai", language="tr")

# Rastgele bir paket hakkında README oluşturun
readme_content = explorer.generate_readme()
print(f"README dosyası oluşturuldu: {explorer.output_dir}")

# veya belirli bir paket için:
readme_content = explorer.generate_readme(package_name="requests")
```

### Komut Satırı Kullanımı

**Rastgele bir kütüphane keşfetmek için:**

```bash
# OpenAI API anahtarınızı çevre değişkeni olarak ayarlayın
export OPENAI_API_KEY=your_api_key_here

# Rastgele bir kütüphane keşfedin (varsayılan dil: İngilizce)
pylib-explorer

# Türkçe dilinde keşfedin
pylib-explorer --language tr

# Almanca dilinde keşfedin
pylib-explorer --language de
```

**Belirli bir kütüphaneyi keşfetmek için:**

```bash
# İngilizce (varsayılan)
pylib-explorer --package requests

# Türkçe
pylib-explorer --package requests --language tr
```

**Claude API kullanmak için:**

```bash
export ANTHROPIC_API_KEY=your_anthropic_api_key

pylib-explorer --provider claude --package pandas --language fr
```

## Komut Satırı Seçenekleri

```
usage: pylib-explorer [-h] [--package PACKAGE] [--provider {openai,claude}]
                      [--api-key API_KEY] [--output-dir OUTPUT_DIR]
                      [--min-downloads MIN_DOWNLOADS] [--language LANGUAGE]
                      [--verbose]

Seçenekler:
  -h, --help            Bu yardım mesajını göster ve çık
  --package PACKAGE, -p PACKAGE
                        Keşfedilecek Python paketinin adı. Belirtilmezse rastgele bir paket seçilir.
  --provider {openai,claude}, -m {openai,claude}
                        Kullanılacak LLM sağlayıcısı ('openai' veya 'claude').
  --api-key API_KEY, -k API_KEY
                        LLM sağlayıcısı için API anahtarı. Belirtilmezse çevre değişkeninden alınır.
  --output-dir OUTPUT_DIR, -o OUTPUT_DIR
                        README dosyalarının kaydedileceği dizin.
  --min-downloads MIN_DOWNLOADS, -d MIN_DOWNLOADS
                        Rastgele seçim için minimum indirme sayısı filtresi.
  --language LANGUAGE, -l LANGUAGE
                        README içeriğinin oluşturulacağı dil (ör: 'en', 'tr', 'fr', 'de', vb.)
  --verbose, -v         Ayrıntılı log çıktısı modunu etkinleştirir.
```

## Desteklenen Diller

PyLib Explorer, LLM'lerin desteklediği herhangi bir dilde README oluşturabilir. Dil seçeneğini belirtmek için:

- ISO dil kodu kullanabilirsiniz: `en`, `tr`, `fr`, `de`, `es`, `it`, vb.
- Veya tam dil adı kullanabilirsiniz: `English`, `Türkçe`, `Français`, `Deutsch`, vb.

Varsayılan dil İngilizce'dir (`en`).

### Dil Seçeneği Nasıl Çalışır?

PyLib Explorer, belirttiğiniz dili LLM'e açık ve güçlü talimatlarla iletir. İşte bu nasıl çalışır:

1. Dil seçeneğiniz (`tr`, `en` gibi kısa kodlar) tam dil adlarına dönüştürülür
2. LLM'e gönderilen komut isteminde şu bilgiler yer alır:
   - Giriş kısmında: "ÖNEMLİ: Bu README dosyasını {dil} dilinde hazırlamalısın!"
   - Çıkış kısmında: "TEKRAR HATIRLATMA: Tüm içerik {dil} dilinde olmalıdır! Bu çok önemlidir."
3. Bu güçlü talimatlar, LLM'in belirtilen dilde içerik üretmesini sağlar

Belirli bir dilde istediğiniz halde farklı bir dilde README üretiliyorsa, lütfen GitHub issues üzerinden bildiriniz.

## API Anahtarlarını Ayarlama

PyLib Explorer, OpenAI ve Claude API'leri için anahtarlar gerektirir. Bu anahtarları şu şekilde sağlayabilirsiniz:

1. **Çevre Değişkenleri:** `OPENAI_API_KEY` veya `ANTHROPIC_API_KEY` çevre değişkenlerini ayarlayın.
2. **Doğrudan Parametre:** API anahtarlarını doğrudan code veya CLI aracılığıyla sağlayın.
3. **.env Dosyası:** Projenizin kök dizininde bir `.env` dosyası oluşturun:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

## Geliştirme

### Gereksinimler

- Python 3.7+
- OpenAI ve/veya Anthropic API anahtarları

### Kurulum

```bash
git clone https://github.com/username/pylib-explorer.git
cd pylib-explorer
pip install -e ".[dev]"
```

### Testleri Çalıştırma

```bash
pytest
```

## Lisans

MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

## İletişim

Sorularınız veya geri bildirimleriniz için [GitHub Issues](https://github.com/username/pylib-explorer/issues) kullanabilirsiniz. 