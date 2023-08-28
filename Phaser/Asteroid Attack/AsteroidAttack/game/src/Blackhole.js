export default class Blackhole extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y){
        super(scene, x, y, 'blackholeSheet')
        this.mainScene = scene
    }

    spawnBlackhole(y, speed, scale, scene) {
        scene.blackholes.add(this)
        this.body.reset(scene.cameras.main.width + 50, y) // spawns blackhole at right of screen with the random y value
        this.setScale(scale) // scales the blackhole
        this.setActive(true) // makes blackhole active
        this.setVisible(true) // makes blackhole visible
        this.setVelocityX(-speed) // x velocity of blackhole
    }

    preUpdate() { // update method
        if (this.x < -this.width/2) { // deletes the blackhole if it exceeds world borders
            this.setActive(false)
            this.setVisible(false)
            this.mainScene.score += this.mainScene.blackholePointAdd // adds score
            this.mainScene.playerScore.text = "Score: " + this.mainScene.score
        }

    }
}
