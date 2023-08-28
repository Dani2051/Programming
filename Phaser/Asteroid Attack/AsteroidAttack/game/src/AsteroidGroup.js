import Asteroid from './Asteroid.js' // Imports Asteroid class

export default class AsteroidGroup extends Phaser.Physics.Arcade.Group {

    constructor(scene) {
        super(scene.physics.world, scene)

        this.createMultiple ({ // creates multiple instances
            classType: Asteroid, // of asteroid class
            frameQuantity: 6, // creates 300 asteroid and stores them for later use 
            active: false,
            visible: false,
            key: 'asteroidSheet' // references asteroid image 
        })
    }

    randGeneration(scene) {
        let rnd = Phaser.Math.RND
        let randomNum = rnd.between(1, 100) // randomly generates integer
        if (randomNum > 10) { // if integer is above spawn rate
            let Asteroid = this.getFirstDead(false) // gets first unused asteroid
            if (Asteroid) { // if true
                let minScale = 2
                let maxScale = 5
                let ranScale = rnd.between(minScale, maxScale)
                let y = rnd.between(Asteroid.height/2 + scene.barHeight, scene.windowY - Asteroid.height/2) // randomly generates asteroid height within spawn area 
                let speed = rnd.between(50, 500) // randomly generates asteroid speed

                Asteroid.spawnAsteroid(y, speed, ranScale, scene)
            }
        }
    }
}