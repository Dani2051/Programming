class HowToPlay extends Phaser.Scene { // creates the class for this scene
    constructor() {
        super("howtoplay") // creates identifier for this scene
    }

    preload() {
        this.load.image('buttonRed', 'assets/buttonRed.png')
        this.load.image('space', 'assets/SPACE.png')
        this.load.image('wasd', 'assets/WASD.png')
        this.load.image('arrows', 'assets/ARROWS.png')
        this.load.atlas('asteroidSheet', 'assets/asteroidSheet.png', 'assets/asteroidSheet.json')
        this.load.atlas('supportPayloadSheet', 'assets/supportPayloadSheet.png', 'assets/supportPayloadSheet.json')
        this.load.atlas('spaceshipSheet', 'assets/spaceshipSheet.png', 'assets/spaceshipSheet.json')
        this.load.atlas('blackholeSheet', 'assets/blackholeSheet.png', 'assets/blackholeSheet.json')
    }

    create() {
        const windowX = this.cameras.main.width
        const windowY = this.cameras.main.height

        const titleX = (windowX + 250)/2

        const exitButtonTextSize = '50px'
        const exitButtonX = 160
        const exitButtonY = 75

        const spriteLabelSpacing = 100
        const labelTextSize = '35px'
        
        const spriteSpacing = 230       
        const spriteCentreY = windowY/2 + exitButtonY + 20
        const asteroidY = spriteCentreY - spriteSpacing*1.5
        const payloadY = spriteCentreY + spriteSpacing*1.5
        const blackholeY = spriteCentreY + spriteSpacing*0.5
        const spaceshipY = spriteCentreY - spriteSpacing*0.5
        const spriteScale = 3
        const spriteX = 170        

        const keyY = windowY - 100
        const keyLabelY = keyY - 150
        const key1X = 700      
        const key2X = key1X + 300
        const spaceX = 1400      

        // title
        this.add.text(titleX, 200, 'How to play', {fontStyle: 'bold', fontSize: '100px', align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)

        // instructions
        this.add.text(titleX, 500, 'The aim of the game is to get the highest score possible and compete against others from around the world. You must dodge, shoot and take down asteroids and each time you have destroyed one you get points! Be careful though, if an asteroid hits you then you lose a life. You must also be aware of blackholes which are so powerful that they cannot be taken down, not even with your bullets so you must get out of their way to dodge them or they will swallow you up and take a life! In case you get low on health and take some hits, support payloads will spawn randomly to give you some health. You will first start the game with 3 health with the ability to hold 4. Goodluck!', 
        { fontStyle: 'bold', align: 'center', fontSize: '35px', fill: '#000000', fontFamily: 'Arial', wordWrap: { width: 1300 }}).setOrigin(0.5)

        // sprite labels
        this.add.text(spriteX, asteroidY - spriteLabelSpacing,  'Asteroid', {fontStyle: 'bold', fontSize: labelTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)
        this.add.text(spriteX, payloadY - spriteLabelSpacing, 'Support payload', {fontStyle: 'bold',fontSize: labelTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)
        this.add.text(spriteX, blackholeY - spriteLabelSpacing, 'Blackhole', {fontStyle: 'bold',fontSize: labelTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)
        this.add.text(spriteX, spaceshipY - spriteLabelSpacing, 'Spaceship', {fontStyle: 'bold',fontSize: labelTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)

        // projectile images
        this.add.sprite(spriteX, asteroidY, 'asteroidSheet').setOrigin(0.5).setScale(spriteScale)
        this.add.sprite(spriteX, payloadY, 'supportPayloadSheet').setOrigin(0.5).setScale(spriteScale)
        this.add.sprite(spriteX, spaceshipY, 'spaceshipSheet').setOrigin(0.5).setScale(spriteScale)
        this.add.sprite(spriteX, blackholeY, 'blackholeSheet').setOrigin(0.5).setScale(spriteScale)

        // control text
        this.add.text((key1X + key2X)/2, keyLabelY,   'Move', {fontStyle: 'bold', fontSize: labelTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)
        this.add.text(spaceX, keyLabelY, 'Shoot', {fontStyle: 'bold',fontSize: labelTextSize, align: 'center', fill: '#000000', fontFamily: 'Arial'}).setOrigin(0.5)

        // control images
        this.add.sprite(key1X, keyY, 'wasd').setOrigin(0.5, 0.75)
        this.add.sprite(key2X, keyY, 'arrows').setOrigin(0.5, 0.75)
        this.add.sprite(spaceX, keyY, 'space').setOrigin(0.5)
        
        // exit button image and text
        this.exitButtonText = this.add.text(exitButtonX, exitButtonY, 'Exit', {fontSize: exitButtonTextSize, fill: '#000000', fontFamily: 'Arial'}).setDepth(2).setOrigin(0.5)
        this.exitButton = this.add.sprite(exitButtonX, exitButtonY, 'buttonRed').setInteractive().setScale(1)
        .on('pointerover', () => this.exitButton.setTint(0xc05050))
        .on('pointerout', () => this.exitButton.clearTint())
        .on('pointerdown', () => this.scene.start("start"))
    }
}
