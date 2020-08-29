from core import *
from core.controllers import *


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=True)
