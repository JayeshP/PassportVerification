from generic import PassportQueue
from time import sleep


def doc_verification():
    while 1:
        # print('doc verificaiton loop ', x)
        person = PassportQueue.deque('doc_verification')

        if person:
            sleep(7)
            PassportQueue.add('police_verification', person)

        
        continue


def police_verification():
    while 1:
        person = PassportQueue.deque('police_verification')

        if person:
            sleep(2)

            PassportQueue.add('biometric_queue', person)

        continue


def biometric_verification():
    while 1:
        person = PassportQueue.deque('biometric_queue')

        if person:
            sleep(5)
            print ('Process completed for ', person.token_number)

        continue
