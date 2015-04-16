/**
 * Created by Wolfram on 16/04/15.
 */
function add(){
    $.ajax({
        url: '/add/' +$("#add_name").val() +'/'+ $("#add_text").val(),
        type: 'GET',
        success: function (data) {
            notySuccess("Added "+ $("#add_name").val());
            $("#add_text").val("");
            $("#add_name").val("");
        },
        error: function (jqXHR, textStatus, errorThrown) {
            notyError(textStatus + ": "+ errorThrown);
        }
    });
}

function del(){
    $.ajax({
        url: '/delete/' +$("#delete_name").val(),
        type: 'GET',
        success: function (data) {
            notySuccess("Deleted "+ $("#delete_name").val());
            $("#delete_name").val("");
        },
        error: function (jqXHR, textStatus, errorThrown) {
            notyError(textStatus + ": "+ errorThrown);
        }
    });
}