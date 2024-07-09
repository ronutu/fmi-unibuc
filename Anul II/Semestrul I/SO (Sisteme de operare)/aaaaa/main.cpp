#include <iostream>
#include <vector>

using namespace std;

class IOinterface {
public:
    virtual istream& citire(istream& in)=0;
    virtual ostream& afisare(ostream& out)const=0;
};

class Vaccin {
protected:
    const int id;
    static int contor;
    float pret, temperatura;
    vector<string> substante;
public:
    Vaccin(): id(contor++) {
        this->pret = 0;
        this->temperatura = 0;
    }

    Vaccin(float pret, float temperatura):  id(contor++) {
        this->pret = pret;
        this->temperatura = temperatura;
        this->substante = substante;
    }

    Vaccin(const Vaccin& p): id(contor++) {
        this->pret = p.pret;
        this->temperatura = p.temperatura;
        this->substante = p.substante;
    }

    Vaccin& operator=(const Vaccin& p) {
        if(this != &p) {
            this->pret = p.pret;
            this->temperatura = p.temperatura;
            this->substante = p.substante;
        }
        return *this;
    }

    istream& citire(istream& in) {
        cout << "Introdu pretul:\n";
        in >> this->pret;
        cout << "Introdu temperatura:\n";
        in >> this->temperatura;
        cout << "Introdu cate substante vrei sa adaugi:\n";
        int nr;
        in >> nr;
        string substanta;
        for(int i=0; i<nr; i++) {
            in >> substanta;
            this->substante.push_back(substanta);
        }
        return in;
    }

    friend istream& operator >> (istream& in, Vaccin& p) {
        return p.citire(in);
    }

    ostream& afisare(ostream& out) const {
        out << "Pretul: " << this->pret << endl;
        out << "Temperatura: " << this->temperatura << endl;
        for(int i=0; i<substante.size(); i++)
            out << substante[i] << endl;
        return out;
    }

    friend ostream& operator << (ostream& out, const Vaccin& p) {
        return p.afisare(out);
    }

    ~Vaccin() {
        this->pret = 0;
        this->temperatura = 0;
        this->substante.clear();
    }
};
int Vaccin :: contor = 0;

int main()
{

    return 0;
}
