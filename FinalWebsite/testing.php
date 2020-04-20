
<?php
	
	$param = $_GET["usertext"];
	$text = json_encode($param) ;
	$answer = $_GET['radiogroup'];  
if ($answer == "URL") { 
	echo "Using URL";         
    $command = escapeshellcmd('python keywordextraction.py --url ' .$text);
    $output = shell_exec($command);  
    //echo $output;   
}
else {
	echo "Using text";
    $command = escapeshellcmd('python keywordextraction.py --text' .$text);
    $output = shell_exec($command);
    //echo $output;
}       

    header("location:dbcon1.php");

?>

