from discopy import grammar, Dim
from lambeq import BobcatParser, Rewriter, AtomicType, MPSAnsatz


def send_into_classical_pipeline(sentence):
    # Convert to string diagram
    parser = BobcatParser(verbose='text')
    diagram = parser.sentence2diagram(sentence)
    grammar.draw(diagram, title='diagram', figsize=(12, 3), fontsize=14)

    # Rewrite string diagram, to reduce performance costs / training time
    rewriter = Rewriter(['prepositional_phrase', 'determiner'])
    prep_reduced_diagram = rewriter(diagram).normal_form()

    curry_functor = Rewriter(['curry'])
    curried_diagram = curry_functor(prep_reduced_diagram).normal_form()
    curried_diagram.draw(figsize=(6, 4), fontsize=16)

    # Parameterize: convert abstract string diagram to concrete tensor network
    # Define atomic types
    N = AtomicType.NOUN
    S = AtomicType.SENTENCE
    P = AtomicType.PREPOSITIONAL_PHRASE
    C = AtomicType.CONJUNCTION

    # Tensor network
    ansatz = MPSAnsatz({N: Dim(4), S: Dim(2), P: Dim(3), C: Dim(1)}, bond_dim=3)
    c_diagram = ansatz(diagram)
    c_diagram.draw(figsize=(13, 7), fontsize=13)

