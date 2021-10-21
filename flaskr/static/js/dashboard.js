const MiGrafica1= document.getElementById("grafica1").getContext("2d")
console.log(MiGrafica1)                   
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

const MiGrafica2 =document.getElementById("grafica2");
console.log(MiGrafica2) 
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