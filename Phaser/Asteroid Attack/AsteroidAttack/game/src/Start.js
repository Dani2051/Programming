class Start extends Phaser.Scene { // creates the class for this scene 
    constructor() {
        super("start") // creates identifier for this scene
    }

    create() {
        const windowX = this.cameras.main.width
        const windowY = this.cameras.main.height
        const buttonSize = '70px'
        const buttonSpacing = 110
        const buttonX = 80
        const buttonY = windowY - 80

        // creates title
        this.add.text(windowX/2, windowY/2, 'Asteroid Attack', {fontSize: '120px', fill: '#ff0000', fontFamily: 'Arial'})
        .setOrigin(0.5)
        
        // creates start button 
        this.startButton = this.add.text(buttonX, buttonY - buttonSpacing*2, 'Start', {fontSize: buttonSize, fill: '#000000', fontFamily: 'Arial'})
        .setInteractive({useHandCursor: true}).setOrigin(0, 1) // sets button to interactive 
        // when first parameter is true then the corresponding function is called
        .on('pointerover', () => this.startButton.setStyle({fill: '#00ff00'}))
        .on('pointerout', () => this.startButton.setStyle({fill: '#000000'}))
        .on('pointerdown', () => this.scene.start("main"))

        // creates how to play button 
        this.howToPlayButton = this.add.text(buttonX, buttonY - buttonSpacing, 'How to play', {fontSize: buttonSize, fill: '#000000', fontFamily: 'Arial'})
        .setInteractive({useHandCursor: true}).setOrigin(0, 1) // sets button to interactive 
        // when first parameter is true then the corresponding function is called
        .on('pointerover', () => this.howToPlayButton.setStyle({fill: '#00ff00'}))
        .on('pointerout', () => this.howToPlayButton.setStyle({fill: '#000000'}))
        .on('pointerdown', () => this.scene.start("howtoplay"))

        // creates leaderboard button
        this.leaderboardButton = this.add.text(buttonX, buttonY, 'Leaderboard', {fontSize: buttonSize, fill: '#000000', fontFamily: 'Arial'})    
        .setInteractive({useHandCursor: true}).setOrigin(0, 1) // sets button to interactive
        // when first parameter is true then the corresponding function is called
        .on('pointerover', () => this.leaderboardButton.setStyle({fill: '#00ff00'}))
        .on('pointerout', () => this.leaderboardButton.setStyle({fill: '#000000'}))
        .on('pointerdown', () => this.scene.start("leaderboard"))

        // creates logout button 
        this.logoutButton = this.add.text(windowX - 50, 50, 'Log out', {fontSize: '35px', fill: '#000000', fontFamily: 'Arial'})
        .setInteractive({useHandCursor: true}).setOrigin(1, 0) // sets button to interactive 
        // when first parameter is true then the corresponding function is called
        .on('pointerover', () => this.logoutButton.setStyle({fill: '#00ff00'}))
        .on('pointerout', () => this.logoutButton.setStyle({fill: '#000000'}))
        .on('pointerdown', () => {  
                let xhr = new XMLHttpRequest()
                xhr.open('GET', 'src/destroySession.php', true)
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
                xhr.send()
                window.location.href = "https://2-12.co.uk/~ddar"
        })

        // creates feedback button 
        this.feedbackButton = this.add.text(windowX - 50, windowY - 50, 'Feedback', {fontSize: '20px', fill: '#000000', fontFamily: 'Arial'})
        .setInteractive({useHandCursor: true}).setOrigin(1, 1) // sets button to interactive 
        // when first parameter is true then the corresponding function is called
        .on('pointerover', () => this.feedbackButton.setStyle({fill: '#00ff00'}))
        .on('pointerout', () => this.feedbackButton.setStyle({fill: '#000000'}))
        .on('pointerdown', () => alert('Have any feedback or questions? Please contact daniyaaldar@gmail.com'))

        // displays users username
        fetch('src/getUsername.php')
        .then(response => response.json()) // parse the JSON response
        .then(data => {
            this.add.text(25, 25, 'Logged in as: ' + data[0].userPlayingUsername, {fontSize: '20px', fill: '#000000', fontFamily: 'Arial'})
        })
    }
}
