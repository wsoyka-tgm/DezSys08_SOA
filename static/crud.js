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
        url: '/delete/' +$("#delete_id").val(),
        type: 'GET',
        success: function (data) {
            notySuccess("Deleted "+ $("#delete_id").val());
            $("#delete_id").val("");
        },
        error: function (jqXHR, textStatus, errorThrown) {
            notyError(textStatus + ": "+ errorThrown);
        }
    });
}

function edit(){
    $.ajax({
        url: '/edit/' +$("#edit_id").val()+'/'+$("#edit_name").val()+'/'+$("#edit_text").val(),
        type: 'GET',
        success: function (data) {
            notySuccess("Edited "+ $("#edit_id").val());
            $("#edit_id").val("");
            $("#edit_name").val("");
            $("#edit_text").val("");
        },
        error: function (jqXHR, textStatus, errorThrown) {
            notyError(textStatus + ": "+ errorThrown);
        }
    });
}