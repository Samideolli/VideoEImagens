import os
import cv2

path = "Images/"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file

        # print(file_name)

        Images.append(file_name)

print(len(Images))
count = len(Images)

frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)

option = input("Do Início Ao Fim(Sim) Ou Invertido(Não): ")


start = ""
end = ""
rangeVar = ""
if option.lower() == "não" or option.lower() == "nao":
    start = count-1
    end = 0
    rangeVar = range(start, end, -1)
elif option.lower() == "sim":
    start = 0
    end = count-1
    rangeVar = range(start, end)

out = cv2.VideoWriter(
    "project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in rangeVar:  # range(count-1, 0, -1)
    frame = cv2.imread(Images[i])
    out.write(frame)

out.release()
print("Concluído!")
