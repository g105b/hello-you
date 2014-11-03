import hello
import unittest



def fun(x):
    return x + 1

class TestMyHelloThing(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.sayHello(), "Hello World!!")
    def test_helloName(self):
    	self.assertEqual(hello.sayName("Martyn"),"Hello Martyn!!")


if __name__ == '__main__':
    unittest.main()