// Description:

// Create a function that returns the
// name of the winner in a fight 
// between two fighters.

// Each fighter takes turns attacking
// the other and whoever kills the 
// other first is victorious. Death
// is defined as having health <= 0.

// Each fighter will be a Fighter 
// object/instance. See the Fighter 
// class below in your chosen 
// language.

// Both health and damagePerAttack
// (damage_per_attack for python) 
// will be integers larger than 0.
// You can mutate the Fighter objects.

// Javascript

function Fighter(name, health, damagePerAttack) {
        this.name = name;
        this.health = health;
        this.damagePerAttack = damagePerAttack;
        this.toString = function() { return this.name; }
}

// Ex. 
//  declareWinner(new Fighter("Lew", 10, 2), new Fighter("Harry", 5, 4), "Lew") => "Lew"

//   Lew attacks Harry; Harry now has 3 health.
//   Harry attacks Lew; Lew now has 6 health.
//   Lew attacks Harry; Harry now has 1 health.
//   Harry attacks Lew; Lew now has 2 health.
//   Lew attacks Harry: Harry now has -1 health
//    and is dead. Lew wins.

function declareWinner(fighter1, fighter2, firstAttacker) {
	if (firstAttacker === fighter1.name){
		while(fighter2.health > 0 && fighter1.health > 0){
			fighter2.health = fighter2.health - fighter1.damagePerAttack;
			
			if (fighter2.health <= 0){
				break;
			}

			fighter1.health = fighter1.health - fighter2.damagePerAttack;
		}
	} else {
		while(fighter2.health > 0 && fighter1.health > 0){
			fighter1.health -= fighter2.damagePerAttack;

			if (fighter1.health <= 0){
				break;
			}

			fighter2.health -= fighter1.damagePerAttack;
		}
	}

	if (fighter1.health > 0){
		return fighter1.name;
	} else{
		return fighter2.name;
	}
}