import Bullet from './Bullet.js' // Imports Bullet class

export default class BulletGroup extends Phaser.Physics.Arcade.Group {

    constructor(scene) {
        super(scene.physics.world, scene)

        this.createMultiple ({ // creates multiple instances
            classType: Bullet, // of bullet class
            frameQuantity: 15, // creates 300 bullets and stores them for later use 
            active: false,
            visible: false,
            key: 'bulletIMG' // references bullet image 
        })
    }

    fire(scene, x, y) {
        let Bullet = this.getFirstDead(false) // gets first unused bullet
        if (Bullet) { // if true
            Bullet.fire(x, y, scene)  
        }
    }
}
