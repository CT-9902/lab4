# Raport Laboratorium 4
## Wprowadzenie do biblioteki pymcdm

### Dane
Do ćwiczeń związanych z nauką pymcdm, stworzyłem tablicę zawierającą dane ... o zestawach klocków LEGO Star Wars. Skrypt ma pomóc w wyborze najlepszego zestawu. Pod uwagę wziąłem następujące kryteria:
- Cenę zestawu
- Liczbę klocków w zestawie
- Radość jaką odczuwa się podczas budowania
- Wygląd, możliwa prezencja zestawu na półce

Program przypisuje tym cechom kolejno wagi (od najważniejszej do najmniej ważnej): Cena, Liczba klocków, Radość, Wygląd.

Cena, bo jestem studentem, więc jest najważniejsza.
Liczba, bo nie często kupuje się takie zestawy i warto żeby długo się je budowało.
Radość, bo tak.
Wygląd, na ostatnim miejscu, bo zawsze można wygląd zmodyfikować.

### Wynik
Program po wykonaniu obliczeń pokazał komunikat:

~~~
Alternatywa    TOPSIS_score  TOPSIS_rank  SPOTIS_score  SPOTIS_rank
0  Kanonierka      0.407817            3      0.404641            2
1     Venator      0.546857            2      0.535681            3
2      X-Wing      0.394748            4      0.379344            1
3  Brzeszczot      0.585019            1      0.723396            4
~~~

Według TOPSIS najlepszym wyborem jest __Brzeszczot__, a według SPOTIS - __X-Wing__.
Wyniki różnią się ze względu na sposoby działania funkcji. TOPSIS używa odległości do idealnego punktu odniesienia, a SPOTIS - odległości w stosunku do granic.
