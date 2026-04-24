---
lesson: 20
tags: [web, project, quiz, javascript, dom, events, state]
summary: Complete project — build an interactive Quiz application with JavaScript, with instant feedback and final score.
---

# Lesson 20 · Project: Quiz Application

!!! tip "What you'll practice"
    - DOM manipulation (dynamic button creation, text changes)
    - Events (click on buttons)
    - Arrays of objects (the quiz questions)
    - State management (current question index, score)
    - `setTimeout` for short pauses

---

## Project overview

You will build a **general knowledge Quiz application** with 6 questions. For each:

- The prompt and 4 options are displayed (as buttons)
- On click: the correct button turns **green**, the wrong one **red**
- After 1 second, we move on to the next question
- At the end: the score and a "Restart" button

**Sample run:**

```
┌──────────────────────────────────────┐
│   General knowledge quiz             │
├──────────────────────────────────────┤
│   Question 2 of 6                    │
│                                      │
│   Which planet is called             │
│   the Red Planet?                    │
│                                      │
│   [ Mars       ]   ← clicked (green) │
│   [ Venus      ]                     │
│   [ Jupiter    ]                     │
│   [ Saturn     ]                     │
└──────────────────────────────────────┘

... after 6 questions ...

┌──────────────────────────────────────┐
│   You answered 5 / 6 correctly.      │
│   Congratulations!                   │
│                                      │
│          [ Restart ]                 │
└──────────────────────────────────────┘
```

---

## Step 1: HTML structure

Create `quiz/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz · General knowledge</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="quiz">
    <h1>General knowledge quiz</h1>

    <p id="progress" class="progress">Question 1 of 6</p>
    <h2 id="question" class="question"></h2>

    <div id="options" class="options"></div>

    <section id="final" class="final hidden">
      <p id="score"></p>
      <p id="message"></p>
      <button id="restart" class="btn">Restart</button>
    </section>
  </main>

  <script src="quiz.js"></script>
</body>
</html>
```

!!! note "ID strategy"
    We use `id` for the elements that JavaScript needs to update: `progress`, `question`, `options`, `final`, `score`, `message`, `restart`. The other elements are styled only with classes.

---

## Step 2: CSS

Create `quiz/styles.css`:

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --primary: #6366f1;
  --correct: #22c55e;
  --wrong: #ef4444;
  --background: #0f172a;
  --card: #1e293b;
  --text: #e2e8f0;
  --text-soft: #94a3b8;
  --radius: 12px;
}

