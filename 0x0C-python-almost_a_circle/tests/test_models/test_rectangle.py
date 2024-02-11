#!/usr/bin/python3
"""Unittest for rectangle.py is defined"""
import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstance(unittest.TestCase):
    """Unittest for instantiating instances of the Rectangle class"""

    def testbaseinstance(self):
        """Test: to verify rectangle is an instance of Base class"""
        self.assertIsInstance(Rectangle(13, 5), Base)

    def testnoarguments(self):
        """Test: to check when Rectangle is argument-free"""
        with self.assertRaises(TypeError):
            Rectangle()

    def testoneargument(self):
        """Test: to check when rectangle has one argument"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testtwoarguments(self):
        """Test: to check when rectangle has two arguments"""
        ret1 = Rectangle(2, 12)
        ret2 = Rectangle(12, 2)
        self.assertEqual(ret1.id, ret2.id - 1)

    def testthreearguments(self):
        """Test: to check when rectangle has three arguments"""
        ret1 = Rectangle(2, 12, 5)
        ret2 = Rectangle(12, 2, 6)
        self.assertEqual(ret1.id, ret2.id - 1)

    def testfourarguments(self):
        """Test: to check when rectangle has four arguments"""
        ret1 = Rectangle(2, 12, 5, 9)
        ret2 = Rectangle(12, 2, 6, 5)
        self.assertEqual(ret1.id, ret2.id - 1)

    def testfivearguments(self):
        """Test: to check when rectangle has five arguments"""
        self.assertEqual(9, Rectangle(11, 4, 6, 8, 9).id)

    def testabovefiveargs(self):
        """Test: to check when rectangle has multiple arguments"""
        with self.assertRaises(TypeError):
            Rectangle(3, 5, 7, 9, 2, 4,)

    def testprivatewidth(self):
        """Test: to check when accessing __width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 7, 2, 3, 8).__width)

    def testprivateheight(self):
        """Test: to check when accessing __height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 7, 4, 1).__height)

    def testprivatex(self):
        """Test: to check when accessing __x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 4, 6, 2, 3).__x)

    def testprivatey(self):
        """Test: to check when accessing __y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 6, 7, 9, 2).__y)

    def testwidthgetter(self):
        """Test: to get the width"""
        ret = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(9, ret.width)

    def testheightgetter(self):
        """Test: to get the height"""
        ret = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(6, ret.height)

    def testxgetter(self):
        """Test: to get the x coordinate"""
        ret = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(3, ret.x)

    def testygetter(self):
        """Test: to get the y coordinate"""
        ret = Rectangle(9, 6, 3, 2, 1)
        self.assertEqual(2, ret.y)

    def testwidthsetter(self):
        """Test: to set the width"""
        ret = Rectangle(9, 6, 3, 2, 1)
        ret.width = 12
        self.assertEqual(12, ret.width)

    def testheightsetter(self):
        """Test: to set the height"""
        ret = Rectangle(9, 6, 3, 2, 1)
        ret.height = 8
        self.assertEqual(8, ret.height)

    def testxsetter(self):
        """Test: to set the x coordinate"""
        ret = Rectangle(9, 6, 3, 2, 1)
        ret.x = 5
        self.assertEqual(5, ret.x)

    def testysetter(self):
        """Test: to set the y coordinate"""
        ret = Rectangle(9, 6, 3, 2, 1)
        ret.y = 4
        self.assertEqual(4, ret.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittest for initialization of width attribute Rectangle class"""

    def testinvalidwidthnone(self):
        """Test: to check for invalid width: None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 7)

    def testinvalidwidthstr(self):
        """Test: to check for invalid width: String"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a_string", 4)

    def testinvalidwidthlist(self):
        """Test: to check for invalid width: List"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4, 6], 8)

    def testinvalidwidthtuple(self):
        """Test: to check for invalid width: Tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 3, 5), 7)

    def testinvalidwidthdict(self):
        """Test: to check for invalid width: Dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"key": 9, "val": 4}, 7)

    def testinvalidwidthset(self):
        """Test: to check for invalid width: Set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 4, 7}, 2)

    def testinvalidwidthfrozenset(self):
        """Test: to check for invalid width: Frozenset"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, 5, 8}), 3)

    def testinvalidwidthfloat(self):
        """Test: to check for invalid width: Float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.8, 3)

    def testinvalidwidthinf(self):
        """Test: to check for invalid width: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 5)

    def testinvalidwidthnan(self):
        """Test: to check invalid width: nan"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 9)

    def testnegativewidth(self):
        """Test: to check width with negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 6)

    def testzerowidth(self):
        """Test: to check width with zero value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def testinvalidwidthcomplex(self):
        """Test: to check for invalid width: Complex number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 9)

    def testinvalidwidthbytes(self):
        """Test: to check for invalid width: Bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Data', 1)

    def testinvalidwidthbytearray(self):
        """Test: to check for invalid width: Bytearray"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'barr'), 7)

    def testinvalidwidthmemoryview(self):
        """Test: to check for invalid width: Memoryview"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'memview'), 8)

    def testinvalidwidthrange(self):
        """Test: to check for invalid width: Range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(4), 3)

    def testinvalidwidthbool(self):
        """Test: to check for invalid width: Bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 3)


