# This File For Any Exceptions

class TooManyRequests(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, "Too many requests, try again later.")
        
class BadProxy(Exception):
    def __init__(self, proxy):
        Exception.__init__(*args, f"{proxy} Is Bad!")

class ErrorInCheck(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, "Error With Check,try again later.", **kwargs)

class ErrorUnKnown(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, "Error UnKnown,try again later, or Connect With Owner", **kwargs)

class RequestError(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UserNotFound(Exception):
    def __init__(self, username):
        Exception.__init__(*args, f"The user {username} not found")

class UsernameTaken(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, "Username taken")
