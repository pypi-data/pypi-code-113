
import os,boto3,time,subprocess,sys
import pandas as pd
import numpy as np

from SharedData.Logger import Logger
from SharedData.SharedDataAWSKinesis import KinesisStreamProducer

class SharedDataRealTime:

    # producer dictionary
    producer = {}

    def Broadcast(shdata,feeder,period,tag,idx,col):        
        producer = SharedDataRealTime.getProducer(shdata)
        data = shdata[feeder][period][tag].loc[idx,col].values
        
        if isinstance(tag,pd.Timestamp):
            msg = {
                'sender' : os.environ['USER_COMPUTER'],
                'msgtype' : 'df',
                'feeder' : feeder,
                'period' : period,
                'tag' : str(tag),
                'idx' : idx,
                'col' : col,
                'data' : data.tolist()
            }            
        else:
            msg = {
                'sender' : os.environ['USER_COMPUTER'],
                'msgtype' : 'ts',
                'feeder' : feeder,
                'period' : period,
                'tag' : tag,
                'idx' : idx.astype('int64').tolist(),
                'col' : col,
                'data' : data.tolist()
            }            
                
        producer.produce(msg, partitionkey=feeder)

    def getProducer(shdata):
        if not shdata.database in SharedDataRealTime.producer.keys():
            streamname = os.environ['BASE_STREAM_NAME']+'-'+shdata.database.lower()
            session = boto3.Session(profile_name=os.environ['REALTIME_PROFILENAME'])
            client = session.client('kinesis')
            #create stream
            try:
                response = client.create_stream(
                    StreamName=streamname,
                    ShardCount=1,
                    StreamModeDetails={
                        'StreamMode': 'PROVISIONED'
                    }
                )
                if response['ResponseMetadata']['HTTPStatusCode']==200:
                    Logger.log.info('Kinesis Stream %s created!' % (streamname))
                    time.sleep(10) #wait stream to be created
            except Exception as e:
                pass
            
            SharedDataRealTime.producer[shdata.database] =\
                KinesisStreamProducer(stream_name=streamname,\
                profile_name=os.environ['REALTIME_PROFILENAME'])
        return SharedDataRealTime.producer[shdata.database]
    
    def Subscribe(shdata):
        today = pd.Timestamp(pd.Timestamp.now().date())
        if not shdata['RT']['D1'].exists(today):
            df = pd.DataFrame(
                0,
                index = ['MarketData','Signals','Porfolios'],
                columns = ['watchdog']
            )
            df.loc[shdata.database,'watchdog'] = time.time() - 61
            shdata['RT']['D1'][today] = df
            shdata['RT']['D1'].tags[today].Write()
        
        # start subprocess if 
        df = shdata['RT']['D1'][today]
        if time.time() - df.loc[shdata.database,'watchdog'] > 60:
            proc = subprocess.Popen([sys.exec_prefix+r'\Scripts\python.exe',\
                sys.exec_prefix+r'Lib\site-packages\SharedDataSharedDataRealTimeProcess.py'],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,\
                universal_newlines=True, shell=True)

