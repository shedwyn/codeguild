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
var brokenDictSorted = brokenDict.sort(function(a, b) {return a[1] - b[1]});

console.log("final ageToCount print", ageToCount);
console.log("brokenDict", brokenDictSorted)

// Credit for below to Peter Dziuba:, thought his solution might
// be more efficient, but needs time to study
// var my_ob = {};
// for (var name in namesToAges) {
//     var tracker = namesToAges[name];
//     if (tracker in my_ob) {
//         my_ob[tracker] += 1;
//     }
//     else {
//         my_ob[tracker] = 1;
//     }
// };
// ​
// var sortable = {};
// for (var number in my_ob) {
//     var flipper = my_ob[number]
//     sortable[flipper] = number;
// };
// ​
// var sort_array = [];
// for (var count in sortable) {
//     sort_array.push(count)
// };
// ​
// sort_array.sort(function(a, b){return a-b});
// var final_number = sort_array[0];
// console.log(sortable[final_number]);