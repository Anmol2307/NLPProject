$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['size', 'camera', 'picture', 'price', 'battery', 'lens', 'vedio'],
datasets: [{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[6.521820839978735, 6.216318591318592, 9.75932966682608, 4.230769230769231, 7.243830501221805, 3.248333333333333, 2.25]}]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var data = [
{
value: 20.689655172413794,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}
,
{
value: 79.3103448275862,
color: "#2baf2b",
highlight: "#42bd41",
label: "Done"
}
];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
