import { PrismaClient } from "@prisma/client";
const prisma = new PrismaClient();

const createPatron = async (req, res) => {
    try {
        const {name, age, height, weight} = req.body;
        const addedPatron = await prisma.patron.create({
            data:{
                name: name,
                age: age,
                height: height,
                weight: weight,
            }
        });
        if(addedPatron){
            res.status(200).send(addedPatron);
        } else {
            res.status(403).send("nu merge")
        }
    } catch(err){
        console.log(err);
    }
};

const getPatron = async (req, res) => {
    try {
        const { id } = req.params;
        if (!id) {
            return res.status(400).send("No ID provided");
        }

        const user = await prisma.patron.findUnique({
            where: {
                id: id,
            },
        });

        if (!user) {
            return res.status(404).send("Patron not found");
        }

        res.send(user);
    } catch (err) {
        console.error(err);
        res.status(500).send("Internal Server Error");
    }
};

const updatePatron = async (req, res) => {
    const { id } = req.params;
    const newObjPatron = req.body;

    if (!id) {
        return res.status(400).send("No ID provided");
    }

    if (!newObjPatron) {
        return res.status(400).send("No new patron data provided");
    }

    try {
        const modifyPatron = await prisma.patron.update({
            where: {
                id: id,
            },
            data: {
                name: newObjPatron.name,
                age: newObjPatron.age,
                height: newObjPatron.height,
                weight: newObjPatron.weight,
            },
        });

        if (modifyPatron) {
            res.status(200).json(modifyPatron);
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ err: "InternalServerError" });
    }
};

const deletePatron = async (req, res) => {
    const { id } = req.params;
    if (id === undefined) {
        res.status(400).send("No id provided");
        return;
      }
      try {
        const deleted = await prisma.patron.delete({
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
    createPatron,
    getPatron,
    updatePatron,
    deletePatron,
};