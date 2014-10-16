$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['lens', 'size', 'battery', 'camera', 'picture'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[1, 3, 3, 5, 13]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(232,78,64,0.5)",
strokeColor: "rgba(232,78,64,0.8)",
highlightFill: "rgba(232,78,64,0.75)",
highlightStroke: "rgba(232,78,64,1)",
data:
[1, 0, 2, 0, 1]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var value_div = document.getElementById("perChartValue");
value_div.innerHTML = "72.41379310344827%";
var data = [
{
value: 27.58620689655173,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 72.41379310344827,
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
value_div.innerHTML = "93.10344827586206%";
var data = [
{
value: 6.896551724137936,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 93.10344827586206,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{animationSteps: 200,animationEasing : "easeOutQuart"});
});
$(function(){
var table = document.getElementById("precision_table");
table.innerHTML = "<tr><td>picture</td><td>78.57142857142857</td><td>100.0</td></tr><tr><td>battery</td><td>100.0</td><td>100.0</td></tr><tr><td>camera</td><td>20.0</td><td>100.0</td></tr><tr><td>size</td><td>100.0</td><td>50.0</td></tr><tr><td>lens</td><td>50.0</td><td>50.0</td></tr>"
});
$(function(){
var ctx = document.getElementById("negChart").getContext("2d");
var data = {labels:
['picture', 'battery', 'camera', 'size', 'lens'],
datasets: [
{
label: "Sentiment Analysed",
fillColor: "rgba(86,119,252,0.5)",
strokeColor: "rgba(86,119,252,0.8)",
highlightFill: "rgba(86,119,252,0.75)",
highlightStroke: "rgba(86,119,252,1)",
data:
[78.57142857142857, 100.0, 20.0, 100.0, 50.0]}
,
{
label: "Sentiment Analysed",
fillColor: "rgba(255,152,0,0.5)",
strokeColor: "rgba(255,152,0,0.8)",
highlightFill: "rgba(255,152,0,0.75)",
highlightStroke: "rgba(255,152,0,1)",
data:
[100.0, 100.0, 100.0, 50.0, 50.0]}
]};
var myLineChart = new Chart(ctx).Bar(data,{animationSteps: 200});
});
