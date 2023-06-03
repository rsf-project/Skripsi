# Klasifikasi Intent dan Pengenalan Entitas pada Framework RASA Menggunakan Softmax dan Conditional Random Field
Framework RASA menggunakan metode Softmax untuk klasifikasi intent dan Conditional Random Field (CRF) untuk pengenalan entitas adalah chatbot yang digunakan untuk klasifikasi intent dan pengenalan entitas dari pertanyaan yang dimasukkan pengguna, dengan masukkan kepada sistem berupa kalimat tanya atau perintah melalui aplikasi telegram yang di integrasikan pada chatbot melalui telegram webhook. Masukkan berupa pertanyaan seputar sistem akademik Teknik Informatika Universitas Sriwijaya.

# RAW Dataset
Link : https://github.com/adikurniawanid/express-unsribot-api

# Testing On
- RASA Framework 2.8.6
- Python 3.18
- Linux KDE Neon 64 Bit
- RAM 4GB
- Intel Core i3-1005G1 1.2GHz
- NVMe SSD 512GB

# Instalasi RASA Framework Build From Source
- Link Source : https://github.com/RasaHQ/rasa/releases/tag/2.8.6
- Link Instalasi : https://github.com/RasaHQ/rasa

# preparation
Membuat bot baru dari telegram dan mendapatkan username dan bot token
```bash
https://learn.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0
```


# Running RASA
Masuk pada directory dimana RASA di install.
Edit credentials.yml
```bash
telegram:
  access_token: "6228868277:AAGEp0MxdkRIKBciZNPxumAm5bh1Zus54y0"
  verify: "devrasa_bot"
  webhook_url: "https://0275-202-67-43-43.ap.ngrok.io/webhooks/telegram/webhook"
```

