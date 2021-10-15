
$(function(){

    function actualizar_paginacion(usuarios_actuales, total_usuarios ,pagina, cantidad_mostrar) {
        if(usuarios_actuales == 0){
            $("#dataTable_info").text("Mostrando 0 usuarios de " + total_usuarios)
        }else{
            if(parseInt(pagina)==1){

                if(usuarios_actuales < parseInt(cantidad_mostrar)){
                    $("#dataTable_info").text("Mostrando 1 a " + usuarios_actuales +" de "+ total_usuarios)
                }else{
                    $("#dataTable_info").text("Mostrando 1 a " + usuarios_actuales +" de "+ total_usuarios)
                }
                
            }else{
                var resultado = (total_usuarios)/(parseInt(cantidad_mostrar))
                console.log("resultado es:"+resultado)
                if(parseInt(pagina)<=resultado){
                    var valor =((parseInt(pagina)-1)*parseInt(cantidad_mostrar))+1
                    $("#dataTable_info").text("Mostrando " + valor + " a "  + (valor + (usuarios_actuales-1)) +" de "+ total_usuarios)
                }else{
                    resultado = resultado%1
                    valor =  resultado * (parseInt(cantidad_mostrar))
                    $("#dataTable_info").text("Mostrando " + (total_usuarios-valor) + " a "  + total_usuarios +" de "+ total_usuarios)
                }
            }
        }
    }

    function cambio_tabla(){         
        var cant = $('.form-select').val();
        var form = $(".filter-form");
        $(".pagination > .numero_pagina").each(function(){
                if($(this).hasClass("active")){
                    pag = $("a",this).html();
                }
        });
        $.ajax({
            type: "GET",
            url: "/system/table",
            data: form.serialize() + "&cantidad=" + cant + "&pagina=" + pag +"&ajax=1"
        }).done(function(data){
            $(".filtro_form").empty().append($(data['tabla']).hide().fadeIn(700));
            actualizar_paginacion(data['usuarios_actuales'], data['total_usuarios'], pag, cant)
            

        });
        
        
    }
    
    $(".form-select").change(function(event){
        event.preventDefault();
        cambio_tabla();

    })

    $(".filter-form").submit(function(event){
        event.preventDefault();
        cambio_tabla();
    })

    $(".pagination > .numero_pagina").on('click','a', function(event){
        
        $(".pagination > .numero_pagina").each(function(){
            if($(this).hasClass("active")){
                $(this).removeClass("active");
            }
            
        });
        
        $(this).closest(".numero_pagina").addClass("active");
        cambio_tabla();
        
    })
        
    
});

