$('document').ready(function(){

    $('#id_number_of_tickets').change(function(){
        $('#total-price').text($('#id_number_of_tickets').val() * 15)

    })

})