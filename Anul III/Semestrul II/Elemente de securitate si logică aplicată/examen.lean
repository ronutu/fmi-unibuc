-- **Examen - Elemente de securitate si logica aplicata**


-- *Subiectul 1* [1p]
-- a. Definiti, prin *recursie structurala*, urmatoarea functie, pentru orice x si y numere naturale:

def my_func(x y : Nat) : Nat :=
  match x with
  | 0 => 2*y
  | x + 1 => 3 * (x+1 + y) + 2 * (my_func x y)

#eval my_func 3 5

-- my_func(x, y) := 2 * y                                 daca x = 0
--                  3 * (x + y) + 2 * my_func(x - 1, y)   altfel


-- b. Evaluati functia in x = 3 si y = 5.

-- *Subiectul 2* [1p]
-- Demonstrati teorema din logica propozitionala: (p → r) ∧ (q → ¬r) → ¬(p ∧ q).
-- Puteti folosi regulile de eliminare, respectiv introducere a dublei negatii.

variable { p q r : Prop }

theorem dne : ¬¬p → p := by
  intro hnnp
  apply Or.elim $ Classical.em p
  . intro hp
    assumption
  . intro hnp
    contradiction

theorem dni : p → ¬¬p := by
  intro hp
  apply Classical.byContradiction
  intro hnnnp
  have hnp := dne hnnnp
  contradiction

example : (p → r) ∧ (q → ¬r) → ¬(p ∧ q) := by
  intro h
  have hleft := And.left h
  have hright := And.right h
  apply Classical.byContradiction
  intro hnnpq
  have hpq := dne hnnpq
  have hp := And.left hpq
  have hq := And.right hpq
  have hr := hleft hp
  have hnr := hright hq
  contradiction


-- *Subiectul 3* [1p]
-- Demonstrati urmatoarea teorema in logica de ordinul I: ∀x (p(x) → q(x)) ∧ ∀x p(x) → q(a).
-- Aveti date predicatele p si q, de tipul α → Prop, si o variabila a : α.

variable {p q : α → Prop}
variable {a : α}

example : (∀ x : α, p x → q x) ∧ (∀ x, p x) → q a := by
  intro h
  have hleft := And.left h
  have hright := And.right h
  specialize hleft a
  specialize hright a
  exact hleft hright
