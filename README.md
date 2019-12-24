# Copy Extra Paths Example

This example shows how to use the new `copy-extra-paths` feature in the faas-cli.

First, build the function
```sh
faas-cli build
```

You can then run the function locally using
```sh
docker run --rm -p 8080:8080 theaxer/echo-common:latest
```


Which you cant test using
```sh
$ curl http://localhost:8080 -d "the coolest"
openfaas
```

