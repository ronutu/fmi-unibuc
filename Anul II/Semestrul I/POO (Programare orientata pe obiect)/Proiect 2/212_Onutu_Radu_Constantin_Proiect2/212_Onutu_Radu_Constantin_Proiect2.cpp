#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

class IOinterface {
public:
    virtual istream& citire(istream& in)=0;
    virtual ostream& afisare(ostream& out)const=0;
};

class Pizzerie: public IOinterface {
protected:
    const int id;

    string locatie, dataFondarii, fondator;
    int clienti;
    static int contor;
public:
    Pizzerie(): id(contor++) {
        this->locatie = "anonim";
        this->dataFondarii = "00/00/0000";
        this->fondator = "anonim";
        this->clienti = 0;
    }

    Pizzerie(string locatie, string dataFondarii, string fondator, int clienti): id(contor++) {
        this->locatie = locatie;
        this->dataFondarii = dataFondarii;
        this->fondator = fondator;
        this->clienti = clienti;
    }

    Pizzerie(const Pizzerie& p): id(p.contor) {
        this->locatie = p.locatie;
        this->dataFondarii = p.dataFondarii;
        this->fondator = p.fondator;
        this->clienti = p.clienti;
    }

    Pizzerie& operator = (const Pizzerie& p) {
        if(this != &p) {
            this->locatie = p.locatie;
            this->dataFondarii = p.dataFondarii;
            this->fondator = p.fondator;
            this->clienti = p.clienti;
        }
        return *this;
    }

    istream& citire(istream& in) {
        cout << "Introdu locatia:\n";
        in >> this->locatie;
        cout << "Introdu data fondarii:\n";
        in >> this->dataFondarii;
        cout << "Introdu numele fondatorului:\n";
        in >> this->fondator;
        cout << "Introdu cati clienti are in medie aceasta pizzerie pe zi:\n";
        in >> this->clienti;
        return in;
    }

    friend istream& operator >> (istream& in, Pizzerie& p) {
        return p.citire(in);
    }

    ostream& afisare(ostream& out)const {
        out << "Locatie: " << this->locatie << endl;
        out << "Data fondarii: " << this->dataFondarii << endl;
        out << "Fondator: " << this->fondator << endl;
        out << "Clienti: " << this->clienti << endl;
        return out;
    }

    friend ostream& operator << (ostream& out, const Pizzerie& p) {
        return p.afisare(out);
    }

    virtual float profit()=0;

    const int getId() {
        return id;
    }

    void setFondator(string fondator) {
        this->fondator = fondator;
    }

    ~Pizzerie() {}
};
int Pizzerie::contor = 0;

class PizzerieTerasa: public Pizzerie {
protected:
    int nrOspatari;
public:
    PizzerieTerasa(): Pizzerie() {
        this->nrOspatari = 0;
    }

    PizzerieTerasa(string locatie, string dataFondarii, string fondator, int clienti, int nrOspatari): Pizzerie(locatie, dataFondarii, fondator, clienti) {
        this->nrOspatari = nrOspatari;
    }

    PizzerieTerasa(const PizzerieTerasa& p): Pizzerie(p) {
        this->nrOspatari = p.nrOspatari;
    }

    PizzerieTerasa& operator = (const PizzerieTerasa& p) {
        if(this != &p) {
            Pizzerie::operator=(p);
            this->nrOspatari = p.nrOspatari;
        }
        return *this;
    }

    istream& citire(istream& in) {
        Pizzerie::citire(in);
        cout << "Introdu cati ospatari sunt:\n";
        in >> this->nrOspatari;
        return in;
    }

    ostream& afisare(ostream& out)const {
        Pizzerie::afisare(out);
        out << "Numar ospatari: " << this->nrOspatari << endl;
        return out;
    }

    float profit() {
        return 30 * (this->clienti * 40 - 0.03 * this->clienti * 40 * this->nrOspatari); //40 de lei este o comanda medie la pizzerie, iar 3% din profitul total se duce la fiecare ospatar
    }
};

class PizzerieLivrare: public Pizzerie {
protected:
    int nrLivratori;
public:
    PizzerieLivrare(): Pizzerie() {
        this->nrLivratori = 0;
    }

    PizzerieLivrare(string locatie, string dataFondarii, string fondator, int clienti, int nrLivratori): Pizzerie(locatie, dataFondarii, fondator, clienti) {
        this->nrLivratori = nrLivratori;
    }

    PizzerieLivrare(const PizzerieLivrare& p): Pizzerie(p) {
        this->nrLivratori = p.nrLivratori;
    }

    PizzerieLivrare& operator = (const PizzerieLivrare& p) {
        if(this != &p) {
            Pizzerie::operator=(p);
            this->nrLivratori=p.nrLivratori;
        }
        return *this;
    }

    istream& citire(istream& in) {
        Pizzerie::citire(in);
        cout << "Introdu cati livratori sunt:\n";
        in >> this->nrLivratori;
        return in;
    }

    ostream& afisare(ostream& out)const {
        Pizzerie::afisare(out);
        out << "Numar livratori: " << this->nrLivratori << endl;
        return out;
    }

