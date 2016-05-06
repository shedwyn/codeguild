"use strict";

var holeImage = $("<img>").attr("src", "hole.png")
var trumpImage =  $("<img>").attr("src", "trump_head.jpg")
function pickRandomNum(){
    return _.random(1, 20)
}
function assembleHoleID(){
    var randomNum = pickRandomNum();
    return "#hole" + randomNum
}





function grabHoleImage(){
    var holeID = assembleHoleID()
}

function clickRevertImage(){

}

function launchTrumpIntervals() {
    setInterval(function(){
    launchFunction; 
    }, 1000);
}

















// Save your solution as mole.html, mole.css, and mole.js.

// Make a 5x4 grid of hole images. Every second, randomly pick a hole 

// in the grid and turn it's image into a mole. If the user clicks on a 

// mole image, turn it back into a hole.

// Use the setInterval function to run a callback function periodically.

// function holeIDs () {
//     var parent = $("#playArea")
//     var childCount = parent.children().length
//     for (i = 0; i <= childCount; i += 1) 
        
// }

// var holeIDs = ["hole01", "hole02", "hole03", "hole04", "hole05", 
//     "hole06", "hole07", "hole08", "hole09", "hole10", "hole11", "hole12",
//     "hole13", "hole14", "hole15", "hole16", "hole17", "hole18", "hole19",
//     "hole20"];