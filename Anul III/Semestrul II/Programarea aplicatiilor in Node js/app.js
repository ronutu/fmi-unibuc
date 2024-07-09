import express from "express";
import cookieParser from "cookie-parser";
import routes from "./src/routes/index.js"
import middleware from "./src/middlewares/middleware.js";

var app = express();

app.use(express.json());
app.use(cookieParser());

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'Radu' && password === 'parola') {
    const token = middleware.createToken();
    res.cookie('cookie', token, { httpOnly: true });
    return res.json({ message: 'Login successful!' });
  }

  return res.status(401).json({ error: 'Invalid credentials' });
});

app.use(routes);

app.listen("3000", () =>
  console.log("Server started at: http://localhost:3000")
);

export default app;