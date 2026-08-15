import csv
import json
import sqlite3



class Memory():
    def __init__(self, text="", image=None):
        self.text = text
        self.image = image
