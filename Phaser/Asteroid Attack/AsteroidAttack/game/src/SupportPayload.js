export default class SupportPayload extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y){
        super(scene, x, y, 'supportPayloadSheet')
    }

    spawnSupportPayload(y, speed, scale, scene) {
        scene.supportPayloads.add(this)
        this.body.reset(scene.cameras.main.width + 50, y) // spawns payload at right of screen with the random y value
        this.setScale(scale) // scales the payload
        this.setActive(true) // makes payload active
        this.setVisible(true) // makes payload visible
        this.setVelocityX(-speed) // x velocity of payload
        this.setSize(50, 30) // sets hitbox of payload
    }

    preUpdate() { // update method
        if (this.x < -this.width/2) { // deletes the payload if it exceeds world borders            
            this.setActive(false) 
            this.setVisible(false)
        }
    }
}
