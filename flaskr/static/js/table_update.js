
$(function(){

    function actualizar_paginacion(usuarios_actuales, total_usuarios ,pagina, cantidad_mostrar) {
        if(usuarios_actuales == 0){
            $("#dataTable_info").text("Mostrando 0 usuarios de " + total_usuarios)
        }else{
            if(parseInt(pagina)==1){
                $("#dataTable_info").text("Mostrando 1 a " + usuarios_actuales +" de "+ total_usuarios)    
            }else{
                var resultado = (total_usuarios)/(parseInt(cantidad_mostrar))
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

    function cambio_numeracion(pag, total_usuarios,cantidad_mostrar){
        var resultado = Math.ceil((total_usuarios)/(parseInt(cantidad_mostrar)))
        $(".pagination > li").each(function(){
            $(this).removeClass("disabled")
            if($(this).text()==resultado){ 
                $(this).nextAll("li").addClass("disabled")
                return false;
            }
        })

        if( pag == 1){
            $("#Previous").addClass('disabled');
        }

 
    }

    function cambio_tabla(pag=0){         
        var cant = $('.form-select').val();
        var form = $(".filter-form");
        if(pag == 0){
            $(".pagination > .numero_pagina").each(function(){
                if($(this).hasClass("active")){
                    pag = $("a",this).html();
                }
            });
        }
        if(pag==1){
            $(".pagination > .numero_pagina").each(function(){
                if($(this).text()==1){
                    $(this).addClass("active");
                }
            });
        }

        $.ajax({
            type: "GET",
            url: "/system/table",
            data: form.serialize() + "&cantidad=" + cant + "&pagina=" + pag +"&ajax=1"
        }).done(function(data){
            console.log(data["usuarios_actuales"]);
            console.log(parseInt(pag))

            if( parseInt(pag) != 1 && data['usuarios_actuales']==0){
                $(".pagination > .numero_pagina").each(function(){
                    if($(this).text()==pag){
                        $(this).removeClass("active");
                    }
                });
                cambio_tabla(pag=1);

            }
            $(".filtro_form").empty().append($(data['tabla']).hide().fadeIn(700));
            actualizar_paginacion(data['usuarios_actuales'], data['total_usuarios'], pag, cant)
            cambio_numeracion(pag, data['total_usuarios'], cant)
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

