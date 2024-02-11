#!/usr/bin/python3
"""Unittest for square.py is defined"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.square import Square


class TestSquareInstance(unittest.TestCase):
    """Unittest for instantiating objects of the Square class"""

    def testbaseinstance(self):
        """Test: to confirm square is an instance of Base class"""
        self.assertIsInstance(Square(18), Base)

    def testrectangleinstance(self):
        """Test: to confirm square is an instance of Rectangle class"""
        self.assertIsInstance(Square(12), Square)

    def testnoarguments(self):
        """Test: to verify when Square has no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def testoneargument(self):
        """Test: to verify when Square has one argument"""
        sqe1 = Square(8)
        sqe2 = Square(6)
        self.assertEqual(sqe1.id, sqe2.id - 1)

    def testtwoarguments(self):
        """Test: to verify when Square has two arguments"""
        sqe1 = Square(9, 3)
        sqe2 = Square(3, 9)
        self.assertEqual(sqe1.id, sqe2.id - 1)

    def testthreearguments(self):
        """Test: to verify when Square has three arguments"""
        sqe1 = Square(8, 4, 4)
        sqe2 = Square(4, 4, 8)
        self.assertEqual(sqe1.id, sqe2.id - 1)

    def testfourarguments(self):
        """Test: to verify when square has four arguments"""
        self.assertEqual(9, Square(8, 3, 3, 9).id)

    def testoverfourarguments(self):
        """Test: to verify when Square has over four arguments"""
        with self.assertRaises(TypeError):
            Square(10, 8, 5, 4, 2)

    def testprivatesize(self):
        """Test: to check when accessing __size"""
        with self.assertRaises(AttributeError):
            print(Square(9, 7, 5, 3).___size)

    def testsizegetter(self):
        """Test: to get size"""
        self.assertEqual(8, Square(8, 6, 4, 2).size)

    def testsizesetter(self):
        """Test: to set size"""
        sqe = Square(8, 4, 6, 2)
        sqe.size = 9
        self.assertEqual(9, sqe.size)

    def testwidthgetter(self):
        """Test: to get width"""
        sqe = Square(8, 4, 6, 2)
        sqe.width = 9
        self.assertEqual(9, sqe.width)

    def testheightgetter(self):
        """Test: to get height"""
        sqe = Square(8, 4, 6, 2)
        sqe.height = 9
        self.assertEqual(9, sqe.height)

    def testxgetter(self):
        """Test: to get x coordinates"""
        self.assertEqual(0, Square(9).x)

    def testygetter(self):
        """Test: to get the y coordinates"""
        self.assertEqual(0, Square(9).y)


class TestSquaresize(unittest.TestCase):
    """Unittest for initialization of the size attribute of Square"""

    def testinvalidsizenone(self):
        """Test: to check for invalid size: None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def testinvalidsizestr(self):
        """Test: to check for invalid size: String"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("a_string")

    def testinvalidsizelist(self):
        """Test: to check for invalid size: List"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 4, 6])

    def testinvalidsizetuple(self):
        """Test: to check for invalid size: Tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 3, 5), 8, 9)

    def testinvalidsizedict(self):
        """Test: to check for invalid size: Dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"key": 9, "val": 4}, 7)

    def testinvalidsizeset(self):
        """Test: to check for invalid size: Set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 4, 7}, 2)

    def testinvalidsizefrozenset(self):
        """Test: to check for invalid size: Frozenset"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({2, 5, 8}))

    def testinvalidsizefloat(self):
        """Test: to check for invalid size: Float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.8)

    def testinvalidsizeinf(self):
        """Test: to check for invalid size: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def testinvalidsizenan(self):
        """Test: to check invalid size: nan"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def testnegativesize(self):
        """Test: to check size with negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-8, 6)

    def testzerosize(self):
        """Test: to check size with zero value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 3)

    def testinvalidsizecomplex(self):
        """Test: to check for invalid size: Complex number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(4))

    def testinvalidsizebytes(self):
        """Test: to check for invalid size: Bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Data')

    def testinvalidsizebytearray(self):
        """Test: to check for invalid size: Bytearray"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'barr'))

    def testinvalidsizememoryview(self):
        """Test: to check for invalid size: Memoryview"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'memview'))

    def testinvalidsizerange(self):
        """Test: to check for invalid size: Range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(4))

    def testinvalidsizebool(self):
        """Test: to check for invalid size: Bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 3, 4)


