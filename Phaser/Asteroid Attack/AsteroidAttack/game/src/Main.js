import AsteroidGroup from './AsteroidGroup.js' // imports AsteroidGroup class
import BulletGroup from './BulletGroup.js' // imports BulletGroup class
import SupportPayloadGroup from './SupportPayloadGroup.js' // imports SupportPayloadGroup class
import BlackholeGroup from './BlackholeGroup.js' // imports BlackholeGroup class

export default class Main extends Phaser.Scene {

    constructor() {
        super('main') // creates identifier for this scene
    }

    preload() {
        this.load.image('bulletIMG', 'assets/bullet.png')
        this.load.image('backgroundIMG', 'assets/bg.png')
        this.load.image('starsIMG', 'assets/bgStars.png')
        this.load.audio('explodeAUDIO', 'assets/explosion.wav')
        this.load.audio('bulletAUDIO', 'assets/shoot.wav')
        this.load.audio('bgAUDIO', 'assets/bgMusic.wav')
        this.load.audio('blackholeShotAUDIO', 'assets/blackholeShot.wav')
        this.load.atlas('asteroidSheet', 'assets/asteroidSheet.png', 'assets/asteroidSheet.json')
        this.load.atlas('supportPayloadSheet', 'assets/supportPayloadSheet.png', 'assets/supportPayloadSheet.json')
        this.load.atlas('spaceshipSheet', 'assets/spaceshipSheet.png', 'assets/spaceshipSheet.json')
        this.load.atlas('blackholeSheet', 'assets/blackholeSheet.png', 'assets/blackholeSheet.json')
    }

