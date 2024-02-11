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
        """Test base with three instances the increments ID corretly"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_incr_id_None(self):
        """Test checks ID increments corretly when initialized with None"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_assign_unique_id(self):
        """Test confirms the corret ID of a unique ID when initialized"""
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
        """Test if string ID is handled corretly"""
        self.assertEqual("test", Base("test").id)

    def test_dictionary_id(self):
        """Test if dictionary ID is handled corretly"""
        seld.assertEqual({"key": 2, "val": 3}, Base({"key": 2, "val": 3}).id)

    def test_list_id(self):
        """Test list ID is handled corretly"""
        self.assertEqual([2, 3, 9], Base([2, 3, 9]).id)

    def test_tuple_id(self):
        """Test evaluates corret handling of tuple ID"""
        self.assertEqual((9, 2), Base((9, 2)).id)

    def test_float_id(self):
        """Test evaluates corret handling of float ID"""
        self.assertEqual(9.8, Base(9.8).id)

    def test_inf_id(self):
        """Test evaluates corret handling of inf ID"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """Test evaluates corret handling of NaN ID"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_complex_id(self):
        """Test evaluates corret handling of complex ID"""
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_bool_id(self):
        """Test evaluates corret handling of bool ID"""
        self.assertEqual(False, Base(False).id)

    def test_set_id(self):
        """Test evaluates corret handling of set ID"""
        self.assertEqual({2, 3, 4}, Base({2, 3, 4}).id)

    def test_frozenset_id(self):
        """Test evaluates corret handling of frozenset ID"""
        self.assertEqual(frozenset({2, 3, 9}), Base({2, 3, 9}).id)

    def test_range_id(self):
        """Test evaluates corret handling of range ID"""
        self.assertEqual(range(8), Base(range(8)).id)

    def test_bytes_id(self):
        """Test evaluates corret handling of bytes ID"""
        self.assertEqual(b'Test', Base(b'Test').id)

    def test_bytearray_id(self):
        """Test evaluates corret handling of byte array ID"""
        self.assertEqual(bytearray(b'val'), Base(bytearray(b'val')).id)

    def test_memoryview_id(self):
        """Test evaluates corret handling of memory view ID"""
        self.assertEqual(memoryview(b'key'), Base(memoryview(b'key')).id)


