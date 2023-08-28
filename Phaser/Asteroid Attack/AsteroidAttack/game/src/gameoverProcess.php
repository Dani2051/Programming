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

    // create empty array
    $userScoreData = array();

    // checks if user has signed in
    if (isset($_SESSION['userPlayingID'])){
        $userID = $_SESSION['userPlayingID']; // get the userID for request
        $sql = "SELECT score FROM scores WHERE userID = $userID ORDER BY score DESC LIMIT 1";
        $result = mysqli_query($conn, $sql); // Performs query on database
        $userScoreData[0]['userPB'] = mysqli_fetch_assoc($result)['score']; // sets userPB
    } else {
        $userScoreData[0]['userPB'] = 'NA'; // if user not logged in
    }

    // echos the scores as JSON
    echo json_encode($userScoreData);

mysqli_close($conn); // Closes connection    
?>