var MiGrafica1= document.getElementById("grafica1").getContext("2d")
var chart = new Chart(MiGrafica1,{
    type:"bar",
    data:{
        labels:["Vino","Tequila","Cerveza","Ron","Aguardiente"],
        datasets:[
            {
                label:"Mi Grafica de Bebidas",
                background:"rgb(0,0,0)",
                borderColor:"rgb(255,255,0)",
                data:[12,39,5,30,55]
            }
        ]
    }

})

var MiGrafica2 =document.getElementById("grafica2");
var myPieChart = new Chart(MiGrafica2, {
    type: "pie",
    data: {
        labels: ['año', 'mes', 'dia'],
        datasets: [{
            label:"Resultados",
            data: [450,200,100],
            backgroundColor: ["#204862", "#757439", "#1c835b"]
        }]
    },
});

var MiGrafica3= document.getElementById("grafica3").getContext("2d")                    
var chart = new Chart(MiGrafica3,{
    type:"line",
    data:{
        labels:["Vino","Tequila","Cerveza","Ron"],
        datasets:[
            {
                label:"Mi Grafica de Bebidas",
                background:"rgb(0,0,0)",
                borderColor:"rgb(255,255,0)",
                data:[12,39,5,30]
            }
        ]
    }

})


var MiGrafica4= document.getElementById("grafica4").getContext("2d")
var chart = new Chart(MiGrafica4,{
    type:"bar",
    data:{
        labels:["Vino","Tequila","Cerveza","Ron","Aguardiente"],
        datasets:[
            {
                label:"Mi Grafica de Bebidas",
                background:"rgb(0,0,0)",
                borderColor:"rgb(255,255,0)",
                data:[12,39,5,30,55]
            }
        ]
    }

})