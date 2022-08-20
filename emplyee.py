#!/usr/bin/python

import sys

# employee dict

employee_dict = {}



def main():
	if len(sys.argv) < 3:
		print('no argument')
		sys.exit()
	in_file_name = sys.argv[1]
	out_file_name = sys.argv[2]
	out_file_name = out_file_name + '.csv'

	#open file
	with open(in_file_name, "r") as fin:
		lines = fin.readlines()
		for line in lines:
			line_list = line.strip('\n').split(',')
			if line_list[4] == '展瑩科妍股份有限公司':
				if line_list[2] not in employee_dict:
					employee_dict[line_list[2]] = []
					my_list = []
					my_list.append(line_list[0])
					my_list.append(line_list[1])
					employee_dict[line_list[2]].append(my_list)
				else:
					my_list = []
					my_list.append(line_list[0])
					my_list.append(line_list[1])
					employee_dict[line_list[2]].append(my_list)

	with open(out_file_name, "w") as fout:
		for k, v in employee_dict.items():
			new_data = [];
			date_count = 0
			for i in v:
				if date_count == 0: ###早上的時間
					new_data.append(i)
					date_count = 1
				elif date_count == 1: ### 晚上的時間
					if new_data[-1][0] == i[0]: ###確認日期
						new_data.append(i)
						date_count = 2
					else:
						new_data.append(i)
						date_count == 0
				elif date_count == 2:
					if new_data[-1][0] == i[0]:
						new_data[-1][1] = i[1]
					else:
						new_data.append(i)
						date_count = 1
			for j in new_data:
				line = k + ',' + j[0] + ',' + j[1] + '\n'
				fout.write(line)

if __name__ == "__main__":
	main()