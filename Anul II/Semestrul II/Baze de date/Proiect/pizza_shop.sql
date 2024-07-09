CREATE SEQUENCE id_count
    START WITH 1
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 1000
    NOCYCLE;

    
CREATE TABLE PIZZERIE (
  id_pizzerie INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255)
);

CREATE TABLE MENIU (
  id_meniu INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  denumire VARCHAR(255),
  pret INT,
  id_pizzerie INT,
  FOREIGN KEY (id_pizzerie) REFERENCES PIZZERIE(id_pizzerie),
  id_portie INT,
  FOREIGN KEY (id_portie) REFERENCES PORTIE(id_portie)
);

CREATE TABLE PORTIE (
  id_portie INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255),
  gramaj INT
);

CREATE TABLE DEPARTAMENT (
  id_departament INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255),
  id_pizzerie INT,
  FOREIGN KEY (id_pizzerie) REFERENCES PIZZERIE(id_pizzerie),
  id_echipa INT,
  FOREIGN KEY (id_echipa) REFERENCES ECHIPA(id_echipa)
);

CREATE TABLE DEPARTAMENT_ECHIPA_MAPPING (
    id_departament INT,
    id_echipa INT,
    PRIMARY KEY (id_departament, id_echipa),
    FOREIGN KEY (id_departament) REFERENCES DEPARTAMENT(id_departament),
    FOREIGN KEY (id_echipa) REFERENCES ECHIPA(id_echipa)
);

CREATE TABLE ECHIPA (
  id_echipa INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  rol VARCHAR(255),
  id_departament INT,
  FOREIGN KEY (id_departament) REFERENCES DEPARTAMENT(id_departament),
  id_angajat INT,
  FOREIGN KEY (id_angajat) REFERENCES ANGAJAT(id_angajat)
);

CREATE TABLE ANGAJAT (
  id_angajat INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255),
  varsta INT,
  sex CHAR(1)
);

CREATE TABLE PATRON (
  id_patron INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255),
  id_pizzerie INT,
  FOREIGN KEY (id_pizzerie) REFERENCES PIZZERIE(id_pizzerie),
  id_oras INT,
  FOREIGN KEY (id_oras) REFERENCES ORAS(id_oras)
);

CREATE TABLE ORAS (
  id_oras INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255),
  nr_locuitori INT,
  id_patron INT,
  FOREIGN KEY (id_patron) REFERENCES PATRON(id_patron),
  id_tara INT,
  FOREIGN KEY (id_tara) REFERENCES TARA(id_tara)
);

CREATE TABLE TARA (
  id_tara INT DEFAULT id_count.NEXTVAL PRIMARY KEY,
  nume VARCHAR(255),
  suprafata INT
);


INSERT INTO PIZZERIE (nume)
SELECT 'Slice' FROM dual
UNION ALL
SELECT 'Pizzarella' FROM dual
UNION ALL
SELECT 'Crust' FROM dual
UNION ALL
SELECT 'The Pizza Joint' FROM dual
UNION ALL
SELECT 'Doughlicious Pizza' FROM dual
UNION ALL
SELECT 'Guys' FROM dual
UNION ALL
SELECT 'Mc' FROM dual
UNION ALL
SELECT 'KFC' FROM dual
UNION ALL
SELECT 'Taco Bell' FROM dual
UNION ALL
SELECT 'Speed Pizza' FROM dual;


INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Aperitive', 20, 2, 11);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Fel principal', 50, 2, 12);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Bauturi', 10, 2, 19);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Aperitive', 20, 4, 11);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Fel principal', 50, 4, 12);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Bauturi', 10, 4, 19);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Aperitive', 20, 6, 11);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Fel principal', 50, 6, 12);
INSERT INTO MENIU (denumire, pret, id_pizzerie, id_portie)
VALUES ('Bauturi', 10, 6, 19);
INSERT INTO MENIU (denumire, pret, id_pizzerie)
VALUES ('Desert', 20, 8);


INSERT INTO PORTIE (nume, gramaj)
VALUES ('Burger', 500);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Pizza', 400);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Apa', 50);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Paste', 300);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Salata', 200);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Sandwich', 250);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Supa', 350);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Frigarui', 450);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Sushi', 350);
INSERT INTO PORTIE (nume, gramaj)
VALUES ('Tortilla', 400);


INSERT INTO DEPARTAMENT (nume, id_pizzerie) VALUES ('Bucatarie', 2);
INSERT INTO DEPARTAMENT (nume, id_pizzerie) VALUES ('Personal', 2);
INSERT INTO DEPARTAMENT (nume, id_pizzerie) VALUES ('Contabilitate', 2);
INSERT INTO DEPARTAMENT (nume, id_pizzerie) VALUES ('Curatenie', 2);
INSERT INTO DEPARTAMENT (nume, id_pizzerie) VALUES ('Marketing', 2);


INSERT INTO DEPARTAMENT_ECHIPA_MAPPING (id_departament, id_echipa) VALUES (51, 52);
INSERT INTO DEPARTAMENT_ECHIPA_MAPPING (id_departament, id_echipa) VALUES (51, 54);
INSERT INTO DEPARTAMENT_ECHIPA_MAPPING (id_departament, id_echipa) VALUES (56, 57);
INSERT INTO DEPARTAMENT_ECHIPA_MAPPING (id_departament, id_echipa) VALUES (59, 55);
INSERT INTO DEPARTAMENT_ECHIPA_MAPPING (id_departament, id_echipa) VALUES (60, 55);


