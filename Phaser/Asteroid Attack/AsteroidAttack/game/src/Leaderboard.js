class Leaderboard extends Phaser.Scene {

    constructor() {
        super("leaderboard")
    }

    preload() {
        this.load.image('leaderboardBack', 'assets/leaderboardBack.png')
        this.load.image('leaderboardTemplate', 'assets/leaderboardTemplate.png')
        this.load.image('buttonRed', 'assets/buttonRed.png')
        this.load.image('bigButtonBlue', 'assets/bigButtonBlue.png')
        this.load.image('longButtonBlue', 'assets/longButtonBlue.png')
    }

    create() {
        const windowX = this.cameras.main.width
        const windowY = this.cameras.main.height

        // fetch the JSON data from the server
        fetch('src/leaderboardProcess.php')
        .then(response => response.json()) // parse the JSON response
        .then(data => {
            var userPB = data[0].userPB
            var user1name = data[1].username
            var user1score = data[1].score
            var user2name = data[2].username
            var user2score = data[2].score
            var user3name = data[3].username
            var user3score = data[3].score
            var user4name = data[4].username
            var user4score = data[4].score
            var user5name = data[5].username
            var user5score = data[5].score

            // exit button
            var exitButtonTextSize = '50px'
            var exitButtonX = 160
            var exitButtonY = 75

            // personal best button
            var pbButtonTextSize = '30px'
            var pbButtonX = 1750
            var pbButtonY = 105  
            var spacing = 155
            var rowScale = 2.3

            // score rows
            var rowTextSize = '30px'
            var rowX = windowX/2
            var row1Y = 300
            var row2Y = row1Y + spacing
            var row3Y = row2Y + spacing
            var row4Y = row3Y + spacing
            var row5Y = row4Y + spacing
            var rowTextX = windowX/2 - 500
            var row1TextY = 285
            var row2TextY = row1TextY + spacing
            var row3TextY = row2TextY + spacing
            var row4TextY = row3TextY + spacing
            var row5TextY = row4TextY + spacing
            var rowScoreX = 1460

            // Global leaderboard title
            this.title = this.add.text(windowX/2, 140, 'Global Leaderboard', {fontSize: '75px', fill: '#000000', fontFamily: 'Arial'}).setDepth(2).setOrigin(0.5)
        
            // leaderboard back image
            this.add.sprite(windowX/2, windowY/2, 'leaderboardBack').setOrigin(0.5).setScale(2.2)

            // exit button image and text
            this.exitButtonText = this.add.text(exitButtonX, exitButtonY, 'Exit', {fontSize: exitButtonTextSize, fill: '#000000', fontFamily: 'Arial'}).setDepth(2).setOrigin(0.5)
            this.exitButton = this.add.sprite(exitButtonX, exitButtonY, 'buttonRed').setInteractive().setScale(1)
            .on('pointerover', () => this.exitButton.setTint(0xc05050))
            .on('pointerout', () => this.exitButton.clearTint())
            .on('pointerdown', () => this.scene.start("start"))

            // personal best button image and text
            this.pbButton = this.add.sprite(pbButtonX, pbButtonY, 'bigButtonBlue').setOrigin(0.5).setScale(2.4)
            this.pbButtonText = this.add.text(pbButtonX, pbButtonY, 'Personal best: \n' + userPB, {fontSize: pbButtonTextSize, align: 'center',  fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2).setOrigin(0.5) 

            // all the row images
            this.row1 = this.add.sprite(rowX, row1Y, 'longButtonBlue').setScale(rowScale)
            this.row2 = this.add.sprite(rowX, row2Y, 'longButtonBlue').setScale(rowScale)
            this.row3 = this.add.sprite(rowX, row3Y, 'longButtonBlue').setScale(rowScale)
            this.row4 = this.add.sprite(rowX, row4Y, 'longButtonBlue').setScale(rowScale)
            this.row5 = this.add.sprite(rowX, row5Y, 'longButtonBlue').setScale(rowScale)

            // all the row scores
            this.row1Score = this.add.text(rowScoreX, row1TextY, user1score, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2).setOrigin(1, 0) 
            this.row2Score = this.add.text(rowScoreX, row2TextY, user2score, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2).setOrigin(1, 0) 
            this.row3Score = this.add.text(rowScoreX, row3TextY, user3score, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2).setOrigin(1, 0) 
            this.row4Score = this.add.text(rowScoreX, row4TextY, user4score, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2).setOrigin(1, 0) 
            this.row5Score = this.add.text(rowScoreX, row5TextY, user5score, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2).setOrigin(1, 0) 

            // all the row text
            this.row1text = this.add.text(rowTextX, row1TextY, '#1 ' + user1name, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2) 
            this.row2text = this.add.text(rowTextX, row2TextY, '#2 ' + user2name, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2) 
            this.row3text = this.add.text(rowTextX, row3TextY, '#3 ' + user3name, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2) 
            this.row4text = this.add.text(rowTextX, row4TextY, '#4 ' + user4name, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2) 
            this.row5text = this.add.text(rowTextX, row5TextY, '#5 ' + user5name, {fontSize: rowTextSize, fill: '#000000', fontFamily: 'Arial'})    
            .setDepth(2)
        })
        .catch(error => console.error(error))
    }
}