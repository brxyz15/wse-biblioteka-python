# Administracja Biblioteką - aplikacja napisana w Python 3.14.5 w celu zaliczenia przedmiotu

## Wykorzystane moduły i biblioteki
W aplikacji zostały użyte:
- pandas
- tkinter
- datetime
- random

Moduły stworzone jako element aplikacji:
- book
- customer
- purchase

## Moduł "book"
### parseBooks()
W pliku book.xlsx podanym do zadania wszystkie dane zapisane są w jednej kolumnie, oddzielone przecinkiem. Funkcja ta odpowiada za utworzenie DataFrame z odpowiednio nazwanymi kolumnami zawierającymi rozdzielone dane, co ułatwia dalszą pracę na danych z pliku book.xlsx.

### addBook(bookWindow, title, author, bookCount)
Argument bookWindow przekazuje z głównego modułu okno interfejsu na którym znajduje się wykonywana teraz funkcja dodania książki, jest to zrobione po to, aby bookWindow był podany w wyskakujących tu oknach jako element rodzic. Dzięki temu okna powiadomień są na wierzchu. Argumenty title oraz author, jak nazwy wskazują, przekazują tytuł i autora książki z uzupełnionego pola tekstowego, oraz sprawdzają czy jest uzupełnione. Argument bookCount wskazuje, jaki wolumen książek ma być ustawiony na start.

### removeBook(bookWindow, bookList, title = "", bookId = 0)
Tym razem przekazywany jest również Listbox, w którym znajdują się wypisane książki wraz z autorami, po to aby móc od razu po usunięciu książki wykasować ją także z widocznej listy. Argumenty title oraz bookId mają podane wartości standardowe, ponieważ tylko jeden z nich jest konieczny. Oczywiście funkcja nie zadziała gdy nie zostanie podany żaden argument.

## Moduł "customer"
### generateId()
Zgodnie z wymogiem zadania, dla każdego klienta generowany jest pseudo-losowy 4-liczbowy numer identyfikacyjny. Funkcja sprawdza również czy nie istnieje już takie ID, a jeśli jest taka potrzeba, losuje i sprawdza nowe.

### addCustomer(customerWindow, firstName, lastName, email, phoneNumber, street, city, country, generateId)
Rekordzista pod względem argumentów funkcji. Tak jak bookWindow, konieczne było przekazanie customerWindow w dokładnie tym samym celu. Przekazywane są wszystkie potrzebne dane do uzupełnienia plików customer.csv oraz address.csv. Dodałem funkcję generateId tylko dlatego, że w wymogach zadania było napisane, aby utworzyć funkcję wyższą. Nie wiem czy dobrze to zrobiłem i po co to zrobiłem.

### removeCustomer(customerWindow, customerList, name = "", customerId = 0)
Działa adekwatnie do removeBook, lecz usuwa również adres odpowiadający klientowi z pliku address.csv.

## Moduł "purchase"
### sellBook(purchaseWindow, bookList, bookId, customerId, sellCount=1)
Z nazw funkcji możnaby powiedzieć, że to powinno być częścią modułu "book", co jest najprawdopodobniej racją. Zdecydowałem się jednak je oddzielić, ponieważ są używane one w innej części programu.
Argument purchaseWindow jest przekazywany w celu adekwatnym do bookWindow i customerWindow.
Id książki oraz klienta jest podane, aby zarejestrować zakup przez klienta w odpowiadającym pliku tekstowym znajdującym się w folderze DATABASE, a także aby zaktualizować plik book.xlsx z nową ilością dostępnych książek. Naturalnie, funkcja sprawdza czy jest w ogóle wystarczająca ich ilość.
Ustawienie argumentu sellCount na wartość domyślną 1 służy w celach uniknięcia błędu, ale też i przyspieszenia obsługi programu, ponieważ jest to przypuszczalnie najczęściej kupowana ilość książek przez jedną osobę na raz. Przy funkcjach tego modułu już traciłem siły, więc przyznaję, że jest tu dużo brzydkiego kopiuj wklej które na pewno dało się zamknąć w oddzielnych metodach lub lepiej ustrukturyzować.

### increaseBookCount(purchaseWindow, bookList, bookId, bookCount=1)
Funkcja analogiczna do poprzedniej, uzupełnia wolumen wybranej książki, tym razem bez konieczności wybrania klienta.

<sub>Bartłomiej Brzozowski, 13.06.2025 godz. 02:05</sub>