INSERT INTO ECHIPA (rol, id_departament, id_angajat) VALUES ('Bucatar', 51, 41);
INSERT INTO ECHIPA (rol, id_departament, id_angajat) VALUES ('Ajutor', 51, 42);
INSERT INTO ECHIPA (rol, id_departament, id_angajat) VALUES ('Chelner', 51, 43);
INSERT INTO ECHIPA (rol, id_departament, id_angajat) VALUES ('Chelner', 53, 44);
INSERT INTO ECHIPA (rol, id_departament, id_angajat) VALUES ('Contabil', 56, 45);


INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Radu', 50, 'M');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Elena', 35, 'F');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Andrei', 28, 'M');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Maria', 42, 'F');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Alexandru', 31, 'M');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Ana', 55, 'F');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Cristian', 39, 'M');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Simona', 27, 'F');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Mihai', 48, 'M');
INSERT INTO ANGAJAT (nume, varsta, sex)
VALUES ('Ioana', 33, 'F');


INSERT INTO TARA (nume, suprafata)
VALUES ('Romania', 238);
INSERT INTO TARA (nume, suprafata)
VALUES ('SUA', 962);
INSERT INTO TARA (nume, suprafata)
VALUES ('Canada', 997);
INSERT INTO TARA (nume, suprafata)
VALUES ('China', 964);
INSERT INTO TARA (nume, suprafata)
VALUES ('Rusia', 170);
INSERT INTO TARA (nume, suprafata)
VALUES ('Australia', 769);
INSERT INTO TARA (nume, suprafata)
VALUES ('Brazil', 851);
INSERT INTO TARA (nume, suprafata)
VALUES ('India', 328);
INSERT INTO TARA (nume, suprafata)
VALUES ('Argentina', 278);
INSERT INTO TARA (nume, suprafata)
VALUES ('Kazakhstan', 272);

INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Bucuresti', 20, 61);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Craiova', 2, 61);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Brasov', 6, 61);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Suceava', 8, 61);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Constanta', 10, 61);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Los Angeles', 200, 62);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('California', 30, 62);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('San Francisco', 50, 62);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('Alaska', 45, 62);
INSERT INTO ORAS (nume, nr_locuitori, id_tara) VALUES ('New York', 150, 62);


INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Marian', 2, 71);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Marius', 2, 72);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Andreea', 4, 73);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Dima', 4, 74);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Ghita', 2, 75);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Andrei', 2, 75);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Marcus', 6, 76);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Ciolacu', 2, 77);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Marcel', 6, 77);
INSERT INTO PATRON (nume, id_pizzerie, id_oras) VALUES ('Traian', 2, 78);


-- cerere in care folosesc 5 tabele si folosesc clauza FROM
-- afiseaza cati angajati are o pizzerie
SELECT p.nume nume_pizzerie, COUNT(*) numar_angajati
FROM pizzerie p JOIN departament d
    ON p.id_pizzerie = p.id_pizzerie
    JOIN DEPARTAMENT_ECHIPA_MAPPING de 
    ON d.id_departament = de.id_departament
    JOIN ECHIPA e
    ON de.id_echipa = e.id_echipa
    JOIN angajat a ON
    e.id_angajat = a.id_angajat
WHERE p.nume LIKE 'Pizzarella'
GROUP BY p.nume;

-- cerere care contine UPPER, LOWER
-- scrie cu majuscule numele pizzeriilor so cu litere mici numele patronilor
SELECT
  CONCAT('Pizzeria ', UPPER(p.nume)) nume_pizzerie,
  CONCAT('Patronul ', LOWER(pa.nume)) nume_patron
FROM
  PIZZERIE p
JOIN PATRON pa ON p.id_pizzerie = pa.id_pizzerie;

-- cerere care contine functie pe date calendaristice
-- afiseaza ziua si luna curenta
SELECT P.*, EXTRACT(DAY FROM CURRENT_DATE) ZiuaCurenta, TO_CHAR(CURRENT_DATE, 'Month') LunaCurenta
FROM PIZZERIE P;

-- cerere care foloseste nvl si decode
-- afiseaza angajatii si ii filtreaza in functie de varsta
SELECT a.nume nume_angajat, a.varsta,
       NVL(a.sex, 'Necunoscut') AS sex_angajat,
       DECODE(SIGN(a.varsta - 30), -1, 'Tanar', SIGN(a.varsta - 50), 'Matur', 'In Varsta') categorie_varsta
FROM angajat a
ORDER BY a.nume;

-- cerere care foloseste with si case
-- filtreaza preturile si spune daca sunt scumpe sau ieftine
WITH cte AS (
  SELECT
    m.id_meniu, m.denumire, m.pret, p.nume
  FROM
    MENIU m
    INNER JOIN PIZZERIE p ON m.id_pizzerie = p.id_pizzerie
  ORDER BY
    m.pret DESC
)
SELECT
  id_meniu, denumire, pret, nume,
  CASE
    WHEN pret >= 50 THEN 'Scump'
    WHEN pret >= 30 THEN 'Ieftin'
    ELSE 'Ieftin'
  END AS price_category
FROM
  cte
ORDER BY
  pret DESC;



UPDATE MENIU
SET pret = (
    SELECT pret + 5
    FROM MENIU
    WHERE id_meniu = 12
)
WHERE id_meniu = 12;

UPDATE PIZZERIE
SET nume = (
    SELECT CONCAT(nume, ' Restaurant')
    FROM PIZZERIE
    WHERE id_pizzerie = 6
)
WHERE id_pizzerie = 6;

DELETE FROM MENIU WHERE id_meniu = 31;







