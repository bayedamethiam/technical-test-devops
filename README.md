# Technical test : Secret message API

![Me](https://i.pinimg.com/736x/60/b7/50/60b750dbb4841120b308ac826b572573.jpg)

Here is a little project I'm really proud of: a system for one-time messages! I thought it would be useful to share secrets...

However, I'm a bit concerned about the security, and I have no idea how to ensure my project complies with high security standards.

Also, I want to deploy it on Kubernetes... But I have no idea how.

## TODO

Let's help our friend. The goal of this test is to:

- Help secure this secret message API (OWASP, ISO27001, etc.), ensuring there are no obvious security issues. You are free to take any approach, but ideally, the **outcome would be a report of fixes to implement**.
- How would you deploy it to Kubernetes following DevSecOps best practices? The **outcome** would be **at least** an architecture diagram with explanations, but you can also provide deployment instructions, YAML files, etc. Whatever you think is relevant.
- How would you implement the CI/CD? What checks would you integrate to help our friend developer avoid making mistakes? The **outcome would be an example of a CI/CD pipeline and tools**, ideally using GitHub Actions and/or any other tool you think is relevant.
- What should we monitor? How? The **outcome would be a simple description of metrics to monitor and how to monitor them**.
- What would you improve on this project? What would you suggest to our friend developer? The **outcome would be a simple description of improvements to implement**.

You are free to choose tools, approaches, and implementation details. In the report, you can provide your thoughts and reasoning.

> [!info]
> This test is an opportunity for you to showcase what you can do and what you like working on. You are welcome to delve deeper into some aspects.
> You are expected to share your work as a Git private repository and give access to @disconico on Github. Good luck!

**The final deliverable should be a fork of this git repository, with :**

- Any changes and additions to the files ( code, dockerfiles, etc.)
- A report in the `report.md` file

Happy hacking!

## More details...

To run the project, you can use Docker Compose:

```bash
docker compose up
```

Then:

- [The UI is available at http://localhost:8080](http://localhost:8080)
- [The API is available at http://localhost:8000](http://localhost:8000)
