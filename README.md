# Nauka Gita
## Pierwsze cwiczenia

### Notatki:
* circuit breaker - system służacy do ochrony układów elektrycznych przed przeciążeniami lub zwarciami.
* cascading failures - sytuacja, gdy awaria jednego elementu powoduje łańcuchową reakcję awarii w innych powiązanych elementach, prowadząc do całkowitego wyłączenia systemu. Aby zapobiec temu, stosuje się redundancję, systemy zapasowe i monitorowanie.
* service degradation - Sstopniowe pogarszanie się jakości lub wydajności usługi systemowej. 

    ```bash
    curl --fail -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"natalia"}' https://httpbin.org/post
    ```

    ```bash
    curl --fail -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"natalia"}' https://httpbin.org/get
    ```

    ```bash
    curl --fail -X GET \
    -H "Content-Type: application/json" \
    https://httpbin.org/get
    ```

    ```bash
    curl --fail \
    -X DELETE \
    -H "Content-Type: application/json" https://httpbin.org/delete
    ```

    ```bash
    curl -s --fail -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"natalia"}' https://httpbin.org/post
    ```

    ```bash
    curl -s --fail -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"natalia"}' https://httpbin.org/post | jq
   ```

```bash
curl -s --fail -X POST \
     -H "Content-Type: application/json" \
     -d '{"name":"natalia"}' https://httpbin.org/post | jq '.json'
```

```bash
curl -s --fail -X \
    GET -H "Content-Type: application/json" \
    -d '{"name":"natalia"}' https://httpbin.org/get \
    | jq '.json | .name'
```
