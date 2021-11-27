var fixture_id = $('#id_fixture_id').text();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// calls python function to delete all team goals if team is changed
async function delete_all_team_goals(data){
    let csrftoken = getCookie('csrftoken')
    response = await fetch(`/fixtures/delete_team_goals/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
           "X-CSRFToken": csrftoken 
        },
        body: JSON.stringify(data),
        credentials: 'same-origin',
    }).then((data) =>{
        location.reload();
    })
}

function display_goal_involvement(){
    if($('#id_team').val() == 1){
        $('#div_id_goal_scorer').show()
        $('#div_id_assist_maker').show()
    }else{
        $('#div_id_goal_scorer').hide()
        $('#div_id_assist_maker').hide()
    }
}

$(document).ready(function(){
    var optionVal 
    var goalPopover = new bootstrap.Popover($('#id_goal_scorer'), {
        container: 'body',
        title:'Error',
        content: 'Please input a player.',
        placement: 'bottom'
    })
    var assistPopover = new bootstrap.Popover($('#id_assist_maker'), {
        container: 'body',
        title:'Error',
        content: 'Please input a player.',
        placement: 'bottom'
    })

    $('#id_team').append(`
        <option></option>
        <option></option>
    `)

    $('#add-goal-btn').click(function(){

        // Gets what teams are selected up at the top of the page
        homeTeamVal= $('#id_home_team option:selected').val()
        homeTeamText= $('#id_home_team option:selected').text()
        awayTeamVal= $('#id_away_team option:selected').val()
        awayTeamText= $('#id_away_team option:selected').text()

        // Inputs it into goal form
        $('#id_team option:first').val(homeTeamVal)
        $('#id_team option:first').text(homeTeamText)

        $('#id_team option:last').val(awayTeamVal)
        $('#id_team option:last').text(awayTeamText)


    })

    $('.team-select').focus(function(){
        optionVal = $(this).val()

    })

    $('.team-select').change(function(){
        confirmation = confirm('Are you sure you want to change teams, if you change teams it deletes all goalsin this fixture for this team.')
        if(confirmation == false){
            $(this).val(optionVal)
        }else{
            data = {
                'old_team': optionVal,
                'new_team': $(this).val(),
                'fixture': fixture_id
            }
            delete_all_team_goals(data)
            console.log(data)
        }
    })

});
