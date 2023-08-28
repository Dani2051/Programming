<?php
    // Starts a session
    session_start();

    $server = "localhost";
    $username = "ddar";
    $password = "tjwa1234";
    $database = "AsteroidAttack";

    // Create connection
    $conn = mysqli_connect($server, $username, $password, $database);
    // Check connection
    if (!$conn) {
        echo("connection unsuccessful");
    }

    session_destroy();

    //mail('ddar16@thejohnwallisacademy.org', 'Hello', 'This was sent with PHP');
    header("Location: /~ddar/AsteroidAttack/game"); // Redirects to game page

mysqli_close($conn); // Closes connection    
?>