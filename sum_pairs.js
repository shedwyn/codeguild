//sum_pairs.js

var findSumPairs = function(pairs, pairSum){
    var finalResult = [];
    for (var i = 0; i < pairs.length; i += 1) { //while i < pairs.length
        for (var secondI = i + 1; secondI <= pairs.length; secondI += 1){
            if (pairs[i] + pairs[secondI] === pairSum){
                finalResult.push([pairs[i], pairs[secondI]])
            };
        };
    };
    return finalResult;
};

console.dir(findSumPairs([-1, 0, 1, 2], 3)); // 6 unique combos
console.dir(findSumPairs([-1, 0, 1, 2], 1)); // 6 unique combos
console.dir(findSumPairs([2, -1, 2], 1)); // 5 unique combos
console.dir(findSumPairs([-1, 1, 2, 2], 3)); // 6 unique combos


// for (var i = 0; i < pairs.length; i += 1) {
    //         if (pairs[i] + pairs[i - 1] === pairSum){
    //             finalResult.push([pairs[i], pairs[i - 1]])
    //         }
    //     };

// This is how you can approach these problems in general on your own:

// The first of the pair can be picked in N (=100) ways. You don't want to 
// pick this item again, so the second of the pair can be picked in N-1 (=99) 
// ways. In total you can pick 2 items out of N in N(N-1) (= 100*99=9900) 
// different ways.

// But hold on, this way you count also different orderings: AB and BA are 
// both counted. Since every pair is counted twice you have to divide N(N-1) 
// by two (the number of ways that you can order a list of two items). 
// The number of subsets of two that you can make with a set of N is then 
// N(N-1)/2 (= 9900/2 = 4950)

// loop through find_sum_pairs[lowerIndex, lowerIndex + 1] while lowerIndex < find_sum_pairs.length
//     ratchet lowerIndex + 1 through each loop
// loop through each number (starting with -1?) and add to one previous ie 0 + -1, 1 + 0, 2 + 1, 3 + 2