import express from "express";
import citiesController from "../controllers/cities.js";
import middleware from '../middlewares/middleware.js';

const citiesRouter = express.Router();

citiesRouter.post('/', middleware.verificaToken, citiesController.createCity);
citiesRouter.get('/:id', citiesController.getCity);
citiesRouter.put('/:id', citiesController.updateCity);
citiesRouter.delete('/:id', middleware.verificaToken, citiesController.deleteCity);


export default citiesRouter;