var fixture_id = $('#id_fixture_id').text();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function delete_all_team_goals(data){
    let csrftoken = getCookie('csrftoken')
    response = await fetch(`/teams/delete_team_goals/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
           "X-CSRFToken": csrftoken 
        },
        body: JSON.stringify(data),
        credentials: 'same-origin',
    })
}

$(document).ready(function(){
    var optionVal 

    $('#id_team').append(`
        <option></option>
        <option></option>
    `)

    $('#add-goal-btn').click(function(ev){
        homeTeamVal= $('#id_home_team option:selected').val()
        homeTeamText= $('#id_home_team option:selected').text()
        awayTeamVal= $('#id_away_team option:selected').val()
        awayTeamText= $('#id_away_team option:selected').text()

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
            location.reload();


        }

    })



});
