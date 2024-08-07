# Impor
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variabel yang memungkinkan penghitungan konsumsi energi peralatan
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')
# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Halaman ketiga
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Perhitungan
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Formulir
@app.route('/form')
def form():
    return render_template('form.html')

#Hasil formulir
@app.route('/submit', methods=['POST'])
def submit_form():
    # Mendeklarasikan variabel untuk pengumpulan data
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']
    file = request.form['file']
    number = request.form['number']
    password = request.form['password']



    with open('data.txt', 'a') as f:
        f.write(f'name: {name}\n')
        f.write(f'email: {email}\n')
        f.write(f'address: {address}\n')
        f.write(f'date: {date}\n')
        f.write(f'file: {file}\n')
        f.write(f'number: {number}\n')
        f.write(f'password: {password}\n')
        f.write('==============\n')

    # Anda dapat menyimpan data Anda atau mengirimkannya melalui email
    return render_template('form_result.html', 
                           # Tempatkan variabel di sini
                           name=name,
                           email=email,
                           address=address,
                           date=date,
                           file=file,
                           number=number,
                           password=password
                           )

app.run(debug=True)
