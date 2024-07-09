
/-
  Timp de lucru: 1 ora.
  La final, incarcati un fisier lean denumit `Nume_Prenume_Grupa.lean` la adresa https://www.dropbox.com/request/UagLsQbkdC6miELtFcLp
-/

section

  /-
    **Exercitiul 1: Definiti, prin recursie structurala,
    functie `sumInterval` astfel incat
    `sumInterval n m` calculeaza suma numerelor naturale din intervalul `m, ..., m + n` (inclusiv).
  -/

  def sumInterval (n : Nat) (m : Nat) : Nat :=
    match n with
    |0=>m
    |n'+1 => m + sumInterval n' (m+1)
end


/-
  Demonstrati urmatoarea teorema.
-/

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

section
variable (p q r : Prop)
theorem ex2 : p ∧ q → q ∧ ¬¬p := by
  intro h
  have hp := And.left h
  have hq := And.right h
  have hnnp := dni hp
  exact And.intro hq hnnp

end


/-
  Demonstrati urmatoarea teorema
-/
section
variable {α : Type} (p : α → Prop) (q : α → Prop)

theorem ex3 : (∀ x, p x) → (∀ x, p x ∨ q x) := by
  intro h
  intro x
  have px := h x
  exact Or.inl px
end
