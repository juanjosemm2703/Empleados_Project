/* setInterval(function(){ */ 
var MiGrafica1= document.getElementById("grafica1").getContext("2d")
var chart = new Chart(MiGrafica1,{
    type:"bar",
    data:{
        labels:["Indefinido","Fijo","Prestación de servicios","Hora labor"],
        datasets:[
            {
                label:"Cantidad de contratos",
                data: [datosGrafica1.Indefinido, datosGrafica1.Fijo , datosGrafica1.Prestacion , datosGrafica1.HoraLab ,0 ],
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
            legend:{
                display:false,
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
            backgroundColor: ["#4e73df", "#1cc88a", "#36b9cc","#f6c23e", "#e74a3b" ],
        }]
    },
})

var MiGrafica3= document.getElementById("grafica3").getContext("2d")
var chart = new Chart(MiGrafica3,{
    type: 'polarArea',
    data: data = {
    labels: ['Administrativo', 'Gerencia', 'Ingenieria', 'Producción', 'Sistemas'],
    datasets: [
    {
        label: 'Dataset 1',
        backgroundColor: ['#03C71D', '#BBDC14', '#3EB794', '#A63EB7', '#E669A0'],
        bordercolor: '#051414',
        borderWidth: 1,
        data: [datosGrafica3.Administrativo, datosGrafica3.Gerencia, datosGrafica3.Ingenieria, datosGrafica3.Produccion, datosGrafica3.Sistemas],
    }]
}

})
/* },10000); */