class TestSquareXCoordinate(unittest.TestCase):
    """Unittest for initialization of X coordinate attribute of Square"""

    def testinvalidxnone(self):
        """Test: to check for invalid x: None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, None)

    def testinvalidxstr(self):
        """Test: to check for invalid x: String"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(4, "a_string", )

    def testinvalidxlist(self):
        """Test: to check for invalid x: List"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, [2, 4, 6])

    def testinvalidxtuple(self):
        """Test: to check for invalid x: Tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, (1, 3, 5))

    def testinvalidxdict(self):
        """Test: to check for invalid x: Dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, {"key": 9, "val": 4}, 8)

    def testinvalidxset(self):
        """Test: to check for invalid x: Set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 4, 7})

    def testinvalidxfrozenset(self):
        """Test: to check for invalid x: Frozenset"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, frozenset({2, 5, 8}))

    def testinvalidxfloat(self):
        """Test: to check for invalid x: Float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 9.8)

    def testinvalidxinf(self):
        """Test: to check for invalid x: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, float('inf'), 6)

    def testinvalidxnan(self):
        """Test: to check invalid x: nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, float('nan'), 7)

    def testnegativex(self):
        """Test: to check x with negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(6, -8, 4)

    def testinvalidxcomplex(self):
        """Test: to check for invalid x: Complex number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, complex(4))

    def testinvalidxbytes(self):
        """Test: to check for invalid x: Bytes"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Data')

    def testinvalidxbytearray(self):
        """Test: to check for invalid x: Bytearray"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, bytearray(b'barr'))

    def testinvalidxmemoryview(self):
        """Test: to check for invalid x: Memoryview"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, memoryview(b'memview'))

    def testinvalidxrange(self):
        """Test: to check for invalid x: Range"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, range(4))

    def testinvalidxbool(self):
        """Test: to check for invalid x: Bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, True)


class TestSquareYCoordinate(unittest.TestCase):
    """Unittest for initialization of Y coordinate attribute of Square"""

    def testinvalidynone(self):
        """Test: to check for invalid y: None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 2, None)

    def testinvalidystr(self):
        """Test: to check for invalid y: String"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 7, "a_string")

    def testinvalidylist(self):
        """Test: to check for invalid y: List"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 1, [2, 4, 6])

    def testinvalidytuple(self):
        """Test: to check for invalid y: Tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 2, (1, 3, 5))

    def testinvalidydict(self):
        """Test: to check for invalid y: Dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 2, {"key": 9, "val": 4})

    def testinvalidyset(self):
        """Test: to check for invalid y: Set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 5, {1, 4, 7})

    def testinvalidyfrozenset(self):
        """Test: to check for invalid y: Frozenset"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 7, frozenset({2, 5, 8}))

    def testinvalidyfloat(self):
        """Test: to check for invalid y: Float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 5, 9.8)

    def testinvalidyinf(self):
        """Test: to check for invalid y: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 6, float('inf'))

    def testinvalidynan(self):
        """Test: to check invalid y: nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 7, float('nan'))

    def testnegativey(self):
        """Test: to check y with negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(6, 4, -8)

    def testinvalidycomplex(self):
        """Test: to check for invalid y: Complex number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 5, complex(4))

    def testinvalidybytes(self):
        """Test: to check for invalid y: Bytes"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 4, b'Data')

    def testinvalidybytearray(self):
        """Test: to check for invalid y: Bytearray"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 5, bytearray(b'barr'))

    def testinvalidymemoryview(self):
        """Test: to check for invalid y: Memoryview"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 6, memoryview(b'memview'))

    def testinvalidyrange(self):
        """Test: to check for invalid y: Range"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 1, range(4))

    def testinvalidybool(self):
        """Test: to check for invalid y: Bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 9, False)


