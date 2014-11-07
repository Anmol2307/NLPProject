$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['video', 'general', 'price', 'battery', 'size', 'picture', 'lens'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[1, 1, 2, 5, 5, 10, 2]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[1, 0, 0, 2, 0, 1, 0]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var value_div = document.getElementById("perChartValue");
value_div.innerHTML = "93.33333333333333%";
var data = [
{
value: 6.666666666666671,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 93.33333333333333,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{animationSteps: 200,animationEasing : "easeOutQuart"});
});
$(function(){
var ctx = document.getElementById("sentiPerChart").getContext("2d");
var value_div = document.getElementById("sentiPerChartValue");
value_div.innerHTML = "93.33333333333333%";
var data = [
{
value: 6.666666666666671,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 93.33333333333333,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{animationSteps: 200,animationEasing : "easeOutQuart"});
});
$(function(){
var ctx = document.getElementById("negChart").getContext("2d");
var data = {labels:
['price', 'picture', 'battery', 'general', 'size', 'video', 'lens'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(86,119,252,0.5)",
strokeColor: "rgba(86,119,252,0.8)",
highlightFill: "rgba(86,119,252,0.75)",
highlightStroke: "rgba(86,119,252,1)",
data:
[100.0, 100.0, 71.42857142857143, 100.0, 100.0, 100.0, 100.0]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(255,152,0,0.5)",
strokeColor: "rgba(255,152,0,0.8)",
highlightFill: "rgba(255,152,0,0.75)",
highlightStroke: "rgba(255,152,0,1)",
data:
[100.0, 91.66666666666667, 100.0, 100.0, 83.33333333333333, 100.0, 100.0]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
