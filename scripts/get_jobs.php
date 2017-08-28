<?php
$user_id = 1;
$mysqli = new mysqli("192.168.2.48", "ViMala", "ViMala@Sql", "ViMala");
$stmt = $mysqli->prepare("SELECT ID,TIME,STATUS FROM JobSubmission WHERE USER = ?");
$stmt->bind_param("i", $user_id);
if ($stmt->execute())
    echo "oh yeah";
else
    echo "oh no";


$content = "<b>Username:</b>&nbsp;&nbsp;&nbsp;&nbsp<br><br>\n";
$result = $stmt->get_result();
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
	$content = $content . "<tr><td>".$row["ID"]."</td><td>".$row["TIME"]."</td><td>".$status."</td></tr>";
    }
    $content = $content . "</table>";
} else {
    $content = $content . "There is no job submitted.";
}
$result->free();

$stmt->close();
$mysqli->close();
?>