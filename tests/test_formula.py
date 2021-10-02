import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal
from sbfl.base import SBFL
import sbfl.sbfl_formula as formula

def X_y_sample_1():
    X = np.array([
        [1,0,1],
        [0,0,1],
        [1,1,0]
    ], dtype=bool)
    y = np.array([1,0,1], dtype=bool)
    # spectrum
    # - e_p = [2, 1, 1]
    # - n_p = [0, 1, 1]
    # - e_f = [0, 0, 1]
    # - n_f = [1, 1, 0]
    return X, y

"""
Test each formula
"""
def test_ochiai():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Ochiai')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 1/np.sqrt(2))

def test_tarantula():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Tarantula')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 2/3)

def test_jaccard():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Jaccard')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 1/2)

def test_russellrao():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='RussellRao')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 1/3)

def test_hamann():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Hamann')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == -1.0
    assert_allclose(scores[1], -1/3)
    assert_allclose(scores[2], 1/3)

def test_sorensondice():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='SorensonDice')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 2/3)

def test_dice():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Dice')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert scores[2] == 1.0

def test_kulczynski1():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Kulczynski1')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert scores[2] == 1.0

def test_kulczynski2():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Kulczynski2')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 3/4)

def test_simplematching():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='SimpleMatching')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert_allclose(scores[1], 1/3)
    assert_allclose(scores[2], 2/3)

def test_sokal():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='Sokal')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert_allclose(scores[1], 1/2)
    assert_allclose(scores[2], 4/5)

def test_m1():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='M1')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert_allclose(scores[1], 1/2)
    assert scores[2] == 2.0

def test_m2():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula='M2')
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 1/4)

def test_er1a():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="ER1a")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == -1.0
    assert scores[1] == -1.0
    assert scores[2] == 1.0

def test_er1b():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="ER1b")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert_allclose(scores[0], -2/3)
    assert_allclose(scores[1], -1/3)
    assert_allclose(scores[2], 2/3)

def test_wong1():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="Wong1")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert scores[2] == 1.0

def test_wong2():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="Wong2")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == -2.0
    assert scores[1] == -1.0
    assert scores[2] == 0.0

def test_wong3():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="Wong3")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == -2.0
    assert scores[1] == -1.0
    assert scores[2] == 0.0

def test_ample():
    X, y = X_y_sample_1()
    ample = SBFL(formula="Ample")
    ample.fit(X, y)
    scores = ample.scores_
    assert scores[0] == 1.0
    assert_allclose(scores[1], 1/2)
    assert_allclose(scores[2], 1/2)

def test_dstar2():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="Dstar2")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert scores[2] == 1.0

def test_gp02():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="GP02")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert_allclose(scores[0], 4.242641)
    assert_allclose(scores[1], 3.828427)
    assert_allclose(scores[2], 5.828427)

def test_gp03():
    X, y = X_y_sample_1()
    formula = SBFL(formula="GP03")
    formula.fit(X, y)
    scores = formula.scores_
    assert_allclose(scores[0], 1.189207)
    assert scores[1] == 1.0
    assert scores[2] == 0.0

def test_gp13():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="GP13")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 4/3)

def test_gp19():
    X, y = X_y_sample_1()
    sbfl = SBFL(formula="GP19")
    sbfl.fit(X, y)
    scores = sbfl.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert scores[2] == 1.0

def test_er5c():
    X, y = X_y_sample_1()
    formula = SBFL(formula="ER5C")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert scores[2] == 1.0

def test_sbi():
    X, y = X_y_sample_1()
    formula = SBFL(formula="SBI")
    formula.fit(X, y)
    scores = formula.scores_
    assert_allclose(scores[0], 0.0)
    assert_allclose(scores[1], 0.0)
    assert_allclose(scores[2], 0.5)

def test_goodman():
    X, y = X_y_sample_1()
    formula = SBFL(formula="Goodman")
    formula.fit(X, y)
    scores = formula.scores_
    assert_allclose(scores[0], -1.0)
    assert_allclose(scores[1], -1.0)
    assert_allclose(scores[2], 1 / 3)

def test_zoltar():
    X, y = X_y_sample_1()
    formula = SBFL(formula="Zoltar")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 1 / 2)
    
def test_ochiai2():
    X, y = X_y_sample_1()
    formula = SBFL(formula="Ochiai2")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0
    assert scores[1] == 0
    assert_allclose(scores[2], 1 / 2)

def test_anderberg():
    X, y = X_y_sample_1()
    formula = SBFL(formula="Anderberg")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.0
    assert_allclose(scores[2], 1 / 3)

def test_hamming():
    X, y = X_y_sample_1()
    formula = SBFL(formula="Hamming")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0.0
    assert scores[1] == 1.0
    assert scores[2] == 2.0

def test_rogertanimoto():
    X, y = X_y_sample_1()
    formula = SBFL(formula="RogerTanimoto")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0.0
    assert scores[1] == 0.2
    assert scores[2] == 0.5

def test_euclid():
    X, y = X_y_sample_1()
    formula = SBFL(formula="Euclid")
    formula.fit(X, y)
    scores = formula.scores_
    assert scores[0] == 0.0
    assert_allclose(scores[1], 1.0)
    assert_allclose(scores[2], 1.414213562)


"""
Test shallow copy
"""
def test_er1a_deep_copy():
    e_p = np.array([2, 1, 0, 0])
    n_p = np.array([0, 2, 1, 0])
    e_f = np.array([0, 0, 2, 1])
    n_f = np.array([1, 0, 0, 2])
    scores = formula.ER1a(e_p, n_p, e_f, n_f)

    assert_array_equal(scores, np.array([-1, 2, 1, -1]))
    assert_array_equal(n_p, np.array([0, 2, 1, 0]), 'Shallow copy occurred')
