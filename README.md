# hydra_config_example
A sample hydra app to demonstrate configuration composability

## Setting up the application

1. Create a virtualenvironment `venv` using the `venv` tool 
```python3 venv venv```
2. Activate the virtual environment
```source venv/bin/activate```
3. Install the dependencies
```pip install -r requirements.txt```

## Running the application

```python3 app.py```

## Expected outputs

The base config is listed in the `config.yaml`. Custom configuration for two different customers are listed under `nestle.yaml` and `rb.yaml` configuration files. The application initializes configuration object for both the customers separately. The base configuration will then be merged with the customer specific configuration with the customer configuration overriding any base configuration.

### Output for the Nestle Customer

```
res_msg_hd:
  '0':
    msg: 0
    heading: Genuine
  '1':
    msg: 2
    heading: Not Encoded
  '2':
    msg: 4
    heading: Photo Quality not good
  '3':
    msg: 3
    heading: Fake
products_list:
- nestle_product1
- nestle_product2
- nestle_product3
- nestle_product4
```

### Output for the RB customer

```
res_msg_hd:
  '0':
    msg: 0
    heading: Genuine
  '1':
    msg: 2
    heading: Not Encoded
  '2':
    msg: 4
    heading: Photo Quality not good
  '3':
    msg: 3
    heading: Fake
products_list:
- rb_product1
- rb_product2
- rb_product3
- rb_product4
```
