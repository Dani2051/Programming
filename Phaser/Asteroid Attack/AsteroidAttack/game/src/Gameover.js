class Gameover extends Phaser.Scene { // creates the class for this scene
    constructor() {
        super("gameover"); // creates identifier for this scene
    }

    init (data)
    {
        this.userCurrentScore = data.score;
    }

    preload() {
        this.load.image('buttonRed', 'assets/buttonRed.png')
        this.load.image('buttonGreen', 'assets/buttonGreen.png')
        this.load.image('gameoverBack', 'assets/gameoverBack.png')
    }

    create() {
        // create an instance of XMLHttpRequest
        var xhttp = new XMLHttpRequest();

        // set the request URL and method
        var url = "src/uploadScoreProcess.php";
        var method = "POST";

        // set the request parameters
        var params = "score=" + this.userCurrentScore;

        // send the POST request
        xhttp.open(method, url, true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send(params);

        fetch('src/gameoverProcess.php')
        .then(response => response.json()) // parse the JSON response
        .then(data => {

            const userPB = data[0].userPB // selects user PB
            const windowX = this.cameras.main.width;
            const windowY = this.cameras.main.height;
            const buttonOffset = 215;
            const titleTextSize = '110px';
            const buttonTextSize = '40px';
            const scoreTextSize = '55px';
            const titleY = 400
            const playerScoreY = 525
            const highscoreY = playerScoreY + 100
            const buttonY = 770
            const scoresX = windowX/2
            const buttonScale = 1.3

            // creates back
            this.add.sprite(windowX/2, windowY/2, 'gameoverBack').setOrigin(0.5).setScale(2.5) // gameover back

            // creates buttons
            this.exitButton = this.add.sprite(windowX/2 - buttonOffset, buttonY, 'buttonGreen').setInteractive().setScale(buttonScale)
            .on('pointerover', () => this.exitButton.setTint(0x36bb5b))
            .on('pointerout', () => this.exitButton.clearTint())
            .on('pointerdown', () => this.scene.start("main")) // play again button

            this.playAgainButton = this.add.sprite(windowX/2 + buttonOffset, buttonY, 'buttonRed').setInteractive().setScale(buttonScale)
            .on('pointerover', () => this.playAgainButton.setTint(0xc05050))
            .on('pointerout', () => this.playAgainButton.clearTint())
            .on('pointerdown', () => this.scene.start("start")) // exit text

            // creates text
            this.add.text(windowX/2, titleY, 'GAME OVER', {fontSize: titleTextSize, align: 'center', fill: '#000000', fontFamily: 'Times New Roman'})
            .setOrigin(0.5) // gameover text

            this.add.text(scoresX, playerScoreY, 'Your score: ' + this.userCurrentScore, {fontSize: scoreTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'})
            .setOrigin(0.5) // Score text

            this.playAgainButtonText = this.add.text(windowX/2 - buttonOffset, buttonY, 'Play again', {fontSize: buttonTextSize, fill: '#000000', fontFamily: 'Arial'})
            .setOrigin(0.5) // play again text

            this.exitButtonText = this.add.text(windowX/2 + buttonOffset, buttonY, 'Exit', {fontSize: buttonTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setOrigin(0.5) // exit text        
            
            if (this.userCurrentScore >= userPB) {
                this.add.text(scoresX - 270, highscoreY, 'NEW', {fontSize: scoreTextSize, align: 'center', fill: '#FF0000', fontFamily: 'Arial'})
                .setOrigin(0.5) // NEW text
                this.add.text(scoresX, highscoreY, 'Highscore: ' + this.userCurrentScore, {fontSize: scoreTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'})
                .setOrigin(0.5) // PB text
            } else {
                this.add.text(scoresX, highscoreY, 'Highscore: ' + userPB, {fontSize: scoreTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'})
                .setOrigin(0.5) // PB text
            }
        })
        .catch(error => console.error(error));
    }
}
