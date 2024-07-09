import express from "express";
import patroniRouter from "./patroni.js";
import citiesRouter from "./cities.js";
import restaurantsRouter from "./restaurants.js";

const router = express.Router();

router.use("/patroni", patroniRouter);
router.use("/cities", citiesRouter);
router.use("/restaurants", restaurantsRouter);

export default router;