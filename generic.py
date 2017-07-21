STAGE1 = 1
STAGE2 = 2
STAGE3 = 3

class PassportQueue:
    doc_verification_queue = []
    police_verification_queue = []
    biometric_queue = []

    @classmethod
    def add(cls, queue_name, person):
        screen_number = None
        if queue_name == 'doc_verification':
            screen_number = 1
            PassportQueue.doc_verification_queue.append(person)
        elif queue_name == 'police_verification':
            screen_number = 2
            PassportQueue.police_verification_queue.append(person)
        elif queue_name == 'biometric_queue':
            screen_number = 3
            PassportQueue.biometric_queue.append(person)
        else:
            raise Exception("wrong queue name")

        print('adding to queue ', queue_name, person.token_number)
        Screen.update_screen(screen_number)

    @classmethod
    def deque(cls, queue_name):
        try:
            screen_number = None
            if queue_name == 'doc_verification':
                person = PassportQueue.doc_verification_queue.pop(0)
                screen_number = 1
            elif queue_name == 'police_verification':
                person = PassportQueue.police_verification_queue.pop(0)
                screen_number = 2
            elif queue_name == 'biometric_queue':
                person = PassportQueue.biometric_queue.pop(0)
                screen_number = 3
        except IndexError as e:
            return None
        
        print('processing queue ', queue_name, person.token_number)
        Screen.update_screen(screen_number)

        return person

    @classmethod
    def print_queue(cls, queue_name):
        if queue_name == 'doc_verification':
            queue = PassportQueue.doc_verification_queue
        elif queue_name == 'police_verification':
            queue = PassportQueue.police_verification_queue
        elif queue_name == 'biometric_queue':
            queue = PassportQueue.biometric_queue

        for person in queue:
            # print "printing from queue..."
            print person.token_number

class Screen:
    @classmethod
    def update_screen(cls, screen_number):
        if screen_number == STAGE1:
            print "updating screen 1"
            PassportQueue.print_queue('doc_verification')
        elif screen_number == STAGE2:
            print "updating screen 2"
            PassportQueue.print_queue('police_verification')
        elif screen_number == STAGE3:
            print "updating screen 3"
            PassportQueue.print_queue('biometric_queue')
        else:
            raise Exception("Wrong screen number passed")

class Person:
    def __init__(self):
        self.token_number = TokenMachine.generate_new_token_number()

    def get_token_number():
        return self.token_number


class TokenMachine:
    token_number = 1

    @classmethod
    def generate_new_token_number(cls):
        next_token = TokenMachine.token_number
        TokenMachine.token_number = TokenMachine.token_number + 1

        return next_token
