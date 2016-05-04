"use strict";

function getNumberToRoll(){
    return $("#numberToRoll").val()
}
function rollSingleDie(){
    return _.random(1, 6)
}
function fetchDieImageURL(dieValue) {
    return diceImages[dieValue]
}
function makeDieImage(dieValue){
    return $("<img>").attr("src", fetchDieImageURL(dieValue))   
}
function createSingleDie(dieValue, idNum){
    return $("<a></a>").append(makeDieImage(dieValue)).attr("href", "").attr("id", "dice-" + idNum)
}
function createDieRollsArray(){
    var numberOfRolls = getNumberToRoll();
    var dieRolls = [];
    for (var i = 0; i < numberOfRolls; i += 1) {
        var dieValue = rollSingleDie();
        dieRolls.push(dieValue);
        // $("#diceArea").append(createSingleDie(dieValue, i))
    };
    return dieRolls
}
function addDieToDiceArea(dieRolls) {
    //Adding children to parent section
    for (var i = 0; i < dieRolls.length; i += 1) {
        var dieValue = dieRolls[i];
        createSingleDie(dieValue, i);
    }
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
        $("#diceArea").empty();
        var dieRolls = createDieRollsArray;
        addDieToDiceArea(dieRolls);
        tallyHand(dieRolls);

    })
}
function getIndexOfDice() {
    var diceIndex;
    return diceIndex 
}
function addSingleDiceToDiceArea(dieValue, indexNum) {
    return $("#diceArea").append(createSingleDie(dieValue,indexNum))
}
function getNewDiceValue() {
    var newDiceValue = rollSingleDie();
}
function replaceDiceInDieRolls(dieRolls, indexNum, newDiceValue) {
    return dieRolls[indexNum] = newDiceValue
}
// function clickChangeSingleDie() {
//     $("a").on("click", "img", function (event){
//         console.log("yes, clicked")
//         event.preventDefault();
//         // UNNAMEDFUNCTION HERE
// })
// function changeSingleDie(){
//     $("a").on("click", "img", function (event){
//         console.log("yes, clicked")
//         event.preventDefault();
//         // var anchorAttributes = this.attr();
//         // console.log(anchorAttributes);//not sure, #diceArea in first paren did not work
//     } )
// }
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
    var dieRolls = createDieRollsArray();
    initiateFullRoll();
    // clickChangeSingleDie();
})
// $(document).on("click", ".pageNumControl", function(){
//     var pageNum=$(".pageNumControl").html();