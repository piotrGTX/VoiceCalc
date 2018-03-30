## prepare.py

Skrypt "prepare.py" zawsze zwraca jeden nadmiarowy plik, który jest pusty ! Trzeba go usunać ręcznie

Przykładowe wywołanie:

* cd ./Train
* cd ./0
* python ../../prepare.py 0all.wav

Tworzy foldery:

* './out' zawierający podzielone pliki
* './outSilent' podzielone z domiksowaną ciszą

## loadData.py

Odczytuje wszystkie katalogi w podanej ścieżce i pobiera pliki z katalogu 'outSilent'. Akceptuje tylko pliki >= 0.5 sekundy, nadmiar obcina. 

## Tensor.py

* X, Y = loadData("./Train")
* X_test, Y_test = loadData("./Test")

Dane uczące i testowe powinny być różne !