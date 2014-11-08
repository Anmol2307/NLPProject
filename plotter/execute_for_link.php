<?php
/*
$txt = $_POST["text_input"];
echo $txt;
*/
/*$myfile = fopen("../Interface/flipkart/flipkart/spiders/link.py", "w") or die("Unable to open file!");
fwrite($myfile, "input_link = \"".$txt."\"");
fclose($myfile);

$command = 'cd ../Interface/flipkart ; scrapy crawl review -o ../input.xml';
echo '<br/>'.$command.'<br/>';
$output = shell_exec($command);
echo $output.'<br/>DONE';
*/
$file_text = file_get_contents('../Interface/input.xml', true);
$file_text = nl2br($file_text);
$file_text = strip_tags($file_text);
$file_text = html_entity_decode($file_text);
$file_text = strip_tags($file_text);
$file_text = preg_replace("/&#?[a-z0-9]{2,8};/i","",$file_text);
$file_text =  mb_convert_encoding ( $file_text,'ASCII');
// echo $file_text;

$myfile = fopen("../Interface/input.txt", "w") or die("Unable to open file!");
fwrite($myfile, $file_text);
fclose($myfile);

$js_txt = '$(function(){$("#query").html("'.trim($file_text).'");});';
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