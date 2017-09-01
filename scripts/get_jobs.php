<?php
$servername = "192.168.2.48";
$username = "ViMala";
$password = "ViMala@Sql";
$db_name = "ViMala";
// Create connection
$mysqli = new mysqli($servername, $username, $password, $db_name);
echo "bla";
// Check connection
if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}
echo "Connected successfully\n";
if($result = $mysqli->query("SELECT * FROM JobSubmission WHERE STATUS = 0")) {
    echo " test";
    if ($result->num_rows > 0) {
	while ($row = $result->fetch_assoc()) {
	    $field_array = explode($row['PARAMS'],"|");
	    print_r($field_array);
	}
       
} else 
    print "Failed to prepare statement\n";
$result->free(); 
$conn->close();
?>