
import pandas as pd
from pathlib import Path


class LoadData(object):

	def __init__(self, data_path):
		
		self.data_path = Path(data_path)
		self.data = None
		self.line_size = 0

	def LoadData_Python():
		pass

	def LoadData_Pandas(self):
		self.data = pd.read_csv(self.data_path, sep="\t", header=None) 	
		return self.data

	def ColumnsCount(self):
		return len(self.data.columns)


	def MazeLineSize(self):
		return self.line_size

	def LoadMaze(self):

		lines_list = []	

		with open(self.data_path, 'r') as reader:
			line = reader.readline()
			line = line.replace('\n', '')
			self.line_size = len(line)
			while line != '':
				line = line.replace('\n', '')
				lines_list.extend(list(line))
				line = reader.readline()
		return lines_list