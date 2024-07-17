from datetime import datetime
import json

class ok:
    """
    The `ok` class is used to store and manage information related to a user's status.
    
    Attributes:
    - status (bool): Represents the status of the user.
    - username (str): The username associated with the status.
    - time (int): Timestamp of when the object was created.
    - note (str): A note or comment related to the status.
    - real_status (str, optional): Additional real status information.
    """
    def __init__(self, status: bool, username: str, note: str, real_status: str = None):
        self.status = status
        self.username = username
        self.time = int(datetime.now().timestamp())
        self.note = note
        self.real_status = real_status
        
    def __str__(self):
        """
        Returns a JSON string representation of the object.
        """
        all = {'status': self.status, 'username': self.username, 'time': self.time, 'note': self.note, 'real_status':self.real_status}
        return json.dumps(all, indent=4)


class info:
    """
    The `info` class is used to store and manage information related to a bidding process.
    
    Attributes:
    - status (bool): Represents the status of the bidding process.
    - username (str): The username of the bidder.
    - domain (str): The domain associated with the bid.
    - highest_bid (str): The highest bid amount.
    - bid_step (str): The step increment for the bid.
    - minimum_bid (str): The minimum bid amount.
    - all_time (str): A formatted string indicating the remaining time for the bid.
    - data_time (dict): A dictionary containing days, hours, minutes, and seconds left.
    - bid_history (dict): A dictionary containing bid history information.
    - check_time (int): Timestamp of when the object was created.
    - note (str): A note or comment related to the bidding process.
    """
    def __init__(
        self,
        status:       bool,
        username:     str,
        domain:       str,
        highest_bid:  str,
        bid_step:     str,
        minimum_bid:  str,
        days:         str,
        hours:        str,
        minutes:      str,
        seconds:      str,
        bid_history:  dict,
        note
        ):
        self.status = status
        self.username = username
        self.domain = domain
        self.highest_bid = highest_bid
        self.bid_step = bid_step
        self.minimum_bid = minimum_bid
        self.all_time = f'Ends In {days} days : {hours}:{minutes}:{seconds}'
        self.data_time = {
            'days':    days,
            'hours':   hours,
            'minutes': minutes,
            'seconds': seconds
        }
        self.bid_history = {
            'bin_array': bid_history['binArray'],
            'history_array': bid_history['historyArray'],
            'url_array': bid_history['urlArray'],
            'hash_array': bid_history['hashArray']
        }
        self.check_time = int(datetime.now().timestamp())
        self.note = note

    def __str__(self):
        """
        Returns a JSON string representation of the object.
        """
        all = {
            'status': self.status, 
            'username': self.username, 
            'domain': self.domain,
            'highest_bid': self.highest_bid,
            'bid_step': self.bid_step,
            'minimum_bid': self.minimum_bid,
            'all_time': self.all_time,
            'data_time': self.data_time,
            'bid_history': self.bid_history,
            'check_time': self.check_time, 
            'note': self.note
        }
        return json.dumps(all, indent=4)
