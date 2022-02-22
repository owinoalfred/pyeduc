import numpy as np

height_of_prezos = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183,
                    180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]


# turn it into an array that will easily be used by numpy
#prezos_aray = np.array(height_of_prezos)

'''
once an array is created in numpy it cant be increased and cant be changed. we have to remeber that
'''

# the now start to use it to do things in numpy using numpy commands
#print((prezos_aray > 193).sum())

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51,
        47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70, 89]


new_array = height_of_prezos + ages

new_arrat_np = np.array(new_array)

print(new_arrat_np.reshape(2,45))

#print(new_arrat_np.reshape(2,-1)) when we put a negative value it will guess the number for us

print(new_arrat_np[2])