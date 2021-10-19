$(".form-select").change(function(event){
    var id = $('.form-select').val();
    var form = $(".form-select");

    $.ajax({
        type: "GET",
        url: form.attr("action"),
        data:  "&id=" + id +"&ajax=1",
        dataType: "json",

    }).done(function(data){
        $("#puntaje").val(data['puntaje'])
        $("#retroalimentacion").val(data['comentario'])
        
        $('.stars i').each(function(index){
            if (index<= data['puntaje']-1){
                $(this).addClass("active");
            };
            if (index > data['puntaje']-1){
                $(this).removeClass("active");
            };
        });
    });

})




