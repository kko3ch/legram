// var modalBtn = document.querySelector('.modal_btn')
// var modal = document.querySelector('.modal-bg')

// modalBtn.addEventListener('click',function(){
//     modal.classList.add('.modal-active')
// })
$(document).ready(function(){
    $('.modal_btn').click(function(){
        $('.modal-bg').modal('show'); 
        $(".modal-bg").addClass(".modal-active");
    })
});


