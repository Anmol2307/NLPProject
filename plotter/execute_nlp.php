<?php 

$txt = $_POST["text_input"];
echo $txt;

$myfile = fopen("../Interface/input.txt", "w") or die("Unable to open file!");
fwrite($myfile, $txt);
fclose($myfile);

$js_txt = '$(function(){$("#query").html("'.htmlentities(trim($txt)).'");});';
$myfile = fopen("js/prev_sentence.js", "w") or die("Unable to open file!");
fwrite($myfile, $js_txt);
fclose($myfile);

$command = 'cd ../Interface/ ; bash auto_execute.sh 2>&1';
// echo '<br/>'.$command.'<br/>';
$output = shell_exec($command);
// echo $output.'<br/>DONE';

$command = 'cd ../Interface/ ; python3 aspect_analysis.py; python3 sentiment_analysis.py';
// echo '<br/>'.$command.'<br/>';
$output = shell_exec($command);
// echo $output.'<br/>DONE';

header("LOCATION: interface.html");	
?>