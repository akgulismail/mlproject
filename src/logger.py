import logging
import os
from datetime import datetime

##Log File Name
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#os'deki dizininin altına logs klasörü açar onun altına log dosyasını ekler.(../logs/05252023095900.log)
#exist_ok Dosya varsa içerisine ekleme yapar
#dosya içerisine yazılacak format
#logging.INFO ekrana output messagı yazdırır


logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

