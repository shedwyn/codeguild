"use strict";
//inputs
function fetchFullNameInput(){
    return $("#fullName").val()
}
function fetchBirthDateInput(){
    return $("#birthDate").val()
}
function fetchPhoneNumInput(){
    return $("#phoneNum").val()
}
//transform
function checkFieldEmpty(anyObject){
    if (anyObject !== "") {
        return false
    }
    else {
        return true
    }
    // can I use jQuery.isEmptyObject($("#fullName"))?
}
function checkNameCount(namesList){
    if (namesList.length !== 2) {
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
    if (checkNameCount(namesList) !== true || 
        firstName[0] !== firstName[0].toUpperCase() ||
        lastName[0] !== lastName[0].toUpperCase()
        ){
        return false
    }
    else {
        return true
    }
}
function checkFullName(){
    // needs check for alpha characters
    var fullName = fetchFullNameInput()
    var namesList = fullName.split(" ");
    var fieldName = "Full Name"
    if (checkFieldEmpty(fullName) === false && checkNameCount(namesList) === false || 
        checkFieldEmpty(fullName) === false && checkNameCapital(namesList) === false) {
        return false
    }
    else {
        return true
    }
}
function checkBirthDate(){
    var regexLayout = /^(\d{4})(\-)(\d{2})(\-)(\d{2})$/
    var birthDate = fetchBirthDateInput()
    // var regexLayout = /(\d{4})-(\d{2})-(\d{2})/
    if (checkFieldEmpty(birthDate) === false && !(birthDate.match(regexLayout))){
        return false
    }
    else {
        return true
    }
}
function checkPhoneNum(){
    var regexLayout = /^(\d{3})(\-)(\d{3})(\-)(\d{4})$/
    var phoneNum = fetchPhoneNumInput()
    if (checkFieldEmpty(phoneNum) === false && !(phoneNum.match(regexLayout))){
        return false
    }
    else {
        return true
    }
}
function createWarningIDTag(fieldName){
    var fieldNameParts = fieldName.split(" ");
    // fieldNameParts[1] = fieldNameParts[1].toUpperCase()
    return fieldNameParts.join("")
}
function runFinalCheck(){
    if (checkFieldEmpty() === false && checkFullName() === true && checkBirthDate() === true && checkPhoneNum() === true) {
        return true
    }
    else {
        return false
    }
}
//create
function updateFullNameWarning(boolVal){
    if (boolVal === false) {
        $("#fullName").css("background-color", "yellow");
        $("#warnings").append(formatWarningNotice("full name"));
    }
    else {
        $("#warnings").empty();
        $("#fullName").css("background-color", "initial")
    }
}
function formatWarningNotice(fieldName){
    var idTagForNotice = createWarningIDTag(fieldName);
    var warningNotice = $("<p></p>").text("WARNING!  You are in danger! The " + fieldName +
        " field you have been editing is incorrect.  Take a look at the example given " +
        "and try again, mmm-Kay?  What are you waiting for?  GO NOW!")
        .css("background-color", "yellow")
        .attr("id", idTagForNotice)
    return warningNotice
}
function updateBirthDateWarning(boolVal){
    if (boolVal === false) {
        $("#birthDate").css("background-color", "yellow");
        $("#warnings").append(formatWarningNotice("birth date"));
    }
    else {
        $("#warnings").empty();
        $("#birthDate").css("background-color", "initial")
    }
}
function updatePhoneNumWarning(boolVal){
    if (boolVal === false) {
        $("#phoneNum").css("background-color", "yellow");
        $("#warnings").append(formatWarningNotice("phone number"));
    }
    else {
        $("#warnings").empty();
        $("#phoneNum").css("background-color", "initial")
    }
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
function submitButtonEvent(){
    if (runFinalCheck() === true) {
        $("#warnings").empty();
        $("#warnings").append(formatApprovalNotice())
    }
    else {
        $("#warnings").empty();
        $("#warnings").append(formatMalformNotice())
    }
}    
//mains
function runNameCheckMain(){
    var fullName = fetchFullNameInput();
    var nameCheckResult = checkFullName();
    updateFullNameWarning(nameCheckResult)
}
function runBirthDateCheckMain(){
    var birthDate = fetchBirthDateInput();
    var birthDateCheckResult = checkBirthDate();
    updateBirthDateWarning(birthDateCheckResult)
}
function runPhoneNumCheckMain(){
    var phoneNum = fetchBirthDateInput();
    var phoneNumCheckResult = checkPhoneNum();
    updatePhoneNumWarning(phoneNumCheckResult)
}
//registration
function registerInitialCallback(){
    $("#fullName").on("change", runNameCheckMain);
    $("#birthDate").on("change", runBirthDateCheckMain);
    $("#phoneNum").on("change", runPhoneNumCheckMain);
    // how do i write the item below with a prevent default action?
    $("#submitButton").on("submit", function(event){
        event.preventDefault();
        submitButtonEvent
    })
}
registerInitialCallback()