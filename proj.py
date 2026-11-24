from __future__ import annotations
from typing import List
import json
import os

# Trie Variant 1
# AI Usage:
# Write details about how you used AI for this project.

# The class for a particular node in the tree.
# DO NOT MODIFY!
# This class is used for both types of Node.
# For an internal node the value is None.
# The branches are a list of objects each of which has a 'label' and a 'child',
# the latter is the pointer to the child node.

class Node():
    def  __init__(self,
                  value      : int = None,
                  branches   : List[None] = None):
        self.value      = value
        self.branches   = branches

class Trie():
    def __init__(self,
                 root: Node = None):
         self.root = None

    # DO NOT MODIFY!
    def dump(self):
        def recurse(node,indent):
            if node.value is not None:
                print(f"{indent*' '}  Value: {node.value}")
            #node.branches.sort(key=lambda x:x['label'])
            for b in node.branches:
                if b['label'] == '$':
                    print(f"{indent*' '}  {b['label']} \u2192 {b['child'].value}")
                else:
                    print(f"{indent*' '}  {b['label']} \u2192 Internal Node")
                    recurse(b['child'],indent+2)

        if self.root is not None:
            print('Internal Node Root')
            recurse(self.root,0)
        else:
            print("No Tree!")

    def insert(self,word,value):
        # This next line is just to make it run.
        dummy = True

    def delete(self,word):
        # This next line is just to make it run.
        dummy = True


    # Return the value associated to the string.

    def search(self,word):
        return(None)

    # Return something else about the string.

    def data(self,word):
        # You'll need to return the right thing, whatever that is.
        return(None)
