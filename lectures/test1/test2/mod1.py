import logging
logging.basicConfig(filename='exception.log',level=logging.INFO,format='%(asctime)s - %(message)s')

def even(range_no):
    try:
        return [i for i in range(int(range_no)) if i%2 == 0]
        logging.info('successfully executed.')
    except Exception as e:
        print('exception occured',e)
        logging.error('exception'+str(e))

    