class TestSquareInstanceOrder(unittest.TestCase):
    """Unittest for order of attributes in instances of Square class"""

    def testsizeorderbeforex(self):
        """Test: to check the attribute order is size before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("thesize", "thex")

    def testsizeorderbeforey(self):
        """Test: to check the attribute order is size before y"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("thesize", 2, "theY")

    def testxorderbeforey(self):
        """Test: to check the attribute order is x before y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, "thex", "theY")


class TestSquareArea(unittest.TestCase):
    """Unittest for the area method in the Square class"""

    def testsmallsquare(self):
        """Test: to calcuate the area of a small square"""
        self.assertEqual(144, Square(12, 0, 0, 1).area())

    def testbigsquare(self):
        """Test: to calculate the area of a large/big square"""
        sqe = Square(246813579, 0, 0, 1)
        self.assertEqual(60916942778789241, sqe.area())

    def testchangedattributes(self):
        """Test: to calculate the area after changing the attributes"""
        sqe = Square(3, 0, 0, 1)
        sqe.size = 8
        self.assertEqual(64, sqe.area())

    def testareawithonearg(self):
        """Test: when are method takes in one argument"""
        sqe = Square(4, 6, 3, 7)
        with self.assertRaises(TypeError):
            sqe.area(1)


class TestSquarestdout(unittest.TestCase):
    """Unittest for __str__ and display maethods in the Square class"""

    @staticmethod
    def capt_stdout(sqe, method):
        """Gets and return printed text to the stdout
        Args: sqe (Square): square to print to the stdout
        method (str): method to run on the sqe (square)"""
        capt = StringIO()
        sys.stdout = capt
        if method == "print":
            print(sqe)
        else:
            sqe.display()
        sys.stdout = sys.__stdout__
        return capt

    def teststrsize(self):
        """Test: __str__ method with size"""
        sqe = Square(3)
        capt = TestSquarestdout.capt_stdout(sqe, "print")
        exp_output = "[Square] ({}) 0/0 - 3\n".format(sqe.id)
        self.assertEqual(exp_output, capt.getvalue())

    def teststrsizex(self):
        """Test: __str__ method with size and x coordinate"""
        sqe = Square(3, 2)
        exp_output = "[Square] ({}) 2/0 - 3".format(sqe.id)
        self.assertEqual(exp_output, sqe.__str__())

    def teststrsizexy(self):
        """Test: __str__ method with size, x and y coordinate"""
        sqe = Square(3, 6, 2)
        exp_output = "[Square] ({}) 6/2 - 3".format(sqe.id)
        self.assertEqual(exp_output, str(sqe))

    def teststrsizexyid(self):
        """Test: __str__ method with size, x, y, id"""
        sqe = Square(12, 3, 6, 9)
        self.assertEqual("[Square] (9) 3/6 - 12", str(sqe))

    def teststrchnagedattr(self):
        """Test: __str__ method with changed attributes"""
        sqe = Square(2, 6, 8, [4])
        sqe.size = 1
        sqe.x = 5
        sqe.y = 7
        self.assertEqual("[Square] ([4]) 5/7 - 1", str(sqe))

    def teststronearg(self):
        """Test: __str__ method with one argument"""
        sqe = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            sqe.__str__(1)

    def testdisplaysize(self):
        """Test: display method with size"""
        sqe = Square(3, 0, 0, 1)
        capt = TestSquarestdout.capt_stdout(sqe, "display")
        self.assertEqual("###\n###\n###\n", capt.getvalue())

    def testdisplaysizex(self):
        """Test: display method with size and x coordinate"""
        sqe = Square(2, 1, 0, 6)
        capt = TestSquarestdout.capt_stdout(sqe, "display")
        self.assertEqual(" ##\n ##\n", capt.getvalue())

    def testdisplaysizexy(self):
        """Test: display method with size, x and y coordinate"""
        sqe = Square(3, 0, 1, 7)
        capt = TestSquarestdout.capt_stdout(sqe, "display")
        exp_output = "\n###\n###\n###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplaysizexyid(self):
        """Test: display method with size, x, y, id"""
        sqe = Square(3, 3, 2, 1)
        capt = TestSquarestdout.capt_stdout(sqe, "display")
        exp_output = "\n\n   ###\n   ###\n   ###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplayonearg(self):
        """Test: display method with one argument"""
        sqe = Square(2, 4, 6, 8)
        with self.assertRaises(TypeError):
            sqe.display(1)


class TestSquareupdateargs(unittest.TestCase):
    """Unittest for update_args method in the Square class."""

    def testupdateargszero(self):
        """Test: to modify square with zero arguments"""
        sqe = Square(13, 13, 13, 13)
        sqe.update()
        self.assertEqual("[Square] (13) 13/13 - 13", str(sqe))

    def testupdateargsone(self):
        """Test: to modify square with one argument"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89)
        self.assertEqual("[Square] (89) 13/13 - 13", str(sqe))

    def testupdateargstwo(self):
        """Test: to modify square with two arguments"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 2)
        self.assertEqual("[Square] (89) 13/13 - 2", str(sqe))

    def testupdateargsthree(self):
        """Test: to modify square with three arguments"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/13 - 2", str(sqe))

    def testupdateargsfour(self):
        """Test: to modify square with four arguments"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqe))

    def testupdateargsmorethanfour(self):
        """Test: to modify square with over four arguments"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(sqe))

    def testupdateargswidthsetter(self):
        """Test: to modify the width setter"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 6)
        self.assertEqual(6, sqe.width)

    def testupdateargsheightsetter(self):
        """Test: to modify the height setter"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 6)
        self.assertEqual(6, sqe.height)

    def testupdateargsNoneid(self):
        """Test: to modify square id with None"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(None)
        exp_output = "[Square] ({}) 13/13 - 13".format(sqe.id)
        self.assertEqual(exp_output, str(sqe))

    def testupdateargsNoneidandmore(self):
        """Test: to modify square id with None and other attr"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(None, 4, 5)
        exp_output = "[Square] ({}) 5/13 - 4".format(sqe.id)
        self.assertEqual(exp_output, str(sqe))

    def testupdateargstwice(self):
        """Test: to modify square twice"""
        sqe = Square(13, 13, 13, 13)
        sqe.update(89, 2, 3, 4)
        sqe.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(sqe))

    def testupdateargsinvalidsizetype(self):
        """Test: to modify size with invalid type"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqe.update(89, "not_valid")

    def testupdateargssizezero(self):
        """Test: to modify the value of size with zero"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqe.update(89, 0)

    def testupdateargssizenegative(self):
        """Test: to modify the size args with negative value"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqe.update(89, -4)

    def testupdateargsinvalidx(self):
        """Test: to modify x with invalid type"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqe.update(89, 1, "not_valid")

    def testupdateargsxnegative(self):
        """Test: to modify the x args with negative value"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqe.update(98, 1, -4)

    def testupdateargsinvalidy(self):
        """Test: to modify y with invalid type"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqe.update(89, 1, 2, "not_valid")

    def testupdateargsynegative(self):
        """Test: to modify the y args with negative value"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqe.update(98, 1, 2, -4)

    def testupdateargssizebeforex(self):
        """Test: to modify the size args before x"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqe.update(89, "not_valid", "not_valid")

    def testupdateargssizebeforey(self):
        """Test: to modify the size args before y"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqe.update(89, "not_valid", 2, "not_valid")

    def testupdateargsxbeforey(self):
        """Test: to modify the x args before y"""
        sqe = Square(13, 13, 13, 13)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqe.update(89, 1, "not_valid", "not_valid")


class TestSquareupdatekwargs(unittest.TestCase):
    """Unittest for update_kwargs method in the Square class."""

    def testupdatekwargsone(self):
        """Test: to modify square with one argument"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32)
        self.assertEqual("[Square] (32) 27/27 - 27", str(sqe))

    def testupdatekwargstwo(self):
        """Test: to modify square with two arguments"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32, size=2)
        self.assertEqual("[Square] (32) 27/27 - 2", str(sqe))

    def testupdatekwargsthree(self):
        """Test: to modify square with three arguments"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32, size=2, x=3)
        self.assertEqual("[Square] (32) 3/27 - 2", str(sqe))

    def testupdatekwargsfour(self):
        """Test: to modify square with four arguments"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32, size=2, x=3, y=4)
        self.assertEqual("[Square] (32) 3/4 - 2", str(sqe))

    def testupdatekwargswidthsetter(self):
        """Test: to modify the width setter"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32, size=6)
        self.assertEqual(6, sqe.width)

    def testupdatekwargsheightsetter(self):
        """Test: to modify the height setter"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32, size=6)
        self.assertEqual(6, sqe.height)

    def testupdatekwargsNoneid(self):
        """Test: to modify square id with None"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=None)
        exp_output = "[Square] ({}) 27/27 - 27".format(sqe.id)
        self.assertEqual(exp_output, str(sqe))

    def testupdatekwargsNoneidandmore(self):
        """Test: to modify square id with None and other attr"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=None, size=4, x=5)
        exp_output = "[Square] ({}) 5/27 - 4".format(sqe.id)
        self.assertEqual(exp_output, str(sqe))

    def testupdatekwargstwice(self):
        """Test: to modify square twice"""
        sqe = Square(27, 27, 27, 27)
        sqe.update(id=32, size=2, x=3)
        sqe.update(id=4, size=3, x=2, y=32)
        self.assertEqual("[Square] (4) 2/32 - 3", str(sqe))

    def testupdatekwargsinvalidsizetype(self):
        """Test: to modify size with invalid type"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqe.update(size="not_valid")

    def testupdatekwargssizezero(self):
        """Test: to modify the value of size with zero"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqe.update(size=0)

    def testupdatekwargssizenegative(self):
        """Test: to modify the size kwargs with negative value"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqe.update(size=-4)

    def testupdatekwargsinvalidx(self):
        """Test: to modify x with invalid type"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqe.update(x="not_valid")

    def testupdatekwargsxnegative(self):
        """Test: to modify the x kwargs with negative value"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqe.update(x=-4)

    def testupdatekwargsinvalidy(self):
        """Test: to modify y with invalid type"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqe.update(y="not_valid")

    def testupdatekwargsynegative(self):
        """Test: to modify the y kwargs with negative value"""
        sqe = Square(27, 27, 27, 27)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqe.update(y=-4)

    def testupdateargsandkwargs(self):
        """Test: to modify args and kwargs"""
        sqe = Square(9, 7, 5, 3)
        sqe.update(23, 5, x=17)
        self.assertEqual("[Square] (23) 7/5 - 5", str(sqe))

    def testpdatekwargswithwrongkeys(self):
        """Test: to modify kwargs with wrong keys"""
        sqe = Square(10, 8, 6, 4)
        sqe.update(t=4, d=7)
        self.assertEqual("[Square] (4) 8/6 - 10", str(sqe))

    def testupdatekwargsandsomewrongkeys(self):
        """Test: to modify kwargs and some wrong keys"""
        sqe = Square(9, 7, 5, 3)
        sqe.update(size=8, id=2, t=6, d=31)
        self.assertEqual("[Square] (2) 7/5 - 8", str(sqe))


class TestSquaretoDictionary(unittest.TestCase):
    """Unittest for the to_dictionary method in the Square class"""

    def testoutputmatchtodictionary(self):
        """Test: if return dictionary aligns the expected result"""
        sqe = Square(16, 8, 4, 2)
        exp_output = {'id': 2, 'x': 8, 'y': 4, 'size': 16}
        self.assertDictEqual(exp_output, sqe.to_dictionary())

    def testnochangeofobject(self):
        """Test: to confirm calling update does not alter original object"""
        sqe1 = Square(10, 8, 6, 2)
        sqe2 = Square(9, 7, 1)
        sqe2.update(**sqe1.to_dictionary())
        self.assertNotEqual(sqe1, sqe2)

    def testpassingargtodict(self):
        """Test: to verify when argument is passed to dictionary"""
        sqe = Square(10, 7, 6, 3)
        with self.assertRaises(TypeError):
            sqe.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
