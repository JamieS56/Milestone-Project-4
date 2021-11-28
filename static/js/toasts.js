$(document).ready(function(){

    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
      toast = new bootstrap.Toast(toastEl);
    });

    $('.toast-container').find($('.btn-close')).click(function(){
        $('.toast-container').children().hide();
    });
});