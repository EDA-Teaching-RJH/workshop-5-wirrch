import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
			"shields": 100, 
			"weapons": 100, 
			"engines": 100, 
			"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		use_resource("torpedoes",100)
		display_status() 

		action = get_user_action() 

		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
			print(f"Simulation ended. Final score: {score}")
			break
		else: 
			print("ERROR: Invalid action. Please try again.")
			continue
			
		turns += 1 
		handle_random_event() 

		if turns % 3 == 0: 
			replenish_resources() 

def display_status(): 
	# TODO: Implement function to display ship status, resources, and crew
	print("Current ship status:")

	# first layer of dictionary
	for system, name in ship.items():
		print(f"{system.capitalize()}:")
		# prints each second layer item and its value
		for resource, value in name.items():
			print(f"	{resource.capitalize()} = {value}")
		
def get_user_action(): 
	# TODO: Implement function to get and return user's chosen action 
	print("")

	return input("What do you want to do: ")

def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}")
	new_score = 0

	match mission_type:
		case "Exploration":
			print("Captain's Log: 'The Enterprise has entered an uncharted sector on the edge of the Beta Quadrant. Long-range sensors have detected an anomalous planet, emitting unknown energy signatures. Initial readings suggest the planet has never been explored by any Federation ship.'")
		case "Diplomacy":
			print("Captain's Log: 'The Federation has been called upon to mediate peace talks between Dothran and Velari factions, and I have been tasked with representing Starfleet in these negotiations. Both sides remain deeply entrenched in their positions, but I believe that common ground can be found.'")
		case "Combat":
			print("Captain's Log: 'The Enterprise has been drawn into a confrontation with a hostile fleet. Despite our best efforts to de-escalate the situation, negotiations have failed. We are now preparing for combat.'")
		case "Rescue":
			print("Captain's Log: 'We have received a distress signal from a nearby vessel. Initial scans reveal extensive damage to their hull and life support systems. Time is of the essence.'")
		case "Scientific Research":
			print("Captain's Log: 'The Enterprise is currently in orbit around a rare pulsar. This phenomenon offers a unique opportunity to expand our understanding of subspace physics. The crew is working closely with the research team to gather data from the pulsar’s intense magnetic field. This discovery could redefine our knowledge of stellar evolution.'")

	return new_score

	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

# def repair_system(): 
# 	# TODO: Implement system repair functionality


def add_crew_member():
	# TODO: Implement functionality to add a new crew member
	new_name = input("Enter new crew member's name: ")
	new_role = input("Enter this new member's role: ")
	ship["crew"][new_name] = new_role
	print(f"Welcome aboard the USS Enterprise, {new_name}.")

# def handle_random_event():
# 	# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
 	# TODO: Implement resource usage logic 
	if ship["resources"][resource] >= amount:
		ship["resources"][resource] -= amount
		print(f"{resource} decreased by {amount} ({ship["resources"][resource]} remaining)")
	else:
		print(f"ERROR: You only have {ship["resources"][resource]} {resource} ({amount - ship["resources"][resource]} more needed)")

def replenish_resources(): 
 	# TODO: Implement resource replenishment logic
	ship["resources"]["energy"] = 1000
	ship["resources"]["torpedoes"] = 10
	print("Captain's Log: 'The Enterprise has completed its scheduled systems replenishment. Our energy reserves, replicator supplies, and essential materials have been fully restored, ensuring the ship remains at peak efficiency.'")
	print("(Ship's Energy returned to 1000)")
	print("(Ship's Torpedoes returned to 10)")

main()
