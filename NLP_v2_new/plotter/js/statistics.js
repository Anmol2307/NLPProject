$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['price', 'picture', 'battery', 'storage', 'general', 'software', 'size', 'design', 'video', 'service', 'lens', 'focus', 'exposure', 'shutter'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[5, 4, 0, 0, 0, 0, 1, 2, 1, 1, 1, 0, 0, 2]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[0, 2, 2, 1, 1, 1, 7, 7, 1, 4, 4, 5, 0, 14]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var value_div = document.getElementById("perChartValue");
value_div.innerHTML = "56.6666666667%";
var data = [
{
value: 43.3333333333,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 56.6666666667,
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
value_div.innerHTML = "86.6666666667%";
var data = [
{
value: 13.3333333333,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 86.6666666667,
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
['price', 'picture', 'battery', 'storage', 'general', 'software', 'size', 'design', 'video', 'service', 'lens', 'focus', 'shutter'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(86,119,252,0.5)",
strokeColor: "rgba(86,119,252,0.8)",
highlightFill: "rgba(86,119,252,0.75)",
highlightStroke: "rgba(86,119,252,1)",
data:
[20.0, 100.0, 100.0, 0.0, 0.0, 0.0, 62.5, 0.0, 50.0, 0.0, 40.0, 0.0, 0.0]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(255,152,0,0.5)",
strokeColor: "rgba(255,152,0,0.8)",
highlightFill: "rgba(255,152,0,0.75)",
highlightStroke: "rgba(255,152,0,1)",
data:
[50.0, 50.0, 40.0, -1, 0.0, -1, 83.33333333333333, -1, 50.0, -1, 100.0, -1, -1]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
