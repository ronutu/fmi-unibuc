-- Seminar 2 - Lean 4
-- Sistemul Hilbert - sistem de deductie pentru LP

-- trei axiome si o regula de deductie
-- (A₁) φ → (ψ → φ)
-- (A₂) (φ → (ψ → χ)) → ((φ → ψ) → (φ → χ))
-- (A₃) (¬ψ → ¬φ) → (φ → ψ)

-- (MP) daca φ si φ → ψ atunci ψ

-- Azi este miercuri, deci avem seminar de Lean.
-- p = Azi este miercuri
-- q = avem seminar de Lean
-- p → q
-- ¬(p → q) = ¬(¬p ∨ q) = p ∧ ¬q
-- negatia: Azi este miercuri SI NU avem seminar de Lean.

-- Sistemul Hilbert este un sistem bun pentru verificarea
-- proprietatilor logice si a rezultatelor logicii propozitionale.

-- dar vom utiliza un sistem echivalent si mai simplu, numit
-- Sistemul deductiei naturale

-- Avem reguli pentru toti conectorii logici
-- iar pentru fiecare conector in parte avem
-- reguli de introducere si de eliminare

-- Reguli pentru conjunctie (∧)

-- reguli de introducere (∧ i)

-- vreau sa demonstrez ca o propozitie p ∧ q este adevarata
-- demonstrez p ∧ q demonstrand p si q

#check And.intro

-- reguli de eliminare (∧ e)

-- daca p ∧ q este o propozitie adevarata
-- atunci, in particular
-- p este adevarata
-- q este adevarata

#check And.left
#check And.right

-- Reguli pentru implicatie (→)

-- reguli de introducere

-- pentru a demonstra p → q
-- presupunem ca p este adevarat
-- demonstram q din ipoteza p

-- reguli de eliminare (modus ponens)
-- in Lean, este aplicarea de functie
-- a : α, f : α → β si dem β aplicand f a

-- Reguli pentru disjunctie (∨)

-- reguli de introducere

-- daca p este adevarat, p ∨ q este adevarat, oricare ar fi q
#check Or.inl

-- daca q este adevarat, p ∨ q este adevarat, oricare ar fi p
#check Or.inr

-- regula de eliminare

-- stim p ∨ q
-- incercam sa demonstram ca din p se deduce r
-- incercam sa demonstram ca din q se deduce r
-- atunci, am demonstrat r

#check Or.elim

-- Regula de eliminare a negatiei

#check Classical.byContradiction

-- Avem acces la Tertium non datur

#check Classical.em

-- Exercitii

-- *Exercitiul 1*
example {p q : Prop} : p → (p → q) → q := by
  intro hp
  intro hpq
  exact hpq hp

-- *Exercitiul 2*
example {p q : Prop} : p ∧ q → q ∧ p := by
  intro hpq
  have hp := And.left hpq
  have hq := And.right hpq
  exact And.intro hq hp

example {p q : Prop} : p ∧ q → q ∧ p := by
  intro hpq
  exact And.intro (And.right hpq) (And.left hpq)

-- *Exercitiul 3*
example {p q : Prop} : p → q → (p ∧ q) := by
  intros hp hq
  exact And.intro hp hq

-- *Exercitiul 4*
example {p q r : Prop} : (p ∧ (q ∨ r)) → ((p ∧ q) ∨ (p ∧ r)) := by
  intro h
  have hp := And.left h
  have hqr := And.right h
  apply Or.elim hqr
  . intro hq
    have hpq := And.intro hp hq
    exact Or.inl hpq
  . intro hr
    have hpr := And.intro hp hr
    exact Or.inr hpr

-- *Exercitiul 5*

example {p q : Prop} : (p ∨ q) → (q ∨ p) := by
  intro h
  apply Or.elim h
  . intro hp
    exact Or.inr hp
  . intro hq
    exact Or.inl hq

-- *Exercitiul 6*

#check absurd


theorem dne {p : Prop} : ¬¬p → p := by
  intro hnnp
  apply Or.elim (Classical.em p)
  . intro hp
    exact hp
  . intro hnp
    exact absurd hnp hnnp

theorem dni {p : Prop} : p → ¬¬p := by
  intro hp
  apply Classical.byContradiction
  intro hnnnp
  have hnp := dne hnnnp
  exact absurd hp hnp

-- *Exercitiul 7*

example {p q : Prop} : (p → q) → ¬q → ¬p := by
  intro hpq
  intro hnq
  apply Classical.byContradiction
  intro hnnp
  have hp := dne hnnp
  have hq := hpq hp
  exact hnq hq
