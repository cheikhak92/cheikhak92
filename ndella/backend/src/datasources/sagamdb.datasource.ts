import {inject, lifeCycleObserver, LifeCycleObserver} from '@loopback/core';
import {juggler} from '@loopback/repository';

const config = {
  name: 'sagamdb',
  connector: 'mongodb',
  url: 'mongodb+srv://ndella:jiminie23@clustersagam.sf1hcbf.mongodb.net/sagamdb',
  database: 'sagamdb',
  useNewUrlParser: true
};

// Observe application's life cycle to disconnect the datasource when
// application is stopped. This allows the application to be shut down
// gracefully. The `stop()` method is inherited from `juggler.DataSource`.
// Learn more at https://loopback.io/doc/en/lb4/Life-cycle.html

@lifeCycleObserver('datasource')
export class SagamdbDataSource extends juggler.DataSource
  implements LifeCycleObserver {
  static dataSourceName = 'sagamdb';
  static readonly defaultConfig = config;

  constructor(
    @inject('datasources.config.sagamdb', {optional: true})
    dsConfig: object = config,
  ) {
    super(dsConfig);
  }
}
