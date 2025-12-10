#### Questão 1

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
    
    def __repr__(self):
        return (f"Book(title='{self._title}', author='{self._author}', "
            f"genre='{self._genre}', conservation='{self._conservation}')")

    
    def conservation(self):
        return self._conservation
    
    def title(self):
        return self._title
    
    def author(self):
        return self._author
    
    def genre(self):    
        return self._genre

            
class Transaction:
    def __init__(self, user_1, user_2, book_1: Book, book_2: Book):
        self._giver = user_1
        self._receiver = user_2
        if not book_1 in user_1.books():
            raise InconsistentTradeError(f"{user_1} doesn't have that book.")
        if not book_2 in user_2.books():
            raise InconsistentTradeError(f"{user_2} doesn't have that book.")
        self._book_1 = book_1
        self._book_2 = book_2
        self._status = "Pending"
        self._date = None
        user_2.add_solicitation_to_trade(self)
        print("Solicitação feita")
    
    def __repr__(self):
        return (f"Transaction(giver={self._giver._name!r}, "
            f"receiver={self._receiver._name!r}, "
            f"book_1={self._book_1.title()!r}, "
            f"book_2={self._book_2.title()!r}, "
            f"status={self._status!r})")

    
    def giver(self):
        return self._giver
    
    def receiver(self):
        return self._receiver
    
    @property
    def status(self):
        return self._status
    
    def date(self):
        return self._date
    
    @status.setter
    def status(self, status: str):
        self._status = status
    
    def set_date(self):
        self._date = datetime.date.today()
    
    def book_1(self):
        return self._book_1
    
    def book_2(self):
        return self._book_2

class User:
    def __init__(self, name: str):
        self._name = name
        self._books = []
        self._trades_received = []
        self._rating = 0
        self._rating_num = 0
    
    def books(self):
        return self._books
        
    def add_book(self, book : Book):
        self._books.append(book)
        
    def remove_book(self, book : Book):
        self.books().remove(book)
    
    def trades(self):
        return self._trades_received
    
    def rating(self):
        return self._rating
    
    def set_rating(self, rating):
        self._rating = rating
    
    @property
    def num_ratings(self):
        return self._rating_num

    @num_ratings.setter
    def num_ratings(self, num):
        self._rating_num = num

    def att_ratings(self):
        self.num_ratings = self.num_ratings + 1

    def add_solicitation_to_trade(self, trade):
        self._trades_received.append(trade)
        
    def give_rating(self, trade : Transaction, rating: int):
        if trade.status != "Accepted":
            raise TransactionError("Can only rate after a completed transaction.")
        if trade.giver() == self:
            trade.receiver().receive_rating(rating)
        else:
            trade.giver().receive_rating(rating)
            
    def receive_rating(self, rating):
        if self.num_ratings == 0:
            self.set_rating(rating)
            self.att_ratings()
        else:
            rating_atual = self.rating()
            rating_novo = (rating + rating_atual*self.num_ratings)/(self.num_ratings + 1)
            self.set_rating(rating_novo)
            self.att_ratings()

    def answer_trade(self, trade: Transaction, accept: str):
        if trade in self.trades() and trade.status == "Pending":
            if accept.lower().strip() == "yes":
                trade.status = "Accepted"
                trade.giver().remove_book(trade.book_1())
                trade.giver().add_book(trade.book_2())
                trade.receiver().remove_book(trade.book_2())
                trade.receiver().add_book(trade.book_1())
                trade.set_date()
                print("Transaction finished.")
            elif accept.lower().strip() == "no":
                trade.status = "Canceled"
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
book_2 = Book("Morro dos ventos uivantes", author = "Emily Bronte", genre = "Romance", conservation = "usado")
user_1.add_book(book_1)
user_2.add_book(book_2)
transaction_1 = Transaction(user_1, user_2, book_1, book_2)
print(transaction_1)
print(user_1.books())
print(user_2.books())
user_2.answer_trade(transaction_1, "yes")
print(user_1.books())
print(user_2.books())
user_1.give_rating(transaction_1, 4)
user_1.give_rating(transaction_1, 3)
user_1.give_rating(transaction_1, 4)
user_2.give_rating(transaction_1, 3)
print(user_1.rating())
print(user_2.rating())
