import express from "express";
import patroniController from "../controllers/patroni.js";
import middleware from '../middlewares/middleware.js';

const patroniRouter = express.Router();

patroniRouter.post('/', middleware.verificaToken, patroniController.createPatron);
patroniRouter.get('/:id', patroniController.getPatron);
patroniRouter.put('/:id', patroniController.updatePatron);
patroniRouter.delete('/:id', middleware.verificaToken, patroniController.deletePatron);


export default patroniRouter;