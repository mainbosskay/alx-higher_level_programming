#!/usr/bin/python3
"""Defining Unittest for base.py"""
import unittest
from os import remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstance(unittest.TestCase):
    """Unittest to create instances of Base class"""

    def test_incr_id_no_arg(self):
        """Test base with no arguments the increments ID properly"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_incr_id_three_bases(self):
        """Test base with three instances the increments ID correctly"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_incr_id_None(self):
        """Test checks ID increments correctly when initialized with None"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_assign_unique_id(self):
        """Test confirms the correct ID of a unique ID when initialized"""
        self.assertEqual(23, Base(23).id)

    def test_inst_after_unique_id(self):
        """Test validates the instance count post-unique ID assignment"""
        base1 = Base()
        base2 = Base(19)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_public_id_mod(self):
        """Test public modification of ID after instantation"""
        base = Base(23)
        base.id = 19
        self.assertEqual(19, base.id)

    def test_private_nb_inst(self):
        """Test __nb_instances attribute is private"""
        with self.assertRaises(AttributeError):
            print(Base(23).__nb_instances)

    def test_inst_with_two_args(self):
        """Test assesses base handling instances with two arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_string_id(self):
        """Test if string ID is handled correctly"""
        self.assertEqual("test", Base("test").id)

    def test_dictionary_id(self):
        """Test if dictionary ID is handled correctly"""
        seld.assertEqual({"key": 2, "val": 3}, Base({"key": 2, "val": 3}).id)

    def test_list_id(self):
        """Test list ID is handled correctly"""
        self.assertEqual([2, 3, 9], Base([2, 3, 9]).id)

    def test_tuple_id(self):
        """Test evaluates correct handling of tuple ID"""
        self.assertEqual((9, 2), Base((9, 2)).id)

    def test_float_id(self):
        """Test evaluates correct handling of float ID"""
        self.assertEqual(9.8, Base(9.8).id)

    def test_inf_id(self):
        """Test evaluates correct handling of inf ID"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """Test evaluates correct handling of NaN ID"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_complex_id(self):
        """Test evaluates correct handling of complex ID"""
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_bool_id(self):
        """Test evaluates correct handling of bool ID"""
        self.assertEqual(False, Base(False).id)

    def test_set_id(self):
        """Test evaluates correct handling of set ID"""
        self.assertEqual({2, 3, 4}, Base({2, 3, 4}).id)

    def test_frozenset_id(self):
        """Test evaluates correct handling of frozenset ID"""
        self.assertEqual(frozenset({2, 3, 9}), Base({2, 3, 9}).id)

    def test_range_id(self):
        """Test evaluates correct handling of range ID"""
        self.assertEqual(range(8), Base(range(8)).id)

    def test_bytes_id(self):
        """Test evaluates correct handling of bytes ID"""
        self.assertEqual(b'Test', Base(b'Test').id)

    def test_bytearray_id(self):
        """Test evaluates correct handling of byte array ID"""
        self.assertEqual(bytearray(b'val'), Base(bytearray(b'val')).id)

    def test_memoryview_id(self):
        """Test evaluates correct handling of memory view ID"""
        self.assertEqual(memoryview(b'key'), Base(memoryview(b'key')).id)


