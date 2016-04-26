"use strict";

var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};
var ageToCount = {
    "19":10,
};
var agesOnly = [];
for (var key in namesToAges) {
    var value = namesToAges[key];
    agesOnly.push(value);
};
for (var i = 0; i < agesOnly.length; i += 1) {
    var value = String(agesOnly[i]);
    if (!(value in ageToCount)){
        var count = 0;
        ageToCount[value] = count + 1;
    }
    else if (value in ageToCount){
        var prevCount = ageToCount[value];
        ageToCount[value] = prevCount + 1;   
    }
};
var brokenDict = [];
for (var age in ageToCount)
    brokenDict.push([age, ageToCount[count]]);
brokenDict.sort(function(a, b) {return a[1] - b[1]});
console.log("final ageToCount print", ageToCount);
console.log("brokenDict", brokenDict)

