$('#sub_1').click((e) => {
    e.preventDefault();
    
    // get data from the form
    let data = $('#contract_input').val();
    
    // post the data
    $.ajax({
        url: '/post_contract',
        data: {'data': data},
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
})