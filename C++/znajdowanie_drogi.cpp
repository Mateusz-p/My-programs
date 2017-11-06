// Rozwiązanie problemu komiwojażera, przy użyciu algorytmu najbliższego sąsiada.

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    vector<vector<double> > punkty;
    vector<double> punkt;
    double wspolrzedna_x = 0;
    double wspolrzedna_y = 0;
    int licznik = 1;
    string koniec = "";

    cout << "Podaj wspolrzedne punktu. Pierwszy z podanych punktow bedzie miejscem startu.\n\n";

    while (koniec != "n") {
        cout << "Punkt nr " << licznik++ << endl;
        cout << "Wspolrzedna x: ";
        cin >> wspolrzedna_x;
        cout << "Wspolrzedna y: ";
        cin >> wspolrzedna_y;
        cout << "Czy chcesz podac nastepny punkt? (tak - \"t\" nie - \"n\"): ";
        cin >> koniec;
        cout << endl;
        punkt.push_back(wspolrzedna_x);
        punkt.push_back(wspolrzedna_y);
        punkty.push_back(punkt);
        punkt.pop_back();
        punkt.pop_back();
    }

    vector<vector<double> > droga;

    cout << "\nWprowadziles nastepujace punkty: \n";
    for (int i=0; i<punkty.size(); i++) {
        cout << "(";
        cout << punkty[i][0];
        cout << ", ";
        cout << punkty[i][1] << ") ";
    }

    droga.push_back(punkty[0]);
    punkty.erase(punkty.begin());
    licznik = 0;
    double odleglosc_obecna = 0;
    double odleglosc_najkrotsza = 0;
    double suma = 0;

    while (punkty.size() != 1) {
        odleglosc_najkrotsza = 9999;

        for (int i=0; i<punkty.size(); i++) {
            odleglosc_obecna = sqrt(pow(droga[droga.size()-1][0] - punkty[i][0], 2) + pow(droga[droga.size()-1][1] - punkty[i][1], 2));
            if (odleglosc_obecna <= odleglosc_najkrotsza) {
                odleglosc_najkrotsza = odleglosc_obecna;
                licznik = i;
            }
        }
            droga.push_back(punkty[licznik]);
            punkty.erase(punkty.begin() + licznik);
            suma = suma + odleglosc_najkrotsza;
            odleglosc_najkrotsza = 0;
            odleglosc_obecna = 0;
            licznik = 0;
    }

    suma = suma + sqrt(pow(droga[droga.size()-1][0] - punkty[0][0], 2) + pow(droga[droga.size()-1][1] - punkty[0][1], 2));

    droga.push_back(punkty[0]);
    punkty.erase(punkty.begin());

    suma = suma + sqrt(pow(droga[droga.size()-1][0] - droga[0][0], 2) + pow(droga[droga.size()-1][1] - droga[0][1], 2));

    cout << "\nZnaleziona droga: \n";

    for (int i=0; i<droga.size(); i++) {
        cout << "(";
        cout << droga[i][0];
        cout << ", ";
        cout << droga[i][1] << ") ";
    }

    cout << "\nLaczna przebyta droga wynosi: " << suma;

    return 0;
}
