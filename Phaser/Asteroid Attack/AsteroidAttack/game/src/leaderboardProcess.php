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
    
    // create empty  array
    $leaderboardData = array();

    // checks if user has signed in
    if (isset($_SESSION['userPlayingID'])){
        $userID = $_SESSION['userPlayingID'];
        $sql1 = "SELECT score FROM scores WHERE userID = $userID ORDER BY score DESC LIMIT 1";
        $result1 = mysqli_query($conn, $sql1); // Performs query on database
        if (mysqli_num_rows($result1) == 1) {
            $leaderboardData[0]['userPB'] = mysqli_fetch_assoc($result1)['score'];
        } else {
            $leaderboardData[0]['userPB'] = 'NA';
        }
    } else {
        $leaderboardData[0]['userPB'] = 'NA';
    }

    $sql2 = "SELECT * FROM scores INNER JOIN users ON scores.userID = users.userID ORDER BY score DESC LIMIT 5;";
    $result2 = mysqli_query($conn, $sql2); // Performs query on database
    
    $i = 1;
    // stores top results in array
    while ($row = mysqli_fetch_assoc($result2)) { 
        $leaderboardData[$i]['score'] = $row['score'];
        $leaderboardData[$i]['userID'] = $row['userID'];
        $leaderboardData[$i]['username'] = $row['username'];
        $i ++;
    }

    // echos the scores as JSON
    echo json_encode($leaderboardData);
  
mysqli_close($conn); // Closes connection    
?>