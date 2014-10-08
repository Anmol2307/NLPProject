$(function(){
var ctx = document.getElementById("posChart").getContext("2d");
var data = {labels:
['picture', 'size', 'sound', 'lens', 'feature', 'upgrade', 'battery'],
datasets: [{
label: "Sentiment Analysed",
fillColor: "rgba(37,155,36,0.5)",
strokeColor: "rgba(37,155,36,0.8)",
highlightFill: "rgba(37,155,36,0.75)",
highlightStroke: "rgba(37,155,36,1)",
data:
[246.0937117845599, 99.91190476190475, -5.333333333333333, 7.083333333333334, 10.961538461538462, -4.0, -9.833333333333334]}]};
var myLineChart = new Chart(ctx).Bar(data,{});
});
$(function(){
var ctx = document.getElementById("perChart").getContext("2d");
var data = [
{
value: 40.90909090909091,
color: "#46BFBD",
highlight: "#5AD3D1",
label: "Done"
},
{
value: 59.09090909090909,
color:"#F7464A",
highlight: "#FF5A5E",
label: "Not Done"
}];
var myDoughnutChart = new Chart(ctx).Doughnut(data,{});
});
