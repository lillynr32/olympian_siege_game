"""
Olympian Siege Game - Flask Server
Run with: python3 app.py
Then open http://localhost:5000 in your browser
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random
import json

app = Flask(__name__)
CORS(app)

class Olympian:
    """Represents an Olympian god/goddess"""
    def __init__(self, name, health, attack_power, special_ability):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.special_ability = special_ability
    
    def take_damage(self, damage):
        """Reduce health by damage amount"""
        self.health = max(0, self.health - damage)
    
    def is_alive(self):
        """Check if Olympian is still alive"""
        return self.health > 0
    
    def special_attack(self):
        """Perform special ability attack with bonus damage"""
        bonus = random.randint(10, 20)
        return self.attack_power + bonus
    
    def to_dict(self):
        """Convert to dictionary for JSON"""
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "attack_power": self.attack_power,
            "special_ability": self.special_ability,
            "is_alive": self.is_alive()
        }


class Fortress:
    """Represents a fortress being sieged"""
    def __init__(self, name, defense, resources, garrison_size):
        self.name = name
        self.defense = defense
        self.max_defense = defense
        self.resources = resources
        self.garrison_size = garrison_size
    
    def take_siege_damage(self, damage):
        """Reduce fortress defense"""
        self.defense = max(0, self.defense - damage)
    
    def is_standing(self):
        """Check if fortress is still standing"""
        return self.defense > 0
    
    def to_dict(self):
        """Convert to dictionary for JSON"""
        return {
            "name": self.name,
            "defense": self.defense,
            "max_defense": self.max_defense,
            "resources": self.resources,
            "garrison_size": self.garrison_size,
            "is_standing": self.is_standing()
        }


class OlympianSiegeGame:
    """Main game class for Olympian Siege"""
    
    def __init__(self):
        """Initialize the game"""
        self.olympians = {}
        self.fortresses = {}
        self.turn_count = 0
        self.game_over = False
        self.winner = None
        self.battle_log = []
        self.setup_olympians()
        self.setup_fortresses()
    
    def setup_olympians(self):
        """Create Olympian characters"""
        olympians_data = [
            ("Zeus", 100, 25, "Lightning Strike"),
            ("Athena", 85, 20, "Strategic Defense"),
            ("Ares", 90, 28, "War Fury"),
            ("Poseidon", 95, 22, "Tidal Wave"),
            ("Aphrodite", 70, 15, "Charm Spell"),
            ("Apollo", 80, 18, "Solar Beam"),
        ]
        
        for name, health, attack, ability in olympians_data:
            self.olympians[name] = Olympian(name, health, attack, ability)
    
    def setup_fortresses(self):
        """Create fortress structures"""
        fortresses_data = [
            ("Troy", 150, 500, 100),
            ("Sparta", 120, 800, 150),
            ("Athens", 100, 600, 80),
            ("Olympus", 200, 1000, 200),
        ]
        
        for name, defense, resources, garrison in fortresses_data:
            self.fortresses[name] = Fortress(name, defense, resources, garrison)
    
    def attack(self, attacker_name, defender_name=None, target_fortress=None):
        """Perform an attack"""
        if attacker_name not in self.olympians:
            return {"success": False, "message": f"Attacker {attacker_name} not found!"}
        
        attacker = self.olympians[attacker_name]
        
        if not attacker.is_alive():
            return {"success": False, "message": f"{attacker_name} is defeated and cannot attack!"}
        
        if target_fortress:
            if target_fortress not in self.fortresses:
                return {"success": False, "message": f"Fortress {target_fortress} not found!"}
            
            fortress = self.fortresses[target_fortress]
            if not fortress.is_standing():
                return {"success": False, "message": f"{target_fortress} is already conquered!"}
            
            damage = attacker.special_attack()
            fortress.take_siege_damage(damage)
            
            log_message = f"⚔️ {attacker_name} uses {attacker.special_ability} on {target_fortress} for {damage} damage! (Defense: {fortress.defense}/{fortress.max_defense})"
            
            if not fortress.is_standing():
                log_message += f" - 🏛️ {target_fortress} CONQUERED!"
            
            self.battle_log.append(log_message)
            
            return {
                "success": True,
                "message": log_message,
                "damage": damage,
                "target_type": "fortress"
            }
        
        else:
            if defender_name not in self.olympians:
                return {"success": False, "message": f"Defender {defender_name} not found!"}
            
            defender = self.olympians[defender_name]
            
            if not defender.is_alive():
                return {"success": False, "message": f"{defender_name} is already defeated!"}
            
            damage = attacker.special_attack()
            defender.take_damage(damage)
            
            log_message = f"⚔️ {attacker_name} uses {attacker.special_ability} on {defender_name} for {damage} damage! (HP: {defender.health}/{defender.max_health})"
            
            if not defender.is_alive():
                log_message += f" - ☠️ {defender_name} DEFEATED!"
            
            self.battle_log.append(log_message)
            
            return {
                "success": True,
                "message": log_message,
                "damage": damage,
                "target_type": "olympian"
            }
    
    def get_status(self):
        """Get current game status"""
        olympians_status = {name: olympian.to_dict() for name, olympian in self.olympians.items()}
        fortresses_status = {name: fortress.to_dict() for name, fortress in self.fortresses.items()}
        
        return {
            "turn": self.turn_count,
            "olympians": olympians_status,
            "fortresses": fortresses_status,
            "game_over": self.game_over,
            "winner": self.winner,
            "battle_log": self.battle_log[-5:]  # Last 5 messages
        }
    
    def next_turn(self):
        """Advance to next turn"""
        self.turn_count += 1
    
    def check_win_condition(self):
        """Check if game is over"""
        alive_olympians = sum(1 for o in self.olympians.values() if o.is_alive())
        standing_fortresses = sum(1 for f in self.fortresses.values() if f.is_standing())
        
        if alive_olympians == 0:
            self.game_over = True
            self.winner = "Fortresses"
            self.battle_log.append("🏰 FORTRESSES WIN! The Gods Have Fallen!")
            return True
        elif standing_fortresses == 0:
            self.game_over = True
            self.winner = "Olympians"
            self.battle_log.append("⚡ OLYMPIANS WIN! All Fortresses Conquered!")
            return True
        
        return False


# Global game instance
game = OlympianSiegeGame()


@app.route('/')
def index():
    """Serve the game page"""
    return render_template('index.html')


@app.route('/api/status')
def get_status():
    """Get current game status"""
    return jsonify(game.get_status())


@app.route('/api/attack', methods=['POST'])
def perform_attack():
    """Perform an attack"""
    data = request.json
    attacker = data.get('attacker')
    defender = data.get('defender')
    fortress = data.get('fortress')
    target_type = data.get('target_type')
    
    if not attacker or (not defender and not fortress):
        return jsonify({"success": False, "message": "Missing required parameters"}), 400
    
    # Perform attack
    result = game.attack(attacker, defender_name=defender, target_fortress=fortress)
    
    if result['success']:
        game.next_turn()
        game.check_win_condition()
    
    return jsonify({**result, "status": game.get_status()})


@app.route('/api/targets')
def get_targets():
    """Get available targets for attack"""
    alive_olympians = [name for name, o in game.olympians.items() if o.is_alive()]
    standing_fortresses = [name for name, f in game.fortresses.items() if f.is_standing()]
    
    return jsonify({
        "olympians": alive_olympians,
        "fortresses": standing_fortresses
    })


@app.route('/api/restart', methods=['POST'])
def restart_game():
    """Restart the game"""
    global game
    game = OlympianSiegeGame()
    return jsonify(game.get_status())


if __name__ == '__main__':
    print("🎮 Olympian Siege Game Server")
    print("📍 Open your browser and go to: http://localhost:5000")
    print("⚡ Enjoy the game!")
    app.run(debug=True, host='0.0.0.0', port=5000)
