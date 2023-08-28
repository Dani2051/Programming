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

    // checks if user has signed in
    if (isset($_SESSION['userPlayingID'])){
        $userID = $_SESSION['userPlayingID'];
        $sql = "SELECT username FROM users WHERE userID = $userID";
        $result = mysqli_query($conn, $sql); // Performs query on database
        $userPlayingUsername[0]['userPlayingUsername'] = mysqli_fetch_assoc($result)['username'];
    } else {
        $userPlayingUsername[0]['userPlayingUsername'] = 'Guest'; // if user has not signed in
    }

    // echos the results as JSON
    echo json_encode($userPlayingUsername); 

mysqli_close($conn); // closes connection    
?>
