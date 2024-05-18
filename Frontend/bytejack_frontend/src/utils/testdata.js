export const testData = {
    gameID: 12345,
    playerTurn: "player1",
    dealer: { hand: ["K♠", "2♣", "3♦"] },
    winners: ["player1", "player2"],
    players: {
      player1: {
        name: "Jeremiah",
        chips: 100,
        hand: ["A♥", "A♦", "A♠", "2♣"],
        bet: 10,
      },
      player2: { name: "Joe", chips: 100, hand: ["K♠", "10♥"], bet: 10 },
      player3: { name: "Bob", chips: 100, hand: ["K♠", "8♥"], bet: 10 },
      player4: { name: "John", chips: 100, hand: ["Q♠", "9♥"], bet: 10 },
      player5: { name: "Matt", chips: 100, hand: ["K♠", "A♥"], bet: 10 },
    },
  };