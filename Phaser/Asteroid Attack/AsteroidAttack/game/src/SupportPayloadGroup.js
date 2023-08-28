import SupportPayload from './SupportPayload.js' // Imports Asteroid class

export default class SupportPayloadGroup extends Phaser.Physics.Arcade.Group {

    constructor(scene) {
        super(scene.physics.world, scene)

        this.createMultiple ({ // creates multiple instances
            classType: SupportPayload, // of asteroid class
            frameQuantity: 1, // max number of sprites at any time
            active: false,
            visible: false,
            key: 'supportPayloadSheet' // references payload image 
        })
    }

    randGeneration(scene) {
        let rnd = Phaser.Math.RND
        let randomNum = rnd.between(1, 1000000) // randomly generates integer
        if (randomNum < 2) { // if integer is above spawn rate
            let SupportPayload = this.getFirstDead(false) // gets first unused payload
            if (SupportPayload) { // if true
                let minScale = 2
                let maxScale = 5
                let ranScale = rnd.between(minScale, maxScale)
                let y = rnd.between(SupportPayload.height/2 + scene.barHeight, scene.windowY - SupportPayload.height/2) // randomly generates asteroid height within spawn area 
                let speed = rnd.between(100, 700) // randomly generates payload speed

                SupportPayload.spawnSupportPayload(y, speed, ranScale, scene)
            }
        }
    }
}