class TestRectangleHeight(unittest.TestCase):
    """Unittest for intialization of height attribue for Rectangle"""

    def testinvalidheightnone(self):
        """Test: to check for invalid height: None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, None)

    def testinvalidheightstr(self):
        """Test: to check for invalid height: String"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "a_string")

    def testinvalidheightlist(self):
        """Test: to check for invalid height: List"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, [2, 4, 6])

    def testinvalidheighttuple(self):
        """Test: to check for invalid height: Tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (1, 3, 5))

    def testinvalidheightdict(self):
        """Test: to check for invalid height: Dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, {"key": 9, "val": 4})

    def testinvalidheightset(self):
        """Test: to check for invalid height: Set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 4, 7})

    def testinvalidheightfrozenset(self):
        """Test: to check for invalid height: Frozenset"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, frozenset({2, 5, 8}))

    def testinvalidheightfloat(self):
        """Test: to check for invalid height: Float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 9.8)

    def testinvalidheightinf(self):
        """Test: to check for invalid height: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, float('inf'))

    def testinvalidheightnan(self):
        """Test: to check invalid height: nan"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))

    def testnegativeheight(self):
        """Test: to check height with negative value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, -8)

    def testzeroheight(self):
        """Test: to check height with zero value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)

    def testinvalidheightcomplex(self):
        """Test: to check for invalid height: Complex number"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, complex(4))

    def testinvalidheightbytes(self):
        """Test: to check for invalid height: Bytes"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Data')

    def testinvalidheightbytearray(self):
        """Test: to check for invalid height: Bytearray"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, bytearray(b'barr'))

    def testinvalidheightmemoryview(self):
        """Test: to check for invalid height: Memoryview"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, memoryview(b'memview'))

    def testinvalidheightrange(self):
        """Test: to check for invalid height: Range"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, range(4))

    def testinvalidheightbool(self):
        """Test: to check for invalid height: Bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, True)