    float profit() {
        return 30 * ((this->clienti * 40) - 0.01 * this->clienti * 40 * this->nrLivratori);
    }
};

class PizzerieFull: public PizzerieTerasa {
private:
    int nrLivratori;
public:
   PizzerieFull(): PizzerieTerasa() {
       this->nrLivratori = 0;
   }

   PizzerieFull(string locatie, string dataFondarii, string fondator, int clienti, int capacitate, int nrLivratori): PizzerieTerasa(locatie, dataFondarii, fondator, clienti, capacitate) {
       this->nrLivratori = nrLivratori;
   }

   PizzerieFull(const PizzerieFull& p): PizzerieTerasa(p) {
       this->nrLivratori = p.nrLivratori;
    }

   PizzerieFull& operator = (const PizzerieFull& p) {
       if(this != &p) {
            PizzerieTerasa::operator=(p);
            this->nrLivratori = p.nrLivratori;
       }
       return *this;
   }

   istream& citire(istream& in) {
       PizzerieTerasa::citire(in);
       cout << "Introdu cati livratori sunt:\n";
       in >> this->nrLivratori;
       return in;
   }

  ostream& afisare(ostream& out)const {
      PizzerieTerasa::afisare(out);
      out << "Numar livratori: " << this->nrLivratori << endl;
  }

  float profit() {
      return 30 * ((this->clienti * 40) - 0.03 * this->clienti * 40 * this->nrOspatari - 0.01 * this->clienti * 40 * this->nrLivratori);
  }
};

int main()
{
    vector<Pizzerie*> vectorPizzerii;
    cout << "Radu's Pizza!\n";
    int i=1;
    while(i==1) {
        cout << "\t0 - Inchide aplicatia\n";
        cout << "\t1 - Adauga o pizzerie doar cu terasa\n";
        cout << "\t2 - Adauga o pizzerie doar cu livrare\n";
        cout << "\t3 - Adauga o pizzerie si cu terasa si cu livrare\n";
        cout << "\t4 - Afiseaza toate pizzeriile\n";
        cout << "\t5 - Afiseaza profitul mediu al unei pizzerii intr-o luna\n";
        cout << "\t6 - Afiseaza profitul mediu lunar pentru toate pizzeriile\n";
        cout << "\t7 - Cumpara una dintre pizzerii\n";
        cout << "\t8 - Inchide o pizzerie\n";
        int a;
        cin >> a;
        switch(a) {
            case 0: {
                i = 0;
                break;
            }
            case 1: {
                PizzerieTerasa p;
                cin >> p;
                vectorPizzerii.push_back(new PizzerieTerasa(p));
                break;
            }
            case 2: {
                PizzerieLivrare p;
                cin >> p;
                vectorPizzerii.push_back(new PizzerieLivrare(p));
                break;
            }
            case 3: {
                PizzerieFull p;
                cin >> p;
                vectorPizzerii.push_back(new PizzerieFull(p));
                break;
            }
            case 4: {
                vector<Pizzerie*>::iterator it;
                for(it = vectorPizzerii.begin(); it != vectorPizzerii.end(); it++)
                    cout << (**it).getId() << ". " << **it << endl;
                break;
            }
            case 5: {
                vector<Pizzerie*>::iterator it;
                for(it = vectorPizzerii.begin(); it != vectorPizzerii.end(); it++)
                    cout << (**it).getId() << ". " << **it << endl;
                cout << "Introdu numarul pizzeriei la care vrei sa vezi profitul:\n";
                int nr;
                cin >> nr;
                cout << "Profitul pizzeriei cu numarul " << nr << " este " << (*vectorPizzerii[nr-1]).profit() << " lei." << endl << endl;
                break;
            }
            case 6: {
                float profit = 0;
                vector<Pizzerie*>::iterator it;
                for(it = vectorPizzerii.begin(); it != vectorPizzerii.end(); it++)
                    profit += (**it).profit();
                cout << "Profitul total este " << profit << " lei.\n";
                break;
            }
            case 7: {
                vector<Pizzerie*>::iterator it;
                for(it = vectorPizzerii.begin(); it != vectorPizzerii.end(); it++)
                    cout << (**it).getId() << ". " << **it << endl;
                cout << "Introdu numarul pizzeriei pe care vrei sa o cumperi:\n";
                int b;
                cin >> b;
                cout << "Numele noului fondator:\n";
                string a;
                cin >> a;
                cout << "Introdu suma de bani cu care cumperi aceasta pizzerie:\n";
                float c;
                cin >> c;
                (*vectorPizzerii[b-1]).setFondator(a);
                cout << *vectorPizzerii[b-1] << endl;
                break;
            }
            case 8: {
                vector<Pizzerie*>::iterator it;
                for(it = vectorPizzerii.begin(); it != vectorPizzerii.end(); it++)
                    cout << (**it).getId() << ". " << **it << endl;
                cout << "Introdu numarul pizzeriei pe care vrei sa o inchizi:\n";
                int a;
                cin >> a;
                it = vectorPizzerii.begin();
                vectorPizzerii.erase(it);
                break;
            }
        }
    }

    return 0;
}