body {
  font-family: "Inter", system-ui, sans-serif;
  background: var(--background);
  color: var(--text);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.quiz {
  max-width: 600px;
  width: 100%;
  background: var(--card);
  padding: 2.5rem 2rem;
  border-radius: 18px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
  animation: appear 0.4s ease;
}

@keyframes appear {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

.quiz h1 {
  font-size: 1.5rem;
  text-align: center;
  margin-bottom: 0.5rem;
}

.progress {
  text-align: center;
  color: var(--text-soft);
  font-size: 0.9rem;
  margin-bottom: 2rem;
}

.question {
  font-size: 1.35rem;
  line-height: 1.4;
  margin-bottom: 1.75rem;
  min-height: 3.5em;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option {
  padding: 0.9rem 1.25rem;
  background: transparent;
  color: var(--text);
  border: 2px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius);
  font-size: 1rem;
  font-family: inherit;
  text-align: left;
  cursor: pointer;
  transition: background 0.2s ease, border-color 0.2s ease, transform 0.2s ease;
}

.option:hover:not(:disabled) {
  border-color: var(--primary);
  transform: translateX(4px);
}

.option:disabled { cursor: not-allowed; opacity: 0.7; }
.option.correct  { background: var(--correct); border-color: var(--correct); color: white; }
.option.wrong    { background: var(--wrong); border-color: var(--wrong); color: white; }

.final { text-align: center; margin-top: 1rem; }
.final p { margin-bottom: 1rem; }
.final p:first-child { font-size: 1.5rem; font-weight: 700; }

.btn {
  padding: 0.75rem 2rem;
  background: var(--primary);
  color: white;
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.btn:hover { transform: translateY(-2px); }

.hidden { display: none; }
```

---

## Step 3: The quiz data

In `quiz/quiz.js`, we define the questions as an **array of objects**:

```js
const questions = [
  {
    text: "Which planet is called the Red Planet?",
    options: ["Mars", "Venus", "Jupiter", "Saturn"],
    correct: 0
  },
  {
    text: "How much is 7 × 8?",
    options: ["54", "56", "58", "64"],
    correct: 1
  },
  {
    text: "Who wrote 'Hamlet'?",
    options: ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"],
    correct: 2
  },
  {
    text: "Which planet is closest to the Sun?",
    options: ["Venus", "Earth", "Mars", "Mercury"],
    correct: 3
  },
  {
    text: "What is the largest ocean on Earth?",
    options: ["Pacific", "Atlantic", "Indian", "Arctic"],
    correct: 0
  },
  {
    text: "Which language runs in the browser?",
    options: ["Python", "JavaScript", "Java", "C++"],
    correct: 1
  }
];
```

!!! tip "Indexing from 0"
    In programming, the first element in `options` has index `0`, the second `1`, etc. If the correct answer is the third option, `correct: 2`.

---

## Step 4: The application state

The state is **the data that changes over time** as the player progresses:

```js
let currentIndex = 0;  // which question we show (0..n-1)
let score = 0;         // how many correct answers the player has
```

We also grab the references to the DOM elements once:

```js
const progressEl = document.getElementById("progress");
const questionEl = document.getElementById("question");
const optionsEl  = document.getElementById("options");
const finalEl    = document.getElementById("final");
const scoreEl    = document.getElementById("score");
const messageEl  = document.getElementById("message");
const restartEl  = document.getElementById("restart");
```

---

## Step 5: The `showQuestion()` function

Show the current question and create the buttons for the options:

```js
function showQuestion() {
  const question = questions[currentIndex];

  progressEl.textContent = `Question ${currentIndex + 1} of ${questions.length}`;
  questionEl.textContent = question.text;

  optionsEl.innerHTML = "";  // clear the old buttons

  question.options.forEach((opt, i) => {
    const btn = document.createElement("button");
    btn.className = "option";
    btn.textContent = opt;
    btn.addEventListener("click", () => check(i, btn));
    optionsEl.appendChild(btn);
  });
}
```

!!! note "Closure on `i`"
    Each button "remembers" its own `i` thanks to the arrow function `() => check(i, btn)`. When the user presses the button, the exact index of the pressed option is sent.

---

## Step 6: Checking the answer

We compare the pressed index with `correct` and color the buttons:

```js
function check(pressedIndex, pressedButton) {
  const question = questions[currentIndex];
  const buttons = optionsEl.querySelectorAll(".option");

  // Disable all buttons
  buttons.forEach(b => b.disabled = true);

  if (pressedIndex === question.correct) {
    pressedButton.classList.add("correct");
    score++;
  } else {
    pressedButton.classList.add("wrong");
    // Also show the correct answer
    buttons[question.correct].classList.add("correct");
  }

  // After 1 second, move to the next
  setTimeout(next, 1000);
}
```

---

## Step 7: The end of the quiz

The `next()` function decides if there are more questions or we show the score:

```js
function next() {
  currentIndex++;

  if (currentIndex < questions.length) {
    showQuestion();
  } else {
    showScore();
  }
}

function showScore() {
  questionEl.classList.add("hidden");
  optionsEl.classList.add("hidden");
  progressEl.classList.add("hidden");

  finalEl.classList.remove("hidden");
  scoreEl.textContent = `You answered ${score} out of ${questions.length} correctly.`;

  const percent = (score / questions.length) * 100;
  if (percent === 100)      messageEl.textContent = "Perfect! You're an expert.";
  else if (percent >= 75)   messageEl.textContent = "Very good! Just a few details to work on.";
  else if (percent >= 50)   messageEl.textContent = "Good start. Keep practicing!";
  else                      messageEl.textContent = "Don't give up — try again!";
}
```

---

## Step 8: Restart

The "Restart" button resets the state and restarts the quiz:

```js
restartEl.addEventListener("click", () => {
  currentIndex = 0;
  score = 0;

  questionEl.classList.remove("hidden");
  optionsEl.classList.remove("hidden");
  progressEl.classList.remove("hidden");
  finalEl.classList.add("hidden");

  showQuestion();
});
```

At the end, we start the quiz:

```js
showQuestion();
```

---

## Complete code

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quiz · General knowledge</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <main class="quiz">
    <h1>General knowledge quiz</h1>
    <p id="progress" class="progress">Question 1 of 6</p>
    <h2 id="question" class="question"></h2>
    <div id="options" class="options"></div>

    <section id="final" class="final hidden">
      <p id="score"></p>
      <p id="message"></p>
      <button id="restart" class="btn">Restart</button>
    </section>
  </main>

  <script src="quiz.js"></script>
</body>
</html>
```

### `styles.css`

(use the full CSS from Step 2)

### `quiz.js`

```js
const questions = [
  { text: "Which planet is called the Red Planet?",
    options: ["Mars", "Venus", "Jupiter", "Saturn"], correct: 0 },
  { text: "How much is 7 × 8?",
    options: ["54", "56", "58", "64"], correct: 1 },
  { text: "Who wrote 'Hamlet'?",
    options: ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], correct: 2 },
  { text: "Which planet is closest to the Sun?",
    options: ["Venus", "Earth", "Mars", "Mercury"], correct: 3 },
  { text: "What is the largest ocean on Earth?",
    options: ["Pacific", "Atlantic", "Indian", "Arctic"], correct: 0 },
  { text: "Which language runs in the browser?",
    options: ["Python", "JavaScript", "Java", "C++"], correct: 1 }
];

let currentIndex = 0;
let score = 0;

const progressEl = document.getElementById("progress");
const questionEl = document.getElementById("question");
const optionsEl  = document.getElementById("options");
const finalEl    = document.getElementById("final");
const scoreEl    = document.getElementById("score");
const messageEl  = document.getElementById("message");
const restartEl  = document.getElementById("restart");

function showQuestion() {
  const question = questions[currentIndex];
  progressEl.textContent = `Question ${currentIndex + 1} of ${questions.length}`;
  questionEl.textContent = question.text;
  optionsEl.innerHTML = "";

  question.options.forEach((opt, i) => {
    const btn = document.createElement("button");
    btn.className = "option";
    btn.textContent = opt;
    btn.addEventListener("click", () => check(i, btn));
    optionsEl.appendChild(btn);
  });
}

function check(pressedIndex, pressedButton) {
  const question = questions[currentIndex];
  const buttons = optionsEl.querySelectorAll(".option");
  buttons.forEach(b => b.disabled = true);

  if (pressedIndex === question.correct) {
    pressedButton.classList.add("correct");
    score++;
  } else {
    pressedButton.classList.add("wrong");
    buttons[question.correct].classList.add("correct");
  }

  setTimeout(next, 1000);
}

function next() {
  currentIndex++;
  if (currentIndex < questions.length) {
    showQuestion();
  } else {
    showScore();
  }
}

function showScore() {
  questionEl.classList.add("hidden");
  optionsEl.classList.add("hidden");
  progressEl.classList.add("hidden");
  finalEl.classList.remove("hidden");

  scoreEl.textContent = `You answered ${score} out of ${questions.length} correctly.`;
  const percent = (score / questions.length) * 100;

  if (percent === 100)    messageEl.textContent = "Perfect! You're an expert.";
  else if (percent >= 75) messageEl.textContent = "Very good! Just a few details to work on.";
  else if (percent >= 50) messageEl.textContent = "Good start. Keep practicing!";
  else                    messageEl.textContent = "Don't give up — try again!";
}

restartEl.addEventListener("click", () => {
  currentIndex = 0;
  score = 0;
  questionEl.classList.remove("hidden");
  optionsEl.classList.remove("hidden");
  progressEl.classList.remove("hidden");
  finalEl.classList.add("hidden");
  showQuestion();
});

showQuestion();
```

---

## Ideas to extend

1. **Shuffle questions and options** with the Fisher–Yates algorithm for variety on each replay.
2. **Timer per question** — 10 seconds; if it expires, automatically mark the answer as wrong.
3. **Categories** — an initial menu: "Geography", "History", "Math", "Technology". Each category has its own array of questions.
4. **Saved score** — `localStorage.setItem("highScore", score)` to keep the best result between sessions.
5. **Leaderboard** — input for name at the end, the top players' scores stored in `localStorage`.
6. **Multi-answer questions** — add `correct: [0, 2]` for questions with multiple correct options.
7. **Sound** — a short *ding* on correct answer, *buzz* on wrong (with `new Audio()`).

---

## Summary

You've learned how to:

- Model the data of a quiz with an **array of objects**
- Generate buttons **dynamically** with `createElement` and `appendChild`
- Manage the state (current question, score) with module-level variables
- Provide visual feedback through CSS classes (`correct`, `wrong`)
- Use `setTimeout` for pauses between steps

---

**Next step:** [→ Project: Weather Application](21-proiect-meteo.md)
