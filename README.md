requests-runscope
=================

Runscope Adapter for Python Requests (python-requests.org)

- Requires a free Runscope account, [sign up here](https://www.runscope.com/signup)
- Automatically create Runscope URLs for your requests

### Installation

    pip install requests-runscope


### Example

    import requests
    from dashboard.runscope_adapter import RunscopeAdapter


    def main():
        session = requests.Session()
        session.mount('http://', RunscopeAdapter("bucket_key"))
        session.mount('https://', RunscopeAdapter("bucket_key"))

        resp = session.get("http://github.com")
        print resp.content


    if __name__ == '__main__':
        main()