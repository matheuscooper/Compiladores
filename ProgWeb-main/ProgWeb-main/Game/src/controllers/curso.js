
const models = require('../models/index');
const Curso = models.Curso;

async function index (req, res) {
    const cursos = await Curso.findAll();
    res.render('curso/index', {
        cursos: cursos.map(curso => curso.toJSON())
    });
};

async function read (req, res) {
    const { id } = req.params;
    const curso = await Curso.findOne({ where: { id }, include: models.Area });

    res.render('/curso/read',{
        curso: curso.toJSON()
    });
};

async function create (req, res) {
    if (req.route.methods.get) {
        res.render('curso/create');
    } else {
        const curso_1 = await Curso.create({
            sigla: req.body.sigla,
            nome: req.body.nome,
            descricao: req.body.descricao,
            areaId: req.body.area
        });
        res.redirect('/curso');
    }
};

async function update (req, res) {};
async function remove (req, res) {};

module.exports = { index, read, create, update, remove }