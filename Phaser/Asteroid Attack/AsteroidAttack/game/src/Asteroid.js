export default class Asteroid extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y){
        super(scene, x, y, 'asteroidSheet')
    }

    spawnAsteroid(y, speed, scale, scene) {
        scene.asteroids.add(this)
        this.body.reset(scene.cameras.main.width + 50, y) // spawns asteroid at right of screen with the random y value
        this.setScale(scale) // scales the asteroid
        this.setActive(true) // makes asteroid active
        this.setVisible(true) // makes asteroid visible
        this.setVelocityX(-speed) // x velocity of asteroid
        this.setOffset(33, 35) // adjusts offset from scaling 
        this.setCircle((this.width - 65)/2) // adjusts the asteroids hitbox
    }

    preUpdate() { // update method
        if (this.x == -100 && this.y == -100) { // if asteroid has been shot down
            this.setActive(false) 
            this.setVisible(false)
        }

        else if (this.x < -this.width/2) { // if asteroid reaches left         
            this.setActive(false) 
            this.setVisible(false)

            if (scene.health > 1) { // checks if health remains
                scene.health -= 1
                scene.playerHealth.text = "Health: " + scene.health
            } 
            else {
                scene.bgMusic.pause()
                scene.scene.start('gameover', { score: scene.score }) // calls gameover scene if all health lost
            }
        }
    }
}
