
"""
Observer is a behavioral design pattern that lets you define a subscription mechanism to
notify multiple objects about any events that happen to the object they’re observing.

* observer has an update method -> create abstract method and create a class that implements this method
    for EACH kind of updating (slack, email, text, etc.)
* subject: holds list of obervers, can register, remove, notify_all_observers, specific method
    for the "Event" -> (e.g., posted job, ticket bought, set_measurements) and within this method
    we're going to call self.notify_observers()
"""

from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass

class JobPostingInterface(ABC):

    @abstractmethod
    def register_observer(self):
        pass
    
    @abstractmethod
    def remove_observer(self):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

class EmailObserver(Observer):

    def update(self, job_posting):
        print(f'Email Posting: {job_posting}')

class TextObserver(Observer):

    def update(self, job_posting):
        print(f'Text Posting: {job_posting}')

class JobPosting(JobPostingInterface):

    def __init__(self):
        self.observers = []
        self.posting = ""

    def register_observer(self, observer: Observer):
        print('New observer added.')
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        del self.observers[self.observers.index(observer)]
    
    def notify_observers(self, posting):
        print('Observers notified.')
        for obs in self.observers:
            obs.update(posting)

    def post(self, posting):
        print('Post Created.')
        self.posting = posting
        self.notify_observers(posting)

def main():

    jp = JobPosting()

    email = EmailObserver()
    text = TextObserver()

    jp.register_observer(email)
    jp.register_observer(text)
    

    new_post = "NEW JOB ALERT: Head Chef"
    jp.post(new_post)

    jp.remove_observer(text)

    new_post = "NEW JOB ALERT: Creative Director"
    jp.post(new_post)
    
if __name__ == "__main__":
    main()