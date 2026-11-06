SWING LONG ARASTIRMA - TOPLAM ISLEM MALIYETI %0,30

Kaynak: xhqing/Swing, kullanicinin sagladigi ZIP.
Yalnizca arastirma; gercek emir veya broker baglantisi yok.

Orijinal engine/backtest.py icinde US maliyeti 3 bps/yon idi.
Bu pakette US maliyeti 15 bps/yon olarak degistirildi.
Alis %0,15 + satis %0,15 = toplam yaklasik %0,30.
Trend stratejisinin kurallari korunmustur.

ONEMLI: Kaynak ZIP icinde engine/data_cache/*.parquet fiyat verileri YOK.
Bu nedenle yalnizca bu ZIP ile 20 yillik backtest CALISMAZ.
Orijinal proje Futu OpenD ile veri toplar veya GitHub Release
veri snapshot restore islevini tarif eder. Veri kaynagi
dogrulanmadan performans sonucu uretmeyin.

Veri elde edilip engine/data_cache/ altina dogru formatta
yerlestirildikten sonra: 
  cd swing_research/trend
  python backtest.py --scheme 1

Gereken Python paketleri veri kaynagina gore degisir.
README'deki raporlanmis performans bagimsiz olarak dogrulanmamistir.

Dikkat: Orijinal strateji 37 enstruman listesinde SPY, QQQ, DIA,
IWM ETF'lerini de barindirir; 37'si de tekil sirket hissesi degildir.
