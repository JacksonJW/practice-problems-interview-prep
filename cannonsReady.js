function cannonsReady (gunners) {
	var activeGunners = 0;
	var totalGunners = 0;
	for (var pirate in gunners){
		if(gunners[pirate] === 'aye'){
			activeGunners++;
		}
		totalGunners++;
	}
	
	if (activeGunners === totalGunners) {
		return "Fire!";
	} else{
		return "Shiver me timbers!"
	}
}