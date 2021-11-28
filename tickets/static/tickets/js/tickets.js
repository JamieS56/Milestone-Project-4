$('document').ready(function(){

    // updates the total price on the tickets page.

    $('#id_number_of_tickets').change(function(){
        $('#total-price').text($('#id_number_of_tickets').val() * 15);

    });
    $('#payment-form').submit(function(){
        $('#loading-overlay').show();
    });

});