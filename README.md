# Flask AdminLTE 3

Repository ini merupakan template dasar penggunaan  **Bootstrap AdminLTE 3** dengan **Flask**  untuk membangun dashboard yang rapi.

## 📌 Fitur
- Menggunakan **Flask** sebagai backend
- Template UI berbasis **AdminLTE 3** (Bootstrap 4)
- Struktur template modular dengan **header, sidebar, footer**
- Mudah dikembangkan dan diperluas

## 🛠️ Instalasi

### 1. Clone Repository
```sh
git clone https://github.com/harunid12/baseFlaskAdmin.git
cd repository
```

### 2. Buat dan Aktifkan Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```sh
pip install flask
```

### 4. Jalankan Aplikasi
```sh
python main.py
```
Akses aplikasi di `http://127.0.0.1:5000/`

## 📂 Struktur Folder
```
/project-root
│── static/                # File CSS, JS, AdminLTE assets
│── templates/
│   ├── layouts/
│   │   ├── base.html      # Template utama
│   │   ├── header.html    # Header
│   │   ├── sidebar.html   # Sidebar
│   │   ├── footer.html    # Footer
│   ├── dashboard/
│   │   ├── view.html      # Halaman dashboard
│── main.py                # File utama Flask
│── requirements.txt        # Dependensi
│── README.md               # Dokumentasi
```

## 🔗 Referensi
- [Flask Documentation](https://flask.palletsprojects.com/)
- [AdminLTE 3](https://adminlte.io/)

