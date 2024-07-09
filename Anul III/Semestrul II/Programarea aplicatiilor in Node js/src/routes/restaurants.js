import express from "express";
import restaurantsController from "../controllers/restaurants.js";
import middleware from '../middlewares/middleware.js';

const restaurantsRouter = express.Router();

restaurantsRouter.post('/', middleware.verificaToken, restaurantsController.createRestaurant);
restaurantsRouter.get('/:id', restaurantsController.getRestaurant);
restaurantsRouter.put('/:id', restaurantsController.updateRestaurant);
restaurantsRouter.delete('/:id', middleware.verificaToken, restaurantsController.deleteRestaurant);


export default restaurantsRouter;