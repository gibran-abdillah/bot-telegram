from core import *
from .otak import *
from core.tools.curang import *


# inti class 
my_session = requests.Session()
my_session.headers.update({'User-Agent':'Mozilla'})
 
 
class bot_gibran:
    def __init__(self,data_json=None,chat_id=None,pesan=None,logika=None,file_id=None,poto=None):
        self.data_json = data_json
        self.chat_id = chat_id
        self.pesan = pesan
        self.logika = logika
        self.file_id = file_id
        self.poto = poto
        
    # send message function
    def send_message(self,id,pesan):
        data = {'chat_id':id,
        'text':pesan
        }
        rr = my_session.post(my_url+'/sendMessage',data=data) # reply a message 
        
    def download_file(self,file_id,chat_id):
        get_f = my_session.get(my_url+'/getFile?file_id='+file_id).json()
        file_path = get_f['result']['file_path']
        donlod = my_session.get('https://api.telegram.org/file/{}/{}'.format(bot_token,file_path)).text
        nama_file = file_path.split('/')[-1]
        open(nama_file,'w').write(donlod)
        gibran_curang(nama_file).anjay_curang(nama_file)
        self.sendPhoto(poto='gibran.jpg',chat_id=chat_id)
        
    
    def sendPhoto(self,poto,chat_id):
        data = {'chat_id':chat_id,
                 'caption':'result ..'}
        files = {'photo':open(poto,'rb')}
        self.send_message(id=chat_id,pesan='Sedang mengupload file anda')
        pp = my_session.post(my_url+'/sendPhoto',data=data,files=files)
        print(pp.text)


    def check_update(self,data_json):
        chat_id = data_json['message']['chat']['id']
        if 'new_chat_member' in str(data_json):
           mem_baru = data_json['message']['new_chat']['first_name'] # mendapatkan nama depan member 
           self.send_message(id=chat_id,pesan='Halo, saya adalah bot')

        elif 'mime_type' in str(data_json):
            print(data_json)
            file_id = data_json['message']['document']['file_id']
            if data_json['message']['document']['mime_type'] == 'text/plain':
                self.send_message(id=chat_id,pesan='File anda sedang di proses ...')
                self.download_file(file_id=file_id,chat_id=chat_id)
            else:
                self.send_message(id=chat_id,pesan='Bot hanya menerima file dengan extension .txt')

        else:
           chat_id = data_json['message']['chat']['id']
           isi_pesan = data_json['message']['text']
           print(data_json) # menampilkan di log 
           self.send_message(id=chat_id,pesan=membersihkan(isi_pesan))
        
# end inti class



@app.route('/',methods=['GET','POST'])

def index_route():
    if request.method == 'POST': # kenapa post? karena dari telegram nya, kalo ada pesan. auto post data ke webhook
        data_json = request.get_json() # get data json
        bot_gibran(data_json=data_json).check_update(data_json)
        return 'OKE'
    else:
        return "ini adalaah page index bot" # ganti pake template ..