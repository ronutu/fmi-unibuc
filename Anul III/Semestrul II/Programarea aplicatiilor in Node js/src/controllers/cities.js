import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

const createCity = async (req, res) => {
    try {
        const {name, nr_citizens, area} = req.body;
        const adddedCity = await prisma.city.create({
            data:{
                name: name,
                nr_citizens: nr_citizens,
                area: area,
            }
        });
        if(adddedCity){
            res.status(200).send(adddedCity);
        } else {
            res.status(403).send("nu merge")
        }
    } catch(err){
        console.log(err);
    }
};

const getCity = async (req, res) => {
    try {
        const { id } = req.params;
        if (!id) {
            return res.status(400).send("No ID provided");
        }

        const user = await prisma.city.findUnique({
            where: {
                id: id,
            },
        });

        if (!user) {
            return res.status(404).send("City not found");
        }

        res.send(user);
    } catch (err) {
        console.error(err);
        res.status(500).send("Internal Server Error");
    }
};

const updateCity = async (req, res) => {
    const { id } = req.params;
    const newObjCity = req.body;

    if (!id) {
        return res.status(400).send("No ID provided");
    }

    if (!newObjCity) {
        return res.status(400).send("No new city data provided");
    }

    try {
        const modifyCity = await prisma.city.update({
            where: {
                id: id,
            },
            data: {
                name: newObjCity.name,
                nr_citizens: newObjCity.nr_citizens,
                area: newObjCity.area,
            },
        });

        if (modifyCity) {
            res.status(200).json(modifyCity);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ err: "InternalServerError" });
    }
};

const deleteCity = async (req, res) => {
    const { id } = req.params;
    if (id === undefined) {
        res.status(400).send("No id provided");
        return;
      }
      try {
        const deleted = await prisma.city.delete({
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
    createCity,
    getCity,
    updateCity,
    deleteCity,
};