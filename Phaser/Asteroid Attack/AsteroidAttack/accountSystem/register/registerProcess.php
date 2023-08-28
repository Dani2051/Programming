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
    if (!$conn){
        echo("connection unsuccessful");
    }

    // Pulls in inputs from the login form and sets them as variables    
    $un = $_POST["uname"];
    $pw = $_POST["pword"];
    $confirmPw = $_POST["confirm_pword"];

    // Checks to see if any users with uname already exists
    $sql = "SELECT * FROM users WHERE username = '$un'";
    $result = mysqli_query($conn, $sql); // Performs query on database

    // Checks to see if any fields are empty 
    if ($un == "" or $pw == "" or $confirmPw == ""){
        $_SESSION['error'] = "emptyFields";
    } 
    // Checks to see if any fields contains spaces 
    elseif (preg_match('/\s/',$un) or preg_match('/\s/',$pw)){
        $_SESSION['error'] = "spaceExists";
    }
    // Checks to see if password and username are between 6 to 50 chars long
    elseif (strlen($un) > 50 or strlen($un) < 6 or strlen($pw) > 50 or strlen($pw) < 6){
        $_SESSION['error'] = "incorrectLength";
    }
    // Checks to see if any users exist with username entered
    elseif (mysqli_num_rows($result) >= 1) {
        $_SESSION['error'] = "userExists";
    }
    // Checks to see if password and confirm password are the same
    elseif ($pw !== $confirmPw) {
        $_SESSION['error'] = "notMatching";    
    }
    
    // Checks to see if there was any error
    if ($_SESSION['error'] != '') {
        header("Location: registerPage.php"); // Redirects to register page if error
    }
    else { // If there are no errors
        // Hashes password
        $pw = password_hash($pw, PASSWORD_DEFAULT);
        // Inserts username and password into table
        $sql = "INSERT INTO users (username, password, dateCreated) VALUES ('$un', '$pw', now())";
        mysqli_query($conn, $sql); // Performs query on database

        // Selects userID from database
        $sql = "SELECT userID FROM users WHERE username = '$un'";
        $result = mysqli_query($conn, $sql); // Performs query on database

        $_SESSION['userPlayingID'] = mysqli_fetch_assoc(mysqli_query($conn, $sql))['userID']; // Selects userID from database
        header("Location: /~ddar/AsteroidAttack/game"); // Once complete, the user is redirected to the game 
    }
    
mysqli_close($conn); // Closes connection
?>
