# git 

```shell
fatal: unable to access 'https://github.com/Thomaszz4/Shell.git/': Couldn't connect to server
```

SOLOTION: change `https` to `git`  but can not push this repo

```shell
You can't push to git://github.com/Thomaszz4/Shell.git
Use https://github.com/Thomaszz4/Shell.git
```

SOLUTION: using `git clone https://github.com/Thomaszz4/Shell.git`

```shell
error: failed to push some refs to 'https://github.com/xxxx.git'
```

SOLOTION: the remote repo changed, `git pull` first then `git push` again

# zsh

```shell
Insecure completion-dependent directories detected
```

SOLUTION: that is because some of the file lack of authority, `chmod 775 xx/xx`

## tensorflow related

when `model.predict`

```python
"""
    model_config = json.loads(model_config.decode('utf-8'))
AttributeError: 'str' object has no attribute 'decode'
"""
```

SOLOTION: that's because the version of h5py >= 3.0.0

```shell
pip uninstall h5py
pip install h5py==2.8.0
```

## flask

Happen:

`self.socket.bind(self.server_address)
socket.gaierror: [Errno 8] nodename nor servname provided, or not known`

SOLOTION:

```python
# when more than 2 thish blocks occur, this ERROR happened
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')
```





