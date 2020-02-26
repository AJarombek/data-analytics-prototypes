# Learning the basics of R.  Working with R helps me understand what inspired and influenced the
# design choices in the numpy and pandas Python libraries.
# Author: Andrew Jarombek
# Date: 2/25/2020

name <- "Andy"

# Print out the contents of the variable 'name'
name 

# Print out the class of the variable 'name'
class(name)

age <- 24
class(age)

writing_r = TRUE
class(writing_r)

# Create a vector
vec1 <- c(1, 2, 3)
vec1
class(vec1)

vec2 <- c(3, 2, 1)

# Perform addition of two vectors (this likely inspired array vectorization in numpy)
result_vec <- vec1 + vec2
result_vec

# Vectors are 1 indexed (not 0 indexed) c(3, 2)
vec1_slice <- vec2[1:2]
vec1_slice

# Quickly create a range vector
vec3 <- c(1:10)
vec3

# More Vectorization operations (note the similarities to numpy)
# Return TRUE/FALSE for each element depending on whether its value is greater than 2.
gt2 <- vec3 > 2
gt2

# Return elements from the original vector that are greater than 2.  1 and 2 are dropped from the result.
onlygt2 <- vec3[vec3 > 2]
onlygt2

# Returns a vector with elements less than 3 and greater than 1.  Returns c(1, 2)
range <- vec3[(vec3 < 3) & (vec3 >= 1)]
range

# Creating matrices with R
# Fill the columns with values first.
grid = matrix(1:6, byrow=FALSE, nrow=2)
grid

# Get the dimension of the matrix (2 3)
dim(grid)

# Fill the rows with values first.
grid = matrix(1:6, byrow=TRUE, nrow=3)
grid

# Add a new column to the grid.  This does not mutate the original matrix, 
# so the result must be assigned back to 'grid'.
grid <- cbind(grid, c(3, 5, 7))
print(grid)

catsdogs <- c("cat", "catdog", "dog", "dog", "dog", "cat")

# Factors are used with categorial data (of type integer or string).  For example, the 'catsdogs' vector
# can be categorized into "cat", "dog", and "catdog"
f_catsdogs <- factor(catsdogs)
print(f_catsdogs)

# catsdogs is a Vector, not an Array.
print(is.vector(catsdogs))
print(is.array(catsdogs))

# f_catsdogs is a Factor.
print(is.factor(f_catsdogs))
