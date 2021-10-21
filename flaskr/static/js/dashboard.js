var MiGrafica1= document.getElementById("grafica1").getContext("2d")
var chart = new Chart(MiGrafica1,{
    type:"bar",
    data:{
        labels:["Administrativo","Gerencia","Ingeniería","Producción","Sistemas"],
        datasets: [{
            label: 'Calificaciones',
            data: [5, 3, 2, 4, 3, 0],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }

})



var MiGrafica2 =document.getElementById("grafica2");
var myPieChart = new Chart(MiGrafica2, {
    type: "pie",
    data: {
        labels: ["Administrativo","Gerencia","Ingeniería","Producción","Sistemas"],
        datasets: [{
            label:"Resultados",
            data: [90,10,40,85,20],
            backgroundColor: ["#1B5B88", "#21AB19", "#B24519","#CBDF06", "#" ]
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
                data:[12,39,5,30,0]
            }
        ]
    }

})


var MiGrafica4= document.getElementById("grafica4").getContext("2d")
var chart = new Chart(MiGrafica4,{
    type:"bar",
    data:{
        labels:["Indefinido","Fijo","Prestación de servicios","Hora labor"],
        datasets:[
            {
                label:"Cantidad de contratos",
                data: [100, 50, 40, 4, 0],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            // Elements options apply to all of the options unless overridden in a dataset
            // In this case, we are setting the border of each horizontal bar to be 2px wide
            elements: {
              bar: {
                borderWidth: 2,
              }
            },
            responsive: true,
            plugins: {
              legend: {
                position: 'right',
              },
              title: {
                display: true,
                text: 'Chart.js Horizontal Bar Chart'
              }
            }
          },

})