from um import count

def test_um():
    assert count("um, wrum, rum, um...") == 2
    assert count("Mom, where's my VODKA?") == 0

def test_case():
    assert count("Um, um, MUM, MuMm, uM, UM") == 4
    assert count(".UM...") == 1

def test_space():
    assert count("   )  &ô  um     -  .  ") == 1
    assert count(" u m ") == 0
