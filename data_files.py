# 
# This file is part of https://github.com/dannerlab/rat-sci-locomotion.
# Copyright (c) 2023 Simon M. Danner.
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
c_names_1 = {'X': ['RL.X', 'RR.X', 'FL.X', 'FR.X'], 'Y': ['RL.Y', 'RR.Y', 'FL.Y', 'FR.Y']}

c_names_2 = {'X': ['Point #4.X', 'Point #3.X', 'Point #2.X', 'Point #1.X'], 
            'Y': ['Point #4.Y', 'Point #3.Y', 'Point #2.Y', 'Point #1.Y']}

file_desc = [{'filename': './data/042016/042016 ASCII 13/LT-4202016-BL-13-C.xlsx', 'c_names': c_names_1, 'sample_rate': 100.0, 'ID': 13, 'SCI': 'intact'},
             {'filename': './data/051216/05122016 15ASCII/LongTank-5122016-BL3-15-C.xlsx', 'c_names': c_names_1, 'sample_rate': 100.0, 'ID': 15, 'SCI': 'intact'},
             {'filename': './data/051216/05122016 16ASCII/LongTank-5122016-BL3-16-C.xlsx', 'c_names': c_names_1, 'sample_rate': 100.0, 'ID': 16, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-17-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 17, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-18-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 18, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-23-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 23, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-24-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 24, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-25-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 25, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-26-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 26, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-27-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 27, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-28-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 28, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-29-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 29, 'SCI': 'intact'},
             {'filename': './data/07252016/LT-7252016-BL2-30-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 30, 'SCI': 'intact'}, 
             {'filename': './data/07292016/LT-7292016-BL2-17-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 17, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-18-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 18, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-21-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 21, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-24-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 24, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-25-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 25, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-26-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 26, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-27-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 27, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-28-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 28, 'SCI': 'intact'},
             {'filename': './data/07292016/LT-7292016-BL2-30-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 30, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-17-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 17, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-18-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 18, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-19-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 19, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-20-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 20, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-21-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 21, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-22-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 22, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-23-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 23, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-25-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 25, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-26-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 26, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-27-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 27, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-28-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 28, 'SCI': 'intact'},
             {'filename': './data/08012016/LT-812016-BL3-29-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 29, 'SCI': 'intact'},

             {'filename': './data/08302016/LongTank-8302016-W4-17-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 17, 'SCI': 'hemisection'},
             {'filename': './data/08302016/LongTank-8302016-W4-19-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 19, 'SCI': 'hemisection'},
             {'filename': './data/08302016/LongTank-8302016-W4-21-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 21, 'SCI': 'hemisection'},
             {'filename': './data/08302016/LongTank-8302016-W4-22-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 22, 'SCI': 'hemisection'},
             {'filename': './data/08302016/LongTank-8302016-W4-23-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 23, 'SCI': 'hemisection'},
             {'filename': './data/08302016/LongTank-8302016-W4-24-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 24, 'SCI': 'contusion'},
             {'filename': './data/08302016/LongTank-8302016-W4-25-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 25, 'SCI': 'contusion'},
             {'filename': './data/08302016/LongTank-8302016-W4-26-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 26, 'SCI': 'contusion'},
             {'filename': './data/08302016/LongTank-8302016-W4-27-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 27, 'SCI': 'contusion'},
             {'filename': './data/08302016/LongTank-8302016-W4-28-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 28, 'SCI': 'contusion'},
             {'filename': './data/08302016/LongTank-8302016-W4-29-C.xlsx', 'c_names': c_names_2, 'sample_rate': 200.0, 'ID': 29, 'SCI': 'contusion'},

             {'filename': './data/09132016/LongTank-9132016-W6-17-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 17, 'SCI': 'hemisection'},
             {'filename': './data/09132016/LongTank-9132016-W6-20-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 20, 'SCI': 'hemisection'},
             {'filename': './data/09132016/LongTank-9132016-W6-22-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 22, 'SCI': 'hemisection'},
             {'filename': './data/09132016/LongTank-9132016-W6-23-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 23, 'SCI': 'hemisection'},
             {'filename': './data/09132016/LongTank-9132016-W6-24-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 24, 'SCI': 'contusion'},
             {'filename': './data/09132016/LongTank-9132016-W6-27-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 27, 'SCI': 'contusion'},
             {'filename': './data/09132016/LongTank-9132016-W6-28-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 28, 'SCI': 'contusion'},
             {'filename': './data/09132016/LongTank-9132016-W6-29-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 29, 'SCI': 'contusion'},
             {'filename': './data/09132016/LongTank-9132016-W6-30-C.xlsx', 'c_names': c_names_1, 'sample_rate': 200.0, 'ID': 30, 'SCI': 'contusion'}]
