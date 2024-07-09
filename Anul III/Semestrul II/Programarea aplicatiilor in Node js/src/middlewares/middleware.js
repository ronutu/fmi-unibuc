import pkg from 'jsonwebtoken';
const { verify, sign } = pkg;

function verificaToken(req, res, next) {
  const token = req.cookies.cookie;

  if (!token) {
    return res.status(401).json({ error: 'Unauthorized access. No JWT token provided.' });
  }

  verify(token, 'crypto', (err, decoded) => {
    if (err) {
      return res.status(401).json({ error: 'Unauthorized access. Invalid JWT token.' });
    }

    req.user = decoded;
    next();
  });
}

function createToken() {
  return sign({ username: "Radu" }, "crypto", { expiresIn: '1h' });
};

export default {
  verificaToken,
  createToken
};
