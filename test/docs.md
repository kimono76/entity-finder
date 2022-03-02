In this folder are located the unit tests, end to end test, and integration tests

the [[unittest]] library works by #flashcard 
convention over configuration

For a class to be collected by [[unittest]], the name of the class has to start with #flashcard
```py
    Test<NameOfTheClass>
    #example
    TestClient(unittest.TestCase):
```

For a function to be collected by [[unittest]], the name of the function has to start with #flashcard
```py
    test_<name_of_the_function>
    #example
    def test_givenFunction_whenSomeInput_thenSomeOutput(self):
```

The command for runing the test of [[unittest]] in the [[terminal]] is #flashcard
```sh
    python -m pytest
```