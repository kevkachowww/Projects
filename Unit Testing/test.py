'''

Sam's Surf Shop
Welcome to Sam’s Surf Shop! This project will exercise your knowledge of errors and unit testing practices in Python. It will also give you a small taste of testing a full application.

You’ve been hired to create a handful of tests for the shopping cart software at the surf shop. Once that is done, you’ll implement some improvements for these tests using more advanced unit testing features (skipping, parameterization, and expected failures). Finally, you’ll have the opportunity to fix bugs that were exposed by your tests.

The shopping cart software for Sam’s Surf Shop lives inside of the file called surfshop.py. Look over the files and familiarize yourself with their contents. Most of our work will take place in tests.py.

If you get stuck, you can look at a final version of the project by looking at solution_surf.py and solution_test.py - but try it out on your own first.

Let’s get started!

'''


import unittest
import surfshop

class SurfShopTests(unittest.TestCase):

  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboards(self):
    self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboards to cart!')

  def test_add_surfboards(self):
    for i in range(2,5):
      with self.subTest(i):
        self.assertEqual(self.cart.add_surfboards(i), f'Successfully added {i} surfboards to cart!')
        self.setUp()

  @unittest.skip
  def test_too_many_boards_error(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  #@unittest.expectedFailure
  def test_apply_local_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

unittest.main()