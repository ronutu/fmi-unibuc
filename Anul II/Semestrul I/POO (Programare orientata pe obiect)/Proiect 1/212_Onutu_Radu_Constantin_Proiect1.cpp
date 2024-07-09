#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

class Pizza //Functionalitate: Adaugare pizza noua
{
private:
    char marime;
    bool topping;
    char* nume;
    char* blat;
    float pret;

public:
    Pizza() : marime(-1), topping(false), pret(-1) {                                                                                  //Constructorul neparametrizat
        nume = new char[100];
        blat = new char[100];
    }

    Pizza(bool _topping, char* _nume, float _pret) : marime('M'), topping(_topping), pret(_pret) {                                    //Constructorul partial parametrizat
        this->nume = new char[strlen(_nume) + 1];
        strcpy_s(nume, strlen(_nume) + 1, _nume);

        char* pufos = new char[50];
        strcpy_s(pufos, 50, "Pufos");
        this->blat = pufos;
        delete[] pufos;

    }

    Pizza(char _marime, bool _topping, char* _nume, char* _blat, float _pret) : marime(_marime), topping(_topping), pret(_pret) {     //Constructorul cu toti parametrii
        this->nume = new char[strlen(_nume) + 1];
        strcpy_s(nume, strlen(_nume) + 1, _nume);

        this->blat = new char[strlen(_blat) + 1];
        strcpy_s(blat, strlen(_blat) + 1, _blat);
    }

    Pizza(const Pizza& p) : marime(p.marime), topping(p.topping), pret(p.pret) {                                                      //Constructorul de copiere
        this->nume = new char[strlen(p.nume) + 1];
        strcpy_s(nume, strlen(p.nume) + 1, p.nume);

        this->blat = new char[strlen(p.blat) + 1];
        strcpy_s(blat, strlen(p.blat) + 1, p.blat);
    }

    ~Pizza() {                                                                                                                       //Destructorul
        if (nume != nullptr)
            delete[] nume;
        if (blat != nullptr)
            delete[] blat;
    }

    //Setteri:
    void setMarime(char _marime) {
        this->marime = _marime;
    }

    void setTopping(bool _topping) {
        this->topping = _topping;
    }

    void setNume(char* _nume) {
        if (this->nume != nullptr)
            delete[] this->nume;
        this->nume = new char[strlen(_nume) + 1];
        strcpy_s(nume, strlen(_nume) + 1, _nume);
    }

    void setBlat(char* _blat) {
        if (this->blat != nullptr)
            delete[] this->blat;
        this->blat = new char[strlen(_blat) + 1];
        strcpy_s(blat, strlen(_blat) + 1, _blat);
    }

    void setPret(float _pret) {
        this->pret = _pret;
    }

    //Getteri:
    char getMarime() {
        return this->marime;
    }

    bool getTopping() {
        return this->topping;
    }

    char* getNume() {
        return this->nume;
    }

    char* getBlat() {
        return this->blat;
    }

    float getPret() {
        return this->pret;
    }

    Pizza& operator= (const Pizza& p) {                                                                                              //Supraincarcarea operatorului =
        if (this != &p) {
            this->setMarime(p.marime);
            this->setTopping(p.topping);
            this->setNume(p.nume);
            this->setBlat(p.blat);
            this->setPret(p.pret);
        }
        return *this;
    };

    friend ostream& operator<<(ostream& output, const Pizza& p) {                                                                    //Supraincarcarea operatorului <<
        output << "Nume: " << p.nume << "\n";
        output << "Marime: " << p.marime << "\n";
        output << "Blat: " << p.blat << "\n";
        output << "Topping: " << p.topping << "\n";
        output << "Pret: " << p.pret << "\n";
        return output;
    }

    friend istream& operator>>(istream& input, Pizza& p) {                                                                           //Supraincarcarea operatorului >>
        cout << "Introduceti marimea: S/M/L\n";
        input >> p.marime;
        cout << "Topping: 0/1\n";
        input >> p.topping;
        cout << "Blat: Classic/Italian/Subtire/Pufos\n";
        input >> p.blat;
        cout << "Nume:\n";
        input >> p.nume;
        cout << "Pret: \n";
        input >> p.pret;
        return input;
    }

};

