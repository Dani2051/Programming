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

    // checks if user has signed in
    if (isset($_SESSION['userPlayingID'])){
        if (isset($_POST['score'])){
            // get the userID and score for request
            $userID = $_SESSION['userPlayingID'];
            $score = $_POST['score'];

            // insert the userID and score into the 'scores' table
            $sql = "INSERT INTO scores (userID, score, date) VALUES ('$userID', '$score', now())";
            $result1 = mysqli_query($conn, $sql);
        }
    }

mysqli_close($conn); // Closes connection    
?>