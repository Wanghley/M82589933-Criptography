# This is a sample of wanghley's encryptation algorithm
# AUTHOR: Wanghley Soares Martins (@wanghley)
# DATE: September, 2020

from rich.console import Console
from encryptation.encrypt import Encryptor, Decryptor

class Printer:
    def __init__(self):
        self.console = Console()

    def head(self):
        self._lockPrint()
        self.console.print(
            ":lock:\t     [bold yellow]WANGHLEY'S ENCRYPTION ALGORITHM V0.1[/bold yellow]\t     :lock:")
        self.console.print(":lock:\t  [i]This is a example of use of the encryptation[/i]\t     :lock:"
                           "\n:lock:\t    algorithm created to educational purposes\t     :lock:")
        self.console.print(":lock:\t\t   by: Wanghley Soares Martins\t             :lock:\n"
                           ":lock:\t        (https://www.github.com/wanghley)\t     :lock:")
        self._lockPrint()

    def askForText(self):
        self.console.print("\nPlease, enter a message to criptograph: ")

    def askForencryptedFile(self):
        self.console.print("\nPlease, enter a location with the criptographed message: ")

    def selectOption(self):
        self.console.print("\nWhat would you like to do? [1 - encrypt / 2 - decrypt] ")

    def UUID(self, uuid):
        self.console.print("UUID of the message: [bold red]" + str(uuid) + "[/bold red]")

    def message(self,msg):
        self._lockPrint()
        self.console.print("[cyan]MESSAGE DECRYPTOGRAPHED[/cyan]: [red bold]"+msg+"[/red bold]")
        self._lockPrint()

    def success(self,cript=True):
        if cript:
            self.console.print("\t[green]MESSAGE CRIPTOGRAPHED [bold]SUCCESSFULLY[/bold][/green]!")
        else:
            self.console.print("\t[green]MESSAGE DECRIPTOGRAPHED [bold]SUCCESSFULLY[/bold][/green]!")

    def error(self,cript=True):
        if cript:
            self.console.print(":lock:[red][bold]ERROR[/bold] ON MESSAGE CRIPTOGRAPHY[/red]!")
        else:
            self.console.print(":lock:[red][bold]ERROR[/bold] ON MESSAGE DECRIPTOGRAPHY[/red]!")

    def _lockPrint(self):
        self.console.print(":lock::lock::lock::lock::lock::lock::lock::lock::lock::lock:"
                           ":lock::lock::lock::lock::lock::lock::lock::lock::lock::lock::lock:"
                           ":lock::lock::lock::lock::lock::lock::lock::lock::lock::lock::lock:")
    def printLock(self):
        self._lockPrint()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    printer = Printer()
    printer.head()

    opt = -1

    while True:
        printer.selectOption()
        opt = int(input())
        if ((opt!=1) & (opt!=2)):
            print('Invalid option! Try again')
        else:
            break
    if opt==1:
        printer.askForText()
        msg = input()

        enc = Encryptor(msg)

        printer.UUID(enc.uuid)

        enc.encrypt()

        try:
            f = open('msg ' + str(enc.uuid) + ".txt", 'a')
            f.write(enc.encrypted_msg)
            f.close()
            printer.success()
        except Exception as e:
            printer.error()
            print(e)
    else:
        printer.askForencryptedFile()
        dec = None
        txt = input()
        try:
            msg = open(txt).read()
            uuid = ((txt.split(" ")[1]).split(".")[0])
            dec = Decryptor(msg, uuid)
            printer.success(False)
            printer.message(dec.decrypt())
        except FileNotFoundError as  e:
            printer.error(False)
            print(e)
        except Exception as e:
            printer.error(False)
            print(e)