class Angajat // Functionalitate: Angajatii sub 18 ani sau peste 60 de ani primesc bonus la salariu
{
private:
    double salariu;
    char* rol;
    char sex;     //M sau F
    int varsta;
public:
    Angajat() : salariu(-1), sex(-1), varsta(-1) {                                                                                       //Constructorul neparametrizat
        rol = new char[100];
    }

    Angajat(char _sex, int _varsta) : salariu(-1), rol(nullptr), sex(_sex), varsta(_varsta) {}                                           //Constructorul partial parametrizat

    Angajat(double _salariu, char* _rol, char _sex, int _varsta) : salariu(_salariu), sex(_sex), varsta(_varsta) {                       //Constructorul cu toti parametrii
        this->rol = new char[strlen(_rol) + 1];
        strcpy_s(rol, strlen(_rol) + 1, _rol);
    }

    Angajat(const Angajat& p) : salariu(p.salariu), sex(p.sex), varsta(p.varsta) {                                                      //Constructorul de copiere
        this->rol = new char[strlen(p.rol) + 1];
        strcpy_s(rol, strlen(p.rol) + 1, p.rol);
    }

    ~Angajat() {                                                                                                                        //Destructorul
        if (rol != nullptr)
            delete[] rol;
    }

    //Setteri:
    void setSalariu(double _salariu) {
        this->salariu = _salariu;
    }

    void setRol(char* _rol) {
        if (this->rol != nullptr)
            delete[] this->rol;
        this->rol = new char[strlen(_rol) + 1];
        strcpy_s(rol, strlen(_rol) + 1, _rol);
    }

    void setSex(char _sex) {
        this->sex = _sex;
    }

    void setVarsta(int _varsta) {
        this->varsta = _varsta;
    }

    //Getteri:
    double getSalariu() {
        return this->salariu;
    }

    char* getRol() {
        return this->rol;
    }

    char getSex() {
        return this->sex;
    }

    int getVarsta() {
        return this->varsta;
    }

    Angajat& operator= (const Angajat& p) {                                                                                            //Supraincarcarea operatorului =
        if (this != &p) {
            this->setSalariu(p.salariu);
            this->setRol(p.rol);
            this->setSex(p.sex);
            this->setVarsta(p.varsta);
        }
        return *this;
    };

    friend ostream& operator<<(ostream& output, const Angajat& p) {                                                                    //Supraincarcarea operatorului <<
        output << "Rol: " << p.rol << "\n";
        output << "Salariu: " << p.salariu << "\n";
        output << "Sex: " << p.sex << "\n";
        output << "Varsta: " << p.varsta << "\n";
        return output;
    }

    friend istream& operator>>(istream& input, Angajat& p) {                                                                           //Supraincarcarea operatorului >>
        cout << "Introduceti rolul (Daca rolul este alcatuit din mai multe cuvinte se va folosi _ in loc de spatiu):\n";
        input >> p.rol;
        cout << "Introduceti salariu:\n";
        input >> p.salariu;
        cout << "Introduceti sexul: M/F\n";
        input >> p.sex;
        cout << "Introduceti varsta:\n";
        input >> p.varsta;
        return input;
    }

    void bonusSalariu() {
        if (this->varsta < 18)
            cout << "Bonusul este de " << 0.2 * this->salariu << " de lei.\n";
        else if (this->varsta > 60)
            cout << " Bonusul este de " << 0.3 * this->salariu << " de lei.\n";
        else
            cout << "Acest angajat nu beneficiaza de bonus.\n";
    }
};

class Chitanta //Functionalitate: Preluare comanda
{
private:
    char* strada;
    int nr_strada;
    char* client;
    float total;
    int locatie;

public:
    Chitanta() : nr_strada(-1), total(0), locatie(-1) {                                                                                 //Constructorul neparametrizat
        strada = new char[100];
        client = new char[100];
    }

    Chitanta(char* _client, float _total, int _locatie) : nr_strada(-1), total(_total), locatie(_locatie) {                             //Constructorul partial parametrizat
        strada = new char[100];

        this->client = new char[strlen(_client) + 1];
        strcpy_s(client, strlen(_client) + 1, _client);
    }

