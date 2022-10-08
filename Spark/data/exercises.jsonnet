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
    Exercise("10/8/2022", "walk", 5.01, "New York, NY", 1, 22, 51),
    Exercise("10/6/2022", "walk", 7.99, "Sandy Springs, GA", 2, 11, 27),
    Exercise("10/6/2022", "walk", 1.39, "Atlanta, GA", 0, 39, 45),
    Exercise("10/5/2022", "strength training", null, "Sandy Springs, GA", 0, 11, 13),
    Exercise("10/5/2022", "core", null, "Sandy Springs, GA", 0, 16, 9),
    Exercise("10/5/2022", "walk", 2.07, "Sandy Springs, GA", 0, 35, 54)
]