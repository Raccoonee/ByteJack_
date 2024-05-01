export const numChecker = (num) => {
  if (num.length > 2) return num.substring(0, 2);
  else return num.substring(0, 1);
};

export const suitChecker = (suit) => {
  if (suit === "♠") {
    return "spades";
  } else if (suit === "♥") {
    return "hearts";
  } else if (suit === "♦") {
    return "diams";
  } else if (suit === "♣") {
    return "clubs";
  }
};

export const cardCount = (cards = []) => {
    let total = 0;
    let value;
    let aceCounter = 0;

    for (let i = 0; i < cards.length; i++) {
      if (
        cards[i].substring(0, 1) === "J" ||
        cards[i].substring(0, 1) === "Q" ||
        cards[i].substring(0, 1) === "K"
      ) {
        value = 10;
      } else if (cards[i].substring(0, 1) === "A") {
        value = 11;
        aceCounter++;
      } else {
        value = parseInt(cards[i]);
      }

      total += value;
    }

    for (let i = 0; i < aceCounter; i++) {
      if (total > 21) {
        total -= 10;
      }
    }

    return total;
  };