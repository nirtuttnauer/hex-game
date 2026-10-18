# Hex Game

## Description
The Hex Game is a strategic board game implemented in Python. It involves two players, 'red' and 'blue', who alternately place their colored stones on a hexagonal grid. The objective is for a player to form an unbroken chain of stones between two opposite sides of the board. The game uses advanced data structures, including disjoint sets, to manage game state and determine the winner efficiently.

## Installation

This is a Python 3 project using only the standard library; no third-party packages are required.

To set up the Hex Game on your local machine, follow these steps:

```bash
git clone https://github.com/nirtuttnauer/hex-game.git
cd hex-game
```

## Usage

To play the game, run the main script:

```bash
python3 main.py
```

The default board is 11 × 11. Enter zero-based row and column coordinates separated by a space (for example, `0 0`). Red moves first and connects the top and bottom; blue connects the left and right. Printed cells use `0` for empty, `1` for red, and `2` for blue. Out-of-bounds or occupied cells currently raise an assertion rather than prompting again.

## Contributing

Contributions to the development of the Hex Game are welcome. Please fork the repository and submit a pull request with your enhancements.

## Tests

The project includes a series of tests that ensure the functionality of the game mechanics and the integrity of the game's data structures. Run the tests using:

```bash
python3 -m unittest discover -v
```

## Credits

- Nir Tuttnauer
- Tomer Mizrahi

These contributors have developed the Hex Game, focusing on the use of advanced data structures for efficient gameplay.

## License

No LICENSE file is currently included in this repository; do not assume an MIT license grant.