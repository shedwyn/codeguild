"use strict";
var convertWordToLeetSpeak = function(originalWord){
    var originalCharToLeetChar = {
        "o": "0",
        "l": "1",
        //more can be written here 
    }
    for (var originalChar in originalCharToLeetChar){
        originalWord = originalWord.replace("o", "0")
    }
    return originalWord.replace("o", "0");
}
console.log(convertWordToLeetSpeak("hello"));