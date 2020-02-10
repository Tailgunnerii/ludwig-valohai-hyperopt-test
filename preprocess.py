from shutil import copyfile

#Just copying my inputs to outputs
src="/valohai/inputs/winequalityN.csv"
dst="/valohai/outputs/winequalityN.csv"
copyfile(src, dst)
