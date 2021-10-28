
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
                    $("#dataTable_info").text("Mostrando " + ((total_usuarios+1)-valor) + " a "  + total_usuarios +" de "+ total_usuarios)
                }
            }
        }
    }

    function cambio_numeracion(pag, total_usuarios,cantidad_mostrar){
        var resultado = Math.ceil((total_usuarios)/(parseInt(cantidad_mostrar)))


        $(".pagination > li").each(function(){
            $(this).removeClass("disabled")
            if($(this).text()==resultado){ 
                $(this).nextUntil(".cambio_pagina").addClass("disabled")
                if($(this).text()==parseInt(pag)){
                    $(this).nextAll("li").addClass("disabled")
                    return false;
                }
                $("#Next").removeClass("disabled")
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

            if( parseInt(pag) != 1 && data['usuarios_actuales']==0){
                const value = parseInt(pag)/3;
                cambioPagina = 1;
                $(".pagination > .numero_pagina").each(function(){
                    if($(this).text()==pag){
                        $(this).removeClass("active");  
                    }
                    if(value>1){
                        $("a",this).text(cambioPagina);
                        cambioPagina++;
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
        event.preventDefault();
        
        $(".pagination > .numero_pagina").each(function(){
            if($(this).hasClass("active")){
                $(this).removeClass("active");
            }
        });
        $(this).closest(".numero_pagina").addClass("active");
        cambio_tabla();
    })

    $(".pagination > .cambio_pagina").on('click','a', function(event){ 
        event.preventDefault();
        
        if($(this).closest("li").attr("id") == "Previous"){
            
            $(".pagination > .numero_pagina").each(function(){
                
                if($(this).hasClass("active")){
                    var numeroPagina=parseInt($(this).text())
                    var value = numeroPagina/3
                    value = (value%1).toFixed(1)
                    if(value==0.3){ 
                        var cont=1;
                        $(".pagination > .numero_pagina").each(function(){
                            cambioPagina = parseInt($(this).text())-3
                            $("a",this).text(cambioPagina)
                            if(cont==3){
                                $(this).addClass("active")
                            }
                            cont++;
                        })
                    }
                    $(this).removeClass("active");
                    $(this).prev(".numero_pagina").addClass("active");
                    return false;  
                }
            });
        
        }
        else if($(this).closest("li").attr("id") == "Next"){
            $(".pagination > .numero_pagina").each(function(){
                if($(this).hasClass("active")){
                    var numeroPagina=parseInt($(this).text())
                    var value = numeroPagina/3
                    value = value%1
                    if(value==0){ 
                        var cont=1;
                        $(".pagination > .numero_pagina").each(function(){
                            cambioPagina = parseInt($(this).text())+3
                            $("a",this).text(cambioPagina)
                            if(cont==1){
                                $(this).addClass("active")
                            }
                            cont++;
                        })
                    }
                    $(this).removeClass("active");
                    $(this).next(".numero_pagina").addClass("active");
                    return false;    
                }
            });
        }

        cambio_tabla();
    })            
    
});