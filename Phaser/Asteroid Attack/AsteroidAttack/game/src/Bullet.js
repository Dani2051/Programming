export default class Bullet extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y){
        super(scene, x, y, 'bulletIMG')
        this.mainScene = scene 
    }

    fire(x, y, scene) {
        scene.bullets.add(this)
        this.body.reset(x + this.width, y) // makes bullets x and y value where the spaceship is
        this.setScale(2)
        this.setActive(true) // makes bullet active
        this.setVisible(true) // makes bullet visible
        this.setVelocityX(1000) // x velocity of bullet
    }   

    preUpdate() { // update method 
        if (this.x >= this.mainScene.windowX + this.width/2) { // deletes the bullet if it exceeds world borders
            this.setActive(false) 
            this.setVisible(false)
        }
    }
}