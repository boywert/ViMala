<?php
$user_id = 1;
$servername = "192.168.2.48";
$username = "ViMala";
$password = "ViMala@Sql";
$db_name = "ViMala";
// Create connection
$mysqli = new mysqli($servername, $username, $password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully\n";
if(!($result = $mysqli->query("SELECT * FROM JobSubmission WHERE STATUS = 0"))) {
    print "Failed to prepare statement\n";
} else {
    if ($result->num_rows > 0) {
	while ($field_array = $result->fetch_assoc()) {
	    $field = explode($row['PARAMS'],"|");
	    print_r($field_array);
	}
    $result->free();
}
$stmt->close();
$conn->close();
?>