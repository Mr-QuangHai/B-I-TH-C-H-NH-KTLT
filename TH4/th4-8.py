print("Nguyễn Quang Hải")
print("Msv:235752021610099")
ds_tu = input("Nhập dãy các từ: ").split()
do_dai_max = max(len(tu) for tu in ds_tu)
tu_dai_nhat = [tu for tu in ds_tu if len(tu) == do_dai_max]
print(" ".join(tu_dai_nhat))
