"use strict";

function getNumberToRoll(){
    return $("#numberToRoll").val()
}
function rollSingleDie(){
    return _.random(1, 6)
}
function createDieImage(){
    var dieImageLocation = diceImages[rollSingleDie()];
    return $("<img>").attr("src", dieImageLocation)
}
function addDieToDiceArea(){
    var numberOfRolls = getNumberToRoll();
    for (var i = 0; i < numberOfRolls; i += 1) {
        $("#diceArea").append(createDieImage());
    };
    //Adding children to parent section
}
function tallyHand(){
    var parent = $("#diceArea");
    var childCount = parent.children().length;
    $("#tallyHand").text("Simple Dice Score:  " + childCount);
}
function runIntialRoll(){
    $("form").on("submit", function (event){
        event.preventDefault();
        addDieToDiceArea();
        tallyHand();
    })
}
function deleteSingleDie(){
}
function eraseEntireHand(){
}
var diceImages = {
    "1":"http://www.wpclipart.com/recreation/games/dice/.cache/die_face_1.png",
    "2":"http://www.wpclipart.com/recreation/games/dice/.cache/die_face_2.png",
    "3":"http://www.wpclipart.com/recreation/games/dice/.cache/die_face_3.png",
    "4":"http://www.wpclipart.com/recreation/games/dice/.cache/die_face_4.png",
    "5":"http://www.wpclipart.com/recreation/games/dice/.cache/die_face_5.png",
    "6":"http://www.wpclipart.com/recreation/games/dice/.cache/die_face_6.png",
};
console.log(createImageElement());
// Give the user a number input box with a button "roll". When they click that 
    // button, make that many 6-sided dice appear on the screen.
// The dice should appear visually as dice, although for testing you can just 
    // start with numbers. Come up with any reasonable way to display the visual dice.
// If the user clicks any of the dice, it re-rolls just that one. If they re-click 
    // the roll button, erase the dice and roll new ones.
// At the bottom of the screen, show the sum of all the dice currently out.