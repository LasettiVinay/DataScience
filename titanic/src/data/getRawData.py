# _*_ coding: utf-8 _*_
import os
import logging
from dotenv import load_dotenv, find_dotenv
from requests import session

# payload for login to keggle
payload = {
    'action': 'login',
    'username' : os.environ.get("KAGGLE_USERNAME"),
    'password' : os.environ.get("KAGGLE_PASSWORD")
}

urln='https://youtu.be/pKvuh1qH6M4'

def extract_data(url, file_path):
    '''
    extract data from kaggle
    '''
    # setup session
    with session() as c:
        # post request
        c.post("https://www.youtube.com/", data=payload)
        with open(file_path, 'w') as handle:
            # get request
            response = c.get(url, stream=True)
            for block in response.iter_content(1024):
                handle.write(block)


def main(project_dir):
    '''
    main method
    '''
    #get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    #urls
    test_url = 'https://youtu.be/pKvuh1qH6M4'
    train_url = 'https://www.kaggle.com/c/titanic/download/train.csv'
    
    #file paths
    raw_data_path = os.path.join(project_dir, 'data', 'raw')
    test_data_path = os.path.join(raw_data_path, 'test.csv')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    
    #extract data
    extract_data(test_url, test_data_path)
    extract_data(train_url, train_data_path)
    logger.info('downloaded raw training and test data')
    
if __name__ == '__main__':
    # getting root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    # find .env automatically by walking up directories until it's found
    dotenv_path = find_dotenv()
    # load up the entries as environment variables
    load_dotenv(dotenv_path)
    
    # call the main
    main(project_dir)