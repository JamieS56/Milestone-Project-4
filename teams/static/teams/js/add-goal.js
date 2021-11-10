var addGoalBtn = document.getElementById('add-goal-btn')
var goalCounter = document.getElementById('goal-counter')
var playerPill = '<span class="badge bg-dark">Goal<button type="button" class="btn-close btn-close-white close" aria-label="Close"></button></span>'

function increaseGoalCount(){
    $('#goal-counter').val(parseInt($('#goal-counter').val()) + 1);
    console.log($('#goal-counter').val());
    $('#goal-counter-pills').append(playerPill);
}

function decreaseGoalCount(){
    
    $('#goal-counter').val(parseInt($('#goal-counter').val()) - 1);
    console.log($('#goal-counter').val());
    $(this).parent().remove();
}

$(document).ready(function(){

    $('#add-goal-btn').click(increaseGoalCount);

    $('#goal-counter-pills').on('click', '.close', decreaseGoalCount);

});