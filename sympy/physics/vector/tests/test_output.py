from sympy import S, Function
from sympy.physics.vector import Vector, ReferenceFrame, Dyadic, \
     VectorLatexPrinter
from sympy.utilities.pytest import raises


Vector.simp = True
A = ReferenceFrame('A')


def test_latex_printer():
    r = Function('r')('t')
    assert VectorLatexPrinter().doprint(r**2) == "r^{2}"


def test_output_type():
    A = ReferenceFrame('A')
    v = A.x + A.y
    d = v | v
    zerov = Vector(0)
    zerod = Dyadic(0)

    # dot products
    assert isinstance(d & d, Dyadic)
    assert isinstance(d & zerod, Dyadic)
    assert isinstance(zerod & d, Dyadic)
    assert isinstance(d & v, Vector)
    assert isinstance(v & d, Vector)
    assert isinstance(d & zerov, Vector)
    assert isinstance(zerov & d, Vector)
    raises(TypeError, lambda: d & S(0))
    raises(TypeError, lambda: S(0) & d)
    raises(TypeError, lambda: d & 0)
    raises(TypeError, lambda: 0 & d)
    assert not isinstance(v & v, (Vector, Dyadic))
    assert not isinstance(v & zerov, (Vector, Dyadic))
    assert not isinstance(zerov & v, (Vector, Dyadic))
    raises(TypeError, lambda: v & S(0))
    raises(TypeError, lambda: S(0) & v)
    raises(TypeError, lambda: v & 0)
    raises(TypeError, lambda: 0 & v)

    # cross products
    raises(TypeError, lambda: d ^ d)
    raises(TypeError, lambda: d ^ zerod)
    raises(TypeError, lambda: zerod ^ d)
    assert isinstance(d ^ v, Dyadic)
    assert isinstance(v ^ d, Dyadic)
    assert isinstance(d ^ zerov, Dyadic)
    assert isinstance(zerov ^ d, Dyadic)
    assert isinstance(zerov ^ d, Dyadic)
    raises(TypeError, lambda: d ^ S(0))
    raises(TypeError, lambda: S(0) ^ d)
    raises(TypeError, lambda: d ^ 0)
    raises(TypeError, lambda: 0 ^ d)
    assert isinstance(v ^ v, Vector)
    assert isinstance(v ^ zerov, Vector)
    assert isinstance(zerov ^ v, Vector)
    raises(TypeError, lambda: v ^ S(0))
    raises(TypeError, lambda: S(0) ^ v)
    raises(TypeError, lambda: v ^ 0)
    raises(TypeError, lambda: 0 ^ v)

    # outer products
    raises(TypeError, lambda: d | d)
    raises(TypeError, lambda: d | zerod)
    raises(TypeError, lambda: zerod | d)
    raises(TypeError, lambda: d | v)
    raises(TypeError, lambda: v | d)
    raises(TypeError, lambda: d | zerov)
    raises(TypeError, lambda: zerov | d)
    raises(TypeError, lambda: zerov | d)
    raises(TypeError, lambda: d | S(0))
    raises(TypeError, lambda: S(0) | d)
    raises(TypeError, lambda: d | 0)
    raises(TypeError, lambda: 0 | d)
    assert isinstance(v | v, Dyadic)
    assert isinstance(v | zerov, Dyadic)
    assert isinstance(zerov | v, Dyadic)
    raises(TypeError, lambda: v | S(0))
    raises(TypeError, lambda: S(0) | v)
    raises(TypeError, lambda: v | 0)
    raises(TypeError, lambda: 0 | v)