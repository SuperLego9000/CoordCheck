#coords=[[1,2,3],[4,5,6]]
coords=[0,0]
for corner in range(2):
    temp=[0,0,0]
    for axis in  range(3):
        temp[axis]=int(input(f"corner {corner+1} at {axis+1} axis="))
    coords[corner]=temp #dump temp into the coords var
dif=[0,0,0]
for axis in range(3):dif[axis]=abs(coords[0][axis]-coords[1][axis]) #get the difference between all of the axis into the dif var
for axis in range(3):
    if dif[axis]==0:
        dif[axis]=1
area=dif[0]*dif[1]*dif[2]  #calculate area
print(f"size:{area}")
print(f"fillable:{area<32768}")