<?php
//echo "first\n";
$servername = "192.168.2.48";
$username = "ViMala";
$password = "ViMala@Sql";
$db_name = "ViMala";
// // Create connection
$mysqli = new mysqli($servername, $username, $password, $db_name);
//echo "bla\n";
// // Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}
//echo "Connected successfully\n";
if($result = $mysqli->query("SELECT * FROM JobSubmission WHERE STATUS = 0")) {
    //    echo " test\n";
    if ($result->num_rows > 0) { 
        echo "more than 0\n";
        while ($row = $result->fetch_assoc()) {
            $row['PARAMS'][0] = "";
            $id = $row['ID'];
            $field_array = explode("|",$row['PARAMS']);
            unset($field_array[count($field_array)-1]);
            $string = implode(",", $field_array);
            $conds = $mysqli->real_escape_string($row['CONDITIONS']);
            $sql = "SELECT ". $string . " FROM Lightcone";
            if($conds != "")
                $sql .= " WHERE ". $conds;
            $sql = "'$sql'";
            echo "\n";
            $cmd = "qsub /lustre/HI_FAST/ViMala/scripts/submit.pbs ".$id.";

            system($cmd,$return_value);
            ($return_value == 0) or die("returned an error: $cmd\n");
        }
    }
}
// } else 
//     print "Failed to prepare statement\n";
// $result->free(); 
$mysqli->close();
?>