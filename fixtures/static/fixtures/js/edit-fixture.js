var fixtureId = $('#id_fixture_id').text();

// Gets the csrftoken so that a POST request can be sent to Django. Code taken from https://stackoverflow.com/questions/43606056/proper-django-csrf-validation-using-fetch-post-request.
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

// Calls python function to delete all team goals if team is changed
async function deleteAllTeamGoals(data){
    let csrftoken = getCookie('csrftoken');
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
    });
}

$(document).ready(function(){
    var optionVal;

    // Adds the options to the bottom of the teams crispy form input 
    $('#id_team').append(`
        <option></option>
        <option></option>
    `);

    // Triggers when the teams input is updated because i couldn't get what teams were seleced from inside forms.py
    $('#add-goal-btn').click(function(){

        // Gets what teams are selected up at the top of the page
        homeTeamVal= $('#id_home_team option:selected').val();
        homeTeamText= $('#id_home_team option:selected').text();
        awayTeamVal= $('#id_away_team option:selected').val();
        awayTeamText= $('#id_away_team option:selected').text();

        // Inputs it into goal form
        $('#id_team option:first').val(homeTeamVal);
        $('#id_team option:first').text(homeTeamText);

        $('#id_team option:last').val(awayTeamVal);
        $('#id_team option:last').text(awayTeamText);


    });


    // Finds oout what team is gunna get changed
    $('.team-select').focus(function(){
        optionVal = $(this).val();
    });

    // Confirms that the team does want to be changed and goals deleted
    $('.team-select').change(function(){
        confirmation = confirm('Are you sure you want to change teams, if you change teams it deletes all goalsin this fixture for this team.');
        if(confirmation == false){
            $(this).val(optionVal);
        }else{
            data = {
                'old_team': optionVal,
                'new_team': $(this).val(),
                'fixture': fixtureId
            };
            deleteAllTeamGoals(data);
        }
    });

});
