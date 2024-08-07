from flask import Flask, url_for, request, redirect, render_template_string
import random
import string
import time
import datetime

app = Flask(__name__)

fakta = [
    'Kecanduan shopping online dapat membuat uang habis',
    'Kecanduan game online dapat membuat waktu habis',
    'Kecanduan sosmed membuat hidupmu percuma',
    'Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka',
    'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
    'Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan',
    'Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja',
    'Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati',
    'Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten',
    'Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita',
    'Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini'
]

gambar_urls = [
    'gambar1.jpg',
    'gambar2.jpg',
    'gambar3.jpg',
    'gambar4.jpg',
]

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Halaman Utama</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #241f32;
                margin: 0;
                padding: 0;
            }
            h1 {
                text-align: center;
                padding: 20px;
                background-color: #6a5bc2;
                color: white;
                margin: 0;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin: 10px 0;
            }
            a {
                display: block;
                width: 300px;
                margin: 10px auto;
                padding: 10px;
                background-color: #f6f389;
                color: #241f32;
                text-decoration: none;
                text-align: center;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            a:hover {
                background-color: #ec6083;
                color: #7ae284;
            }
            .container {
                width: 80%;
                margin: auto;
                overflow: hidden;
            }
        </style>
    </head>
    <body>
        <h1>INI ADALAH HALAMAN UTAMA</h1>
        <div class="container">
            <ul>
                <li><a href="/random_facts">Klik untuk melihat fakta acak</a></li>
                <li><a href="/lempar_koin">Klik untuk lempar koin</a></li>
                <li><a href="/generator_kata_sandi">Klik untuk generator kata sandi acak</a></li>
                <li><a href="/gambar_acak">Klik untuk melihat gambar acak</a></li>
                <li><a href="/angka_acak">Klik untuk melihat angka acak</a></li>
                <li><a href="/pilih_warna">Klik untuk memilih warna acak</a></li>
                <li><a href="/waktu_sekarang">Klik untuk melihat waktu sekarang</a></li>
                <li><a href="/quote_acak">Klik untuk melihat quote acak</a></li>
                <li><a href="/tebak_angka">Klik untuk menebak angka</a></li>
                <li><a href="/fakta_unik">Klik untuk melihat fakta unik</a></li>
                <li><a href="/jumlah_kata">Klik untuk menghitung jumlah kata dalam kalimat</a></li>
                <li><a href="/konversi_suhu">Klik untuk konversi suhu</a></li>
                <li><a href="/kalkulator_umur">Klik untuk menghitung umur</a></li>
                <li><a href="/tebak_angka_game">Klik untuk bermain tebak angka</a></li>
                <li><a href="/uji_kepribadian">Klik untuk uji kepribadian</a></li>
            </ul>
        </div>
    </body>
    </html>
    '''


@app.route('/random_facts')
def random_facts():
    fact = random.choice(fakta)
    return f"<h1>Fakta Acak</h1><br><p>{fact}</p><br><a href='/'>Back to Home</a>"

@app.route('/lempar_koin')
def lempar_koin():
    hasil = random.choice(['Kepala', 'Ekor'])
    return f"<h1>Hasil Lempar Koin: {hasil}</h1><br><a href='/'>Back to Home</a>"

@app.route('/generator_kata_sandi')
def generator_kata_sandi():
    panjang = 12
    karakter = string.ascii_letters + string.digits + string.punctuation
    kata_sandi = ''.join(random.choice(karakter) for _ in range(panjang))
    return f"<h1>Kata Sandi Acak</h1><br><p>{kata_sandi}</p><br><a href='/'>Back to Home</a>"

@app.route('/gambar_acak')
def gambar_acak():
    gambar_url = random.choice(gambar_urls)
    full_url = url_for('static', filename='img/' + gambar_url)
    return f"<h1>Gambar Acak</h1><br><img src='{full_url}' alt='Gambar Acak'><br><a href='/'>Back to Home</a>"

@app.route('/angka_acak')
def angka_acak():
    angka = random.randint(1, 100)
    return f"<h1>Angka Acak</h1><br><p>{angka}</p><br><a href='/'>Back to Home</a>"

@app.route('/pilih_warna')
def pilih_warna():
    warna = [
        "Merah", "Hijau", "Biru", "Kuning", "Ungu", "Hitam", "Putih", "Cokelat", "Oranye", "Abu-abu",
        "Emas", "Perak", "Pink", "Turquoise", "Magenta", "Lavender", "Zaitun", "Smaragd", "Maroon", "Teal"
    ]
    warna_acak = random.choice(warna)
    return f"<h1>Warna Acak</h1><br><p>{warna_acak}</p><br><a href='/'>Back to Home</a>"

@app.route('/waktu_sekarang')
def waktu_sekarang():
    return '''
        <h1>Waktu Sekarang</h1>
        <p id="waktu"></p>
        <script>
            function updateTime() {
                var now = new Date();
                var waktuString = now.getFullYear() + '-' +
                                  ('0' + (now.getMonth()+1)).slice(-2) + '-' +
                                  ('0' + now.getDate()).slice(-2) + ' ' +
                                  ('0' + now.getHours()).slice(-2) + ':' +
                                  ('0' + now.getMinutes()).slice(-2) + ':' +
                                  ('0' + now.getSeconds()).slice(-2);
                document.getElementById('waktu').innerHTML = waktuString;
            }
            setInterval(updateTime, 1000);
            updateTime();
        </script>
        <br><a href='/'>Back to Home</a>
    '''

@app.route('/quote_acak')
def quote_acak():
    quotes = [
        "Hidup adalah perjuangan.",
        "Cinta adalah kekuatan terbesar di dunia.",
        "Kegagalan adalah kesempatan untuk memulai lagi dengan lebih cerdas.",
        "Kesuksesan tidak datang kepada orang yang menunggu.",
        "Kebahagiaan bukanlah sesuatu yang siap dibuat. Itu berasal dari tindakan Anda sendiri.",
        "Hidup adalah 10% apa yang terjadi pada kita dan 90% bagaimana kita bereaksi terhadapnya.",
        "Jangan takut untuk menyerah pada yang baik untuk pergi untuk yang hebat.",
        "Jangan biarkan apa yang tidak bisa Anda lakukan mengganggu apa yang bisa Anda lakukan.",
        "Anda tidak pernah terlalu tua untuk menetapkan tujuan lain atau untuk memimpikan mimpi baru.",
        "Satu-satunya cara untuk melakukan pekerjaan hebat adalah mencintai apa yang Anda lakukan.",
        "Kesuksesan tidak selalu tentang kebesaran. Ini tentang konsistensi.",
        "Motivasi adalah apa yang membuat Anda memulai. Kebiasaan adalah apa yang membuat Anda terus berjalan.",
        "Jangan menunggu waktu yang sempurna, ambil waktu dan buat itu sempurna.",
        "Anda adalah satu-satunya orang di bumi yang bisa menggunakan kemampuan Anda.",
        "Kegagalan adalah bumbu yang memberi kesuksesan rasanya.",
        "Kesuksesan berjalan dari kegagalan ke kegagalan tanpa kehilangan antusiasme.",
        "Bekerja keras dalam diam, biarkan kesuksesan membuat kebisingan.",
        "Hidup ini singkat. Waktu itu cepat. Tidak ada replay, tidak ada rewind, jadi nikmati setiap momen seperti yang datang.",
        "Jangan biarkan kemarin mengambil terlalu banyak hari ini.",
        "Hidup bukan tentang menunggu badai berlalu, tetapi belajar menari di tengah hujan."
    ]
    quote = random.choice(quotes)
    return f"<h1>Quote Acak</h1><br><p>{quote}</p><br><a href='/'>Back to Home</a>"

@app.route('/tebak_angka')
def tebak_angka():
    angka = random.randint(1, 10)
    return f"<h1>Tebak Angka</h1><br><p>Angka yang harus ditebak adalah {angka}</p><br><a href='/'>Back to Home</a>"


@app.route('/fakta_unik')
def fakta_unik():
    fakta_unik = [
        "Otak manusia memiliki berat sekitar 1,4 kilogram.",
        "Madu adalah satu-satunya makanan yang tidak pernah basi.",
        "Gajah adalah satu-satunya hewan yang tidak bisa melompat.",
        "Satu-satunya huruf yang tidak digunakan dalam nama negara bagian AS adalah Q.",
        "Jantung manusia berdetak sekitar 100.000 kali sehari.",
        "Kupu-kupu merasakan dengan kaki mereka.",
        "Seekor siput bisa tidur selama tiga tahun.",
        "Hati manusia dapat memompa darah sejauh 96.000 kilometer setiap hari.",
        "Tulang paha manusia lebih kuat daripada beton.",
        "Lidah biru-hitam beruang kutub berfungsi untuk menyerap lebih banyak panas dari matahari.",
        "Bayi lahir dengan 300 tulang, tetapi orang dewasa hanya memiliki 206.",
        "Otak manusia terdiri dari sekitar 75% air.",
        "Rambut manusia tumbuh sekitar 6 inci per tahun.",
        "Mata manusia dapat membedakan sekitar 10 juta warna.",
        "Sidik jari koala hampir tidak bisa dibedakan dari sidik jari manusia.",
        "Rata-rata manusia berjalan sekitar 100.000 mil dalam seumur hidup.",
        "Satu sendok teh madu adalah hasil dari kerja keras sekitar 12 lebah.",
        "Tawa dapat meningkatkan sistem kekebalan tubuh Anda.",
        "Suhu permukaan Matahari adalah sekitar 5.500 derajat Celsius.",
        "Burung Hummingbird adalah satu-satunya burung yang bisa terbang mundur."
    ]
    fakta = random.choice(fakta_unik)
    return f"<h1>Fakta Unik</h1><br><p>{fakta}</p><br><a href='/'>Back to Home</a>"

@app.route('/jumlah_kata', methods=['GET', 'POST'])
def jumlah_kata():
    if request.method == 'POST':
        kalimat = request.form['kalimat']
        return redirect(url_for('hasil_jumlah_kata', kalimat=kalimat))
    return '''
        <h1>Hitung Jumlah Kata</h1>
        <form method="post" action="/jumlah_kata">
            <label for="kalimat">Masukkan kalimat:</label><br>
            <input type="text" id="kalimat" name="kalimat"><br><br>
            <input type="submit" value="Hitung">
        </form>
        <br><a href='/'>Back to Home</a>
    '''

@app.route('/hasil_jumlah_kata')
def hasil_jumlah_kata():
    kalimat = request.args.get('kalimat', '')
    kata = kalimat.split()
    jumlah = len(kata)
    return f"<h1>Jumlah Kata</h1><br><p>Kalimat: '{kalimat}'</p><br><p>Jumlah kata: {jumlah}</p><br><a href='/'>Back to Home</a>"


@app.route('/konversi_suhu', methods=['GET', 'POST'])
def konversi_suhu():
    if request.method == 'POST':
        suhu = float(request.form['suhu'])
        satuan = request.form['satuan']
        if satuan == 'c_to_f':
            hasil = (suhu * 9/5) + 32
            satuan_hasil = 'Fahrenheit'
        else:
            hasil = (suhu - 32) * 5/9
            satuan_hasil = 'Celsius'
        return f"<h1>Hasil Konversi</h1><br><p>{suhu} derajat dalam {satuan_hasil} adalah {hasil:.2f}</p><br><a href='/konversi_suhu'>Kembali</a><br><a href='/'>Back to Home</a>"
    return '''
        <h1>Konversi Suhu</h1>
        <form method="post" action="/konversi_suhu">
            <label for="suhu">Masukkan suhu:</label><br>
            <input type="text" id="suhu" name="suhu"><br><br>
            <input type="radio" id="c_to_f" name="satuan" value="c_to_f" checked>
            <label for="c_to_f">Celsius ke Fahrenheit</label><br>
            <input type="radio" id="f_to_c" name="satuan" value="f_to_c">
            <label for="f_to_c">Fahrenheit ke Celsius</label><br><br>
            <input type="submit" value="Konversi">
        </form>
        <br><a href='/'>Back to Home</a>
    '''

@app.route('/kalkulator_umur', methods=['GET', 'POST'])
def kalkulator_umur():
    if request.method == 'POST':
        tahun = int(request.form['tahun'])
        bulan = int(request.form['bulan'])
        hari = int(request.form['hari'])
        tanggal_lahir = datetime.date(tahun, bulan, hari)
        hari_ini = datetime.date.today()
        umur = hari_ini - tanggal_lahir
        tahun_umur = umur.days // 365
        bulan_umur = (umur.days % 365) // 30
        hari_umur = (umur.days % 365) % 30
        return f"<h1>Hasil Kalkulator Umur</h1><br><p>Umur Anda adalah {tahun_umur} tahun, {bulan_umur} bulan, dan {hari_umur} hari.</p><br><a href='/kalkulator_umur'>Kembali</a><br><a href='/'>Back to Home</a>"
    return '''
        <h1>Kalkulator Umur</h1>
        <form method="post" action="/kalkulator_umur">
            <label for="tahun">Masukkan tahun lahir:</label><br>
            <input type="text" id="tahun" name="tahun"><br><br>
            <label for="bulan">Masukkan bulan lahir:</label><br>
            <input type="text" id="bulan" name="bulan"><br><br>
            <label for="hari">Masukkan hari lahir:</label><br>
            <input type="text" id="hari" name="hari"><br><br>
            <input type="submit" value="Hitung Umur">
        </form>
        <br><a href='/'>Back to Home</a>
    '''

@app.route('/tebak_angka_game', methods=['GET', 'POST'])
def tebak_angka_game():
    angka_rahasia = random.randint(1, 50)  # Angka acak setiap kali halaman dimuat
    if request.method == 'POST':
        try:
            tebakan = int(request.form['tebakan'])
        except ValueError:
            return f"<h1>Masukkan angka yang valid!</h1><br><a href='/tebak_angka_game'>Coba Lagi</a><br><a href='/'>Back to Home</a>"
        if tebakan < angka_rahasia:
            pesan = "Tebakan Anda terlalu rendah!"
        elif tebakan > angka_rahasia:
            pesan = "Tebakan Anda terlalu tinggi!"
        else:
            pesan = "Tebakan Anda benar!"
        return f"<h1>Hasil Tebak Angka</h1><br><p>{pesan} Angka rahasia adalah {angka_rahasia}.</p><br><a href='/tebak_angka_game'>Coba Lagi</a><br><a href='/'>Back to Home</a>"
    return '''
        <h1>Tebak Angka</h1>
        <form method="post" action="/tebak_angka_game">
            <label for="tebakan">Masukkan tebakan (1-50):</label><br>
            <input type="text" id="tebakan" name="tebakan"><br><br>
            <input type="submit" value="Tebak">
        </form>
        <br><a href='/'>Back to Home</a>
    '''

@app.route('/uji_kepribadian', methods=['GET', 'POST'])
def uji_kepribadian():
    if request.method == 'POST':
        jawaban1 = request.form['pertanyaan1']
        jawaban2 = request.form['pertanyaan2']
        jawaban3 = request.form['pertanyaan3']
        jawaban4 = request.form['pertanyaan4']
        jawaban5 = request.form['pertanyaan5']
        jawaban6 = request.form['pertanyaan6']
        jawaban7 = request.form['pertanyaan7']
        jawaban8 = request.form['pertanyaan8']
        jawaban9 = request.form['pertanyaan9']
        jawaban10 = request.form['pertanyaan10']

        kepribadian = "<h1>Hasil Uji Kepribadian</h1><br><p>"

        if jawaban1 == 'a':
            kepribadian += "Anda adalah seorang yang sangat kreatif. "
        elif jawaban1 == 'b':
            kepribadian += "Anda adalah seorang yang sangat logis. "
        elif jawaban1 == 'c':
            kepribadian += "Anda adalah seorang yang sangat empatik. "

        if jawaban2 == 'a':
            kepribadian += "Anda suka berpetualang dan mencoba hal-hal baru. "
        elif jawaban2 == 'b':
            kepribadian += "Anda lebih suka berada di rumah dan menikmati kenyamanan rumah. "
        elif jawaban2 == 'c':
            kepribadian += "Anda suka bertemu orang baru dan bersosialisasi. "

        if jawaban3 == 'a':
            kepribadian += "Gaya hidup Anda sangat teratur dan terorganisir. "
        elif jawaban3 == 'b':
            kepribadian += "Anda adalah orang yang spontan dan suka kejutan. "
        elif jawaban3 == 'c':
            kepribadian += "Anda memiliki gaya hidup yang santai dan tidak terburu-buru. "

        if jawaban4 == 'a':
            kepribadian += "Anda menghargai waktu sendirian untuk refleksi diri. "
        elif jawaban4 == 'b':
            kepribadian += "Anda merasa energik setelah bersosialisasi dengan banyak orang. "
        elif jawaban4 == 'c':
            kepribadian += "Anda menyukai keseimbangan antara waktu sendiri dan bersosialisasi. "

        if jawaban5 == 'a':
            kepribadian += "Anda cenderung memikirkan secara mendalam sebelum mengambil keputusan. "
        elif jawaban5 == 'b':
            kepribadian += "Anda sering mengikuti intuisi Anda saat mengambil keputusan. "
        elif jawaban5 == 'c':
            kepribadian += "Anda menggabungkan logika dan intuisi dalam mengambil keputusan. "

        if jawaban6 == 'a':
            kepribadian += "Anda menikmati tantangan dan suka mencari solusi kreatif. "
        elif jawaban6 == 'b':
            kepribadian += "Anda merasa nyaman dengan rutinitas dan stabilitas. "
        elif jawaban6 == 'c':
            kepribadian += "Anda fleksibel dan bisa beradaptasi dengan berbagai situasi. "

        if jawaban7 == 'a':
            kepribadian += "Anda sangat detail-oriented dan memperhatikan hal-hal kecil. "
        elif jawaban7 == 'b':
            kepribadian += "Anda lebih fokus pada gambaran besar dan tujuan akhir. "
        elif jawaban7 == 'c':
            kepribadian += "Anda memiliki keseimbangan antara detail dan gambaran besar. "

        if jawaban8 == 'a':
            kepribadian += "Anda suka merencanakan segala sesuatu jauh-jauh hari. "
        elif jawaban8 == 'b':
            kepribadian += "Anda lebih suka menjalani hidup secara spontan. "
        elif jawaban8 == 'c':
            kepribadian += "Anda kadang-kadang merencanakan dan kadang-kadang spontan. "

        if jawaban9 == 'a':
            kepribadian += "Anda merasa tenang saat berada di alam. "
        elif jawaban9 == 'b':
            kepribadian += "Anda mendapatkan energi dari hiruk-pikuk kota. "
        elif jawaban9 == 'c':
            kepribadian += "Anda menikmati keduanya tergantung suasana hati. "

        if jawaban10 == 'a':
            kepribadian += "Anda suka bekerja dalam tim dan berkolaborasi dengan orang lain. "
        elif jawaban10 == 'b':
            kepribadian += "Anda lebih suka bekerja sendiri dan mandiri. "
        elif jawaban10 == 'c':
            kepribadian += "Anda fleksibel dan bisa bekerja baik dalam tim maupun sendiri. "

        kepribadian += "</p><br><a href='/uji_kepribadian'>Coba Lagi</a><br><a href='/'>Back to Home</a>"

        return kepribadian

    return '''
        <h1>Uji Kepribadian</h1>
        <form method="post" action="/uji_kepribadian">
            <p>1. Apa yang paling menggambarkan diri Anda?</p>
            <input type="radio" id="a" name="pertanyaan1" value="a" required>
            <label for="a">Kreatif</label><br>
            <input type="radio" id="b" name="pertanyaan1" value="b">
            <label for="b">Logis</label><br>
            <input type="radio" id="c" name="pertanyaan1" value="c">
            <label for="c">Empatik</label><br><br>

            <p>2. Apa yang paling Anda nikmati?</p>
            <input type="radio" id="a" name="pertanyaan2" value="a" required>
            <label for="a">Berpetualang</label><br>
            <input type="radio" id="b" name="pertanyaan2" value="b">
            <label for="b">Di rumah</label><br>
            <input type="radio" id="c" name="pertanyaan2" value="c">
            <label for="c">Bertemu orang baru</label><br><br>

            <p>3. Bagaimana Anda menggambarkan gaya hidup Anda?</p>
            <input type="radio" id="a" name="pertanyaan3" value="a" required>
            <label for="a">Teratur</label><br>
            <input type="radio" id="b" name="pertanyaan3" value="b">
            <label for="b">Spontan</label><br>
            <input type="radio" id="c" name="pertanyaan3" value="c">
            <label for="c">Santai</label><br><br>

            <p>4. Apa yang Anda sukai?</p>
            <input type="radio" id="a" name="pertanyaan4" value="a" required>
            <label for="a">Waktu sendirian</label><br>
            <input type="radio" id="b" name="pertanyaan4" value="b">
            <label for="b">Bersosialisasi</label><br>
            <input type="radio" id="c" name="pertanyaan4" value="c">
            <label for="c">Keseimbangan keduanya</label><br><br>

            <p>5. Bagaimana Anda membuat keputusan?</p>
            <input type="radio" id="a" name="pertanyaan5" value="a" required>
            <label for="a">Memikirkan secara mendalam</label><br>
            <input type="radio" id="b" name="pertanyaan5" value="b">
            <label for="b">Mengikuti intuisi</label><br>
            <input type="radio" id="c" name="pertanyaan5" value="c">
            <label for="c">Menggabungkan logika dan intuisi</label><br><br>

            <p>6. Bagaimana Anda menghadapi tantangan?</p>
            <input type="radio" id="a" name="pertanyaan6" value="a" required>
            <label for="a">Menikmati tantangan</label><br>
            <input type="radio" id="b" name="pertanyaan6" value="b">
            <label for="b">Mencari rutinitas</label><br>
            <input type="radio" id="c" name="pertanyaan6" value="c">
            <label for="c">Fleksibel dan adaptif</label><br><br>

            <p>7. Apa yang Anda perhatikan?</p>
            <input type="radio" id="a" name="pertanyaan7" value="a" required>
            <label for="a">Detail</label><br>
            <input type="radio" id="b" name="pertanyaan7" value="b">
            <label for="b">Gambaran besar</label><br>
            <input type="radio" id="c" name="pertanyaan7" value="c">
            <label for="c">Keseimbangan keduanya</label><br><br>

            <p>8. Bagaimana Anda merencanakan?</p>
            <input type="radio" id="a" name="pertanyaan8" value="a" required>
            <label for="a">Merencanakan jauh-jauh hari</label><br>
            <input type="radio" id="b" name="pertanyaan8" value="b">
            <label for="b">Secara spontan</label><br>
            <input type="radio" id="c" name="pertanyaan8" value="c">
            <label for="c">Kombinasi keduanya</label><br><br>

            <p>9. Dimana Anda merasa tenang?</p>
            <input type="radio" id="a" name="pertanyaan9" value="a" required>
            <label for="a">Di alam</label><br>
            <input type="radio" id="b" name="pertanyaan9" value="b">
            <label for="b">Di kota</label><br>
            <input type="radio" id="c" name="pertanyaan9" value="c">
            <label for="c">Tergantung suasana hati</label><br><br>

            <p>10. Bagaimana Anda bekerja?</p>
            <input type="radio" id="a" name="pertanyaan10" value="a" required>
            <label for="a">Dalam tim</label><br>
            <input type="radio" id="b" name="pertanyaan10" value="b">
            <label for="b">Sendiri</label><br>
            <input type="radio" id="c" name="pertanyaan10" value="c">
            <label for="c">Fleksibel</label><br><br>

            <input type="submit" value="Lihat Hasil">
        </form>
        <br><a href='/'>Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
