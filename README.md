# basic CLA encrypter
##### this repo is a very basic encryping method

## how to run
### command line
```commandline
python main.py arguments
```
#### arguments
you have to specify at least 3 arguments:

>_mode_

this argument can be two values: `encode` or `decode` 
 
> _seed_ 

this argument is  the seed for the pseudo-random integers. you have to use the same seed for encoding/decoding! the longer this int is, the harder it will be to crack the code.

> _text to encrypt/decrypt_

the text to encrypt/decrypt can take all arguments that are not _file_ (in this repo always `main.py`), _mode_, _seed_.

## example of a use

### to encrypt:
```commandline
python main.py encode 352121898765432345123543212344388643234527 hello world
```

output:
> ^jkle'wtua

(this output will always be the same, because `random.randint()` isn't random)

in this case _**mode**_ is `encode`, _**seed**_ is a very long number e.g. 352...... and _**text to encrypt**_ takes the two last arguments, hello and world.

### to decrypt
```commandline
python main.py decode 352121898765432345123543212344388643234527 "^jkle'wtua"
```

output:
> hello world

(this output will also always be the same, because `random.randint()` isn't random)

in this case _**mode**_ is `decode`, _**seed**_ is the same number as used to encode and _**text to decrypt**_ is the encrypted text, in this case: `^jkle'wtua`.