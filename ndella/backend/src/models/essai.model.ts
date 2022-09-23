import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class Essai extends Entity {
  @property({
    type: 'string',
    id: true,
    generated: true,
  })
  id?: string;

  @property({
    type: 'string',
    required: true,
  })
  nom: string;

  @property({
    type: 'string',
    required: true,
  })
  prenom: string;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Essai>) {
    super(data);
  }
}

export interface EssaiRelations {
  // describe navigational properties here
}

export type EssaiWithRelations = Essai & EssaiRelations;