    Chitanta(char* _strada, int _nr_strada, char* _client, float _total, int _locatie) : nr_strada(_nr_strada), total(_total), locatie(_locatie) {   //Constructorul cu toti parametrii
        this->strada = new char[strlen(_strada) + 1];
        strcpy_s(strada, strlen(_strada) + 1, _strada);

        this->client = new char[strlen(_client) + 1];
        strcpy_s(client, strlen(_client) + 1, _client);
    }

    Chitanta(const Chitanta& p) : nr_strada(p.nr_strada), total(p.total), locatie(p.locatie) {                                          //Constructorul de copiere
        this->strada = new char[strlen(p.strada) + 1];
        strcpy_s(strada, strlen(p.strada) + 1, p.strada);

        this->client = new char[strlen(p.client) + 1];
        strcpy_s(client, strlen(p.client) + 1, p.client);
    }

    ~Chitanta() {                                                                                                                       //Destructorul
        if (strada != nullptr)
            delete[] strada;
        if (client != nullptr)
            delete[] client;
    }

    //Setteri:
    void setStrada(char* _strada) {
        if (this->strada != nullptr)
            delete[] this->strada;
        this->strada = new char[strlen(_strada) + 1];
        strcpy_s(strada, strlen(_strada) + 1, _strada);
    }

    void setNr_strada(int _nr_strada) {
        this->nr_strada = _nr_strada;
    }

    void setClient(char* _client) {
        if (this->client != nullptr)
            delete[] this->client;
        this->client = new char[strlen(_client) + 1];
        strcpy_s(client, strlen(_client) + 1, _client);
    }

    void setTotal(float _total) {
        this->total = _total;
    }

    void setLocatie(int _locatie) {
        this->locatie = _locatie;
    }

    //Getteri:
    char* getStrada() {
        return this->strada;
    }

    int getNr_strada() {
        return this->nr_strada;
    }

    char* getClient() {
        return this->client;
    }

    float getTotal() {
        return this->total;
    }

    int getLocatie() {
        return this->locatie;
    }

    Chitanta& operator= (const Chitanta& p) {                                                                                          //Supraincarcarea operatorului =
        if (this != &p) {
            this->setStrada(p.strada);
            this->setNr_strada(p.nr_strada);
            this->setClient(p.client);
            this->setTotal(p.total);
            this->setLocatie(p.locatie);
        }
        return *this;
    };

    friend ostream& operator<<(ostream& output, const Chitanta& p) {                                                                   //Supraincarcarea operatorului <<
        output << "Strada: " << p.strada << "\n";
        output << "Numar strada: " << p.nr_strada << "\n";
        output << "Client: " << p.client << "\n";
        output << "Total: " << p.total << "\n";
        output << "Locatie: " << p.locatie << "\n";
        return output;
    }

    friend istream& operator>>(istream& input, Chitanta& p) {                                                                          //Supraincarcarea operatorului >>
        cout << "Introduceti strada (daca strada este formata din mai multe cuvinte, ea se va scrie cu _ in loc de spatiu(ex.: Iuliu_Maniu)):\n";
        input >> p.strada;
        cout << "Introduceti numarul strazii:\n";
        input >> p.nr_strada;
        cout << "Introduecti numele dvs. (Numele se va scrie cu _ in loc de spatiu(de ex.: Radu_Onutu)):\n";
        input >> p.client;
        cout << "Total de plata:\n";
        input >> p.total;
        cout << "Locatia:\n";
        input >> p.locatie;
        return input;
    }

