import os
import wget

# # data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
url = 'https://drive.google.com/uc?export=download&id=1s8Xy8H1xKo-qQLOGkumD2r-aTQZeU4w7'
zip_name = "data_raw.csv"
wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
# import zipfile
# with zipfile.ZipFile(zip_name,"r") as zip_ref:
#     zip_ref.filelist[0].filename = 'data_raw.csv'
#     zip_ref.extract(zip_ref.filelist[0])

# os.remove(zip_name)



# Xuan viet
# Đọc nội dung từ file first-data
# with open('rawdata_new.csv', 'r') as first_file:
#     data = first_file.read()

# # Tạo một file mới có tên là second-data và ghi nội dung vào đó
# with open('data_raw.csv', 'w') as second_file:
#     second_file.write(data)
