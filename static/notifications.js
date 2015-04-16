/**
 * Created by Wolfram on 16/04/15.
 */
//default duration in MS
var defaultDuration = 5000

// Each of the methods shows a notification in different styles/colors
/* yellow */
function notyWarning(sometext) {
    notyWarningDuration(sometext, defaultDuration)
}

function notyWarningDuration(sometext, durationInMS) {
    noty({
        type: "warning",
        text: sometext,
        layout: 'bottomRight',
        timeout: durationInMS,
        force: true,
        closeWith: ['click']
    });
}
/* grey */
function notyInfo(sometext) {
    notyInfoDuration(sometext, defaultDuration)
}

function notyInfoDuration(sometext, durationInMS) {
    noty({
        type: "info",
        text: sometext,
        layout: 'bottomRight',
        timeout: durationInMS,
        force: true,
        closeWith: ['click']
    });
}
/* green */
function notySuccess(sometext) {
    notySuccessDuration(sometext, defaultDuration)
}

function notySuccessDuration(sometext, durationInMS) {
    noty({
        type: "success",
        text: sometext,
        layout: 'bottomRight',
        timeout: durationInMS,
        force: true,
        closeWith: ['click']
    });
}
/* red - very intense */
function notyError(sometext) {
    notyErrorDuration(sometext, defaultDuration)
}

function notyErrorDuration(sometext, durationInMS) {
    noty({
        type: "error",
        text: sometext,
        layout: 'bottomRight',
        timeout: durationInMS,
        force: true,
        closeWith: ['click']
    });
}