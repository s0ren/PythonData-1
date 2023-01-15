
- <https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf>

- <https://websitesetup.org/wp-content/uploads/2020/04/Python-Cheat-Sheet.png>

https://assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf
https://github.com/pandas-dev/pandas/blob/main/doc/cheatsheet/Pandas_Cheat_Sheet.pdf
http://datacamp-community-prod.s3.amazonaws.com/e1a8f39d-71ad-4d13-9a6b-618fe1b8c9e9

TOC

- [\[Part 01\]](#part-01)
- [Basics](#basics)
      - [Øvelse 1 (hej verden)](#øvelse-1-hej-verden)
  - [variabler](#variabler)
  - [Datatyper](#datatyper)
  - [Forgreninger](#forgreninger)
  - [Datastrukturer](#datastrukturer)
  - [String handling](#string-handling)
  - [Moduler](#moduler)
- [\[Part02\]](#part02)
  - [Læs (og skriv, i) filer](#læs-og-skriv-i-filer)
  - [RegEx](#regex)
  - [Objekter](#objekter)
  - [Undtagelser (Exceptions)](#undtagelser-exceptions)
- [Numpy](#numpy)
      - [Exercise 11 (rows and columns)](#exercise-11-rows-and-columns)
      - [Exercise 12 (row and column vectors)](#exercise-12-row-and-column-vectors)
      - [Exercise 13 (diamond)](#exercise-13-diamond)
      - [Exercise 13 (diamond)](#exercise-13-diamond-1)
      - [Exercise 14 (vector lengths)](#exercise-14-vector-lengths)
      - [Exercise 15 (vector angles)](#exercise-15-vector-angles)
- [\[Part03\]](#part03)
- [NumPy (continues) \[`numpy2.ipynb`\]](#numpy-continues-numpy2ipynb)
      - [Exercise 1 (column comparison)](#exercise-1-column-comparison)
      - [Exercise 2 (first half second half)](#exercise-2-first-half-second-half)
      - [Exercise 3 (most frequent first)](#exercise-3-most-frequent-first)
      - [Exercise 4 (matrix power)](#exercise-4-matrix-power)
      - [Exercise 5 (correlation)](#exercise-5-correlation)
      - [Exercise 6 (meeting lines)](#exercise-6-meeting-lines)
      - [Exercise 7 (meeting planes)](#exercise-7-meeting-planes)
      - [Exercise 8 (almost meeting lines)](#exercise-8-almost-meeting-lines)
- [MatPlotLib](#matplotlib)
      - [Exercise 9 (multiple graphs)](#exercise-9-multiple-graphs)
      - [Exercise 10 (subfigures)](#exercise-10-subfigures)
- [Image processing](#image-processing)
      - [Exercise 11 (to grayscale)](#exercise-11-to-grayscale)
        - [Part 1.](#part-1)
        - [Part 2.](#part-2)
      - [Exercise 12 (radial fade)](#exercise-12-radial-fade)
        - [Part1.](#part1)
        - [Part 2.](#part-2-1)
- [Pandas](#pandas)
      - [Exercise 13 (read series)](#exercise-13-read-series)
      - [Exercise 14 (operations on series)](#exercise-14-operations-on-series)
      - [Exercise 15 (inverse series)](#exercise-15-inverse-series)
- [\[ PART 3 \]](#-part-3-)
      - [Exercise 1 (cities)](#exercise-1-cities)
      - [Exercise 2 (powers of series)](#exercise-2-powers-of-series)
      - [Exercise 3 (municipal information)](#exercise-3-municipal-information)
      - [Exercise 4 (municipalities of finland)](#exercise-4-municipalities-of-finland)
      - [Exercise 5 (swedish and foreigners)](#exercise-5-swedish-and-foreigners)
      - [Exercise 6 (growing municipalities)](#exercise-6-growing-municipalities)
      - [Exercise 7 (subsetting with loc)](#exercise-7-subsetting-with-loc)
      - [Exercise 8 (subsetting by positions)](#exercise-8-subsetting-by-positions)
      - [Exercise 9 (snow depth)](#exercise-9-snow-depth)
      - [Exercise 10 (average temperature)](#exercise-10-average-temperature)
      - [Exercise 11 (below zero)](#exercise-11-below-zero)
      - [Exercise 12 (cyclists)](#exercise-12-cyclists)
      - [Exercise 13 (missing value types)](#exercise-13-missing-value-types)
      - [Exercise 14 (special missing values)](#exercise-14-special-missing-values)
      - [Exercise 15 (last week)](#exercise-15-last-week)
      - [Exercise 16 (split date)](#exercise-16-split-date)
      - [Exercise 17 (cleaning data)](#exercise-17-cleaning-data)
      - [Exercise 2 (cycling weather)](#exercise-2-cycling-weather)
      - [Exercise 3 (top bands)](#exercise-3-top-bands)
      - [Exercise 4 (cyclists per day)](#exercise-4-cyclists-per-day)
      - [Exercise 5 (best record company)](#exercise-5-best-record-company)
      - [Exercise 6 (suicide fractions)](#exercise-6-suicide-fractions)
      - [Exercise 7 (suicide weather)](#exercise-7-suicide-weather)
      - [Exercise 8 (bicycle timeseries)](#exercise-8-bicycle-timeseries)
      - [Exercise 9 (commute)](#exercise-9-commute)

# [Part 01]

# Basics

#### Øvelse 1 (hej verden)
Øvelsen har en skabelon-fil eller en "stub". Den ligger i mappen `exercises/part01/e01_hello_world`
Udfyld det manglende stykke i løsnings-stub-filen `hello_world.py` i undermappen `src` og få den til at udskrive følgende:

`Hello, world!`

Sørg for at bruge korrekt indrykning. Du kan køre det med kommando `python src/hello_world.py`. Hvis output ser godt ud, kan du teste det med kommando `python -m tmc`. ~~Hvis testene virker, skal du indsende din løsning til serveren med kommando  `tmc submit`~~.

---

## variabler

## Datatyper

## Forgreninger 

* loops, 
* betingede valg (if/else)

## Datastrukturer

* Lister
* Tupler
* Dictionarys
* Cemprehensions
* sequence processing

## String handling

## Moduler

# [Part02]

## Læs (og skriv, i) filer

## RegEx

## Objekter

## Undtagelser (Exceptions)

# Numpy 
[numpy.ipynb]

#### Exercise 11 (rows and columns)

Write two functions, `get_rows` and `get_columns`, that get a two dimensional array as parameter.
They should return the list of rows and columns of the array, respectively. The rows and columns should be one dimensional arrays. You may use the *transpose* operation, which flips rows to columns, in your solution. The transpose is done by the `T` method:

---
#### Exercise 12 (row and column vectors)

Create function `get_row_vectors` that returns a list of rows from the input array of shape `(n,m)`, but this time the rows must have shape `(1,m)`. Similarly, create function `get_columns_vectors` that returns a list of columns (each having shape `(n,1)`) of the input matrix .

Example: for a 2x3 input matrix

```
 [[5 0 3]
  [3 7 9]]
```

the result should be

```
Row vectors: 
[array([[5, 0, 3]]), array([[3, 7, 9]])]
Column vectors: 
[array([[5],
        [3]]), 
 array([[0],
        [7]]), 
 array([[3],
        [9]])]
```

The above output is basically just the returned lists printed with `print`. Only some
whitespace is adjusted to make it look nicer. Output is not tested.


---

#### Exercise 13 (diamond)

Create a function `diamond` that returns a two dimensional integer array where the `1`s form a diamond shape. Rest of the numbers are `0`. The function should get a parameter that tells the length of a side of the diamond. Do this using the `eye` and `concatenate` functions of NumPy and array slicing.

Example of usage:
```
print(diamond(3))
[[0 0 1 0 0]
 [0 1 0 1 0]
 [1 0 0 0 1]
 [0 1 0 1 0]
 [0 0 1 0 0]]
print(diamond(1))
[[1]]
```

---

#### Exercise 13 (diamond)
Create a function `diamond` that returns a two dimensional integer array where the `1`s form a diamond shape. Rest of the numbers are `0`. The function should get a parameter that tells the length of a side of the diamond. Do this using the `eye` and `concatenate` functions of NumPy and array slicing.

Example of usage:
```
print(diamond(3))
[[0 0 1 0 0]
 [0 1 0 1 0]
 [1 0 0 0 1]
 [0 1 0 1 0]
 [0 0 1 0 0]]
print(diamond(1))
[[1]]
```

---

#### Exercise 14 (vector lengths)

Write function `vector_lengths` that gets a two dimensional array of shape (n,m) as a parameter. Each row in this array corresponds to a vector. The function should return an array of shape (n,), that has the length of each vector in the input. The length is defined by the usual 
[Euclidean norm](<https://en.wikipedia.org/wiki/Norm_(mathematics&#41;#Euclidean_norm>). Don't use loops at all in your solution. Instead use vectorized operations. You must use at least the `np.sum` and the `np.sqrt` functions. You can't use the function `scipy.linalg.norm`. Test your function in the main function.

#### Exercise 15 (vector angles)

Let x and y be m-dimensional vectors. The angle $\alpha$ between two vectors is defined by the equation
$\cos_{xy}(\alpha):=\frac{\langle x,y\rangle}{||x|| ||y||}$,
where the angle brackets denote the [inner product](https://en.wikipedia.org/wiki/Inner_product_space#Euclidean_space), and $||x||:=\sqrt{\langle x,x \rangle}$. 

Write function `vector_angles` that gets two arrays X and Y with same shape (n,m) as parameters. Each row in the arrays corresponds to a vector. The function should return vector of shape (n,) with the corresponding angles between vectors of `X` and `Y` in degrees, not in radians. Again, don't use loops, but use vectorized operations.

Note: function `np.arccos` is only defined on the domain [-1.0,1.0]. If you try to compute `np.arccos(1.000000001)`, it will fail. These kind of errors can occur due to use of finite precision in numerical computations. Force the argument to be in the correct range (`clip` method).

Test your solution in the main program.
<hr/>

# [Part03]
# NumPy (continues) [`numpy2.ipynb`]

#### Exercise 1 (column comparison)

Write function `column_comparison` that gets a two dimensional array as parameter. The function should return a new array containing those rows from the input that have the value in the second column larger than in the second last column. You may assume that the input contains at least two columns. Don't use loops, but instead vectorized operations. Try out your function in the main function.

For array

```
 [[8 9 3 8 8]
 [0 5 3 9 9]
 [5 7 6 0 4]
 [7 8 1 6 2]
 [2 1 3 5 8]]
```
the result would be
```
 [[8 9 3 8 8]
 [5 7 6 0 4]
 [7 8 1 6 2]]
```
<hr/>

#### Exercise 2 (first half second half)

Write function `first_half_second_half` that gets a two dimensional array of shape `(n,2*m)` as a parameter. The input array has `2*m` columns. The output from the function should be a matrix with those rows from the input that have the sum of the first `m` elements larger than the sum of the last `m` elements on the row. Your solution should call the `np.sum` function or the corresponding method exactly twice.

Example of usage:
```python
a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2]])
first_half_second_half(a)
array([[2, 2, 1, 2]])
```
<hr/>

#### Exercise 3 (most frequent first)

**<span style="color:red">Note:</span>** This exercise is fairly difficult. Feel free to skip if you get stuck.

Write function `most_frequent_first` that gets a two dimensional array and an index `c` of a column as parameters. The function should then return the array whose rows are sorted based on column `c`, in the following way. Rows are ordered so that those rows with the most frequent element in column `c` come first, then come the rows with the second most frequent element in column `c`, and so on. Therefore, the values outside column `c` don't affect the ordering in any way.

Example of usage:
```
a:
 [[5 0 3 3 7 9 3 5 2 4]
 [7 6 8 8 1 6 7 7 8 1]
 [5 9 8 9 4 3 0 3 5 0]
 [2 3 8 1 3 3 3 7 0 1]
 [9 9 0 4 7 3 2 7 2 0]
 [0 4 5 5 6 8 4 1 4 9]
 [8 1 1 7 9 9 3 6 7 2]
 [0 3 5 9 4 4 6 4 4 3]
 [4 4 8 4 3 7 5 5 0 1]
 [5 9 3 0 5 0 1 2 4 2]]
print(most_frequent_first(a, -1))
 [[4 4 8 4 3 7 5 5 0 1]
 [2 3 8 1 3 3 3 7 0 1]
 [7 6 8 8 1 6 7 7 8 1]
 [5 9 3 0 5 0 1 2 4 2]
 [8 1 1 7 9 9 3 6 7 2]
 [9 9 0 4 7 3 2 7 2 0]
 [5 9 8 9 4 3 0 3 5 0]
 [0 3 5 9 4 4 6 4 4 3]
 [0 4 5 5 6 8 4 1 4 9]
 [5 0 3 3 7 9 3 5 2 4]]
```

If we look at the last column, we see that the number 1 appears three times, then both numbers 2 and 0 appear twice, and lastly numbers 3, 9, and 4 appear only once. Note that, for example, among those rows that contain in column `c` a number that appear twice in column `c` the order can be arbitrary.

Hint: the function `np.unique` may be useful.

<hr/>

#### Exercise 4 (matrix power)

Repeat the functionality of the NumPy function `numpy.linalg.matrix_power`, which raises a square matrix of shape (m,m) to the `n`th power. Here the multiplication is the matrix multiplication. Square matrix `a` raised to power `n` is therefore `a @ a @ ... @ a` where `a` is repeated `n` times. When n is zero then $a^0$ is equal to `np.eye(m)`.

Write function `matrix_power` that gets as first argument a square matrix `a` and as second argument a non-negative integer `n`. The function should return the matrix `a` multiplied by itself `n-1` times.
Use Python's `reduce` function and a generator expression.

Extend the `matrix_power` function.
For negative powers, we define $a^{-1}$ to be equal to the multiplicative inverse of `a`. You can use NumPy's function `numpy.linalg.inv` for this. And you may assume that the input matrix is invertible.

<hr/>

#### Exercise 5 (correlation)

This exercise can give two points at maximum!

Load the iris dataset using the provided function `load()` in the stub solution. The four columns of the returned array correspond to

* sepal length (cm)
* sepal width (cm)
* petal length (cm)
* petal width (cm)

Part 1. What is the Pearson correlation between the variables `sepal length` and `petal length`. Compute this using the `scipy.stats.pearsonr` function. It returns a tuple whose first element is the correlation. Write a function `lengths` that loads the data and returns the correlation.

Part 2. What are the correlations between all the variables. Write a function `correlations` that returns an array of shape (4,4) containing the correlations. Use the function `np.corrcoef`. Which pair of variables is the most highly correlated?

Note the input formats of both functions `pearsonr` and `corrcoef`.

<hr/>

#### Exercise 6 (meeting lines)

Write function `meeting_lines` that gets the coefficients of two lines as parameters and returns the point where the two lines meet. The equations for the lines are $y=a_1x + b_1$ and $y=a_2x + b_2$. Use the `np.linalg.solve` function. Create a main function to test your solution.

Example of usage:
```
x, y = meeting_lines(a1, b1, a2, b2)
```
<hr/>

#### Exercise 7 (meeting planes)
Write function `meeting_planes` that gets the coefficients of three planes as parameters and returns the point where the planes meet. The equations for the planes are:
$z =a_1y + b_1x+ c_1$,
$z =a_2y + b_2x+ c_2$, and
$z =a_3y + b_3x+ c_3$.

Example of usage:
```
x, y, z = meeting_planes(a1, b1, c1,  a2, b2, c2,  a3, b3, c3)
```
<hr/>

#### Exercise 8 (almost meeting lines)
In the earlier "meeting lines" exercise there is a problem if the lines don't meet at all. Extend that solution so that it tells the meeting point if it exists, and otherwise finds the point that is closest to the both lines.
You can use the `numpy.linalg.lstsq` for this.

Example of usage:
```
(x, y), exact = almost_meeting_lines(1, 2, -1, 0)
print(x, y, exact)
-1.000000 1.000000 True
```

<hr/>

# MatPlotLib

#### Exercise 9 (multiple graphs)

In the above plot the x coordinates were implicitly set to the indices of the array `a`, that is, `arange(10)`. Find out from the documentation of `plt.plot` how to specify the x coordinates explicitly. Find out also how to draw multiple graphs in one axes.

Make your `main` function plot the following two graphs in one axes. The first graphs has x coordinates 2,4,6,7 and y coordinates 4,3,5,1. The second graph has x coordinates 1,2,3,4 and y coordinates 4,2,3,1.

Add also a title and some labels for x axis and y axis. Note that in the non-interactive mode you have to call `plt.show()` for the figure to show.

The plot should look like the one below.

![multiplot](multiplot.png)
<hr/>

#### Exercise 10 (subfigures)

Write function `subfigures` that creates a figure that has two subfigures (two *axes* in matplotlib parlance). The function gets a two dimensional array `a` as a parameter. In the left subfigure draw using the `plot` *method* a graph, whose x coordinates are in the first column of `a` and the y coordinates are in the second column of `a`. In the right subfigure draw using the `scatter` *method* a set of points whose x coords are again in the first column of `a` and whose y coordinates are in the second column of `a`. Additionally, the points should get their color from the third column of `a`, and size of the point from the fourth column of `a`. For this, use the `c` and `s` named parameters of `scatter`, respectively

Test your function `subfigure` from the `main` function.
<hr/>

# Image processing

#### Exercise 11 (to grayscale)

This exercise can give two points at maximum!

##### Part 1.

Write a function `to_grayscale` that takes an RGB image (three dimensional array) and returns a two dimensional gray-scale image. The conversion to gray-scale should take a weighted sum of the red, green, and blue values, and use that as the value of gray. The first axis is the x, the second is y, and the third is the color components (red, green, blue).
Use the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. These weights are so because the human eye is most sensitive to green color and least sensitive to blue color.

In the main function you can, for example, use the provided image `src/painting.png`. Display the grayscale image with the `plt.imshow` function. You may have to call the function `plt.gray` to set the color palette (colormap) to gray.
(See `help(plt.colormaps)` for more information about colormaps.)

##### Part 2.

Write functions `to_red`, `to_green`, and `to_blue` that get a three dimensional array as a parameter and return a three dimensional arrays. For instance, the function `to_red` should zero out the green and blue color components and return the result. In the `main` function create a figure with three subfigures: the top one should be the red image, the middle one the green image, and the bottom one the blue image.
<hr/>

#### Exercise 12 (radial fade)

Make program that does fading of an image as earlier, except now not in horizontal direction but in radial direction. As we move away from the centre of the image, the pixels fade to black.

##### Part1.

Write function `center` that returns coordinate pair (center_y, center_x) of the image center. Note that these coordinates might not be integers. Example of usage:
```python
print(center(np.zeros((10, 11, 3))))
(4.5, 5)
```
The function should work both for two and three dimensional images, that is grayscale and color images.

Write also function `radial_distance` that returns for image with width `w` and height `h` an array with shape (h,w), where the number at index (i,j) gives the euclidean distance from the point (i,j) to the center of the image.

##### Part 2.

Create function `scale(a, tmin=0.0, tmax=1.0)` that returns a copy of the array `a` with its elements scaled to be in the range `[tmin,tmax]`.

Using the functions `radial_distance` and `scale` write function `radial_mask` that takes an image as a parameter and returns an array with same height and width filled with values between 0.0 and 1.0. Do this using the `scale` function.  To make the resulting array values near the center of array to be close to 1 and closer to the edges of the array are values closer to be 0, subtract the previous array from 1.

Write also function `radial_fade` that returns the image multiplied by its radial mask.

Test your functions in the `main` function, which should create, using matplotlib, a figure that has three subfigures stacked vertically. On top the original `painting.png`, in the middle the mask, and on the bottom the faded image.
<hr/>

# Pandas

#### Exercise 13 (read series)

Write function `read_series` that reads input lines from the user and return a Series. Each line should contain first the index and then the corresponding value, separated by whitespace. The index and values are strings (in this case `dtype` is `object`). An empty line signals the end of Series. Malformed input should cause an exception. An input line is malformed, if it is non-empty and, when split at whitespace, does not result in two parts.

Test your function from the `main` function.

---

#### Exercise 14 (operations on series)

Write function `create_series` that gets two lists of numbers as parameters. Both lists should have length 3.
The function should first create two Series, `s1` and `s2`. The first series should have values from the first parameter list and have corresponding indices `a`, `b`, and  `c`. The second series should get its values from the second parameter list and have again the corresponding indices `a`, `b`, and  `c`. The function should return the pair of these Series.

Then, write a function `modify_series` that gets two Series as parameters. It should add to the first Series `s1` a new value with index `d`. The new value should be the same as the value in Series `s2` with index `b`.
Then delete the element from `s2` that has index `b`. Now the first Series should have four values, while the second list has only two values. Adding a new element to a Series can be achieved by assignment, like with dictionaries. Deletion of an element from a Series can be done with the `del` statement.

Test these functions from the main function. Try adding together the Series returned by the `modify_series` function. The operations on Series use the indices to keep the element-wise operations *aligned*. If for some index the operation could not be performed, the resulting value will be `NaN` (Not A Number).

<hr/>

#### Exercise 15 (inverse series)

Write function `inverse_series` that get a Series as a parameter and returns a new series, whose indices and values have swapped roles. Test your function from the `main` function.

What happens if some value appears multiple times in the original Series? What happens if you use this value to index the resulting Series?
<hr/>

# [ PART 3 ]

#### Exercise 1 (cities)

Write function `cities` that returns the following DataFrame of top Finnish cities by population:

```
                 Population Total area
Helsinki         643272     715.48
Espoo            279044     528.03
Tampere          231853     689.59
Vantaa           223027     240.35
Oulu             201810     3817.52
```

<hr/>

#### Exercise 2 (powers of series)

Make function `powers_of_series` that takes a Series and a positive integer `k` as parameters and returns a DataFrame. The resulting DataFrame should have the same index as the input Series. The first column of the dataFrame should be the input Series, the second column should contain the Series raised to power of two. The third column should contain the Series raised to the power of three, and so on until (and including) power of `k`. The columns should have indices from 1 to k.

The values should be numbers, but the index can have any type.
Test your function from the `main` function. Example of usage:

```
s = pd.Series([1,2,3,4], index=list("abcd"))
print(powers_of_series(s, 3))
```
Should print:
```
   1   2   3
a  1   1   1
b  2   4   8
c  3   9  27
d  4  16  64
```


<hr/>

#### Exercise 3 (municipal information)

In the `main` function load a data set of municipal information from the `src` folder (originally from [Statistics Finland](https://pxnet2.stat.fi/PXWeb/pxweb/en/)). Use the function `pd.read_csv`, and note that the separator is a tabulator.

Print the shape of the DataFrame (number of rows and columns) and the column names in the following format:
```
Shape: r,c
Columns:
col1 
col2
...
```

Note, sometimes file ending `tsv` (tab separated values) is used instead of `csv` if the separator is a tab.
<hr/>

#### Exercise 4 (municipalities of finland)

Load again the municipal information DataFrame. The rows of the DataFrame correspond to various geographical areas of Finland. The first row is about Finland as a whole, then rows from Akaa to Äänekoski are municipalities of Finland in alphabetical order. After that some larger regions are listed.

Write function `municipalities_of_finland` that returns a DataFrame containing only rows about municipalities.
Give an appropriate argument for `pd.read_csv` so that it interprets the column about region name as the (row) index. This way you can index the DataFrame with the names of the regions.

Test your function from the `main` function.
<hr/>

#### Exercise 5 (swedish and foreigners)

Write function `swedish_and_foreigners` that

* Reads the municipalities data set
* Takes the subset about municipalities (like in previous exercise)
* Further take a subset of rows that have proportion of Swedish speaking people and proportion of foreigners both above 5 % level
* From this data set take only columns about population, the proportions of Swedish speaking people and foreigners, that is three columns.

The function should return this final DataFrame.

Do you see some kind of correlation between the columns about Swedish speaking and foreign people? Do you see correlation between the columns about the population and the proportion of Swedish speaking people in this subset?

<hr/>

#### Exercise 6 (growing municipalities)

Write function `growing_municipalities` that gets subset of municipalities (a DataFrame) as a parameter and returns the proportion of municipalities with increasing population in that subset.

Test your function from the `main` function using some subset of the municipalities.
Print the proportion as percentages using 1 decimal precision.

Example output:

```
Proportion of growing municipalities: 12.4%
```

<hr/>

#### Exercise 7 (subsetting with loc)

Write function `subsetting_with_loc` that in one go takes the subset of municipalities from Akaa to Äänekoski and restricts it to columns: "Population", "Share of Swedish-speakers of the population, %", and "Share of foreign citizens of the population, %".
The function should return this content as a DataFrame. Use the attribute `loc`.


<hr/>

#### Exercise 8 (subsetting by positions)

Write function `subsetting_by_positions` that does the following.

Read the data set of the top forty singles from the beginning of the year 1964 from the `src` folder. Return the top 10 entries and only the columns `Title` and `Artist`. Get these elements by their positions, that is, by using a single call to the `iloc` attribute. The function should return these as a DataFrame.

<hr/>

#### Exercise 9 (snow depth)

Write function `snow_depth` that reads in the weather DataFrame from the `src` folder and returns the maximum amount of snow in the year 2017.

Print the result in the `main` function in the following form:
```
Max snow depth: xx.x
```

<hr/>

#### Exercise 10 (average temperature)

Write function `average_temperature` that reads the weather data set and returns the average temperature in July.

Print the result in the `main` function in the following form:
```
Average temperature in July: xx.x
```
<hr/>

#### Exercise 11 (below zero)

Write function `below_zero` that returns the number of days when the temperature was below zero.

Print the result in the main function in the following form:

```
Number of days below zero: xx
```
<hr/>

#### Exercise 12 (cyclists)

Write function `cyclists` that does the following.

Load the Helsinki bicycle data set from the `src` folder (https://hri.fi/data/dataset//helsingin-pyorailijamaarat). The dataset contains the number of cyclists passing by measuring points per hour. The data is gathered over about four years, and there are 20 measuring points around Helsinki. The dataset contains some empty rows at the end. Get rid of these. Also, get rid of columns that contain only missing values. Return the cleaned dataset. 

<hr/>

#### Exercise 13 (missing value types)

Make function `missing_value_types` that returns the following DataFrame. Use the `State` column as the (row) index. The value types for the two other columns should be `float` and `object`, respectively. Replace the dashes with the appropriate missing value symbols.

State | Year of independence | President
------|----------------------|----------
United Kingdom | - | -
Finland | 1917 | Niinistö
USA | 1776 | Trump
Sweden | 1523 | -
Germany | - | Steinmeier
Russia | 1992 | Putin

<hr/>

#### Exercise 14 (special missing values)

Write function `special_missing_values` that does the following.

Read the data set of the top forty singles from the beginning of the year 1964 from the `src` folder. Return the rows whose singles' position dropped compared to last week's position (column LW=Last Week).

To do this you first have to convert the special values "New" and "Re" (Re-entry) to missing values (`None`).

<hr/>

#### Exercise 15 (last week)

This exercise can give two points at maximum!

Write function `last_week` that reads the top40 data set mentioned in the above exercise. The function should then try to reconstruct the top40 list of the previous week based on that week's list. Try to do this as well as possible. You can fill the values that are impossible to reconstruct by missing value symbols. Your solution should work for a top40 list of any week. So don't rely on specific features of this top40 list. The column `WoC` means "Weeks on Chart", that is, on how many weeks this song has been on the top 40 list.

Hint. First create the last week's top40 list of those songs that are also on this week's list. Then add those entries that were not on this week's list. Finally sort by position.

Hint 2. The `where` method of Series and DataFrame can be useful. It can also be nested.

Hint 3. Like in NumPy, you can use with Pandas the bitwise operators `&`, `|`, and `~`.
Remember that he bitwise operators have higher precedence than the comparison operations, so you may
have to use parentheses around comparisons, if you combined result of comparisons with bitwise operators.

You get a second point, if you get the columns `LW` and `Peak Pos` correct.

<hr/>

#### Exercise 16 (split date)

Read again the bicycle data set from `src` folder,
and clean it as in the earlier exercise. Then split the `Päivämäärä` column into a DataFrame with five columns with column names `Weekday`, `Day`, `Month`, `Year`, and `Hour`. Note that you also need to to do some conversions. To get Hours, drop the colon and minutes. Convert field `Weekday` according the following rule:
```
ma -> Mon
ti -> Tue
ke -> Wed
to -> Thu
pe -> Fri
la -> Sat
su -> Sun
```
Convert the `Month` column according to the following mapping
```
tammi 1
helmi 2
maalis 3
huhti 4
touko 5
kesä 6
heinä 7
elo 8
syys 9
loka 10
marras 11
joulu 12
```

Create function `split_date` that does the above and returns a DataFrame with five columns. You may want to use the `map` method of Series objects.

So the first element in the `Päivämäärä` column of the original data set should be converted from
`ke 1 tammi 2014 00:00`
to
`Wed 1 1 2014 0` . Test your solution from the `main` function.
<hr/>

#### Exercise 17 (cleaning data)

This exercise can give two points at maximum!

The entries in the following table of US presidents are not uniformly formatted. Make function `cleaning_data` that reads the table from the tsv file `src/presidents.tsv` and returns the cleaned version of it. Note, you must do the edits programmatically using the string edit methods, not by creating a new DataFrame by hand. The columns should have `dtype`s `object`, `integer`, `float`, `integer`, `object`. The `where` method of DataFrames can be helpful, likewise the [string methods](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#string-methods) of Series objects. You get an additional point, if you manage to get the columns President and Vice-president right!

President |	Start |	Last |	Seasons | 	Vice-president|
----------|-------|------|----------|------------------|
donald trump|	2017 Jan|	-|	1|	Mike pence
barack obama|	2009|	2017|	2|	joe Biden
bush, george|	2001|	2009|	2|	Cheney, dick
Clinton, Bill|	1993|	2001|	two|	gore, Al

<hr/>

#### Exercise 2 (cycling weather)

Merge the processed cycling data set (from the previous exercise) and weather data set along the columns year, month, and day. Note that the names of these columns might be different in the two tables: use the `left_on` and `right_on` parameters. Then drop useless columns 'm', 'd', 'Time', and 'Time zone'.

Write function `cycling_weather` that reads the data sets and returns the resulting DataFrame.

<hr/>

#### Exercise 3 (top bands)

Merge the DataFrames UK top40 and the bands DataFrame that are stored in the `src` folder.
Do all this in the parameterless function `top_bands`, which should return the merged DataFrame.
Use the `left_on` and `right_on` parameters to `merge`. Test your function from the `main` function.

<hr/>

#### Exercise 4 (cyclists per day)

This exercise can give two points at maximum!

Part 1.

Read, clean and parse the bicycle data set as before. Group the rows by year, month, and day. Get the sum for each group.
Make function `cyclists_per_day` that does the above. The function should return a DataFrame.
Make sure that the columns Hour and Weekday are not included in the returned DataFrame.

Part 2.

In the `main` function, using the function `cyclists_per_day`, get the daily counts.  The index of the DataFrame now consists of tuples (Year, Month, Day). Then restrict this data to August of year 2017, and plot this data. Don't forget to call the `plt.show` function of matplotlib. The x-axis should have ticks from 1 to 31, and there should be a curve to each measuring station. Can you spot the weekends?

<hr/>

#### Exercise 5 (best record company)

We use again the UK top 40 data set from the first week of 1964 in the `src` folder. Here we define "goodness" of a record company (`Publisher`) based on the sum of the weeks on chart (WoC) of its singles. Return a DataFrame of the singles by the best record company (a subset of rows of the original DataFrame). Do this with function `best_record_company`.

<hr/>

#### Exercise 6 (suicide fractions)

Load the suicide data set from `src` folder. This data was originally downloaded from [Kaggle](https://www.kaggle.com/szamil/who-suicide-statistics). Kaggle contains lots of interesting open data sets.

Write function `suicide_fractions` that loads the data set and returns a Series that has the country as the (row) index and as the column the mean fraction of suicides per population in that country. In other words, the value is the average of suicide fractions. The information about year, sex and age is not used.

<hr/>

#### Exercise 7 (suicide weather)

Copy the function `suicide fractions` from the previous exercise. 

Implement function `suicide_weather` as described below.
We use the dataset of average temperature (over years 1961-1990) in different countries from `src/List_of_countries_by_average_yearly_temperature.html` (https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature) .
You can use the function `pd.read_html` to get all the tables from a html page. By default `pd.read_html` does not know which row contains column headers and which column contains row headers. Therefore, you have to give both `index_col` and `header` parameters to `read_html`. Maku sure you use the country as the (row) index for both of the DataFrames. What is the [Spearman correlation](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) between these variables? Use the `corr` method of Series object. Note the the two Series need not be sorted as the indices of the rows (country names) are used to align them.

The return value of the function `suicide_weather` is a tuple (suicide_rows, temperature_rows, common_rows, spearman_correlation)
The output from the `main` function should be of the following form:

```
Suicide DataFrame has x rows
Temperature DataFrame has x rows
Common DataFrame has x rows
Spearman correlation: x.x
```

You might have trouble when trying to convert the temperatures to float. The is because the negative numbers on that html page use a special *unicode minus sign*, which looks typographically nice, but the float constructor cannot interpret it as a minus sign. You can try out the following example:

---

#### Exercise 8 (bicycle timeseries)

Write function `bicycle_timeseries` that

* reads the data set
* cleans it
* turns its `Päivämäärä` column into (row) DatetimeIndex (that is, to row names) of that DataFrame
* returns the new DataFrame

<hr/>

#### Exercise 9 (commute)

In function `commute` do the following:

Use the function `bicycle_timeseries` to get the bicycle data. Restrict to August 2017, group by the weekday, aggregate by summing. Set the `Weekday` column to numbers from one to seven. Then set the column `Weekday` as the (row) index. Return the resulting DataFrame from the function.

In the `main` function plot the DataFrame. Xticklabels should be the weekdays. Don't forget to call `show` function!

If you want the xticklabels to be `['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']` instead of numbers (1,..,7), then it may get a bit messy. There seems to be a problem with non-numeric `x` values. You could try the following after plotting, but you don't have to:

```python
weekdays="x mon tue wed thu fri sat sun".title().split()
plt.gca().set_xticklabels(weekdays)
```

<hr/>

