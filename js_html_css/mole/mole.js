"use strict";

//inputs
//transform
function pickRandomNum(){return _.random(1, 20)}

function selectRandomHoleID(){
    var randomNum = pickRandomNum();
    return "#hole" + randomNum
}
//create
function changeImageToTrump(holeID) {
    return $(holeID).children("img").attr("src", "trump_head.jpg")
}
function changeImageToHole(holeID){
    return $(holeID).children("img").attr("src", "hole.png")
}
function launchTrumpIntervals() {
    setInterval(function(){
        var holeID = selectRandomHoleID();
        changeImageToTrump(holeID);
    }, 1000);
}
// function stopTrumpIntervals() {
//     clearInterval(launchTrumpIntervals());
//     console.log("stopintervals")
// }

//mains

// register

$("#startGame").on("click", function (event){
    event.preventDefault();
    launchTrumpIntervals();
});
$(".moleHole").on("click", function (event){
    event.preventDefault();
    var holeID = this.getAttribute("id");
    holeID = "#" + holeID;
    changeImageToHole(holeID);
});
// $("#stopGame").on("click", function (event){
//     event.preventDefault();
//     stopTrumpIntervals();
// });







// Make a 5x4 grid of hole images. Every second, randomly pick a hole

// in the grid and turn it's image into a mole. If the user clicks on a

// mole image, turn it back into a hole.

// Use the setInterval function to run a callback function periodically.
