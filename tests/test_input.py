import input_manager


def test_helloworld():

    test_input = input_manager.get_input_by_name('a')
    test_input.set_keydown(True)

    assert test_input.get_keydown() is True
