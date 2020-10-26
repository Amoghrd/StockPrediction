By contributing to this project, you accept and agree to the terms and conditions for present and future Contributions submitted to this project. By contributing you agree that these contributions are your own (or approved by your employer) and you grant a full, complete, irrevocable copyright license to all users and developers of the project, present and future, pursuant to the license of the project. When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull requests

We actively welcome your pull requests. They are the best way to propose changes.

Fork the repo and create your branch from master.

If you've added code that should be tested, add tests.

If you've changed APIs, update the documentation.

Ensure the test suite passes.

Make sure your code linters.

Issue that pull request.

Give proper credit to the contributors!

## Technical

Ensure you have installed python3, pip3, and virtualenv.

Then, to set up your development environment:

```
$ cd projDir
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ pre-commit install
```

Then, before submitting a PR or pushing changes to master:

```
$ pre-commit run --all-files
```
