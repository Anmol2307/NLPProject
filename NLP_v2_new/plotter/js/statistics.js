$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['price', 'picture', 'battery', 'storage', 'upgrade', 'hardware', 'feature', 'size', 'design', 'media', 'sound', 'service', 'help-care', 'overall', 'lens', 'focus', 'exposure', 'shutter'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[1, 4, 0, 0, 0, 0, 0, 1, 2, 1, 5, 0, 0, 0, 1, 0, 0, 0]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[0, 3, 2, 0, 2, 1, 1, 5, 6, 3, 11, 3, 0, 0, 2, 5, 3, 5]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var value_div = document.getElementById("perChartValue");
value_div.innerHTML = "58.6206896552%";
var data = [
{
value: 41.3793103448,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 58.6206896552,
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
value_div.innerHTML = "86.2068965517%";
var data = [
{
value: 13.7931034483,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 86.2068965517,
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
['price', 'picture', 'battery', 'upgrade', 'hardware', 'feature', 'size', 'design', 'media', 'sound', 'service', 'lens', 'focus', 'exposure', 'shutter'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(86,119,252,0.5)",
strokeColor: "rgba(86,119,252,0.8)",
highlightFill: "rgba(86,119,252,0.75)",
highlightStroke: "rgba(86,119,252,1)",
data:
[100.0, 85.71428571428571, 100.0, 0.0, 100.0, 0.0, 66.66666666666667, 0.0, 0.0, 6.25, 0.0, 33.333333333333336, 20.0, 0.0, 0.0]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(255,152,0,0.5)",
strokeColor: "rgba(255,152,0,0.8)",
highlightFill: "rgba(255,152,0,0.75)",
highlightStroke: "rgba(255,152,0,1)",
data:
[50.0, 75.0, 40.0, -1, 33.333333333333336, -1, 66.66666666666667, -1, -1, 100.0, -1, 33.333333333333336, -1, -1, -1]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
