"""
Olympian Siege Game - A Python game featuring Olympian gods and siege mechanics
"""

import random
from dataclasses import dataclass
from typing import List, Dict, Optional


# ANSI Color codes for terminal output
class Colors:
    """ANSI color codes for terminal text styling"""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    
    # Foreground colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    
    # Background colors
    BG_RED = "\033[101m"
    BG_GREEN = "\033[102m"
    BG_YELLOW = "\033[103m"
    BG_BLUE = "\033[104m"


@dataclass
class Olympian:
    """Represents an Olympian god/goddess"""
    name: str
    health: int
    attack_power: int
    special_ability: str
    
    def take_damage(self, damage: int) -> None:
        """Reduce health by damage amount"""
        self.health = max(0, self.health - damage)
    
    def is_alive(self) -> bool:
        """Check if Olympian is still alive"""
        return self.health > 0
    
    def special_attack(self) -> int:
        """Perform special ability attack with bonus damage"""
        bonus = random.randint(10, 20)
        return self.attack_power + bonus


@dataclass
class Fortress:
    """Represents a fortress being sieged"""
    name: str
    defense: int
    resources: int
    garrison_size: int
    
    def take_siege_damage(self, damage: int) -> None:
        """Reduce fortress defense"""
        self.defense = max(0, self.defense - damage)
    
    def is_standing(self) -> bool:
        """Check if fortress is still standing"""
        return self.defense > 0


class OlympianSiegeGame:
    """Main game class for Olympian Siege"""
    
    def __init__(self):
        """Initialize the game"""
        self.olympians: Dict[str, Olympian] = {}
        self.fortresses: Dict[str, Fortress] = {}
        self.turn_count = 0
        self.setup_olympians()
        self.setup_fortresses()
    
    def setup_olympians(self) -> None:
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
    
    def setup_fortresses(self) -> None:
        """Create fortress structures"""
        fortresses_data = [
            ("Troy", 150, 500, 100),
            ("Sparta", 120, 800, 150),
            ("Athens", 100, 600, 80),
            ("Olympus", 200, 1000, 200),
        ]
        
        for name, defense, resources, garrison in fortresses_data:
            self.fortresses[name] = Fortress(name, defense, resources, garrison)
    
    def attack(self, attacker_name: str, defender_name: str, 
               target_fortress: Optional[str] = None) -> str:
        """Perform an attack with color-coded output"""
        if attacker_name not in self.olympians:
            return f"{Colors.RED}Attacker {attacker_name} not found!{Colors.RESET}"
        
        attacker = self.olympians[attacker_name]
        
        if not attacker.is_alive():
            return f"{Colors.RED}{attacker_name} is defeated and cannot attack!{Colors.RESET}"
        
        if target_fortress:
            if target_fortress not in self.fortresses:
                return f"{Colors.RED}Fortress {target_fortress} not found!{Colors.RESET}"
            
            fortress = self.fortresses[target_fortress]
            damage = attacker.special_attack()
            fortress.take_siege_damage(damage)
            
            # Color-code the attack message
            result = f"{Colors.CYAN}⚡ {attacker_name} uses {attacker.special_ability} on {target_fortress}{Colors.RESET} "
            result += f"dealing {Colors.YELLOW}{Colors.BOLD}{damage} damage{Colors.RESET}!\n"
            result += f"🏰 Fortress defense now: {fortress.defense}"
            
            if not fortress.is_standing():
                result += f" {Colors.GREEN}{Colors.BOLD}→ 🎉 {target_fortress} has been conquered!{Colors.RESET}"
            
            return result
        else:
            if defender_name not in self.olympians:
                return f"{Colors.RED}Defender {defender_name} not found!{Colors.RESET}"
            
            defender = self.olympians[defender_name]
            
            if not defender.is_alive():
                return f"{Colors.RED}{defender_name} is already defeated!{Colors.RESET}"
            
            damage = attacker.special_attack()
            defender.take_damage(damage)
            
            # Color-code the duel message
            result = f"{Colors.MAGENTA}⚔️ {attacker_name} targets {defender_name} with {attacker.special_ability}{Colors.RESET} "
            result += f"for {Colors.RED}{Colors.BOLD}{damage} damage{Colors.RESET}!\n"
            result += f"❤️ {defender_name}'s health: {defender.health}"
            
            if not defender.is_alive():
                result += f" {Colors.RED}{Colors.BOLD}→ 💀 {defender_name} has been defeated!{Colors.RESET}"
            
            return result
    
    def get_status(self) -> str:
        """Get current game status with color coding"""
        status = f"\n{Colors.BOLD}=== Turn {self.turn_count} ==={Colors.RESET}" \
                 f"\n\n{Colors.BLUE}{Colors.BOLD}--- Olympians ---{Colors.RESET}\n"
        
        for name, olympian in self.olympians.items():
            status += f"{name}: HP {olympian.health} "
            if olympian.is_alive():
                status += f"{Colors.GREEN}✓{Colors.RESET}\n"
            else:
                status += f"{Colors.RED}✗ DEFEATED{Colors.RESET}\n"
        
        status += f"\n{Colors.BLUE}{Colors.BOLD}--- Fortresses ---{Colors.RESET}\n"
        
        for name, fortress in self.fortresses.items():
            status += f"{name}: Defense {fortress.defense} "
            if fortress.is_standing():
                status += f"{Colors.GREEN}✓{Colors.RESET}\n"
            else:
                status += f"{Colors.RED}✗ CONQUERED{Colors.RESET}\n"
        
        return status
    
    def next_turn(self) -> None:
        """Advance to next turn"""
        self.turn_count += 1


def main():
    """Main game loop"""
    game = OlympianSiegeGame()
    
    print(f"{Colors.BOLD}{Colors.CYAN}=== Welcome to Olympian Siege ==={Colors.RESET}\n")
    print(game.get_status())
    
    # Example game sequence
    actions = [
        ("Zeus", None, "Troy"),
        ("Ares", None, "Troy"),
        ("Athena", "Ares", None),
        ("Poseidon", None, "Sparta"),
    ]
    
    for action in actions:
        game.next_turn()
        attacker, defender, fortress = action
        result = game.attack(attacker, defender, fortress)
        print(f"\n{result}")
        print(game.get_status())
        
        # Check if game is over
        alive_olympians = sum(1 for o in game.olympians.values() if o.is_alive())
        standing_fortresses = sum(1 for f in game.fortresses.values() if f.is_standing())
        
        if alive_olympians == 0 or standing_fortresses == 0:
            print(f"\n{Colors.BOLD}{Colors.RED}=== Game Over ==={Colors.RESET}")
            break


if __name__ == "__main__":
    main()
