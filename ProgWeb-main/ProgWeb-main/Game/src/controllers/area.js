
const models = require('../models/index');
const Area = models.Area;

const index = async (req, res) => {
    const areas = await Area.findAll();
    res.render('main/area', {
        areas: areas.map(area => area.toJSON())
    });
};

module.exports = { index }