    void preluareComanda(vector<Pizza> pizze, int nrPizzerii) {
        int nr;
        char nume[101];
        int indiceLocatie;
        cout << "Introduceti numarul locatiei la care vreti sa plasati comanda: \n";
        cin >> indiceLocatie;
        while (indiceLocatie > nrPizzerii) {
            cout << "Aceasta locatie nu exista! Reintroduceti numarul locatiei: \n";
            cin >> indiceLocatie;
        }
        this->locatie = indiceLocatie - 1;
        cout << "Introduceti numele dvs. (Numele se va scrie cu _ in loc de spatiu(de ex.: Radu_Onutu)):\n";
        cin >> nume;
        this->setClient(nume);
        cout << "Introduceti strada (daca strada este formata din mai multe cuvinte, ea se va scrie cu _ in loc de spatiu(ex.: Iuliu_Maniu)):\n";
        char _strada[101];
        cin >> _strada;
        this->setStrada(_strada);
        int _nrStrada;
        cout << "Introduceti nr. strazii: \n";
        cin >> _nrStrada;
        this->setNr_strada(_nrStrada);
        cout << "Cate pizze doriti sa comandati?\n";
        cin >> nr;
        cout << "Ce indici de pe meniu au acestea?\n";
        for (int i = 0; i < nr; i++) {
            int indicePizza;
            cin >> indicePizza;
            this->total += pizze[indicePizza - 1].getPret();
        }
        cout << "Pretul total al comenzii este " << this->total << " de lei" << "\n";
    }

};

class Pizzerie //functionalitate: Calculare profit
{
private:
    const int id;
    char* locatie;
    int* dataFondarii;
    int fondator;

    static int nr;

public:

    Pizzerie() : id(nr), fondator(-1) {                                                                                              //Constructorul neparametrizat
        locatie = new char[100];
        dataFondarii = new int[3];
        nr++;
    }

    Pizzerie(char* _locatie, int* _dataFondarii) : id(nr), fondator(-1) {                                                            //Constructorul partial parametrizat
        this->locatie = new char[strlen(_locatie) + 1];
        strcpy_s(locatie, strlen(_locatie) + 1, _locatie);

        this->dataFondarii = new int[3];
        for (int i = 0; i < 3; i++)
            this->dataFondarii[i] = _dataFondarii[i];
    }

    Pizzerie(char* _locatie, int* _dataFondarii, int _fondator) : id(nr), fondator(_fondator) {                                      //Constructorul cu toti parametrii
        this->locatie = new char[strlen(_locatie) + 1];
        strcpy_s(locatie, strlen(_locatie) + 1, _locatie);

        this->dataFondarii = new int[3];
        for (int i = 0; i < 3; i++)
            this->dataFondarii[i] = _dataFondarii[i];
    }

    Pizzerie(const Pizzerie& p) : id(p.id), fondator(p.fondator) {                                                                   //Constructorul de copiere
        this->locatie = new char[strlen(p.locatie) + 1];
        strcpy_s(locatie, strlen(p.locatie) + 1, p.locatie);

        this->dataFondarii = new int[3];
        for (int i = 0; i < 3; i++)
            this->dataFondarii[i] = p.dataFondarii[i];
    }

    ~Pizzerie() {                                                                                                                    //Destructorul
        if (locatie != nullptr)
            delete[] locatie;
        if (dataFondarii != nullptr)
            delete[] dataFondarii;
    }

    //Setteri:
    void setLocatie(char* _locatie) {
        if (this->locatie != nullptr)
            delete[] this->locatie;
        this->locatie = new char[strlen(_locatie)];
        strcpy_s(locatie, strlen(_locatie) + 1, _locatie);
    }

    void setDataFondarii(int* _dataFondarii) {
        if (this->dataFondarii != nullptr)
            delete[] this->dataFondarii;
        this->dataFondarii = new int[3];
        for (int i = 0; i < 3; i++)
            dataFondarii[i] = _dataFondarii[i];
    }

    void setFondator(int _fondator) {
        this->fondator = _fondator;
    }

    //Getteri:
    const int getId() {
        return this->id;
    }

    char* getLocatie() {
        return this->locatie;
    }

    int* getDataFondarii() {
        return this->dataFondarii;
    }

    int getFondator() {
        return this->fondator;
    }

    static int getNr() {
        return nr;
    }

    Pizzerie& operator= (const Pizzerie& p) {                                                                                          //Supraincarcarea operatorului =
        if (this != &p) {
            this->setLocatie(p.locatie);
            this->setDataFondarii(p.dataFondarii);
            this->setFondator(p.fondator);
        }
        return *this;
    };