class TestRectangleXCoordinate(unittest.TestCase):
    """Unittest for initialization of X coordinate Rectangle"""

    def testinvalidxnone(self):
        """Test: to check for invalid x: None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 2, None)

    def testinvalidxstr(self):
        """Test: to check for invalid x: String"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 7, "a_string", 1)

    def testinvalidxlist(self):
        """Test: to check for invalid x: List"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 1, [2, 4, 6], 4)

    def testinvalidxtuple(self):
        """Test: to check for invalid x: Tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 2, (1, 3, 5), 6)

    def testinvalidxdict(self):
        """Test: to check for invalid x: Dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 2, {"key": 9, "val": 4}, 8)

    def testinvalidxset(self):
        """Test: to check for invalid x: Set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, {1, 4, 7}, 3)

    def testinvalidxfrozenset(self):
        """Test: to check for invalid x: Frozenset"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, frozenset({2, 5, 8}), 4)

    def testinvalidxfloat(self):
        """Test: to check for invalid x: Float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 1, 9.8, 6)

    def testinvalidxinf(self):
        """Test: to check for invalid x: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 2, float('inf'), 6)

    def testinvalidxnan(self):
        """Test: to check invalid x: nan"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, float('nan'), 7)

    def testnegativex(self):
        """Test: to check x with negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(6, 9, -8, 4)

    def testinvalidxcomplex(self):
        """Test: to check for invalid x: Complex number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 2, complex(4), 5)

    def testinvalidxbytes(self):
        """Test: to check for invalid x: Bytes"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 4, b'Data', 3)

    def testinvalidxbytearray(self):
        """Test: to check for invalid x: Bytearray"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 6, bytearray(b'barr'), 5)

    def testinvalidxmemoryview(self):
        """Test: to check for invalid x: Memoryview"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 3, memoryview(b'memview'), 6)

    def testinvalidxrange(self):
        """Test: to check for invalid x: Range"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, range(4), 1)

    def testinvalidxbool(self):
        """Test: to check for invalid x: Bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 8, True, 9)


class TestRectangleYCoordinate(unittest.TestCase):
    """Unittest for initialization of Y coordinate for Rectangle"""

    def testinvalidynone(self):
        """Test: to check for invalid y: None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 2, 7, None)

    def testinvalidystr(self):
        """Test: to check for invalid y: String"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 7, 1, "a_string")

    def testinvalidylist(self):
        """Test: to check for invalid y: List"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 1, 3, [2, 4, 6])

    def testinvalidytuple(self):
        """Test: to check for invalid y: Tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 2, 6, (1, 3, 5))

    def testinvalidydict(self):
        """Test: to check for invalid y: Dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 2, 8, {"key": 9, "val": 4})

    def testinvalidyset(self):
        """Test: to check for invalid y: Set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 3, {1, 4, 7})

    def testinvalidyfrozenset(self):
        """Test: to check for invalid y: Frozenset"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 7, 4, frozenset({2, 5, 8}))

    def testinvalidyfloat(self):
        """Test: to check for invalid y: Float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 1, 5, 9.8)

    def testinvalidyinf(self):
        """Test: to check for invalid y: inf(positive infinity)"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 2, 6, float('inf'))

    def testinvalidynan(self):
        """Test: to check invalid y: nan"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 3, 7, float('nan'))

    def testnegativey(self):
        """Test: to check y with negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(6, 9, 4, -8)

    def testinvalidycomplex(self):
        """Test: to check for invalid y: Complex number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 2, 5, complex(4))

    def testinvalidybytes(self):
        """Test: to check for invalid y: Bytes"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 4, 3, b'Data')

    def testinvalidybytearray(self):
        """Test: to check for invalid y: Bytearray"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 6, 5, bytearray(b'barr'))

    def testinvalidymemoryview(self):
        """Test: to check for invalid y: Memoryview"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 3, 6, memoryview(b'memview'))

    def testinvalidyrange(self):
        """Test: to check for invalid y: Range"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 7, 1, range(4))

    def testinvalidybool(self):
        """Test: to check for invalid y: Bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 8, 9, False)


class TestRectangleInstanceOrder(unittest.TestCase):
    """Unittest for order of attributes in an instance of Rectangle"""

    def testwidthorderbeforeheight(self):
        """Test: to check the attribute order is width before height"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thewidth", "theheight")

    def testwidthorderbeforeX(self):
        """Test: check the attribute order is width before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thewidth", 4, "thex")

    def testwidthbeforeY(self):
        """Test: check the attribute order is width before Y"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thewidth", 4, 7, "theY")

    def testheightbeforeX(self):
        """Test: check the attribute order is height before X"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "theheight", "theX")

    def testheightbeforeY(self):
        """Test: check the attribute order is height before Y"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "theheight", 7, "theY")

    def testXbeforeY(self):
        """Test: to check the attribute order is X before Y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 8, "theX", "theY")


class TestRectangleArea(unittest.TestCase):
    """Unittest for the area method in the Rectangle class"""

    def testsmallrectangle(self):
        """Test: to calcuate the area of a small rectangle"""
        ret = Rectangle(6, 9, 0, 0, 0)
        self.assertEqual(54, ret.area())

    def testbigrectangle(self):
        """Test: to calculate the area of a big/large rectangle"""
        ret = Rectangle(246813579, 135792468, 0, 0, 1)
        self.assertEqual(33515425028322972, ret.area())

    def testchangedattributes(self):
        """Test: to calculate the area after changing the attributes"""
        ret = Rectangle(3, 9, 1, 1, 1)
        ret.width = 8
        ret.height = 5
        self.assertEqual(40, ret.area())

    def testareawithonearg(self):
        """Test: when are method takes in one argument"""
        ret = Rectangle(4, 6, 3, 7, 2)
        with self.assertRaises(TypeError):
            ret.area(1)


