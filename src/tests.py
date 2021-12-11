# Code for a simple test case

import unittest
import Searcher


class TestWikipediaViz(unittest.TestCase):  # Class that tests different functionality
    def test_searcher1(self):  # tests the functionality that builds up the graph
        dict1 = {'Maryland': ['110th United States Congress', '111th United States Congress', '13 colonies'],
                 '110th United States Congress': ['100-Hour Plan', '100th United States Congress',
                                                  '101st United States Congress'],
                 '111th United States Congress': ['100th United States Congress', '101st United States Congress',
                                                  '102nd United States Congress'],
                 'Thirteen Colonies': ['1860 United States Census', '51st state', 'ABC-CLIO'],
                 '100-Hour Plan': ['110th Congress', '110th United States Congress',
                                   "1987 California's 5th congressional district special election"],
                 '100th United States Congress': ['101st United States Congress', '102nd United States Congress',
                                                  '103rd United States Congress']}
        self.assertEqual(dict1, Searcher.Searcher().search("Maryland", 3, 2))

    def test_seacher2(self):  # tests the functionality that adds edges to the graph
        dict = {'IPhone': ['1984 (advertisement)', '1xRTT', '2013 mass surveillance disclosures'],
                 '1984 (advertisement)': ['100 Greatest (UK TV series)', '1492: Conquest of Paradise',
                                          '1984 (1956 film)'], 'CDMA2000': ['1G', '2G', '3G'],
                 'Global surveillance disclosures (2013–present)': ['12th Unmanned Aerial Vehicles Base',
                                                                    '1984 (advertisement)', '2009 G-20 London summit'],
                 '100 Greatest (TV series)': ['(Everything I Do) I Do It for You', '1080i', '16:9'],
                 '1492: Conquest of Paradise': ['1492: Conquest of Paradise (album)', '1984 (advertisement)',
                                                '1996 Russian presidential election']}
        self.assertEqual(dict, Searcher.Searcher().search("iPhone", 3, 2))

    def test_searcher_diff_dist(self):
        dict = {'MacBook': ['1984 (advertisement)', 'AIM alliance', 'AMD Polaris', 'ARM architecture'], '1984 (advertisement)': ['100 Greatest (UK TV series)', '1492: Conquest of Paradise', '1984 (1956 film)', '1984 (Westinghouse Studio One)'], 'AIM alliance': ['AOL Instant Messenger', 'Advanced Computing Environment', 'Advanced RISC Computing', 'AltiVec'], 'Graphics Core Next': ['12 nm', '14 nanometer', '14 nm', '28 nanometer'], 'ARM architecture': ['1-bit computing', '12-bit computing', '128-bit', '128-bit computing'], '100 Greatest (TV series)': ['(Everything I Do) I Do It for You', '1080i', '16:9', '1966 FIFA World Cup'], '1492: Conquest of Paradise': ['1492: Conquest of Paradise (album)', '1984 (advertisement)', '1996 Russian presidential election', '2011 ICC Cricket World Cup'], '1984 (1956 film)': ['1984 (Westinghouse Studio One)', '1984 (advertisement)', '1984 (opera)', '1984 (play)']}
        self.assertEqual(dict, Searcher.Searcher().search("Macbook", 4, 2))


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
