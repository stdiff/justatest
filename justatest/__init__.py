from typing import Union

def your_function(x:Union[int,float]) -> Union[int,float]:
    return x**2

class Logger:

    @classmethod
    def send_notification(cls, to:str):
        print("sending a notification e-mail to %s" % to)


    @classmethod
    def logging(cls, level:int):
        print("logging ...")

        if level > 3:
            print("sending an e-mail...")
            cls.send_notification("me")

if __name__ == "__main__":
    print("------")
    Logger.logging(level=1)
    print("------")
    Logger.logging(level=10)