 # person coming as a stream
import threading
from worker import doc_verification, police_verification, biometric_verification
from generic import Person, PassportQueue
from time import sleep
import sys

def start_entry():
    for x in xrange(1,100):
        print('next person entered -', x)
        # validate current time is in between 9 to 5
        person = Person()
        # print('token number assigned is -', person.token_number)
        PassportQueue.add('doc_verification', person)
        # print 'printing queue', PassportQueue.print_queue('doc_verification')
        sleep(1)


def start_doc_verification():
    # print('doc verification worker started...')
    doc_verification()

def start_police_verification():
    police_verification()

def start_biometric_verification():
    biometric_verification()

take_input = threading.Thread(target=start_entry)
take_input.start()

# validation on no. of workers, defaults to 0
for doc_worker in xrange(1, int(sys.argv[1])):
    worker_doc_verification = threading.Thread(target=start_doc_verification)
    worker_doc_verification.start()

for police_worker in xrange(1, int(sys.argv[2])):
    worker_police_verification = threading.Thread(target=start_police_verification)
    worker_police_verification.start()

for biometic_worker in xrange(1,int(sys.argv[3])):
    worker_biometric_verification = threading.Thread(target=start_biometric_verification)
    worker_biometric_verification.start()
