"use strict";

function checkFieldEmpty(anyObject){
    if (anyObject === "") {
        return true
    }
    else {
        return false
    }
    // can I use jQuery.isEmptyObject($("#fullName"))?
}
function checkNameCount(namesList){
    if (namesList.length < 2) {
        return false
    }
    if (namesList.length > 2) {
        return false
    }
    else {
        return true
    }
}
function checkNameLength(namesList) {
    if (checkNameCount(namesList) === false) {
        return false
    }
    if (namesList[0].length <= 1) {
        return false
    }
    else if (namesList[1].length <= 1) {
        return false
    }
    else {
        return true
    }
}
function checkNameCapital(namesList){
    // but what about triple last names? de Hoya, de Graf 
    // people who type only first initial
    var firstName = namesList[0];
    var lastName = namesList[1];
    if (checkNameCount(namesList) === false) {
        return false
    }
    else if (!(firstName[0] === firstName[0].toUpperCase())) {
        return false
    }
    else if (!(lastName[0] === lastName[0].toUpperCase())) {
        return false
    }
    else {
        return true
    }
}
function checkFullName(){
    var fullName = $("#fullName").val();
    var namesList = fullName.split(" ");
    var fieldName = "Full Name (First Last)"
    if (checkFieldEmpty(fullName) === true){
        $("#warnings").empty();
        return true
    }
    else if (checkNameCount(namesList) === false) {
        $("#fullName").css("background-color", "yellow");
        $("#warnings").append(formatWarningNotice(fieldName));
        return false
    }
    else if (checkNameLength(namesList) === false) {
        $("#fullName").css("background-color", "yellow");
        $("#warnings").append(formatWarningNotice(fieldName));
        return false
    }
    else if (checkNameCapital(namesList) === false) {
        $("#fullName").css("background-color", "yellow");
        $("#warnings").append(formatWarningNotice(fieldName));
        return false
    }
    else {
        $("#warnings").empty();
        return true
    }
}
function checkBirthDate(){
    var regexLayout = "^(\d{4})(\-)(\d{2})(\-)(\d{2})$"
}

function checkPhoneNum(){
    // 555-555-5555
    //return true or false
}
function formatWarningNotice(fieldName){
    var warningNotice = $("<p></p>").text("WARNING!  You are in danger! The " + fieldName +
        " field you have been editing is incorrect.  Take a look at the example given " +
        "and try again, mmm-Kay?  What are you waiting for?  GO NOW!")
        .css("background-color", "yellow")
    return warningNotice
}
function onNameFieldChange() {
    $("#fullName").on("change", function(event){
        event.preventDefault();
        $("#warnings").empty();
        checkFullName();
    })
}
function formatApprovalNotice(){
    var approvalNotice = $("<p></p>").text("CONGRATULATIONS!  Your data has been " +
        "accepted.  Unfortunately, you are now above the age of mandatory death.  " +
        "A team of mutant giraffes has been deployed to your present location to " +
        "terminate you.  Have a nice day.")
        .css("background-color", "green")
    return approvalNotice
    //approvalNotice.css("background-color", "green")
}
function formatMalformNotice(){
    var malformNotice = $("<p></p>").text("WARNING!  Malformed information has " +
        "been presented to your evil overlords!  This kind of egregious mistake " +
        "cannot be ignored.  A team of ninjas ('assassin' being redundant) is now " +
       "being deployed to your location and death will come on swift sword, or " +
        "nunchucks, we do not like to micro-manage.  END OF WARNING STATEMENT." +
        " Oh, and please take a few moments to fill out the exit survey before dying.")
        .css("background-color", "red")
    return malformNotice
    //malformNotice.css("background-color", "red")
}
function checkFieldsNotEmpty(){
    var fullName = $("#fullName").val()
    var birthDate = $("#birthDate").val()
    var phoneNum = $("#phoneNum").val()

    if (fullName === "") {
        return false
    }
    else if (birthDate === "") {
        return false
    }
    else if (phoneNum === "") {
        return false
    }
    else {
        return true
    }
}
    
function validateForm(){
    // posts a success or error notice
    $("#warnings").empty();
    if (checkFieldsNotEmpty() === false) {
        $("#warnings").append(formatMalformNotice())
    }
    else if (checkFullName() === false) {
        $("#warnings").append(formatMalformNotice())
    }
    // else if (checkBirthDate() === false) {
    //     $("#warnings").append(formatMalformNotice())
    // }
    // else if (checkPhoneNum() === false) {
    //     $("#warnings").append(formatMalformNotice())
    // }
    else {
        $("#warnings").append(formatApprovalNotice())
    }
}
function mainFunction(){
    checkFullName();
    onNameFieldChange();
    checkBirthDate();

    $("form").on("submit", function (event){
        event.preventDefault();
        validateForm();
    });
}
mainFunction();

