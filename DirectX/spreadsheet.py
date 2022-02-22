
# inmporting numpy
import numpy as np

# inputting the changes
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51,
        47, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47,55, 70]

# innputting the height of th different presidents
height = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180,
          168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

# turning the list into an array in numpy
new_ages = np.array(ages)

#turning the list of heigh into an array
new_height  = np.array(height)

'''
finding the number of elementsin each array to find out if i commited a mistake

print(new_ages.size)
print(new_height.size)
'''

'''
finding the shape of an array in numpy as i do in the example below


print(new_height.shape)
print(new_ages.shape)
'''
# lets conmine the two lists and cause one mega one 

height_ages = height + ages

#print(height_ages) #then we have to convert it into an array

Height_and_ages_Array = np.array(height_ages)

print(Height_and_ages_Array.shape) 

#Let us try to reshape the array
'''
what reshaping is is just as it sounds changing the shape or the dimentions of the array.
e.g if the array is in a shape like [2,2] that a 2d array and we can make all our array just like tahat in the array.
'''
#we use the .reshape command or snippet
print(Height_and_ages_Array.reshape(-1, 90))

#calculating the shape for us when we use the -1



