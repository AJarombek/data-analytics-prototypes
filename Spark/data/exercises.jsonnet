# Jsonnet file for my recent exercises.
# Author: Andrew Jarombek
# Date: 10/8/2022

local Exercise(date, type, miles, location, hours, minutes, seconds) = {
    date: date,
    type: type,
    miles: miles,
    location: location,
    hours: hours,
    minutes: minutes,
    seconds: seconds,
};

[
    Exercise("10/8/2022", "core", null, "New York, NY", 0, 17, 12),
    Exercise("10/8/2022", "walk", 5.01, "New York, NY", 1, 22, 51),
    Exercise("10/6/2022", "walk", 7.99, "Sandy Springs, GA", 2, 11, 27),
    Exercise("10/6/2022", "walk", 1.39, "Atlanta, GA", 0, 39, 45),
    Exercise("10/5/2022", "strength training", null, "Sandy Springs, GA", 0, 11, 13),
    Exercise("10/5/2022", "core", null, "Sandy Springs, GA", 0, 16, 9),
    Exercise("10/5/2022", "walk", 2.07, "Sandy Springs, GA", 0, 35, 54),
    Exercise("10/4/2022", "walk", 3.37, "Sandy Springs, GA", 0, 58, 18),
    Exercise("10/3/2022", "strength training", null, "Sandy Springs, GA", 0, 20, 4),
    Exercise("10/3/2022", "core", null, "Sandy Springs, GA", 0, 17, 38),
    Exercise("10/3/2022", "walk", 2.13, "Sandy Springs, GA", 0, 37, 48),
    Exercise("10/3/2022", "walk", 1.78, "New York, NY", 0, 31, 10),
    Exercise("10/3/2022", "walk", 1.75, "New York, NY", 0, 30, 11),
    Exercise("10/2/2022", "strength training", null, "New York, NY", 0, 30, 7),
    Exercise("10/2/2022", "bike", 6.66, "New York, NY", 0, 32, 45),
    Exercise("10/2/2022", "walk", 3.12, "New York, NY", 0, 55, 7),
    Exercise("10/2/2022", "run", 2.10, "New York, NY", 0, 17, 34),
    Exercise("10/2/2022", "core", null, "New York, NY", 0, 17, 22),
    Exercise("10/1/2022", "bike", 7.25, "New York, NY", 0, 40, 24),
    Exercise("10/1/2022", "walk", 2.58, "New York, NY", 0, 40, 17),
    Exercise("10/1/2022", "strength training", null, "New York, NY", 0, 49, 50),
    Exercise("10/1/2022", "core", null, "New York, NY", 0, 20, 29),
    Exercise("10/1/2022", "walk", 3.32, "New York, NY", 0, 58, 27),
    Exercise("9/30/2022", "strength training", null, "New York, NY", 0, 49, 35),
    Exercise("9/29/2022", "strength training", null, "New York, NY", 0, 47, 26),
    Exercise("9/29/2022", "core", null, "New York, NY", 0, 18, 38),
    Exercise("9/29/2022", "run", 3.02, "New York, NY", 0, 22, 10),
    Exercise("9/28/2022", "strength training", null, "New York, NY", 0, 48, 7),
    Exercise("9/27/2022", "walk", 0.90, "New York, NY", 0, 13, 54),
    Exercise("9/27/2022", "strength training", null, "New York, NY", 0, 51, 45),
    Exercise("9/27/2022", "walk", 3.10, "New York, NY", 0, 58, 13),
    Exercise("9/27/2022", "run", 1.90, "New York, NY", 0, 18, 3),
    Exercise("9/26/2022", "walk", 2.50, "New York, NY", 0, 46, 38),
    Exercise("9/26/2022", "walk", 1.77, "New York, NY", 0, 31, 18),
    Exercise("9/26/2022", "walk", 1.79, "New York, NY", 0, 30, 6),
    Exercise("9/25/2022", "walk", 1.70, "New York, NY", 0, 32, 25),
    Exercise("9/25/2022", "run", 1.36, "Old Greenwich, CT", 0, 16, 57),
    Exercise("9/25/2022", "strength training", null, "Riverside, CT", 0, 36, 0),
    Exercise("9/25/2022", "kayak", 7.08, "Stamford, CT", 2, 10, 17),
    Exercise("9/25/2022", "walk", 4.23, "Greenwich, CT", 1, 23, 35),
    Exercise("9/24/2022", "walk", 3.70, "Greenwich, CT", 1, 12, 21),
    Exercise("9/24/2022", "core", null, "Riverside, CT", 0, 17, 54),
    Exercise("9/24/2022", "kayak", 3.02, "Riverside, CT", 0, 52, 35),
    Exercise("9/24/2022", "strength training", null, "Riverside, CT", 0, 40, 14),
    Exercise("9/24/2022", "walk", 4.06, "Greenwich, CT", 1, 16, 20),
    Exercise("9/23/2022", "core", null, "Riverside, CT", 0, 13, 17),
    Exercise("9/23/2022", "bike", null, "Riverside, CT", 0, 30, 2),
    Exercise("9/23/2022", "strength training", null, "Riverside, CT", 0, 41, 58),
    Exercise("9/23/2022", "walk", 1.50, "Riverside, CT", 0, 30, 24),
    Exercise("9/22/2022", "walk", 1.16, "Riverside, CT", 0, 22, 31),
    Exercise("9/22/2022", "walk", 1.74, "New York, NY", 0, 33, 16),
    Exercise("9/22/2022", "strength training", null, "New York, NY", 0, 30, 0),
    Exercise("9/21/2022", "walk", 0.86, "New York, NY", 0, 14, 22),
    Exercise("9/21/2022", "strength training", null, "New York, NY", 0, 35, 26),
    Exercise("9/20/2022", "walk", 3.12, "New York, NY", 0, 58, 24),
    Exercise("9/20/2022", "run", 0.65, "New York, NY", 0, 5, 52),
    Exercise("9/20/2022", "strength training", null, "New York, NY", 0, 36, 52),
    Exercise("9/19/2022", "walk", 1.93, "New York, NY", 0, 37, 7),
    Exercise("9/19/2022", "walk", 1.79, "New York, NY", 0, 32, 47),
    Exercise("9/19/2022", "strength training", null, "New York, NY", 0, 25, 0),
    Exercise("9/19/2022", "walk", 1.86, "New York, NY", 0, 33, 24),
    Exercise("9/18/2022", "run", 1.69, "New York, NY", 0, 18, 32),
    Exercise("9/18/2022", "bike", 7.25, "New York, NY", 0, 36, 42),
    Exercise("9/18/2022", "core", null, "New York, NY", 0, 21, 25),
    Exercise("9/18/2022", "strength training", null, "New York, NY", 0, 36, 56),
    Exercise("9/17/2022", "walk", 0.86, "New York, NY", 0, 15, 34),
    Exercise("9/17/2022", "core", null, "New York, NY", 0, 26, 56),
    Exercise("9/17/2022", "strength training", null, "New York, NY", 0, 35, 21),
    Exercise("9/16/2022", "core", null, "New York, NY", 0, 23, 37),
    Exercise("9/16/2022", "walk", 1.24, "New York, NY", 0, 24, 42),
    Exercise("9/16/2022", "bike", 8.55, "New York, NY", 0, 43, 13),
    Exercise("9/16/2022", "run", 0.54, "New York, NY", 0, 4, 45),
    Exercise("9/16/2022", "strength training", null, "New York, NY", 0, 35, 11),
]