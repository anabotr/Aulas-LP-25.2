#Questão 1
import datetime

class BookMatchError(Exception): pass

class TransactionError(BookMatchError): pass

class InexistentTransaction(TransactionError): pass

class AcceptionError(TransactionError): pass

class InconsistentTradeError(TransactionError): pass

class Book:
    def __init__(self, title: str, author: str, genre: str, conservation: str):
        self._title = title
        self._author = author
        self._genre = genre
        self._conservation = conservation
    
    def conservation(self):
        return self._conservation
    
    def title(self):
        return self._title
    
    def author(self):
        return self._author
    
    def genre(self):    
        return self._genre

            
class Transaction:
    def __init__(self, user_1, user_2, book: Book):
        self._giver = user_1
        self._receiver = user_2
        if not book in user_1.books():
            raise InconsistentTradeError(f"{user_1} doesn't have that book.")
        self._book = book
        self._status = "Pending"
        self._date = None
        user_1.add_solicitation_to_trade(self)
        print("Solicitação feita")
    
    def giver(self):
        return self._giver
    
    def receiver(self):
        return self._receiver
    
    def status(self):
        return self._status
    
    def date(self):
        return self._date
    
    def set_status(self, status: str):
        self.status = status
    
    def set_date(self):
        self.date = datetime.date.today()
    
    def book(self):
        return self._book

class User:
    def __init__(self, name: str):
        self._name = name
        self._books = []
        self._trades_received = []
    
    def books(self):
        return self._books
        
    def add_book(self, book : Book):
        self._books.append(book)
        
    def remove_book(self, book : Book):
        self.books().remove(book)
    
    def trades(self):
        return self._trades_received
        
    def add_solicitation_to_trade(self, trade):
        self._trades_received.append(trade)
        
    
    def answer_trade(self, trade: Transaction, accept: str):
        if trade in self.trades() and trade.status() == "Pending":
            if accept.lower().strip() == "yes":
                trade.set_status = "Accepted"
                trade.giver().remove_book(trade.book())
                trade.receiver().add_book(trade.book())
                trade.set_date()
                print("Transaction finished.")
            elif accept.lower().strip() == "no":
                trade.set_status = "Canceled"
                trade.set_date()
                print("Transaction rejected.")
            else:
                raise AcceptionError("Your acception string must be \"yes\" or \"no\".")
        else:
            raise InexistentTransaction("Transaction inexistent or already done.")
    
    
#Driver Code
user_1 = User("Ana")
user_2 = User("Larissa")
book_1 = Book("O Triste Fim de Policarpo Quaresma", author = "Lima Barreto", genre = "Romance", conservation = "novo")
user_1.add_book(book_1)
transaction_1 = Transaction(user_1, user_2, book_1)
user_1.answer_trade(transaction_1, "no")
