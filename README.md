[![CI for Python Project](https://github.com/lotfibenabdelaziz/Module-2-MLOps/actions/workflows/testing-
ci.yml/badge.svg)](https://github.com/lotfibenabdelaziz/Module-2-MLOps/actions/workflows/testing-ci.yml)
# Python CI Project

This project demonstrates a clean Python setup using:

- 🛠️ `Makefile` for managing commands
- ✅ `pytest` for testing
- 🧼 `black` for formatting
- 🧪 `pylint` for linting
- 🤖 GitHub Actions for continuous integration (CI)

---

## 📁 Project Structure
.
├── hello.py
├── test_hello.py
├── requirements.txt
├── Makefile
└── .github/
└── workflows/
└── ci.yml

---

## 🧪 Available Makefile Commands

```bash
make install     # Install all dependencies
make test        # Run tests using pytest
make format      # Format code using black
make lint        # Lint code with pylint
make all         # Run install, lint, test, and format in one shot

.github/workflows/ci.yml

git clone https://github.com/your-username/your-repo.git
cd your-repo
make install
make all



