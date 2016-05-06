"use strict";

//inputs

var holeImage = $("<img>").attr("src", "hole.png").attr("id", "holeImage";)
var trumpImage =  $("<img>").attr("src", "trump_head.jpg").attr("id", "trumpImage";)

//transform

function pickRandomNum(){return _.random(1, 20)}

function assembleHoleID(){
    var randomNum = pickRandomNum();
    return "#hole" + randomNum
}

//create

function toggleOffHoleImage(holeID){
    return $(holeID).children(".holeImage").css("display", "none")
}
function toggleOffTrumpImage(holeID){
    return $(holeID).children(".trumpImage").css("display", "none")
}
function toggleOnHoleImage(holeID){
    return $(holeID).children(".holeImage").css("display", "block")
}
function toggleOnTrumpImage(holeID) {
    return $(holeID).children(".trumpImage").css("display", "block")
}
function changeImageToTrump(holeID) {
    return $(holeID).children("<img>").attr("src", "trump_head.jpg")
}
function changeImageToHole(holeID){
    return $(holeID).children(".holeImage").css("src", "hole.png")
}
function toggleTrumpToHole(holeID){
    console.log("yes, we got here");
    toggleOffTrumpImage(holeID);
    toggleOnHoleImage(holeID)
}

function launchTrumpIntervals() {
    setInterval(function(){
        var holeID = assembleHoleID();
        console.log(holeID);
        toggleOffHoleImage(holeID);
        toggleOnTrumpImage(holeID);
    }, 1000);
}
function stopTrumpIntervals() {
    clearInterval(launchTrumpIntervals);
}

function clickImageOff(){
    getHoleID()
    toggleOffTrumpImage()
    toggleOnHoleImage()
}



//mains



// register

// $("#playArea").on("click", function (event){
//     event.preventDefault();
//     launchTrumpIntervals;
// });
$(".moleHole").on("click", function (event){
    event.preventDefault();
    var holeID = this.getAttribute("id")
    console.log(holeID)
    toggleTrumpToHole(holeID)
})







// Make a 5x4 grid of hole images. Every second, randomly pick a hole

// in the grid and turn it's image into a mole. If the user clicks on a

// mole image, turn it back into a hole.

// Use the setInterval function to run a callback function periodically.
