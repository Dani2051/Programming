import Blackhole from './Blackhole.js'; // Imports Asteroid class

export default class BlackholeGroup extends Phaser.Physics.Arcade.Group {

    constructor(scene) {
        super(scene.physics.world, scene);

        this.createMultiple ({ // creates multiple instances
            classType: Blackhole, // of asteroid class
            frameQuantity: 7, // max number of sprites at any time
            active: false,
            visible: false,
            key: 'blackholeSheet' // references blackhole image 
        })
    }

    randGeneration(scene) {
        var rnd = Phaser.Math.RND;
        var randomNum = rnd.between(1, 10000); // randomly generates integer
        if (randomNum > 5000) { // if integer is above spawn rate
            let Blackhole = this.getFirstDead(false); // gets first unused blackhole
            if (Blackhole) { // if true
                var minScale = 1;
                var maxScale = 2;
                var ranScale = rnd.between(minScale, maxScale);
                var y = rnd.between(Blackhole.height/2 + scene.barHeight, scene.windowY - Blackhole.height/2); // randomly generates asteroid height within spawn area 
                var speed = rnd.between(100, 700); // randomly generates blackhole speed
                Blackhole.spawnBlackhole(y, speed, ranScale, scene);
            }
        }
    }
}