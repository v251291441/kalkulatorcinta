from flask import Flask, render_template, request, url_for, flash, redirect, session
import sqlite3
import datetime
from werkzeug.exceptions import abort

# Fungsi conncect database


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'


# Fungsi hitung dan insert ke database
def hitung():

    # Masukkan data dari form
    namacowok = request.form['namacowok'].lower()
    tanggalcowok = request.form['tanggalcowok']
    namacewek = request.form['namacewek'].lower()
    tanggalcewek = request.form['tanggalcewek']

    # Validasi form
    if not namacowok or not tanggalcowok or not namacewek or not tanggalcewek:
        flash('Mohon isi data dengan lengkap!')
        return redirect(url_for('history'))
    else:

        # Hitung nilai

        # Declare variable
        nilai = 0
        l_namacowok = list(namacowok)
        l_namacewek = list(namacewek)
        combined = namacowok + namacewek

        # Fungsi cek huruf vokal
        def cekvokal(nama):
            if nama[0] in "aiueo":
                return True
            else:
                return False

        # Fungsi cek huruf konsonan
        def cekkonsonan(nama):
            if nama[0] not in "aiueo":
                return True
            else:
                return False

        # Fungsi hitung huruf
        def hitunghuruf(nama):
            return len(nama) - nama.count(" ")

        # Fungsi cek huruf pertama
        def hurufpertama(nama):
            return nama[0]

        # Fungsi cek huruf terakhir
        def hurufterakhir(nama):
            return nama[-1]

        # Fungsi cek jumlah kata
        def jumlahkata(nama):
            return nama.count(" ") + 1

        # Fungsi cek tahun lahir
        def tahunlahir(tanggal):
            return int(datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%Y'))

        # Fungsi cek bulan lahir
        def bulanlahir(tanggal):
            return datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%B')

        # Fungsi cek hari lahir
        def harilahir(tanggal):
            return datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%A')

        # Fungsi cek minggu lahir
        def minggulahir(tanggal):
            return datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%V')

        # Fungsi penjumlahan tanggal lahir
        def jumlahtanggallahir(tanggal):
            return int(datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%Y')) + int(datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%m')) + int(datetime.datetime.strptime(tanggal, '%Y-%m-%d').strftime('%d'))

        # Fungsi cek zodiak
        def zodiak(tgl):
            tanggal = int(datetime.datetime.strptime(
                tgl, '%Y-%m-%d').strftime('%d'))
            bulan = int(datetime.datetime.strptime(
                tgl, '%Y-%m-%d').strftime('%m'))

            if bulan == 12:
                zodiak = 'Sagittarius' if (tanggal < 22) else 'Capricorn'
            elif bulan == 1:
                zodiak = 'Capricorn' if (tanggal < 20) else 'Aquarius'
            elif bulan == 2:
                zodiak = 'Aquarius' if (tanggal < 19) else 'Pisces'
            elif bulan == 3:
                zodiak = 'Pisces' if (tanggal < 21) else 'Aries'
            elif bulan == 4:
                zodiak = 'Aries' if (tanggal < 20) else 'Taurus'
            elif bulan == 5:
                zodiak = 'Taurus' if (tanggal < 21) else 'Gemini'
            elif bulan == 6:
                zodiak = 'Gemini' if (tanggal < 21) else 'Cancer'
            elif bulan == 7:
                zodiak = 'Cancer' if (tanggal < 23) else 'Leo'
            elif bulan == 8:
                zodiak = 'Leo' if (tanggal < 23) else 'Virgo'
            elif bulan == 9:
                zodiak = 'Virgo' if (tanggal < 23) else 'Libra'
            elif bulan == 10:
                zodiak = 'Libra' if (tanggal < 23) else 'Scorpio'
            elif bulan == 11:
                zodiak = 'Scorpio' if (tanggal < 22) else 'Sagittarius'

            return zodiak

        # Cek kecocokan zodiak
        def zodiakcocok(tanggalcowok, tanggalcewek):
            zodiakcowok = zodiak(tanggalcowok)
            zodiakcewek = zodiak(tanggalcewek)
            cocok = False

            if zodiakcowok == 'Aries':
                cocok = True if (zodiakcewek == 'Libra' or zodiakcewek ==
                                 'Virgo' or zodiakcewek == 'Leo') else False
            elif zodiakcowok == 'Taurus':
                cocok = True if (
                    zodiakcewek == 'Libra' or zodiakcewek == 'Aries') else False
            elif zodiakcowok == 'Gemini':
                cocok = True if (zodiakcewek == 'Aquarius' or zodiakcewek ==
                                 'Sagittarius' or zodiakcewek == 'Cancer') else False
            elif zodiakcowok == 'Cancer':
                cocok = True if (zodiakcewek == 'Aquarius' or zodiakcewek ==
                                 'Capricorn' or zodiakcewek == 'Sagittarius') else False
            elif zodiakcowok == 'Leo':
                cocok = True if (zodiakcewek == 'Aries' or zodiakcewek ==
                                 'Gemini' or zodiakcewek == 'Libra') else False
            elif zodiakcowok == 'Virgo':
                cocok = True if (zodiakcewek == 'Scorpio' or zodiakcewek ==
                                 'Aries' or zodiakcewek == 'Libra') else False
            elif zodiakcowok == 'Libra':
                cocok = True if (zodiakcewek == 'Aries' or zodiakcewek ==
                                 'Virgo' or zodiakcewek == 'Taurus') else False
            elif zodiakcowok == 'Scorpio':
                cocok = True if (zodiakcewek == 'Virgo' or zodiakcewek ==
                                 'Aries' or zodiakcewek == 'Pisces') else False
            elif zodiakcowok == 'Sagittarius':
                cocok = True if (zodiakcewek == 'Capricorn' or zodiakcewek ==
                                 'Aquarius' or zodiakcewek == 'Gemini') else False
            elif zodiakcowok == 'Capricorn':
                cocok = True if (zodiakcewek == 'Aquarius' or zodiakcewek ==
                                 'Sagittarius' or zodiakcewek == 'Gemini') else False
            elif zodiakcowok == 'Aquarius':
                cocok = True if (zodiakcewek == 'Capricorn' or zodiakcewek ==
                                 'Sagittarius' or zodiakcewek == 'Gemini') else False
            elif zodiakcowok == 'Pisces':
                cocok = True if (zodiakcewek == 'Aquarius' or zodiakcewek ==
                                 'Cancer' or zodiakcewek == 'Capricorn') else False

            return cocok

        # 1) Gabungan kedua nama mengandung kata TRUE LOVE
        huruf_t = 5 if combined.count("t") >= 1 else 0
        huruf_r = 8 if combined.count("r") >= 1 else 0
        huruf_u = 4 if combined.count("u") >= 1 else 0
        huruf_e = 10 if combined.count(
            "e") >= 2 else 5 if combined.count("e") == 1 else 0
        huruf_l = 8 if combined.count("l") >= 1 else 0
        huruf_o = 3 if combined.count("o") >= 1 else 0
        huruf_v = 2 if combined.count("v") >= 1 else 0
        nilai += huruf_t + huruf_r + huruf_u + huruf_e + huruf_l + huruf_o + huruf_v

        # 2) Huruf pertama kedua nama merupakan huruf vokal atau konsonan
        if (cekvokal(namacowok) == cekvokal(namacewek)) or (cekkonsonan(namacowok) == cekkonsonan(namacewek)):
            nilai += 1.8

        # 3) Jumlah huruf sama
        if hitunghuruf(namacowok) == hitunghuruf(namacewek):
            nilai += 2.7

        # 4) Huruf pertama sama
        if hurufpertama(namacowok) == hurufpertama(namacewek):
            nilai += 3.5

        # 5) Huruf terakhir sama
        if hurufterakhir(namacowok) == hurufterakhir(namacewek):
            nilai += 2.3

        # 6) Jumlah kata sama
        if jumlahkata(namacowok) == jumlahkata(namacewek):
            nilai += 10.9

        # 7) Zodiak sama atau cocok
        if (zodiak(tanggalcowok) == zodiak(tanggalcewek) or zodiakcocok(tanggalcowok, tanggalcewek)):
            nilai += 9.8

        # 8) Bulan lahir sama
        if bulanlahir(tanggalcowok) == bulanlahir(tanggalcewek):
            nilai += 2.2

        # 9) Lahir di minggu yang sama
        if minggulahir(tanggalcowok) == minggulahir(tanggalcewek):
            nilai += 3.6

        # 10) Hari lahir sama
        if harilahir(tanggalcowok) == harilahir(tanggalcewek):
            nilai += 1.4

        # 11) Penjumlahan hari, bulan, tahun sama
        if jumlahtanggallahir(tanggalcowok) == jumlahtanggallahir(tanggalcewek):
            nilai += 1.8

        # 12) Jarak umur maksimal 5 tahun
        if -5 <= tahunlahir(tanggalcowok) - tahunlahir(tanggalcewek) <= 5:
            nilai += 20

        # Fungsi generate teks
        def text(nilai):
            text = ""

            if nilai >= 88:
                text = "Kalian sudah ditakdirkan untuk bersama, saatnya menata masa depan."
            elif nilai >= 78:
                text = "Hubungan kalian layak untuk diperjuangkan, pertahankan yang sudah ada."
            elif nilai >= 70:
                text = "Sebenarnya kalian sudah berada pada hubungan yang tepat, namun kalian harus memupuk benih cinta yang telah tumbuh di antara kalian."
            elif nilai >= 50:
                text = "Saatnya kalian saling mengintrospeksi hubungan kalian karena ada indikasi bahwa hubungan kalian tidak sehat"
            else:
                text = "Hubungan kalian sudah tidak layak untuk diperjuangkan, kalian tidak ditakdirkan untuk bersama lebih lama lagi"

            return text

        hasil = {
            'namacowok': namacowok.title(),
            'tanggalcowok': tanggalcowok,
            'namacewek': namacewek.title(),
            'tanggalcewek': tanggalcewek,
            'nilai': round(nilai, 1),
            'text': text(nilai)
        }

        # Eksekusi
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO loves (namacowok, tanggalcowok, namacewek, tanggalcewek, nilai) VALUES (?, ?, ?, ?, ?)', (namacowok.title(), tanggalcowok, namacewek.title(), tanggalcewek, round(nilai, 1)))
        conn.commit()
        conn.close()

        session['hasil'] = hasil


# Halaman Hasil Perhitungan
@app.route('/result', methods=('GET', 'POST'))
def result():

    hasil = session['hasil']

    if request.method == 'POST':
        hitung()
        return redirect(url_for('result'))

    return render_template('result.html', hasil=hasil)


# Halaman awal (index)
@app.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        hitung()
        return redirect(url_for('result'))

    return render_template('index.html')


# Halaman Hall of Fame
@app.route('/history', methods=('GET', 'POST'))
def history():

    # Ambil data dari database
    conn = get_db_connection()
    loves = conn.execute('SELECT * FROM loves').fetchall()
    conn.close()

    if request.method == 'POST':
        return redirect(url_for('result', hasil=hitung()))

    return render_template('history.html', loves=loves)

# Hapus data


@app.route('/<int:love_id>/delete', methods=('GET',))
def delete(love_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM loves WHERE id = ?', (love_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('history'))
