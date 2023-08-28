<?php
    // starts a session
    session_start();

    $server = "localhost";
    $username = "ddar";
    $password = "tjwa1234";
    $database = "AsteroidAttack";

    // creates connection
    $conn = mysqli_connect($server, $username, $password, $database);
    // checks connection
    if (!$conn) {
        echo("connection unsuccessful");
    }

    session_destroy(); // destroys all session variables

mysqli_close($conn); // closes connection
?>