    create() {           
        const windowX = this.cameras.main.width
        const windowY = this.cameras.main.height

        this.barHeight = 80
        this.speed = 700
        this.score = 0
        this.asteroidPointAdd = 5
        this.blackholePointAdd = 5
        this.health = 3
        this.maxHealth = 4
        this.asteroidPointDeduct = 5
        this.blackholePointDeduct = 5
        
        this.bar = this.add.graphics().setDepth(1) // creates bar
        this.bar.fillStyle(0x000000, 1)
        this.bar.beginPath()
        this.bar.moveTo(0, 0)
        this.bar.lineTo(windowX , 0)
        this.bar.lineTo(windowX, this.barHeight)
        this.bar.lineTo(0, this.barHeight)
        this.bar.lineTo(0, 0)
        this.bar.closePath()
        this.bar.fillPath()

        this.explodeSFX = this.sound.add('explodeAUDIO', {volume: 0.5})  
        this.bulletSFX = this.sound.add('bulletAUDIO', {volume: 0.10}) 
        this.bgMusic = this.sound.add('bgAUDIO', {volume: 0.1, loop: true})
        this.blackholeShotSFX = this.sound.add('blackholeShotAUDIO', {volume: 0.5})
        this.bgMusic.play()
        
        this.background = this.add.tileSprite(0, 0, windowX*2, windowY*2, 'backgroundIMG').setOrigin(0, 0).setScale(6.5)
        this.stars = this.add.tileSprite(0, 0, windowX*2, windowY*2, 'starsIMG').setOrigin(0, 0).setScale(6.5)
        this.playerScore = this.add.text(windowX - 250, 20, "Score: 0", {font: "40px Arial", fill: "white"}).setDepth(2)
        this.playerHealth = this.add.text(50, 20, "Health: " + this.health, {font: "40px Arial", fill: "white"}).setDepth(2)
        this.spaceship = this.physics.add.sprite(100, windowY/2, 'spaceshipSheet').setDepth(2).setScale(3).setCollideWorldBounds(true).setSize(40, 30, true)// adds ship
        this.spaceship.body.setBoundsRectangle(new Phaser.Geom.Rectangle(0, this.barHeight + 24, windowX, windowY  - this.barHeight - 50)) // sets new world bounds taking bar into account

        this.asteroids = this.add.group()
        this.supportPayloads = this.add.group()
        this.bullets = this.add.group()
        this.blackholes = this.add.group()

        this.AsteroidGroup = new AsteroidGroup(this) // creates new instance of AsteroidGroup class
        this.BulletGroup = new BulletGroup(this) // creates new instance of BulletGroup class        
        this.SupportPayloadGroup = new SupportPayloadGroup(this) // creates new instance of SupportPayloadGroup class
        this.BlackholeGroup = new BlackholeGroup(this) // creates new instance of BlackholeGroup class        
        
        // asteroid and bullet collider
        this.physics.add.overlap(this.asteroids, this.bullets, this.bulletAsteroidCollision, null, this)

        // asteroid and spaceship collider
        this.physics.add.overlap(this.asteroids, this.spaceship, this.spaceshipAsteroidCollision, null, this)

        // payload and bullet collider
        this.physics.add.overlap(this.supportPayloads, this.spaceship, this.spaceshipPayloadCollision, null, this)

        // payload and spaceship collider
        this.physics.add.overlap(this.supportPayloads, this.bullets, this.bulletPayloadCollision, null, this)

        // bullet and blackhole collider
        this.physics.add.overlap(this.bullets, this.blackholes, this.bulletBlackholeCollision, null, this)

        // spaceship and blackhole collider
        this.physics.add.overlap(this.blackholes, this.spaceship, this.spaceshipBlackholeCollision, null, this)

        this.inputKeys = this.input.keyboard.addKeys('left, right, up, down, space, W, S, A, D')

        this.anims.create({
            key: 'explodeAsteroid',
            frames: this.anims.generateFrameNames('asteroidSheet', {
            prefix: 'asteroid',
            suffix: '.png',
            start: 1,
            end: 7,
        }),
        duration: 500,
        skipMissedFrames: false,
        repeat: 0,
        hideOnComplete: true,
        })

        this.anims.create({
            key: 'explodeShip',
            frames: this.anims.generateFrameNames('spaceshipSheet', {
            prefix: 'spaceship',
            suffix: '.png',
            start: 1,
            end: 7,
        }), 
        duration: 500,
        skipMissedFrames: false,
        repeat: 0,
        hideOnComplete: false,
        })

        this.anims.create({
            key: 'explodeSupportPayload',
            frames: this.anims.generateFrameNames('supportPayloadSheet', {
            prefix: 'supportPayload',
            suffix: '.png',
            start: 1,
            end: 6,
        }),
        duration: 500,
        skipMissedFrames: false,
        repeat: 0,
        hideOnComplete: true,
        })

        
        this.anims.create({
            key: 'explodeBlackhole',
            frames: this.anims.generateFrameNames('blackholeSheet', {
            prefix: 'blackhole',
            suffix: '.png',
            start: 1,
            end: 7,
        }),
        duration: 300,
        skipMissedFrames: false,
        repeat: 0,
        hideOnComplete: true,
        })
    }

    spaceshipBlackholeCollision(blackhole) {
        this.blackholeShotSFX.play()
        this.blackhole = this.blackholes.get(blackhole.x, blackhole.y) // finds blackhole
        this.blackhole.play('explodeBlackhole').setScale(blackhole.scale) // plays animation
        blackhole.body.reset(-100, -100) // sends blackhole off page
        this.spaceship.play('explodeShip') // plays animation 

        if (this.score <= this.blackholePointDeduct) { // ensures score never goes negative
            this.score = 0 // deducts score
        }
        else {
            this.score -= this.blackholePointDeduct // deducts score
        }

        this.playerScore.text = "Score: " + this.score
        
        if (this.health > 1) { // checks if health remains
            this.health -= 1
            this.playerHealth.text = "Health: " + this.health
        } 
        else {
            this.bgMusic.pause()
            this.scene.start('gameover', { score: this.score }) // calls gameover scene is all health lost
        }
    }

