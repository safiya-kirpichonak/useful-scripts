# generate-random

## Usage

run following command to understand how to use this script.

```
python3 generaterandom.py --help
```

## Usage like your own command

You can create a little scripts, just follow this instruction.
I will use password_generator for example:

1. Go to the folder with script and open file
2. Add shebang in the beginning of the file: #!/usr/bin/env python
3. Add to execute file: 

```
chmod +x generaterandom.py
```

4. Remove the extension of the file: 

```
mv generaterandom.py generatepassword
```

5. Move it to /usr/local/bin: 

```
mv ./generatepassword /usr/local/bin
```

6. Open terminal and use it:

```
generaterandom
```

# Resources

- [Guide how to create custom command](https://pythobyte.com/create-custom-terminal-command-1dr0yhg33s-eef956b2/)