class TestBasetojsonstring(unittest.TestCase):
    """Unittest for converting instances of Base class to JSON strings"""

    def test_to_json_string_ret_type(self):
        """Test validates to_json_string for rectangles"""
        ret = Rectangle(10, 9, 6, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([ret.to_dictionary()])))

    def test_to_json_string_ret_one_dict(self):
        """Test to_json_string length for a rectangle"""
        ret = rectangle(10, 9, 6, 4, 5)
        self.assertTrue(len(Base.to_json_string([ret.to_dictionary()])) == 53)

    def test_to_json_string_ret_two_dict(self):
        """Test to_json_string length for two rectangle dict"""
        ret1 = Rectangle(2, 4, 6, 18, 3)
        ret2 = Rectangle(2, 4, 3, 6, 12)
        lst_dicts = [ret1.to_dictionary(), ret2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(lst_dicts)) == 106)

    def test_to_json_string_sqr_type(self):
        """Test to_json_string outputs a string for a square"""
        sqe = Square(10, 5, 7, 8)
        self.assertEqual(str, type(Base.to_json_string([sqe.to_dictionary()])))

    def test_to_json_string_sqr_one_dict(self):
        """Test to_json_string outputs length for one square dict"""
        sqe = Square(10, 5, 7, 8)
        self.assertTrue(len(Base.to_json_string([sqe.to_dictionary()])) == 39)

    def test_to_json_string_sqr_two_dict(self):
        """Test to_json_string outputs length for two square dict"""
        sqe1 = Square(15, 10, 9, 6)
        sqe2 = Square(6, 8, 10, 28)
        lst_dicts = [sqe1.to_dictionary(), sqe2.to_dictionary()]
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

    def test_savetofile_oneret(self):
        """Test: save_to_file creating one rectangle file"""
        ret = Rectangle(15, 7, 8, 10, 4)
        Rectangle.save_to_file([ret])
        with open("Rectangle.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 53)

    def test_savetofile_tworet(self):
        """Test: save_to_file creating two rectangle file"""
        ret1 = Rectangle(14, 7, 10, 9, 3)
        ret2 = Rectangle(5, 7, 8, 10, 15)
        Rectangle.save_to_file([ret1, ret2])
        with open("Rectangle.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 106)

    def test_savetofile_onesqr(self):
        """Test: save_to_file creating one square file"""
        sqe = Square(8, 6, 4, 2)
        Square.save_to_file([sqe])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 38)

    def test_savetofile_twosqr(self):
        """Test: save_to_file creating two squares file"""
        sqe1 = Square(9, 6, 7, 8)
        sqe2 = Square(5, 4, 3, 8)
        Square.save_to_file([sqe1, sqe2])
        with open("Square.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 76)

    def test_savetofile_clsnameforfilename(self):
        """Test: save_to_file uses class name as filename"""
        sqe = Square(9, 6, 3, 7)
        Base.save_to_file([sqe])
        with open("Base.json", "r") as fl:
            self.assertTrue(len(fl.read()) == 39)

    def test_savetofile_overwrite(self):
        """Test: save_to_file overwrites file content"""
        sqe = Square(4, 9, 6, 28)
        Square.save_to_file([sqe])
        sqr = Square(14, 8, 7, 10)
        Square.save_to_file([sqe])
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

    def testfromjsonstringoneret(self):
        """Test: from_json_string return accurate output for one rectangle"""
        s_data = [{"id": 77, "width": 23, "height": 4, "x": 8}]
        json_dt = Rectangle.to_json_string(s_data)
        ds_data = Rectangle.from_json_string(json_dt)
        self.assertEqual(s_data, ds_data)

    def testfromjsonstringtworet(self):
        """Test: from_json_string return accurate output for two rectangles"""
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
    """Unittest for instantiating instances with create method of Base class"""

    def testcreateoriginalret(self):
        """Test: create method to return original rectangle"""
        ret1 = Rectangle(2, 5, 8, 3, 4)
        ret1_dct = ret1.to_dictionary()
        ret2 = Rectangle.create(**ret1_dct)
        self.assertEqual("[Rectangle] (4) 8/3 - 2/5", str(ret1))

    def testcreatenewret(self):
        """Test: create method to return new rectangle"""
        ret1 = Rectangle(3, 4, 5, 8, 9)
        ret1_dct = ret1.to_dictionary()
        ret2 = Rectangle.create(**ret1_dct)
        self.assertEqual("[Rectangle] (9) 5/8 - 3/4", str(ret2))

    def testcreateretinst(self):
        """Test: create to return a new rectangle instance"""
        ret1 = Rectangle(2, 5, 8, 3, 4)
        ret1_dct = ret1.to_dictionary()
        ret2 = Rectangle.create(**ret1_dct)
        self.assertIsNot(ret1, ret2)

    def testcreateretdiffinst(self):
        """Test: create to return different instance from original"""
        ret1 = Rectangle(2, 5, 8, 3, 4)
        ret1_dct = ret1.to_dictionary()
        ret2 = Rectangle.create(**ret1_dct)
        self.assertNotEqual(ret1, ret2)

    def testcreateoriginalsqr(self):
        """Test: create method to return original square"""
        sqe1 = Square(4, 5, 9, 2)
        sqe1_dct = sqe1.to_dictionary()
        sqe2 = Square.create(**sqe1_dct)
        self.assertEqual("[Square] (2) 5/9 - 4", str(sqe1))

    def testcreatenewsqr(self):
        """Test: create method to return new square"""
        sqe1 = Square(4, 6, 7, 2)
        sqe1_dct = sqe1.to_dictionary()
        sqe2 = Square.create(**sqe1_dct)
        self.assertEqual("[Square] (2) 6/7 - 4", str(sqe2))

    def testcreatesqrinst(self):
        """Test: create method generates a new square instance"""
        sqe1 = Square(4, 5, 9, 2)
        sqe1_dct = sqe1.to_dictionary()
        sqe2 = Square.create(**sqe1_dct)
        self.assertIsNot(sqe1, sqe2)

    def testcreatediffinst(self):
        """Test create to return different instance from original"""
        sqe1 = Square(4, 6, 7, 2)
        sqe1_dct = sqe1.to_dictionary()
        sqe2 = Square.create(**sqe1_dct)
        self.assertNotEqual(sqe1, sqe2)


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

    def testloadfromfilestret(self):
        """Test: load_from_file to retrieve first rectangle from the file"""
        ret1 = Rectangle(14, 9, 7, 11, 3)
        ret2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file([ret1, ret2])
        loaded_rec = Rectangle.load_from_file()
        self.assertEqual(str(ret1), str(loaded_rec[0]))

    def testloadfromfilescdret(self):
        """Test: load_from_file to retrieve second rectangle from the file"""
        ret1 = Rectangle(14, 9, 7, 11, 3)
        ret2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file([ret1, ret2])
        loaded_rec = Rectangle.load_from_file()
        self.assertEqual(str(ret2), str(loaded_rec[1]))

    def testloadfromfileretype(self):
        """Test load_from_file to retrieve a list of rectangles"""
        ret1 = Rectangle(14, 9, 7, 11, 3)
        ret2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file([ret1, ret2])
        loaded_rec = Rectangle.load_from_file()
        self.assertTrue(all(type(objt) == Rectangle for objt in loaded_rec))

    def testloadfromfilefstsqr(self):
        """Test: load_from_file to retrieve the first square from the file"""
        sqe1 = Square(3, 8, 6, 9)
        sqe2 = Square(5, 8, 3, 7)
        Square.save_to_file([sqe1, sqe2])
        loaded_sqr = Square.load_from_file()
        self.assertEqual(str(sqe1), str(loaded_sqr[0]))

    def testloadfromfilescdsqr(self):
        """Test: load_from_file to retrieve the second square from the file"""
        sqe1 = Square(3, 8, 6, 9)
        sqe2 = Square(5, 8, 3, 7)
        Square.save_to_file([sqe1, sqe2])
        loaded_sqr = Square.load_from_file()
        self.assertEqual(str(sqe2), str(loaded_sqr[1]))

    def testloadfromfilesqrtype(self):
        """Test: load_from_file to retrieve list of squares"""
        sqe1 = Square(3, 8, 6, 9)
        sqe2 = Square(5, 8, 3, 7)
        Square.save_to_file([sqe1, sqe2])
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

    def testsavetofilecsvoneret(self):
        """Test: save_to_file_csv generates file for one rectangle"""
        ret = Rectangle(13, 8, 4, 11, 9)
        Rectangle.save_to_file_csv([ret])
        with open("Rectangle.csv", "r") as fl:
            self.assertTrue("9,13,8,4,11", fl.read())

    def testsavetofilecsvtworets(self):
        """Test: save_to_file_csv generates file for two rectangles"""
        ret1 = Rectangle(10, 3, 4, 6, 7)
        ret2 = Rectangle(4, 7, 9, 11, 3)
        Rectangle.save_to_file_csv([ret1, ret2])
        with open("Rectangle.csv", "r") as fl:
            self.assertTrue("7,10,3,4,6\n4,7,9,11,3", fl.read())

    def testsavetofilecsvonesqr(self):
        """Test: save_to_file_csv generates file for one square"""
        sqe = Square(14, 10, 7, 6)
        Square.save_to_file_csv([sqe])
        with open("Square.csv", "r") as fl:
            self.assertTrue("6,14,10,7", fl.read())

    def testsavetofilecsvtwosqrs(self):
        """Test: save_to_file_csv generates file for two squares"""
        sqe1 = Square(12, 6, 2, 5)
        sqe2 = Square(7, 10, 3, 6)
        Square.save_to_file_csv([sqe1, sqe2])
        with open("Square.csv", "r") as fl:
            self.assertTrue("5,12,6,2\n6,7,10,3", fl.read())

    def testsavetofilecsvclsnameforfilename(self):
        """Test: save_to_file_csv uses class name as filename"""
        sqe = Square(14, 10, 6, 11)
        Base.save_to_file_csv([sqe])
        with open("Base.csv", "r") as fl:
            self.assertTrue("11,14,10,6", fl.read())

    def testsavetofilecsvoverwrite(self):
        """Test: save_to_file_csv overwrites file content"""
        sqe = Square(4, 9, 6, 30)
        Square.save_to_file([sqe])
        sqe = Square(14, 7, 9, 11)
        Square.save_to_file_csv([sqe])
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

    def testloadfromfilecsvfstret(self):
        """Test: load_from_file_csv to retrieve first rectangle from file"""
        ret1 = Rectangle(14, 9, 7, 11, 3)
        ret2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file_csv([ret1, ret2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(ret1), str(loaded_rec[0]))

    def testloadfromfilecsvscdret(self):
        """Test load_from_file_csv to retrieve second rectangle from file"""
        ret1 = Rectangle(14, 9, 7, 11, 3)
        ret2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file_csv([ret1, ret2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertEqual(str(ret2), str(loaded_rec[1]))

    def testloadfromfilecsvretype(self):
        """Test: load_from_file_csv retrieve a list of rectangles"""
        ret1 = Rectangle(14, 9, 7, 11, 3)
        ret2 = Rectangle(5, 8, 10, 7, 6)
        Rectangle.save_to_file_csv([ret1, ret2])
        loaded_rec = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(objt) == Rectangle for objt in loaded_rec))

    def testloadfromfilecsvfstsqr(self):
        """Test: load_from_file_csv retrieve the first square from file"""
        sqe1 = Square(6, 9, 10, 11)
        sqe2 = Square(5, 8, 3, 7)
        Square.save_to_file_csv([sqe1, sqe2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqe1), str(loaded_sqr[0]))

    def testloadfromfilecsvscdsqr(self):
        """Test: load_from_file_csv retrieve the second square from file"""
        sqe1 = Square(6, 9, 10, 11)
        sqe2 = Square(5, 8, 3, 7)
        Square.save_to_file_csv([sqe1, sqe2])
        loaded_sqr = Square.load_from_file_csv()
        self.assertEqual(str(sqe2), str(loaded_sqe[1]))

    def testloadfromfilecsvsqrtype(self):
        """Test: load_from_file_csv to retrieve list of squares"""
        sqe1 = Square(6, 9, 10, 11)
        sqe2 = Square(5, 8, 3, 7)
        Square.save_to_file_csv([sqe1, sqe2])
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
