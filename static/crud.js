/**
 * Created by Wolfram on 16/04/15.
 */
function add() {
    var name = $("#add_name");
    var text = $("#add_text");
    if (name.val() != "" && text.val() != "") {
        $.ajax({
            url: '/add/' + name.val() + '/' + text.val(),
            type: 'POST',
            success: function (data) {
                notySuccess("Added " + name.val());
                text.val("");
                name.val("");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                notyError(textStatus + ": " + errorThrown);
            }
        });
    } else {
        notyWarning("You have to enter both a name and a text to add a new viki entry.")
    }
}

function del() {
    var id = $("#delete_id");
    if (id.val() != "") {
        $.ajax({
            url: '/delete/' + id.val(),
            type: 'DELETE',
            success: function (data) {
                notySuccess("Deleted entry with ID: " + id.val());
                id.val("");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                notyError(textStatus + ": " + errorThrown);
            }
        });
    } else {
        notyWarning("You have to enter an ID to delete.")
    }
}

function edit() {
    var id = $("#edit_id");
    var name = $("#edit_name");
    var text = $("#edit_text");
    if (id.val() != "" && name.val() != "" && text.val() != "") {
        $.ajax({
            url: '/edit/' + id.val() + '/' + name.val() + '/' + text.val(),
            type: 'PUT',
            success: function (data) {
                notySuccess("Edited " + $("#edit_id").val());
                id.val("");
                name.val("");
                text.val("");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                notyError(textStatus + ": " + errorThrown);
            }
        });
    } else {
        notyWarning("You have to edit all fields")
    }
}

function find() {
    $.ajax({
        url: '/search/' + $("#search_tak").val(),
        type: 'GET',
        success: function (data) {
            $("#search_tak").val("");
            //console.log(data);
            $("#search_body").html("");
            var asd = JSON.parse(data);
            for (var i = 0; i<asd.length; i++)
            {
                appendRow(asd[i]['id'], asd[i]['name'], asd[i]['text']);
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            notyError(textStatus + ": " + errorThrown);
        }
    });
}

function appendRow(id, name, text) {
    var body = document.getElementById("search_body");
    var row = body.insertRow();
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell3.vAlign="center";

    $('<div/>', {
        'id': 'id',
        'text': id
    }).appendTo(cell1);

    $('<div/>', {
        'id': 'name',
        'text': name
    }).appendTo(cell2);

    $('<div/>', {
        'id': 'text',
        'text': text
    }).appendTo(cell3);

    /*var edit_button = $('<button/>', {
        'type': 'submit',
        'class': "btn btn-link",
        'style': "margin-left:10px;",
        'onclick': 'edit();'
    }).appendTo(cell4);

    $('<span/>', {
        'class': "glyphicon glyphicon-wrench",
        'style': "color:red"

    }).appendTo(edit_button);

    var trash = $('<button/>', {
        'type': 'submit',
        'class': "btn btn-link",
        'style': "margin-left:10px;",
        'onclick': 'del();'
    }).appendTo(cell4);

    $('<span/>', {
        'class': "glyphicon glyphicon-trash",
        'style': "color:red"

    }).appendTo(trash);*/
}