class TestBasetojsonstring(unittest.TestCase):
    """Unittest for converting instances of Base class to JSON strings"""

    def test_to_json_string_rect_type(self):
        """Test validates to_json_string for rectangles"""
        rect = Rectangle(10, 9, 6, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_rect_one_dict(self):
        """Test to_json_string length for a rectangle"""
        rect = rectangle(10, 9, 6, 4, 5)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_to_json_string_rect_two_dict(self):
        """Test to_json_string length for two rectangle dict"""
        rect1 = Rectangle(2, 4, 6, 18, 3)
        rect2 = Rectangle(2, 4, 3, 6, 12)
        lst_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lst_dicts)) == 106)

    def test_to_json_string_sqr_type(self):
        """Test to_json_string outputs a string for a square"""
        sqre = Square(10, 5, 7, 8)
        self.assertEqual(str, type(Base.to_json_string([sqre.to_dictionary()])))

    def test_to_json_string_sqr_one_dict(self):
        """Test to_json_string outputs length for one square dict"""
        sqre = Square(10, 5, 7, 8)
        self.assertTrue(len(Base.to_json_string([sqre.to_dictionary()])) == 39)

    def test_to_json_string_sqr_two_dict(self):
        """Test to_json_string outputs length for two square dict"""
        sqre1 = Square(15, 10, 9, 6)
        sqre2 = Square(6, 8, 10, 28)
        lst_dicts = [sqre1.to_dictionary(), sqre2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lst_dicts)) == 78)

    def test_to_json_string_empt_lst(self):
        """Test to_json_string for empty list"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """Test to_json_string for None list"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """Test for to_json_string with an empty argument list"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_err_more_than_one_arg(self):
        """Test for to_json_string with more than one argument list"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBasesavetofile(unittest.TestCase):
    """Unittest for saving instances of the Base class to a file"""

    @classmethod
    def tearDown(self):
        """Checks and deletes created files"""
        try:
           remove("Rectangle.json")
        except IOError:
            pass
        try:
            remove("Square.json")
        except IOError:
            pass
        try:
            remove("Base.json")
        except IOError:
            pass

    def test_savetofile_onerect(self):
        """Test: save_to_file creating one rectangle file"""
        rect = Rectangle(15, 7, 8, 10, 4)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 53)

    def test_savetofile_tworect(self):
        """Test: save_to_file creating two rectangle file"""
        rect1 = Rectangle(14, 7, 10, 9, 3)
        rect2 = Rectangle(5, 7, 8, 10, 15)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 106)

    def test_savetofile_onesqr(self):
        """Test: save_to_file creating one square file"""
        sqre = Square(8, 6, 4, 2)
        Square.save_to_file([sqre])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 38)

    def test_savetofile_twosqr(self):
        """Test: save_to_file creating two squares file"""
        sqre1 = Square(9, 6, 7, 8)
        sqre2 = Square(5, 4, 3, 8)
        Square.save_to_file([sqre1, sqre2])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 76)

    def test_savetofile_clsnameforfilename(self):
        """Test: save_to_file uses class name as filename"""
        sqre = Square(9, 6, 3, 7)
        Base.save_to_file([sqre])
        with open("Base.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 39)

    def test_savetofile_overwrite(self):
        """Test: save_to_file overwrites file content"""
        sqre = Square(4, 9, 6, 28)
        Square.save_to_file([sqre])
        sqr = Square(14, 8, 7, 10)
        Square.save_to_file([sqre])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 39)

    def test_savetofile_empt_list(self):
        """Test: save_to_file hamdles empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as fl:
            self.assertEqual("[]", fl.read())

    def test_savetofile_none(self):
        """Test: save_to_file when provided with a None list"""
        Square.save_to_file(None)
        with open("Square.json", "r") as fl:
            self.assertEqual("[]", fl.read())

    def test_savetofile_noargs(self):
        """Test: save_to_file for an arguments-free list"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_savetofile_errmorethanonearg(self):
        """Test: save_to_file with multi-argument list"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBasefromjsonstring(unittest.TestCase):
    """Unittest for instantiating Base class instances from JSON strings"""

     def testfromjsonstringtype(self):
         """Test: from_json_string returns list of rectangle dict"""
        s_data = [{"id": 23, "width": 15, "height": 7}]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(list, type(ds_data))

    def testfromjsonstringonerect(self):
        """Test: from_json_string to return accurate output for one rectangle"""
        s_data = [{"id": 77, "width": 23, "height": 4, "x": 8}]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringtworect(self):
        """Test: from_json_string to return accurate output for two rectangles"""
        s_data = [
            {"id": 33, "width": 15, "height": 8, "x": 2, "y": 7},
            {"id": 65, "width": 9, "height": 3, "x": 4, "y": 8}
        ]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringonesqr(self):
        """Test: from_json_string to return accurate output for one square"""
        s_data = [{"id": 22, "size": 12, "height": 5}]
        json_dt = Square.to_json_string(s_data)
        ds_data = Square.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringtwosqr(self):
        """Test: from_json_string to return accurate output for two squares"""
        s_data = [
            {"id": 23, "size": 15, "height": 8},
            {"id": 6, "size": 9, "height": 3}
        ]
        json_dt = Square.to_json_string(s_data)
        ds_data = Square.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringemptlist(self):
        """Test: from_json_string with an empty list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def testfromjsonstringnone(self):
        """Test: from_json_string with a None list"""
        self.assertEqual([], Base.from_json_string(None))

    def testfromjsonstringnoaargs(self):
        """Test: from_json_string with arguments-free list"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testfromjsonstringerrmorethanonearg(self):
        """Test: from_json_string with multi-argument list"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBasecreate(unittest.TestCase):
    """Unittest for instantiating instances with the create method of Base class"""

    def testcreateoriginalrect(self):
        """Test: create method to return original rectangle"""
        rect1 = Rectangle(2, 5, 8, 3, 4)
        rect1_dct = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dct)
        self.assertEqual("[Rectangle] (4) 8/3 - 2/5", str(rect1))

    def testcreatenewrect(self):
        """Test: create method to return new rectangle"""
        rect1 = Rectangle(3, 4, 5, 8, 9)
        rect1_dct = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dct)
        self.assertEqual("[Rectangle] (9) 5/8 - 3/4", str(rect2))

    def testcreaterectinst(self):
        """Test: create to return a new rectangle instance"""
        rect1 = Rectangle(2, 5, 8, 3, 4)
        rect1_dct = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dct)
        self.assertIsNot(rect1, rect2)

    def testcreaterectdiffinst(self):
        """Test: create to return different instance from original"""
        rect1 = Rectangle(2, 5, 8, 3, 4)
        rect1_dct = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dct)
        self.assertNotEqual(rect1, rect2)

    def testcreateoriginalsqr(self):
        """Test: create method to return original square"""
        sqre1 = Square(4, 5, 9, 2)
        sqre1_dct = sqre1.to_dictionary()
        sqre2 = Square.create(**sqre1_dct)
        self.assertEqual("[Square] (2) 5/9 - 4", str(sqre1))

    def testcreatenewsqr(self):
        """Test: create method to return new square"""
        sqre1 = Square(4, 6, 7, 2)
        sqre1_dct = sqre1.to_dictionary()
        sqre2 = Square.create(**sqre1_dct)
        self.assertEqual("[Square] (2) 6/7 - 4", str(sqre2))

    def testcreatesqrinst(self):
        """Test: create method generates a new square instance"""
        sqre1 = Square(4, 5, 9, 2)
        sqre1_dct = sqre1.to_dictionary()
        sqre2 = Square.create(**sqre1_dct)
        self.assertIsNot(sqre1, sqre2)

    def testcreatediffinst(self):
        """Test create to return different instance from original"""
        sqre1 = Square(4, 6, 7, 2)
        sqre1_dct = sqre1.to_dictionary()
        sqre2 = Square.create(**sqre1_dct)
        self.assertNotEqual(sqre1, sqre2)


class TestBaseloadfromfile(unittest.TestCase):
    """Unittest for loading instances of Base class from file"""

    @classmethod
    def tearDown(self):
        """Checks and deletes created files"""
        try:
            remove("Rectangle.json")
        except IOError:
            pass
        try:
            remove("Square.json")
        except IOError:
            pass

    def testloadfromfilestrect(self):
        """Test: load_from_file to retrieve first rectangle from the file"""
        rect1 = Rectangle(14, 9, 7, 11, 3)
        rect2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file([rect1, rect2])
        loaded_rec = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(loaded_rec[0]))

    def testloadfromfilescdrect(self):
        """Test: load_from_file to retrieve second rectangle from the file"""
        rect1 = Rectangle(14, 9, 7, 11, 3)
        rect2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file([rect1, rect2])
        loaded_rec = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(loaded_rec[1]))

    def testloadfromfilerectype(self):
        """Test load_from_file to retrieve a list of rectangles"""
        rect1 = Rectangle(14, 9, 7, 11, 3)
        rect2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file([rect1, rect2])
        loaded_rec = Rectangle.load_from_file()
        self.assertTrue(all(type(objt) == Rectangle for objt in loaded_rec))

    def testloadfromfilefstsqr(self):
        """Test: load_from_file to retrieve the first square from the file"""
        sqre1 = Square(3, 8, 6, 9)
        sqre2 = Square(5, 8, 3, 7)
        Square.save_to_file([sqre1, sqre2])
        loaded_sqr = Square.load_from_file()
        self.assertEqual(str(sqre1), str(loaded_sqr[0]))

    def testloadfromfilescdsqr(self):
        """Test: load_from_file to retrieve the second square from the file"""
        sqre1 = Square(3, 8, 6, 9)
        sqre2 = Square(5, 8, 3, 7)
        Square.save_to_file([sqre1, sqre2])
        loaded_sqr = Square.load_from_file()
        self.assertEqual(str(sqre2), str(loaded_sqr[1]))

    def testloadfromfilesqrtype(self):
        """Test: load_from_file to retrieve list of squares"""
        sqre1 = Square(3, 8, 6, 9)
        sqre2 = Square(5, 8, 3, 7)
        Square.save_to_file([sqre1, sqre2])
        loaded_sqr = Square.load_from_file()
        self.assertTrue(all(type(objt) == Square for objt in loaded_sqr))

    def testloadfromfilenofile(self):
        """Test: load_from_file without a file"""
        loaded_sqr = Square.load_from_file()
        self.assertEqual([], loaded_sqr)

    def testloadfromfileerrmorethanonearg(self):
        """Test: load_from_file with multiple argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBasesavetofilecsv(unittest.TestCase):
    """Unittest for exporting instances of Base class to CSV file"""

    @classmethod
    def tearDown(self):
        """Checks and deletes created files"""
        try:
            remove("Rectangle.csv")
        except IOError:
            pass
        try:
            remove("Square.csv")
        except IOError:
            pass
        try:
            remove("Base.csv")
        except IOError:
            pass

    def testsavetofilecsvonerect(self):
        """Test: save_to_file_csv generates file for one rectangle"""
        rect = Rectangle(13, 8, 4, 11, 9)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as fl:
            self.assertTrue("9,13,8,4,11", fl.read())

    def testsavetofilecsvtworects(self):
        """Test: save_to_file_csv generates file for two rectangles"""
        rect1 = Rectangle(10, 3, 4, 6, 7)
        rect2 = Rectangle(4, 7, 9, 11, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as fl:
            self.assertTrue("7,10,3,4,6\n4,7,9,11,3", fl.read())

    def testsavetofilecsvonesqr(self):
        """Test: save_to_file_csv generates file for one square"""
        sqre = Square(14, 10, 7, 6)
        Square.save_to_file_csv([sqre])
        with open("Square.csv", "r") as fl:
            self.assertTrue("6,14,10,7", fl.read())

    def testsavetofilecsvtwosqrs(self):
        """Test: save_to_file_csv generates file for two squares"""
        sqre1 = Square(12, 6, 2, 5)
        sqre2 = Square(7, 10, 3, 6)
        Square.save_to_file_csv([sqre1, sqre2])
        with open("Square.csv", "r") as fl:
            self.assertTrue("5,12,6,2\n6,7,10,3", fl.read())

    def testsavetofilecsvclsnameforfilename(self):
        """Test: save_to_file_csv uses class name as filename"""
        sqre = Square(14, 10, 6, 11)
        Base.save_to_file_csv([sqre])
        with open("Base.csv", "r") as fl:
            self.assertTrue("11,14,10,6", fl.read())

    def testsavetofilecsvoverwrite(self):
        """Test: save_to_file_csv overwrites file content"""
        sqre = Square(4, 9, 6, 30)
        Square.save_to_file([sqre])
        sqre = Square(14, 7, 9, 11)
        Square.save_to_file_csv([sqre])
        with open("Square.csv", "r") as fl:
            self.assertTrue("11,14,7,9", fl.read())

    def testsavetofilecsvemptlist(self):
        """Test: save_to_file_csv with an empty list"""
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as fl:
            self.assertEqual("[]", fl.read())

    def testsavetofilecsvnone(self):
        """Test: save_to_file_csv with None list"""
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as fl:
            self.assertEqual("[]", fl.read())

    def testsavetofilecsvnoargs(self):
        """Test: save_to_file_csv with an argument-free list"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def testsavetofilecsverrmorethanonearg(self):
        """Test: save_to_file _csv with multiple argument list"""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBaseloadfromfilecsv(unittest.TestCase):
    """Unittest for loading instances of Base class from CSV file"""

    @classmethod
    def tearDown(self):
        """Checks and deletes created files"""
        try:
            remove("Rectangle.csv")
        except IOError:
            pass
        try:
            remove("Square.csv")
        except IOError:
            pass

    def testloadfromfilecsvfstrect(self):
        """Test: load_from_file_csv to retrieve first rectangle from file"""
        rect1 = Rectangle(14, 9, 7, 11, 3)
        rect2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file_csv([rect1, rect2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec1), str(loaded_rec[0]))

    def testloadfromfilecsvscdrect(self):
        """Test load_from_file_csv to retrieve second rectangle from file"""
        rec1 = Rectangle(14, 9, 7, 11, 3)
        rect2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file_csv([rect1, rect2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec2), str(loaded_rec[1]))

    def testloadfromfilecsvrectype(self):
        """Test: load_from_file_csv retrieve a list of rectangles"""
        rect1 = Rectangle(14, 9, 7, 11, 3)
        rect2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file_csv([rect1, rect2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(objt) == Rectangle for objt in loaded_rec))

    def testloadfromfilecsvfstsqr(self):
        """Test: load_from_file_csv retrieve the first square from file"""
        sqre1 = Square(6, 9, 10, 11)
        sqre2 = Square(5, 8, 3, 7)
        Square.save_to_file_csv([sqre1, sqre2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqr1), str(loaded_sqr[0]))

    def testloadfromfilecsvscdsqr(self):
        """Test: load_from_file_csv retrieve the second square from file"""
        sqre1 = Square(6, 9, 10, 11)
        sqre2 = Square(5, 8, 3, 7)
        Square.save_to_file_csv([sqre1, sqre2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqre2), str(loaded_sqre[1]))

    def testloadfromfilecsvsqrtype(self):
        """Test: load_from_file_csv to retrieve list of squares"""
        sqre1 = Square(6, 9, 10, 11)
        sqre2 = Square(5, 8, 3, 7)
        Square.save_to_file_csv([sqre1, sqre2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertTrue(all(type(objt) == Square for objt in loaded_sqr))

    def testloadfromfilecsvnofile(self):
        """Test: load_from_file_csv without any file"""
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual([], loaded_sqr)

    def testloadfromfilecsverrmorethanonearg(self):
        """Test: load_from_file_csv with multiple argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
