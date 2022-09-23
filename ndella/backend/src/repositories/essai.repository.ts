import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {SagamdbDataSource} from '../datasources';
import {Essai, EssaiRelations} from '../models';

export class EssaiRepository extends DefaultCrudRepository<
  Essai,
  typeof Essai.prototype.id,
  EssaiRelations
> {
  constructor(
    @inject('datasources.sagamdb') dataSource: SagamdbDataSource,
  ) {
    super(Essai, dataSource);
  }
}