class TestRectanglestdout(unittest.TestCase):
    """Unittest for __str__ and display maethods in the Rectangle class"""

    @staticmethod
    def capt_stdout(ret, method):
        """Gets and returns printed text to the stdout
        Args: ret (Rectangle): rectangle to print to the stdout
        method (str): method to run on the ret (rectangle)"""
        capt = StringIO()
        sys.stdout = capt
        if method == "print":
            print(ret)
        else:
            ret.display()
        sys.stdout = sys.__stdout__
        return capt

    def teststrwidthheight(self):
        """Test: __str__ method with width and height"""
        ret = Rectangle(3, 4)
        capt = TestRectanglestdout.capt_stdout(ret, "print")
        exp_output = "[Rectangle] ({}) 0/0 - 3/4\n".format(ret.id)
        self.assertEqual(exp_output, capt.getvalue())

    def teststrwidthheightx(self):
        """Test: __str__ method with width, height and x coordinate"""
        ret = Rectangle(3, 7, 2)
        exp_output = "[Rectangle] ({}) 2/0 - 3/7".format(ret.id)
        self.assertEqual(exp_output, ret.__str__())

    def teststrwidthheightxy(self):
        """Test: __str__ method with width, height, x and y coordinate"""
        ret = Rectangle(3, 5, 6, 2)
        exp_output = "[Rectangle] ({}) 6/2 - 3/5".format(ret.id)
        self.assertEqual(exp_output, str(ret))

    def teststrwidthheightxyid(self):
        """Test: __str__ method with width, height, x, y, id"""
        ret = Rectangle(12, 22, 3, 6, 9)
        self.assertEqual("[Rectangle] (9) 3/6 - 12/22", str(ret))

    def teststrchnagedattr(self):
        """Test: __str__ method with changed attributes"""
        ret = Rectangle(2, 4, 6, 8, [4])
        ret.width = 1
        ret.height = 3
        ret.x = 5
        ret.y = 7
        self.assertEqual("[Rectangle] ([4]) 5/7 - 1/3", str(ret))

    def teststronearg(self):
        """Test: __str__ method with one argument"""
        ret = Rectangle(2, 4, 6, 8, 3)
        with self.assertRaises(TypeError):
            ret.__str__(1)

    def testdisplaywidthheight(self):
        """Test: display method with width and height"""
        ret = Rectangle(3, 4, 0, 0, 0)
        capt = TestRectanglestdout.capt_stdout(ret, "display")
        self.assertEqual("###\n###\n###\n###\n", capt.getvalue())

    def testdisplaywidthheightx(self):
        """Test: display method with width, height and x coordinate"""
        ret = Rectangle(2, 3, 2, 0, 1)
        capt = TestRectanglestdout.capt_stdout(ret, "display")
        self.assertEqual("  ##\n  ##\n  ##\n", capt.getvalue())

    def testdisplaywidthheightxy(self):
        """Test: display method with width, height, x and y coordinate"""
        ret = Rectangle(3, 5, 0, 1, 0)
        capt = TestRectanglestdout.capt_stdout(ret, "display")
        exp_output = "\n###\n###\n###\n###\n###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplaywidthheightxyid(self):
        """Test: display method with width, height, x, y, id"""
        ret = Rectangle(3, 4, 3, 2, 0)
        capt = TestRectanglestdout.capt_stdout(ret, "display")
        exp_output = "\n\n   ###\n   ###\n   ###\n   ###\n"
        self.assertEqual(exp_output, capt.getvalue())

    def testdisplayonearg(self):
        """Test: display method with one argument"""
        ret = Rectangle(2, 4, 6, 8, 3)
        with self.assertRaises(TypeError):
            ret.display(1)


