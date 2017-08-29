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
if(!($result = $mysqli->query("SELECT ID,TIME,STATUS FROM JobSubmission WHERE STATUS = 0"))) {
    print "Failed to prepare statement\n";
} else {
    print_r($result);
    echo $result->num_rows;
    if ($result->num_rows > 0) {
	$content = $content . "<table><tr><th>Job ID</th><th>Time added</th><th>Status</th></tr>";
	while ($row = $result->fetch_assoc()) {
	    if ($row['STATUS'] == 0 )
		$status = "Queueing";
	    if ($row['STATUS'] == 1 )
		$status = "Completed";
	    if ($row['STATUS'] == 2 )
		$status = "Cancelled by user";
	    if ($row['STATUS'] == 3 )
		$status = "Cancelled by system";
	    $content = $content . "<tr><td>".$row["ID"]."</td><td>".$row["TIME"]."</td><td>".$status."</td></tr>\n";
	}
	$content = $content . "</table>";
    } else {
	$content = $content . "There is no job submitted.";
    }
    echo $content;
    $result->free();
}
$stmt->close();
$conn->close();
?>