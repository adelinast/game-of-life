'''
Created on 10.11.2014

@author: AdStanciu
'''
import unittest
import game

class Test(unittest.TestCase):


    def setUp(self):
        self.grid = game.create_grid(10, 10)


    def tearDown(self):
        pass

    def testNoNeighbour(self):
        self.grid[2][2] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 2)
        self.assertEqual(neighbours, 0)

    def testOneNeighbour(self):
        self.grid[2][2] = 1
        self.grid[2][3] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 2)
        self.assertEqual(neighbours, 1)
    
    def testOneNeighbourSimetric(self):
        self.grid[2][2] = 1
        self.grid[2][3] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 3)
        self.assertEqual(neighbours, 1)

    def testOneNeighbourThreeCellsClose(self):
        self.grid[2][2] = 1
        self.grid[2][3] = 1
        self.grid[2][4] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 2)
        self.assertEqual(neighbours, 1)

    def testTwoNeighbours(self):
        self.grid[2][2] = 1
        self.grid[2][3] = 1
        self.grid[2][4] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 3)
        self.assertEqual(neighbours, 2)

    def testTwoNeighboursColumnsClose(self):
        self.grid[1][3] = 1
        self.grid[2][3] = 1
        self.grid[3][3] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 3)
        self.assertEqual(neighbours, 2)

    def testOneNeighbourColumnsClose(self):
        self.grid[1][3] = 1
        self.grid[2][3] = 1
        self.grid[3][3] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 1, 3)
        self.assertEqual(neighbours, 1)
    
    def testThreeNeighbours(self):
        self.grid[1][2] = 1
        self.grid[2][1] = 1
        self.grid[2][2] = 1
        self.grid[2][3] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 2)
        self.assertEqual(neighbours, 3)

    def testFourNeighbours(self):
        self.grid[1][2] = 1
        self.grid[2][1] = 1
        self.grid[2][2] = 1
        self.grid[2][3] = 1
        self.grid[3][2] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 2, 2)
        self.assertEqual(neighbours, 4)
    
    
    def testTwoNeighboursHorizontal(self):
        self.grid[6][4] = 1
        self.grid[6][5] = 1
        self.grid[6][6] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 6, 5)
        self.assertEqual(neighbours, 2)

    def testVerticalFirstLine(self):
        self.grid[0][0] = 1
        self.grid[0][1] = 1
        self.grid[0][2] = 1
        neighbours = game.get_number_neighbours_cell(10, 10, self.grid, 0, 1)
        self.assertEqual(neighbours, 2)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()