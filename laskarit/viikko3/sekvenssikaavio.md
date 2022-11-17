``` mermaid
sequenceDiagram
    main ->> machine: Machine()
    machine ->> fueltank: Fueltank()
    machine ->> fueltank: fill(40)
    activate fueltank
    fueltank -->> machine: -
    deactivate fueltank
    machine ->> engine: Engine(self._fueltank)
    main ->> machine: drive()
    activate machine
    machine ->> engine: start()
    engine ->> fueltank: consume(5)
    activate fueltank
    fueltank -->> engine: -
    deactivate fueltank
    machine ->> engine: is_running()
    activate engine
    engine -->> fueltank: fuel_contents()
    activate fueltank
    fueltank -->> engine: 40
    deactivate fueltank
    engine -->> machine: True
    deactivate engine
    machine ->> engine: use_energy()
    engine ->> fueltank: consume(10)
    activate fueltank
    fueltank -->> engine: -
    deactivate fueltank
    machine -->> main: -
    deactivate machine
   ```