class TestRectangleupdateargs(unittest.TestCase):
    """Unittest for update_args method of the Rectangle class"""

    def testupdateargszero(self):
        """Test: to modify rectangle with zero arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update()
        self.assertEqual("[Rectangle] (3) 6/7 - 12/3", str(ret))

    def testupdateargsone(self):
        """Test: to modify rectangle with one argument"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24)
        self.assertEqual("[Rectangle] (24) 6/7 - 12/3", str(ret))

    def testupdateargstwo(self):
        """Test: to modify rectangle with two arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24, 9)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/3", str(ret))

    def testupdateargsthree(self):
        """Test: to modify rectangle with three arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24, 9, 8)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/8", str(ret))

    def testupdateargsfour(self):
        """Test: to modify rectangle with four arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24, 9, 8, 5)
        self.assertEqual("[Rectangle] (24) 5/7 - 9/8", str(ret))

    def testupdateargsfive(self):
        """Test: to modify rectangle with five arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24, 9, 8, 5, 4)
        self.assertEqual("[Rectangle] (24) 5/4 - 9/8", str(ret))

    def testupdateargsabovefive(self):
        """Test: to modify rectangle with over five arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24, 9, 8, 5, 4, 1)
        self.assertEqual("[Rectangle] (24) 5/4 - 9/8", str(ret))

    def testupdateargsNoneid(self):
        """Test: to modify rectangle id with None"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(None)
        exp_output = "[Rectangle] ({}) 6/7 - 12/3".format(ret.id)
        self.assertEqual(exp_output, str(ret))

    def testupdateargsNoneidandothers(self):
        """Test: to modify rectangle id with None and other attr"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(None, 2, 4, 3, 5)
        exp_output = "[Rectangle] ({}) 3/5 - 2/4".format(ret.id)
        self.assertEqual(exp_output, str(ret))

    def testupdateargstwice(self):
        """Test: to modify rectangle twice"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(24, 9, 8, 5, 4, 1)
        ret.update(16, 5, 8, 9, 2, 1)
        self.assertEqual("[Rectangle] (16) 9/2 - 5/8", str(ret))

    def testupdateinvalidwidthargs(self):
        """Test: to modify width with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            ret.update(24, "a_string")

    def testupdatewidthargswithzero(self):
        """Test: to modify the width value with zero"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            ret.update(18, 0)

    def testupdatewidthargswithnegvalue(self):
        """Test: to modify the width args with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            ret.update(27, -2)

    def testupdateinvalidheightargs(self):
        """Test: to modify height with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            ret.update(24, 5, "a_string")

    def testupdateheightargswithzero(self):
        """Test: to modify the height value with zero"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            ret.update(18, 7, 0)

    def testupdateheightargswithnegvalue(self):
        """Test: to modify the height args with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            ret.update(27, 6, -2)

    def testupdateinvalidxargs(self):
        """Test: to modify x with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            ret.update(24, 5, 9, "a_string")

    def testupdatexargswithnegvalue(self):
        """Test: to modify the x args with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            ret.update(27, 6, 8, -2)

    def testupdateinvalidyargs(self):
        """Test: to modify y with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            ret.update(24, 5, 2, 6, "a_string")

    def testupdateyargswithnegvalue(self):
        """Test: to modify the y args with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            ret.update(27, 6, 8, 7, -2)

    def testupdatewidthargsbeforeheight(self):
        """Test: to modify the width args before height"""
        ret = Rectangle(13, 2, 4, 6, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            ret.update(30, "thewidth", "theheight")

    def testupdatewidthargsbeforex(self):
        """Test: to modify the width args before x"""
        ret = Rectangle(24, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            ret.update(19, "thewidth", 6, "theX")

    def testupdatewidthargsbeforey(self):
        """Test: to modify the width args before y"""
        ret = Rectangle(12, 2, 5, 3, 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            ret.update(23, "thewidth", 11, 9, "theY")

    def testupdateheightargsbeforex(self):
        """Test: to modify the height args before x"""
        ret = Rectangle(24, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            ret.update(19, 4, "theheight", "theX")

    def testupdateheightargsbeforey(self):
        """Test: to modify the height args before y"""
        ret = Rectangle(12, 2, 5, 3, 4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            ret.update(23, 11, "theheight", 9, "theY")

    def testupdatexargsbeforey(self):
        """Test: to modify the x args before y"""
        ret = Rectangle(12, 2, 5, 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            ret.update(23, 11, 10, "thex", "theY")


class TestRectangleupdatekwargs(unittest.TestCase):
    """Unittest for update_kwargs method of  Rectangle class"""

    def testupdatekwargsone(self):
        """Test: to modify rectangle with one argument"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(id=24)
        self.assertEqual("[Rectangle] (24) 6/7 - 12/3", str(ret))

    def testupdatekwargstwo(self):
        """Test: to modify rectangle with two arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(width=9, id=24)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/3", str(ret))

    def testupdatekwargsthree(self):
        """Test to modify rectangle with three arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(width=9, height=8, id=24)
        self.assertEqual("[Rectangle] (24) 6/7 - 9/8", str(ret))

    def testupdatekwargsfour(self):
        """Test: to modify rectangle with four arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(id=24, width=9, height=8, x=5)
        self.assertEqual("[Rectangle] (24) 5/7 - 9/8", str(ret))

    def testupdatekwargsfive(self):
        """Test: to modify rectangle with five arguments"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(id=24, width=9, height=8, x=5, y=4)
        self.assertEqual("[Rectangle] (24) 5/4 - 9/8", str(ret))

    def testupdatekwargsNoneid(self):
        """Test: to modify rectangle id with None"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(id=None)
        exp_output = "[Rectangle] ({}) 6/7 - 12/3".format(ret.id)
        self.assertEqual(exp_output, str(ret))

    def testupdatekwargsNoneidandothers(self):
        """Test: to modify rectangle id with None and other attr"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(id=None, width=2, height=4, x=3, y=5)
        exp_output = "[Rectangle] ({}) 3/5 - 2/4".format(ret.id)
        self.assertEqual(exp_output, str(ret))

    def testupdatekwargstwice(self):
        """Test: to modify rectangle twice"""
        ret = Rectangle(12, 3, 6, 7, 3)
        ret.update(id=24, width=9, height=1)
        ret.update(id=16, width=5, height=8)
        self.assertEqual("[Rectangle] (16) 6/7 - 5/8", str(ret))

    def testupdateinvalidwidthkwargs(self):
        """Test: to modify width with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            ret.update(width="a_string")

    def testupdatewidthkwargswithzero(self):
        """Test: to modify the width value with zero"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            ret.update(width=0)

    def testupdatewidthkwargswithnegvalue(self):
        """Test: to modify the width kwargs with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            ret.update(width=-2)

    def testupdateinvalidheightkwargs(self):
        """Test: to modify height with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            ret.update(height="a_string")

    def testupdateheightkwargswithzero(self):
        """Test: modify the height value to zero"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            ret.update(height=0)

    def testupdateheightkwargswithzero(self):
        """Test: modify the height value with zero"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            ret.update(height=-2)

    def testupdateinvalidxkwargs(self):
        """Test: modify x with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            ret.update(x="a_string")

    def testupdatexkwargswithnegvalue(self):
        """Test: modify x kwargs with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            ret.update(x=-2)

    def testupdateinvalidykwargs(self):
        """Test: modify y with invalid type"""
        ret = Rectangle(12, 1, 3, 5, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            ret.update(y="a_string")

    def testupdateykwargswithnegvalue(self):
        """Test: modify y kwargs with negative value"""
        ret = Rectangle(9, 2, 4, 6, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            ret.update(y=-2)

    def testupdateargsandkwargs(self):
        """Test: to modify args and kwargs"""
        ret = Rectangle(12, 9, 7, 5, 3)
        ret.update(2, 4, height=6, y=8)
        self.assertEqual("[Rectangle] (2) 7/5 - 4/9", str(ret))

    def testpdatekwargswithwrongkeys(self):
        """Test: to modify kwargs with incorret keys"""
        ret = Rectangle(10, 8, 6, 4, 2)
        ret.update(t=5, d=8)
        self.assertEqual("[Rectangle] (2) 6/4 - 10/8", str(ret))

    def testupdatekwargsandsomewrongkeys(self):
        """Test: to modify kwargs and some incorret keys"""
        ret = Rectangle(9, 7, 5, 3, 1)
        ret.update(width=8, id=10, a=4, b=12, x=6, y=4)
        self.assertEqual("[Rectangle] (10) 6/4 - 8/7", str(ret))


class TestRectangletoDictionary(unittest.TestCase):
    """Unittest for to_dictionary method in the Rectangle class"""

    def testoutputmatchtodictionary(self):
        """Test: if return dictionary matches the expected result"""
        ret = Rectangle(16, 12, 8, 4, 2)
        exp_output = {'id': 2, 'x': 8, 'y': 4, 'width': 16, 'height': 12}
        self.assertDictEqual(exp_output, ret.to_dictionary())

    def testnochangeofobject(self):
        """Test: confirm calling update does not alter original object"""
        ret1 = Rectangle(10, 8, 6, 4, 2)
        ret2 = Rectangle(9, 7, 5, 3, 1)
        ret2.update(**ret1.to_dictionary())
        self.assertNotEqual(ret1, ret2)

    def testpassingargtodict(self):
        """Test: checks when argument is passed to dictionary"""
        ret = Rectangle(10, 7, 6, 3, 2)
        with self.assertRaises(TypeError):
            ret.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
