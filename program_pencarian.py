#!/usr/bin/env python
import sys

def main():
	hitung = 0
	if len(sys.argv)< 2: #jika kurang maka error
		print("Parameter kurang :D")
		print("penggunaan python %s input_file output_file string_yang_dicari" % sys.argv[0])
		sys.exit() #memaksa program untuk keluar
	file_buka = sys.argv[1] #menyimpan argv input ke variabel
	file_tampung = sys.argv[2] #menyimpan argv output ke variabel
	cari  = "_vti_bin/fpcount.exe"
	#cari2 = "Mon Mar  8 22:00:08 1999"
	#cari3 = "Mon Mar  8 23:18:46 1999"
	#cari4 = "Mon Mar  8 23:18:47 1999"
	#cari = sys.argv[3]
	#cari = "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"
	buka = open(file_tampung,'w')
	with open(file_buka, 'r') as auto:
		for line in auto:
			if cari in line :
				#hitung = hitung + 1
				buka.write(line)
	#buka.write(str(hitung))

if __name__ == '__main__':
	main()
