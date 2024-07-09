/-
  Timp de lucru: 1 ora.
  La final, incarcati un fisier lean denumit Nume_Prenume_Grupa.lean la adresa https://www.dropbox.com/request/pwPjc4Z7OS5uxbA5c63W
-/

section

  /-
    **Exercitiul 1: Definiti, prin recursie structurala,
    functia nthSquareSum astfel incat
    nthSquareSum n calculeaza sum patratelor numerelor naturale de la 0 la n.
  -/

  def nthSquareSum (n : Nat) : Nat :=
  match n with
  | 0 => 9
  | n' + 1 => Nat.succ n' * Nat.succ n' + nthSquareSum n'
end

#eval nthSquareSum 4

/-
  Demonstrati urmatoarea teorema.
-/
section
variable (p q r : Prop)
theorem ex2 : p ∧ (q ∧ r) → (p ∧ r) ∧ q := by
  intro h
  have hp := And.left h
  have hright := And.right h
  have hq := And.left hright
  have hr := And.right hright
  exact And.intro (And.intro hp hr) hq

/-
  Demonstrati urmatoarea teorema.
-/
section
variable {α : Type} (p : α → Prop)

theorem dne { p : Prop } : ¬¬p → p := by
  intro hnnp
  apply Or.elim $ Classical.em p
  . intro hp
    assumption
  . intro hnp
    contradiction

theorem dni {p : Prop} : p → ¬¬p := by
  intro hp
  apply Classical.byContradiction
  intro hnnnp
  have hnp := dne hnnnp
  contradiction


theorem ex3 : (∀ x, p x) → (∀ x, (¬¬p x)) := by
  intro h
  intro a
  specialize h a
  exact dni h
