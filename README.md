requests-runscope
=================

Runscope Adapter for Python Requests (python-requests.org)

- Requires a free Runscope account, [sign up here](https://www.runscope.com/signup)
- Automatically create Runscope URLs for your requests
- Automatically create proper `Runscope-Request-Port` header when using ports
- Support for authenticated buckets and service regions (see example below)

### Installation

```cli
    pip install requests-runscope
```


### Example

```python
    import requests
    from requests_runscope import RunscopeAdapter


    def main():
        session = requests.Session()
        session.mount('http://', RunscopeAdapter("bucket_key"))
        session.mount('https://', RunscopeAdapter("bucket_key"))

        # for authenticated buckets (https://www.runscope.com/docs/buckets#authentication)
        # session.mount('http://', RunscopeAdapter("bucket_key", auth_token="abcd1234"))
        # session.mount('https://', RunscopeAdapter("bucket_key", auth_token="abcd1234"))

        # for service regions (https://www.runscope.com/docs/regions)
        # session.mount('http://', RunscopeAdapter("bucket_key", gateway_host="eu1.runscope.net"))
        # session.mount('https://', RunscopeAdapter("bucket_key", gateway_host="eu1.runscope.net"))

        resp = session.get("https://api.github.com")
        print resp.content


    if __name__ == '__main__':
        main()
```
