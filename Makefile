init:
	@command -v rye >/dev/null 2>&1 || (echo "rye not installed. Installing..." && curl -sSf https://rye.astral.sh/get | bash && echo "rye is installed!")
	rye sync

all: format lint-all utest
	echo "Format, Lint and Unit Test Done!"

format:
	rye fmt --diff

format-check:
	rye fmt --diff

lint:
	rye check

