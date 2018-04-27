import unittest
import proj1_w18 as proj1
import json

file = open("sample_json.json", "r")
sample = file.read()
file.close()
sample_list = json.loads(sample)


class TestMedia(unittest.TestCase):

    def testConstructor(self):
        m1 = proj1.Media()
        m2 = proj1.Media("1999", "Prince", "2011")

        self.assertEqual(m1.title, "No Title")
        self.assertEqual(m1.author, "No Author")
        self.assertEqual(m1.year, "No Release Year")
        self.assertEqual(m2.title, "1999")
        self.assertEqual(m2.author, "Prince")
        self.assertEqual(m2.year, "2011")
        self.assertRaises(AttributeError, lambda: m2.rating)
        self.assertRaises(AttributeError, lambda: m2.album)

        self.assertEqual(m2.__str__(), "1999 by Prince (2011)")
        self.assertEqual(len(m1), 0)

    def testConstructorFromJSON(self):
    	m1 = proj1.Media("1999", "Prince", "2011", sample_list[2])

    	self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
    	self.assertEqual(m1.author, "Helen Fielding")
    	self.assertEqual(m1.year, "2012")

    	self.assertEqual(m1.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
    	self.assertEqual(len(m1), 0)


class TestSong(unittest.TestCase):
	
	def testConstructor(self):
		m1 = proj1.Song("100%", "One OK Rock", "2008", "Beam of Light", "Rock", 260000)

		self.assertEqual(m1.title, "100%")
		self.assertEqual(m1.author, "One OK Rock")
		self.assertEqual(m1.year, "2008")
		self.assertEqual(m1.album, "Beam of Light")
		self.assertEqual(m1.genre, "Rock")
		self.assertEqual(m1.length, 260000)
		self.assertRaises(AttributeError, lambda: m1.rating)

		self.assertEqual(m1.__str__(), "100% by One OK Rock (2008)[Rock]")
		self.assertEqual(len(m1), 260)

	def testConstructorFromJSON(self):
		m1 = proj1.Song("100%", "One OK Rock", "2008", "Beam of Light", "Rock", 260000, sample_list[1])

		self.assertEqual(m1.title, "Hey Jude")
		self.assertEqual(m1.author, "The Beatles")
		self.assertEqual(m1.year, "1968")
		self.assertEqual(m1.album, "TheBeatles 1967-1970 (The Blue Album)")
		self.assertEqual(m1.genre, "Rock")
		self.assertEqual(m1.length, 431333)

		self.assertEqual(m1.__str__(), "Hey Jude by The Beatles (1968)[Rock]")
		self.assertEqual(len(m1), 431)


class TestMovie(unittest.TestCase):

	def testConstructor(self):
		m1 = proj1.Movie("Coco", "Lee Unkrich", "2017", "PG", 4977536)

		self.assertEqual(m1.title, "Coco")
		self.assertEqual(m1.author, "Lee Unkrich")
		self.assertEqual(m1.year, "2017")
		self.assertEqual(m1.rating, "PG")
		self.assertEqual(m1.length, 4977536)

		self.assertEqual(m1.__str__(), "Coco by Lee Unkrich (2017)[PG]")
		self.assertEqual(len(m1), 83)

	def testConstructorFromJSON(self):
		m1 = proj1.Movie("Coco", "Lee Unkrich", "2017", "PG", 4977536, sample_list[0])

		self.assertEqual(m1.title, "Jaws")
		self.assertEqual(m1.author, "Steven Spielberg")
		self.assertEqual(m1.year, "1975")
		self.assertEqual(m1.rating, "PG")
		self.assertEqual(m1.length, 7451455)

		self.assertEqual(m1.__str__(), "Jaws by Steven Spielberg (1975)[PG]")
		self.assertEqual(len(m1), 124)

class TestItunes(unittest.TestCase):

	def testGetFromItunes(self):
		results1 = proj1.get_from_itunes("love")
		s1 = results1[0]
		mo1 = results1[1]
		me1 = results1[2]

		self.assertLessEqual((len(s1)+len(mo1)+len(me1)), 10)

		if len(s1) > 0:
			self.assertEqual(type(s1[0]), proj1.Song)

		if len(mo1) > 0:
			self.assertEqual(type(mo1[0]), proj1.Movie)

		if len(me1) > 0:
			self.assertEqual(type(me1[0]), proj1.Media)

		results2 = proj1.get_from_itunes("moana")
		s2 = results1[0]
		mo2 = results1[1]
		me2 = results1[2]

		self.assertLessEqual((len(s2)+len(mo2)+len(me2)), 10)

		results3 = proj1.get_from_itunes("&@#!$")
		s3 = results1[0]
		mo3 = results1[1]
		me3 = results1[2]

		self.assertLessEqual((len(s3)+len(mo3)+len(me3)), 10)

		results4 = proj1.get_from_itunes()
		s4 = results4[0]
		mo4 = results4[1]
		me4 = results4[2]

		self.assertEqual((len(s4)+len(mo4)+len(me4)), 0)



unittest.main()
