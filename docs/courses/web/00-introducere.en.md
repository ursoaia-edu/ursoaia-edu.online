---
lesson: 0
tags: [web, internet, http, browser, devtools, client-server]
summary: How the web works, the difference between Internet and Web, the role of the browser, and the tools you'll use.
---

# Lesson 00 · How the web works

!!! tip "What you'll learn"
    - The difference between **the Internet** and **the Web**
    - The **client-server** model and what happens when you open a site
    - The **3 languages** of the web: HTML, CSS, JavaScript
    - Your toolkit: **VS Code**, **Live Server**, **DevTools**
    - How to inspect any web page with `F12`

---

## The Internet vs. the Web

Many people use the words "Internet" and "Web" as if they were the same thing. **They are not.**

- **The Internet** is the global physical network of cables, routers, antennas and servers that connects billions of computers.
- **The Web** (World Wide Web) is the **information layer** built on top of the Internet — the sites, pages, images, and videos you see in the browser.

!!! note "Analogy"
    **The Internet = the highway.** The cables and routers are the asphalt and signs.

    **The Web = the cars driving** on it. The page you're reading right now is a "car" that reached you via the highway.

    Other things travel on the Internet too: e-mail, online games, video calls, app updates. The Web is just **one type** of traffic.

---

## The client-server model

Every web page you open involves **two parties** communicating:

```
[CLIENT]                            [SERVER]
Chrome / Firefox / Edge       A powerful computer
(your computer)               (e.g. Google's servers)

      |   1. Request                     |
      |   GET /index.html                |
      |  ------------------------------> |
      |                                  |
      |   2. Response                    |
      |   200 OK + HTML code             |
      |  <------------------------------ |
      |                                  |
      v                                  v
   Display the page              Forward to others
```

- **The client** asks for a resource (a page, an image, a video).
- **The server** responds with that resource (or with an error if it doesn't exist).

Your browser is a client. Google, YouTube, Wikipedia run on servers.

---

## The HTTP request in a nutshell

The language clients and servers speak is called **HTTP** (HyperText Transfer Protocol). When you type an address and press Enter, this happens (simplified):

1. The browser builds a **request**: "Give me page `/` on `ursoaia-edu.online`".
2. The server replies with a **status code** and the page content.

Codes you'll meet often:

| Code | What it means |
|------|---------------|
| `200 OK` | Everything is fine, here's the page |
| `301` / `302` | Redirect — the page has moved |
| `404 Not Found` | The requested page doesn't exist |
| `500 Internal Server Error` | The server has a problem |

!!! note "HTTPS"
    The **secure** version is **HTTPS** — communication is encrypted. In the browser bar you'll see a **padlock**. All modern websites use HTTPS.

---

## What does the browser do?

When the browser receives a page, it has essentially **3 jobs**:

1. **Reads the HTML** (parses it) and builds a tree-like structure (DOM).
2. **Applies CSS** so the page looks nice (colors, fonts, positions).
3. **Executes JavaScript** to make the page interactive (buttons, animations, dynamic data).

Without a browser, HTML is just a text file. The browser is the "engine" that turns it into what you see.

---

## The 3 languages of the web

Every modern site rests on three pillars:

| Language | Role | Analogy |
|----------|------|---------|
| **HTML** | The structure and content of the page | The skeleton |
| **CSS**  | The look: colors, fonts, layout | The clothes |
| **JavaScript** | The behavior: interactivity | The movements |

!!! tip "One at a time"
    In lessons 01-05 we learn **HTML**, in 06-10 we learn **CSS**, then we move to **JavaScript**. Don't try to learn them all at once — each has its own way of thinking.

---

## Our tools

### 1. Code editor: VS Code

[Visual Studio Code](https://code.visualstudio.com/) is a free, fast editor used in the industry. Download and install it.

After installing, install **a single essential extension** to start with:

- **Live Server** (author: Ritwick Dey) — starts a tiny local server and **automatically refreshes** your page when you save the file.

### 2. Browser: Chrome or Firefox

Any modern browser will do. We recommend **Chrome** or **Firefox** because they have powerful DevTools. Avoid Internet Explorer — it's officially abandoned.

### 3. DevTools (the developer's tools)

The most important shortcut in the entire course:

```
F12
```

(or `Ctrl+Shift+I` on Windows / `Cmd+Opt+I` on Mac)

A panel opens with several tabs. The ones we care about now:

- **Elements** — the HTML tree of the current page. You can temporarily edit any element (only on your machine — nobody else sees the change).
- **Console** — you can type JavaScript commands and see the page's messages.
- **Network** — shows every HTTP request (HTML, images, CSS, JS) the page makes.

!!! warning "DevTools changes are local"
    Anything you change in the Elements tab disappears on refresh. You're not modifying the original site — only what **you** see in **your** browser.

---

## Your first experiment

1. Open **[google.com](https://www.google.com)**.
2. Press **F12**.
3. Go to the **Elements** tab.
4. Click the "Inspect" arrow/icon at the top-left of the panel, then click on the Google search bar.
5. In the panel you'll see the HTML of that element — an `<input>`.
6. Double-click on a visible piece of text on the page (e.g. "Google Search") and change it to your name. Press Enter. The page looks different **only for you**.

Well done! You just made your first "hack" of a web page. (It's not a real hack — just a local change.)

---

## Exercises

### Exercise 1 — Dissect a URL
Explain each part of the address: `https://ursoaia-edu.online/courses/python/04-conditii/`

??? success "Solution"
    - `https` — the **protocol**: how we communicate (HTTPS = secured HTTP).
    - `ursoaia-edu.online` — the **domain**: the server's address.
    - `/courses/python/04-conditii/` — the **path**: which specific page on that server we want to see.

### Exercise 2 — Temporarily change a heading
Open Wikipedia, press `F12`, go to Elements, find the article's `<h1>` tag and change the text. Take a screenshot. After refresh, everything reverts.

??? success "Solution"
    - `F12` → Elements.
    - Click the "Inspect element" icon (the small arrow at the top-left of the panel).
    - Click the article title.
    - Double-click the text in the panel, type something else, Enter.
    - Refresh (`F5`) — the original title comes back.

### Exercise 3 — Use the Console
Open any page and in the **Console** tab type:

```js
document.title
```

and press Enter. What does it show?

??? success "Solution"
    It shows the **text from the browser's tab** (the title of the current page) — the same thing you see in the tab bar. It's your first contact with JavaScript: `document` is the page, `.title` is the property holding its title.

---

## Summary

- **Internet ≠ Web.** The Internet is the infrastructure; the Web is the layer of websites.
- Pages run on the **client-server** model via the **HTTP/HTTPS** protocol.
- The browser does 3 things: parses HTML, applies CSS, runs JS.
- The 3 languages: **HTML** (structure), **CSS** (look), **JavaScript** (behavior).
- Your tools: **VS Code + Live Server + a modern browser + F12**.
- `F12` opens DevTools — the **Elements**, **Console**, and **Network** tabs are your friends.

---

**Next step:** [→ Lesson 01: Your first page](01-prima-pagina.md)
