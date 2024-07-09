
-- Ignore the following two lines
set_option autoImplicit false

macro "use" e:term : tactic => `(tactic| refine Exists.intro $e ?_)

/- *** First-order logic -/

/-
  Beyond the propositional connectives we have seen in Lab2,
  we are also provided with the first-order quantifiers, ∀ and ∃,
  enabling us to state and prove properties of objects.
-/

/- ** Universal quantifier -/
/-
  Given a type `α : Type` and a function `p : α → Prop`
  (i.e. a unary predicate on `α`), we can form the new proposition
  `∀ x : α, p a`, stating that `p` holds for all `x` in `α`.
-/
variable {α : Type} (p : α → Prop)
#check ∀ x : α, p x

/- One may omit type annotations when they are inferrable from context -/
#check ∀ x, p x

/-
  In order to prove a universal statement `∀ x : α, p x`,
  the basic strategy is to assume an aribtrary `x : α`,
  and then prove `p x` for it.
  This can be done using the `intros` tactic, just like assume the hypothesis of an implication.
-/

example : ∀ n : Nat, 0 ≤ n := by
  intros n
  exact Nat.zero_le n -- a lemma from the standard library

#check Nat.zero_add
/- Exercise 1. Hint: Use the lemma above -/
example : ∀ n : Nat, 0 + n = n := by
  intros n
  exact Nat.zero_add n

/- We choose a random n and we prove that it applies -/

#check Nat.add_comm
/- Exercise 2. Hint: Use the lemma above -/
example : ∀ (n : Nat) (m : Nat), n + m = m + n := by
  intros n m
  exact Nat.add_comm n m

/- We choose a random n and m and we prove that it applies -/

/- Exercise 3 -/
example : ∀ x : α, p x → p x := by
  intro x
  intro hpx
  exact hpx

/- We choose a random x, we assume p x, and if p x is true, then... well, p x is true. It just proves itself -/

/-
  If you have a universal hypothesis `h : ∀ x : α, p x`,
  this can be instantiated to any expression `a : α`, producing
  a proof of `p a`.

  This instantiation can be done simply by function application
-/
variable (a : α)
#check p a

example : (∀ x : α, p x) → p a := by
  intros h
  exact h a

/- Or as a function -/
example : (∀ x : α, p x) → p a := fun h => h a

/- Alternatively, the `specialize` tactic can be used to replace a universal hypothesis
  with an instantiation thereof.
-/
example : (∀ x : α, p x) → p a := by
  intros h
  specialize h a
  assumption

variable (q : α → Prop)

example : (∀ x : α, p x) ∧ (∀ x, q x) → (∀ x : α, p x ∧ q x) := by
  intros h
  intros a
  cases h with
  | intro hp hq =>
  specialize hp a
  specialize hq a
  exact And.intro hp hq

/- Exercise 4 -/
example : (∀ x : α, p x ∧ q x) → (∀ x : α, p x) ∧ (∀ x, q x) := by
  intro h
  have hxp : ∀ x, p x := λ x => (h x).left
  have hxq : ∀ x, q x := λ x => (h x).right
  exact And.intro hxp hxq

/-
  I didn't find any other solution easier than this:
  We split the 2 expressions, p x and q x into 2 separate lambda expressions.
  We define them by giving them a name (hxp, hxq), then we give them their meaning, and then we prove them
  The proof is done by creating a lambda expression with a "assignable" value for x, then we extract the left/right side of the And
    in the original argument. I know is sounds weird, but I dunno how to explain this better right now. Sorry :c
  Afterwards, we simply concatenate them in an and to prove the goal

  I have no idea why picking a random x doesn't work here.
  intro x just gives me an error. I'm honestly very confused, but alas.
-/


/- Exercise 5 -/
example : (∀ x, p x → q x) → (∀ x, p x) → (∀ x, q x) := by
  intro hxpq
  intro hxp
  intro x
  specialize hxp x
  specialize hxpq x
  exact hxpq hxp

/-
  We introduce our original 2 assumptions, and a random value for x.
  Then, we specialize the 2 phrases around the random x, which in turn gives us
  p x → q x
  and
  p x
  We can then use the fact that p x is true + the first phrase to prove that q x is true.
  Since we proved this for a random x, it means it's true for any x.
  ..........I think.
-/
