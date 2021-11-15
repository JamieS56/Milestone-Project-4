var addGoalBtn = document.getElementById('add-goal-btn')
var goalCounter = document.getElementById('goal-counter')
var goal_table_row = `<tr class="">
                          <th scope="row"></th>
                          <td class="">${$('#id_goal_scorer option:selected').text()}</td>
                          <td class="">${$('#id_assist_maker option:selected').text()}</td>
                          <td class=""><button type="button" class="btn-close btn-close-white close" aria-label="Close"></button></td>
                          <td class="visually-hidden"><input id='' value='${$('#id_goal_id').val()}' class="visually-hidden goal-id"></input></td>
                      <tr>`


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

async function handle_goals(goal_data){
    let csrftoken = getCookie('csrftoken')
    response = await fetch(`/teams/handle_goal/`, {
        method: 'POST', // or 'PUT'
        headers: {
          'Content-Type': 'application/json',
           "X-CSRFToken": csrftoken 
        },
        body: JSON.stringify(goal_data),
        credentials: 'same-origin',
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);

        $('#goal-counter-pills').find('input').each(function(){
            if (data['goal_id']){
                console.log($(this))
                if($(this).val() == '0'){  
                    $(this).val(data['goal_id'])
                }
            }
        
        })

    })
    .catch((error) => {
        console.error('Error:', error);
 
    })
}


function increaseGoalCount(){
    
    if($('#goal-team-select option:selected').val() == $('#goal-home-team-option').val()){
        $('#home-goal-table').append(goal_table_row);
        $('#home-goal-table').children().addClass('table-dark')
    } else{
        $('#away-goal-table').append(goal_table_row);
    };

    

    goal_data = {
        'goal_id': $('#id_goal_id').val(),
        'team': $('#goal-team-select option:selected').val(),
        'goal_scorer': $('#id_goal_scorer option:selected').val(),
        'assist_maker': $('#id_assist_maker option:selected').val(),
        'fixture': $('#fixture-input').val(),
        'add_or_remove': 'add',
        'submit': 'False'
    }

    handle_goals(goal_data)
    
}

function decreaseGoalCount(){

    goal_data = {
        'goal_id': $(this).siblings('input').val(),
        'goal_scorer': '',
        'assist_maker': '',
        'add_or_remove': 'remove',
        'submit': 'False'
    }
    
    $('#goal-counter').val(parseInt($('#goal-counter').val()) - 1);
    $(this).parent().remove();

    handle_goals(goal_data)
}

function removeRow(){
    $('#goal-counter-pills span:last-child').remove();
}

function submitGoals(){
    goal_data = {
        'goal_id': '',
        'goal_scorer': '',
        'assist_maker': '',
        'fixture': $('#fixture-input').val(),
        'add_or_remove': '',
        'submit': 'True'
    };
    console.log(goal_data)
    handle_goals(goal_data)

}





$(document).ready(function(){

    $('#id_home_team').change(function(){
        $('#goal-home-team-option').text($(this).find('option:selected').text())
        $('#goal-home-team-option').val($(this).find('option:selected').val())
    })

    $('#id_away_team').change(function(){
        $('#goal-away-team-option').text( $(this).find('option:selected').text())
        $('#goal-away-team-option').val( $(this).find('option:selected').val())
    })
    
    // $('#add-goal-btn').click(function(){
    //     $('').append(goal_table_row);
    // });
    $('#add-goal-submit-btn').click(increaseGoalCount);

    $('#goal-counter-pills').on('click', '.close', decreaseGoalCount);

    $('.close-add-goal').click(removePill)

    $('#edit-fixture').click(submitGoals)

    $('#goal-home-team-option').val($('#id_home_team option:selected').val())
    $('#goal-away-team-option').val($('#id_away_team option:selected').val())

});
