<?php
$host = 'db';
$db   = 'appdb';
$user = 'webuser';
$pass = 'webpass';

// Attempt MySQL connection
$conn = new mysqli($host, $user, $pass, $db);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "<h1>Connected to MySQL successfully!</h1>";
$conn->close();
?>
