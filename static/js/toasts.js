$(document).ready(function(){

    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function (toastEl) {
      toast = new bootstrap.Toast(toastEl)
      console.log(toast)
    })

    $('.toast-container').find($('.btn-close')).click(function(){
        console.log('hi')
        $('.toast-container').children().hide()
    })
})