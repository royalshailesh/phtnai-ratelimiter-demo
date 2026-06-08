from src.store import hit, reset


def test_hit_counts_within_window():
    reset("k")
    assert hit("k", 60) == 1
    assert hit("k", 60) == 2


def test_reset_clears():
    hit("k2", 60)
    reset("k2")
    assert hit("k2", 60) == 1