    spaceshipAsteroidCollision(asteroid) {
        this.blackholeShotSFX.play()
        this.asteroid = this.asteroids.get(asteroid.x, asteroid.y) // finds asteroid
        this.asteroid.play('explodeAsteroid').setScale(asteroid.scale) // plays animation
        asteroid.body.reset(-100, -100) // sends asteroid off page
        this.spaceship.play('explodeShip') // plays animation 

        if (this.score <= this.asteroidPointDeduct) { // ensures score never goes negative
            this.score = 0 // deducts score
        }
        else {
            this.score -= this.asteroidPointDeduct // deducts score
        }

        this.playerScore.text = "Score: " + this.score
        
        if (this.health > 1) { // checks if health remains
            this.health -= 1
            this.playerHealth.text = "Health: " + this.health
        } 
        else {
            this.bgMusic.pause()
            this.scene.start('gameover', { score: this.score }) // calls gameover scene is all health lost
        }
    }

    bulletAsteroidCollision(asteroid, bullet) {
        this.explodeSFX.play()
        this.asteroid = this.asteroids.get(asteroid.x, asteroid.y) // finds asteroid
        this.asteroid.play('explodeAsteroid').setScale(asteroid.scale) // plays animation
        this.score += this.asteroidPointAdd // adds score
        this.playerScore.text = "Score: " + this.score
        asteroid.body.reset(-100, -100) // sends asteroid off page which deletes it
        bullet.body.reset(windowX + 100, windowY + 100) // sends bullet off page
    }

    spaceshipPayloadCollision(payload) {
        this.explodeSFX.play()
        this.payload = this.supportPayloads.get(payload.x, payload.y) // finds payload
        this.payload.play('explodeSupportPayload').setScale(payload.scale) // plays animation
        payload.body.reset(-100, -100) // sends payload off page which deletes it

        if (this.health < this.maxHealth) { // ensures health never goes above 3
            this.health += 1 // adds health
        }

        this.playerHealth.text = "Health: " + this.health
    }

    bulletPayloadCollision(payload, bullet) {
        this.explodeSFX.play()
        this.payload = this.supportPayloads.get(payload.x, payload.y) // finds payload
        this.payload.play('explodeSupportPayload').setScale(payload.scale) // plays animation
        payload.body.reset(-100, -100) // sends payload off page which deletes it
        bullet.body.reset(windowX + 100, windowY + 100) // sends bullet off page which deletes it
        
        if (this.health < this.maxHealth) { // ensures health never goes above 3
            this.health += 1 // adds health
        }

        this.playerHealth.text = "Health: " + this.health
    }

    update() {
        if (this.inputKeys.up.isDown || this.inputKeys.W.isDown) {
            this.spaceship.setVelocityY(-this.speed) // moves spaceship up
        }

        else if (this.inputKeys.down.isDown || this.inputKeys.S.isDown) {
            this.spaceship.setVelocityY(this.speed) // moves spaceship down
        }
        
        else  { 
            this.spaceship.setVelocityY(0) // stops spaceship y velocity
        }

        if (this.inputKeys.right.isDown || this.inputKeys.D.isDown) {
            this.spaceship.setVelocityX(this.speed) // moves spaceship right
        }        
        
        else if (this.inputKeys.left.isDown || this.inputKeys.A.isDown) {
            this.spaceship.setVelocityX(-this.speed) // moves spaceship left
        }

        else  { 
            this.spaceship.setVelocityX(0) // stops spaceship x velocity
        }


        if (this.input.keyboard.checkDown(this.inputKeys.space, 120) == true) {
            this.bulletSFX.play()  
            this.BulletGroup.fire(this, this.spaceship.x + this.spaceship.height, this.spaceship.y) // shoots bullets from spaceship 
        }

        // scrolls background left
        this.background.tilePositionX += 0.6
        this.stars.tilePositionX += 0.3 

        // randomly spawns projectiles
        this.AsteroidGroup.randGeneration(this)
        this.SupportPayloadGroup.randGeneration(this)
        this.BlackholeGroup.randGeneration(this)
    }
}