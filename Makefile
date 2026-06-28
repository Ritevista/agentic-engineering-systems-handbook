.PHONY: help lint build serve check link-check

MDBOOK_HOST ?= 127.0.0.1
MDBOOK_PORT ?= 3000

help:
	@printf '%s\n' 'Targets:'
	@printf '  %-12s %s\n' 'lint' 'Lint Markdown sources'
	@printf '  %-12s %s\n' 'build' 'Build the mdBook site'
	@printf '  %-12s %s\n' 'serve' 'Serve the book locally'
	@printf '  %-12s %s\n' 'check' 'Run local pre-PR checks'
	@printf '  %-12s %s\n' 'link-check' 'Check source and generated links with lychee'

lint:
	npx markdownlint-cli2

build:
	mdbook build

serve:
	mdbook serve --hostname $(MDBOOK_HOST) --port $(MDBOOK_PORT)

check: lint build

link-check: build
	lychee --config .lychee.toml "**/*.md" "book/**/*.html"
