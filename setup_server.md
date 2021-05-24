# Apache

## Ubuntu

- Disable ServerTokens
  - `/etc/apache2/conf-available/security.conf`
    - `ServerTocken ProductOnly;`
    - `service apache2 reload`
- Disable .htaccess files
  - `/etc/apache2/apache2.conf`
    - `AllowOverride None`

## More Information

- <https://help.dreamhost.com/hc/en-us/articles/226327268-The-most-important-steps-to-take-to-make-an-Apache-server-more-secure>