    friend ostream& operator<<(ostream& output, const Pizzerie& p) {                                                                   //Supraincarcarea operatorului <<
        output << "Id: " << p.id << "\n";
        output << "Locatie: " << p.locatie << "\n";
        output << "Data fondarii: " << p.dataFondarii[0] << "/" << p.dataFondarii[1] << "/" << p.dataFondarii[2] << "\n";
        output << "Fondator: " << p.fondator << "\n";
        return output;
    }

    friend istream& operator>>(istream& input, Pizzerie& p) {                                                                          //Supraincarcarea operatorului >>
        cout << "Introduceti locatia:\n";
        input >> p.locatie;
        cout << "Introduceti data fondarii (zi luna an):\n";
        input >> p.dataFondarii[0] >> p.dataFondarii[1] >> p.dataFondarii[2];
        cout << "Introduceti fondatorul (int):\n";
        input >> p.fondator;
        return input;
    }

    float calculProfit(vector<Chitanta> chitante) {
        float profit = 0;
        for (int i = 0; i < chitante.size(); i++)
            if (chitante[i].getLocatie()+1 == this->id)
                profit += chitante[i].getTotal();
        return profit;
    }
};

int Pizzerie::nr = 0;

vector<Pizzerie> pizzerii;
vector<Pizza> pizze;
vector<Angajat> angajati;
vector<Chitanta> chitante;

void afisareMeniu() {
    for (int i = 0; i < pizze.size(); i++)
        cout << i + 1 << ".\n" << pizze[i] << "\n";
}

void pizzerieNoua() {
    Pizzerie aux;
    cin >> aux;
    pizzerii.push_back(aux);
}

void angajatNou() {
    Angajat aux;
    cin >> aux;
    angajati.push_back(aux);
}

void pizzaNoua() {
    Pizza aux;
    cin >> aux;
    pizze.push_back(aux);
}

void comandaNoua() {
    Chitanta aux;
    afisareMeniu();
    cout << "\n";
    cout << "Unde doriti sa plasati comanda?\n";
    for (int i = 0; i < pizzerii.size(); i++)
        cout << pizzerii[i] << "\n";
    aux.preluareComanda(pizze, Pizzerie::getNr());
    chitante.push_back(aux);
}

void vizualizareProfit() {
    float total = 0;
    for (int i = 0; i < pizzerii.size(); i++) {
        cout << pizzerii[i]<<"\n";
        total += pizzerii[i].calculProfit(chitante);
        cout << "Profit: " << pizzerii[i].calculProfit(chitante) << "\n";
    }
    cout << "\nProfitul total:" << total << "\n";
}

void vizualizareBonus() {
    int id;
    for (int i = 0; i < angajati.size(); i++)
        cout << i << angajati[i].getRol() << "\n";
    cout << "Id angajat: ";
    cin >> id;
    angajati[id].bonusSalariu();
}

void Meniu() {
    int optiune;

    cout << "Radu's Pizza\n\n";
    while (true) {
        cout << "Optiunile sunt: \n";
        cout << "(Pentru admin:)\n";
        cout << "       0 - Inchide aplicatia\n";
        cout << "       1 - Pizzerie noua\n";
        cout << "       2 - Angajat nou\n";
        cout << "       3 - Pizza noua\n";
        cout << "(Pentru client:)\n";
        cout << "       4 - Afiseaza meniu\n";
        cout << "       5 - Plaseaza comanda\n";
        cout << "       6 - Vizualizare profit\n";
        cout << "       7 - Vizualizare bonus\n";
        cout << "\n";
        cout << "Alegeti o optiune: ";
        cin >> optiune;
        cout << "\n";

        Chitanta aux4;

        switch (optiune) {
        case 0:
            return;
        case 1:
            pizzerieNoua();
            cout << "\n";
            break;
        case 2:
            angajatNou();
            cout << "\n";
            break;
        case 3:
            pizzaNoua();
            cout << "\n";
            break;
        case 4:
            afisareMeniu();
            cout << "\n";
            break;
        case 5:
            comandaNoua();
            cout << "\n";
            break;
        case 6:
            vizualizareProfit();
            cout << "\n";
            break;
        case 7:
            vizualizareBonus();
            cout << "\n";
            break;
        }
    }
}

int main() {
    Meniu();
    return 0;
}
