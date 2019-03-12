#! /usr/bin/python3

from MaxRect import MaxRect

def main():
	map = MaxRect([
		[31, 32, 29, 25, 24],
		[25, 30, 29, 25, 24],
		[20, 22, 29, 31, 40],
		[31, 23, 29, 20, 40],
		[31, 32, 16, 15, 50]
	]);
	map.calMaxRect(30);
	print(map.getMaxRectLoc())

if __name__ == "__main__":
	main()
