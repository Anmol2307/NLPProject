$(function(){
var nodes_1 = [
{id: 1, label: "battery"},
{id: 2, label: "good"},
{id: 3, label: "even"},
{id: 4, label: "bad"},
{id: 5, label: "light"},
];
var edges_1 = [
{from: 1, to: 2},
{from: 1, to: 3},
{from: 1, to: 4},
{from: 1, to: 5},
];
var container_1 = document.getElementById("container_1");
var data_1= {
nodes: nodes_1,
edges: edges_1
};
var options_1 = {
width: "600px",
height: "600px"
};
var network_1 = new vis.Network(container_1, data_1, options_1);
});
