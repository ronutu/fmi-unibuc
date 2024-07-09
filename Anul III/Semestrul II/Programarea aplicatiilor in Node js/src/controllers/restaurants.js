import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

const createRestaurant = async (req, res) => {
    try {
        const {name, idPatron, patron, idCity, city} = req.body;
        const addedRestaurant = await prisma.restaurant.create({
            data:{
                name: name,
                idPatron: idPatron,
                patron: patron,
                idCity: idCity,
                city: city,
            }
        });
        if(addedRestaurant){
            res.status(200).send(addedRestaurant);
        } else {
            res.status(403).send("nu merge")
        }
    } catch(err){
        console.log(err);
    }
};

const getRestaurant = async (req, res) => {
    try {
        const { id } = req.params;
        if (!id) {
            return res.status(400).send("No ID provided");
        }

        const user = await prisma.restaurant.findUnique({
            where: {
                id: id,
            },
        });

        if (!user) {
            return res.status(404).send("restaurant not found");
        }

        res.send(user);
    } catch (err) {
        console.error(err);
        res.status(500).send("Internal Server Error");
    }
};

const updateRestaurant = async (req, res) => {
    const { id } = req.params;
    const newObjRestaurant = req.body;

    if (!id) {
        return res.status(400).send("No ID provided");
    }

    if (!newObjRestaurant) {
        return res.status(400).send("No new restaurant data provided");
    }

    try {
        const modifyRestaurant = await prisma.restaurant.update({
            where: {
                id: id,
            },
            data: {
                name: newObjRestaurant.name,
                idPatron: newObjRestaurant.idPatron,
                patron: newObjRestaurant.patron,
                idCity: newObjRestaurant.idCity,
                city: newObjRestaurant.city,
            },
        });

        if (modifyRestaurant) {
            res.status(200).json(modifyRestaurant);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ err: "InternalServerError" });
    }
};

const deleteRestaurant = async (req, res) => {
    const { id } = req.params;
    if (id === undefined) {
        res.status(400).send("No id provided");
        return;
      }
      try {
        const deleted = await prisma.restaurant.delete({
          where: {
            id: id,
          },
        });
        if (!deleted) {
          res.status(400).send("oops");
        }
        res.status(200).json(deleted);
      } catch (err) {
        res.status(500).json({ err: "InternalServerError" });
      }
};

export default {
    createRestaurant,
    getRestaurant,
    updateRestaurant,
    deleteRestaurant,
};