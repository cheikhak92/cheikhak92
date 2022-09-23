import {
  Count,
  CountSchema,
  Filter,
  FilterExcludingWhere,
  repository,
  Where,
} from '@loopback/repository';
import {
  post,
  param,
  get,
  getModelSchemaRef,
  patch,
  put,
  del,
  requestBody,
  response,
} from '@loopback/rest';
import {Essai} from '../models';
import {EssaiRepository} from '../repositories';

export class ApisagamController {
  constructor(
    @repository(EssaiRepository)
    public essaiRepository : EssaiRepository,
  ) {}

  @post('/essais')
  @response(200, {
    description: 'Essai model instance',
    content: {'application/json': {schema: getModelSchemaRef(Essai)}},
  })
  async create(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Essai, {
            title: 'NewEssai',
            exclude: ['id'],
          }),
        },
      },
    })
    essai: Omit<Essai, 'id'>,
  ): Promise<Essai> {
    return this.essaiRepository.create(essai);
  }

  @get('/essais/count')
  @response(200, {
    description: 'Essai model count',
    content: {'application/json': {schema: CountSchema}},
  })
  async count(
    @param.where(Essai) where?: Where<Essai>,
  ): Promise<Count> {
    return this.essaiRepository.count(where);
  }

  @get('/essais')
  @response(200, {
    description: 'Array of Essai model instances',
    content: {
      'application/json': {
        schema: {
          type: 'array',
          items: getModelSchemaRef(Essai, {includeRelations: true}),
        },
      },
    },
  })
  async find(
    @param.filter(Essai) filter?: Filter<Essai>,
  ): Promise<Essai[]> {
    return this.essaiRepository.find(filter);
  }

  @patch('/essais')
  @response(200, {
    description: 'Essai PATCH success count',
    content: {'application/json': {schema: CountSchema}},
  })
  async updateAll(
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Essai, {partial: true}),
        },
      },
    })
    essai: Essai,
    @param.where(Essai) where?: Where<Essai>,
  ): Promise<Count> {
    return this.essaiRepository.updateAll(essai, where);
  }

  @get('/essais/{id}')
  @response(200, {
    description: 'Essai model instance',
    content: {
      'application/json': {
        schema: getModelSchemaRef(Essai, {includeRelations: true}),
      },
    },
  })
  async findById(
    @param.path.string('id') id: string,
    @param.filter(Essai, {exclude: 'where'}) filter?: FilterExcludingWhere<Essai>
  ): Promise<Essai> {
    return this.essaiRepository.findById(id, filter);
  }

  @patch('/essais/{id}')
  @response(204, {
    description: 'Essai PATCH success',
  })
  async updateById(
    @param.path.string('id') id: string,
    @requestBody({
      content: {
        'application/json': {
          schema: getModelSchemaRef(Essai, {partial: true}),
        },
      },
    })
    essai: Essai,
  ): Promise<void> {
    await this.essaiRepository.updateById(id, essai);
  }

  @put('/essais/{id}')
  @response(204, {
    description: 'Essai PUT success',
  })
  async replaceById(
    @param.path.string('id') id: string,
    @requestBody() essai: Essai,
  ): Promise<void> {
    await this.essaiRepository.replaceById(id, essai);
  }

  @del('/essais/{id}')
  @response(204, {
    description: 'Essai DELETE success',
  })
  async deleteById(@param.path.string('id') id: string): Promise<void> {
    await this.essaiRepository.deleteById(id);
  }
}
