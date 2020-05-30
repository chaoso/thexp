"""
    Copyright (C) 2020 Shandong University

    This program is licensed under the GNU General Public License 3.0 
    (https://www.gnu.org/licenses/gpl-3.0.html). 
    Any derivative work obtained under this license must be licensed 
    under the GNU General Public License as published by the Free 
    Software Foundation, either Version 3 of the License, or (at your option) 
    any later version, if this derivative work is distributed to a third party.

    The copyright for the program is owned by Shandong University. 
    For commercial projects that require the ability to distribute 
    the code of this program as part of a program that cannot be 
    distributed under the GNU General Public License, please contact 
            
            sailist@outlook.com
             
    to purchase a commercial license.
"""

import sys
sys.path.insert(0,"../../")
from thexp.utils.screen import ScreenStr
import time

s = "\rLong Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text;Long Text"
for i in range(100):
    print(ScreenStr(s,leftoffset=10),end="")
    time.sleep(0.2)


from thexp.torch.data.collate import AutoCollate
from torch.utils.data.dataloader import DataLoader
import torch
device = torch.device('cuda:1')
DataLoader(...,collate_fn=AutoCollate(device))
