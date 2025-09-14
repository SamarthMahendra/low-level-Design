from abc import ABC, abstractmethod
import random
from typing import Type


# --- Character Interface ---
class Character(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

    @abstractmethod
    def defend(self) -> str:
        pass


# --- Concrete Characters ---
class Warrior(Character):
    def attack(self) -> str:
        return "⚔️ Warrior attacks with a sword!"

    def defend(self) -> str:
        return "🛡️ Warrior blocks with a shield!"


class Archer(Character):
    def attack(self) -> str:
        return "🏹 Archer shoots an arrow!"

    def defend(self) -> str:
        return "🏃 Archer dodges the attack!"


class Mage(Character):
    def attack(self) -> str:
        return "🔥 Mage casts a fireball!"

    def defend(self) -> str:
        return "✨ Mage conjures a magical barrier!"


class Healer(Character):
    def attack(self) -> str:
        return "🔮 Healer strikes with a staff!"

    def defend(self) -> str:
        return "💊 Healer heals wounds!"


# --- Simple Factory ---
class CharacterFactory:
    _characters: dict[str, Type[Character]] = {
        "warrior": Warrior,
        "mage": Mage,
        "archer": Archer,
        "healer": Healer,
    }

    @staticmethod
    def create_character(character_type: str) -> Character:
        character_type = character_type.lower()
        try:
            return CharacterFactory._characters[character_type]()
        except KeyError:
            raise ValueError(f"Unknown character type: {character_type}")


# --- Bonus: Random Character Factory ---
class RandomCharacterFactory:
    @staticmethod
    def create_random_character() -> Character:
        character_cls = random.choice(list(CharacterFactory._characters.values()))
        return character_cls()


# --- Demo ---
if __name__ == "__main__":
    # Simple factory usage
    hero1 = CharacterFactory.create_character("Warrior")
    hero2 = CharacterFactory.create_character("Mage")

    print(hero1.attack())
    print(hero2.defend())

    # Bonus: Random NPC generation
    print("\nRandom NPCs:")
    for _ in range(3):
        npc = RandomCharacterFactory.create_random_character()
        print(f"{npc.__class__.__name__} -> {npc.attack()}")
