"use strict";

function getNumberToRoll(){
    return $("#numberToRoll").val()
}
function rollSingleDie(){
    return _.random(1, 6)
}
function createDieImage(dieValue){
    var dieImageLocation = diceImages[dieValue];
    return $("<img>").attr("src", dieImageLocation)
}
function addDieToDiceArea(){
    var numberOfRolls = getNumberToRoll();
    var dieRolls = [];
    for (var i = 0; i < numberOfRolls; i += 1) {
        var dieValue = rollSingleDie();
        dieRolls.push(dieValue);
        $("#diceArea").append(createDieImage(dieValue));
    };
    //Adding children to parent section
    return dieRolls
}
function tallyHand(dieRolls){
    var diceTally = _.reduce(
        dieRolls,
        function (runningTotal, item) {
            return runningTotal + item;
        },
        0);
    $("#handTally").text("Simple Dice Score:  " + diceTally);
}
function initiateFullRoll(){
    $("form").on("submit", function (event){
        event.preventDefault();
        $("#diceArea").empty()
        var dieRolls = addDieToDiceArea();
        tallyHand(dieRolls);
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
$(document).ready(function(){
    //this could be the equivalent of jquery main
    initiateFullRoll();
});
// Give the user a number input box with a button "roll". When they click that 
    // button, make that many 6-sided dice appear on the screen.
// The dice should appear visually as dice, although for testing you can just 
    // start with numbers. Come up with any reasonable way to display the visual dice.
// If the user clicks any of the dice, it re-rolls just that one. If they re-click 
    // the roll button, erase the dice and roll new ones.
// At the bottom of the screen, show the sum of all the dice currently out.