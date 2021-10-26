var MiGrafica1= document.getElementById("grafica1").getContext("2d")
var chart = new Chart(MiGrafica1,{
    type:"bar",
    data:{
        labels:["Indefinido","Fijo","Prestación de servicios","Hora labor"],
        datasets:[
            {
                label:"Cantidad de contratos",
                data: [datosGrafica1.Indefinido, datosGrafica1.Fijo , datosGrafica1.Prestacion , datosGrafica1.HoraLab ,0 ],
                // data: [25,10,25,6,0],
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

var MiGrafica2 =document.getElementById("grafica2");
var myPieChart = new Chart(MiGrafica2, {
    type: "pie",
    data: {
        labels: ["Administrativo","Gerencia","Ingeniería","Producción","Sistemas"],
        datasets: [{
            label:"Resultados",
            data: [datosGrafica2.Administrativo, datosGrafica2.Gerencia, datosGrafica2.Ingenieria, datosGrafica2.Produccion,datosGrafica2.Sistemas, 0],
            backgroundColor: ["#4e73df", "#1cc88a", "#36b9cc","#f6c23e", "#e74a3b" ]
        }]
    },
})

var MiGrafica3= document.getElementById("grafica3").getContext("2d")                    
var chart = new Chart(MiGrafica3,{
    type:"line",
    data:{
        labels:["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
        datasets:[
            {
                label:"Adminsitrativo",
                borderColor:"#4e73df",
                backgroundColor: "rgb(220,243,104,0)",
                data:[5,3,2,4,]
            },
            {
                label:"Gerencia",
                borderColor:"#1cc88a",
                backgroundColor: "rgb(150,243,104,0)",
                data:[2,4,3,1]
            },
            {
                label:"Ingeniería",
                borderColor:"#36b9cc",
                backgroundColor: "rgb(150,243,104,0)",
                data:[3,5,2,0]
            },
            {
                label:"Producción",
                borderColor:"#f6c23e",
                backgroundColor: "rgb(150,243,104,0)",
                data:[4,3,5,2]
            },
            {
                label:"Sistemas",
                borderColor:"#e74a3b",
                backgroundColor: "rgb(150,243,104,0)",
                data:[3,1,0,4,0]
            }

        ]

      
                
        
    }

})

var MiGrafica4= document.getElementById("grafica4").getContext("2d")
var chart = new Chart(MiGrafica4,{
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
