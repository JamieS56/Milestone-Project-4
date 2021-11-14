var addGoalBtn = document.getElementById('add-goal-btn')
var goalCounter = document.getElementById('goal-counter')
var playerPill = `<span class="badge bg-dark">Goal\
                        <input id='' value='0' class="visually-hidden goal-id"></input>
                        <button type="button" class="btn-close btn-close-white close" aria-label="Close"></button>
                    </span>`


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
        console.log(data['goal_id'])

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
    
    $('#goal-counter').val(parseInt($('#goal-counter').val()) + 1);

    goal_data = {
        'goal_id': $('#id_goal_id').val(),
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
    console.log($('#goal-counter').val());
    $(this).parent().remove();

    handle_goals(goal_data)
}

function removePill(){
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

    

    $('#add-goal-btn').click(function(){
        $('#goal-counter-pills').append(playerPill);
    });
    $('#add-goal-submit-btn').click(increaseGoalCount);

    $('#goal-counter-pills').on('click', '.close', decreaseGoalCount);

    $('.close-add-goal').click(removePill)

    $('#edit-fixture').click(submitGoals)

    


});
