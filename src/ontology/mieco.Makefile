## Customize Makefile settings for mieco
## 
## If you need to customize your Makefile, make
## changes here rather than in the main Makefile

# ----------------------------------------
# Ontology documentation for MkDocs
# ----------------------------------------
# Generate a Markdown term list from the source ontology using ROBOT and place
# it in the docs_src directory so MkDocs includes it in the website.
#
# Requires: python3, and either:
#   - `robot` on PATH (e.g. inside the ODK Docker container), or
#   - the ROBOT_JAR variable set to the path of a robot.jar file.
#
# Usage inside ODK Docker:
#   ./run.sh make ontology_docs
#
# Usage with a local robot.jar:
#   make ontology_docs ROBOT_JAR=/path/to/robot.jar

ROBOT_JAR ?=
ONTOLOGY_DOCS_SCRIPT = ../../src/scripts/generate_ontology_docs.py

.PHONY: ontology_docs
ontology_docs:
	@if [ -n "$(ROBOT_JAR)" ]; then \
	  python3 $(ONTOLOGY_DOCS_SCRIPT) --robot-jar "$(ROBOT_JAR)"; \
	else \
	  python3 $(ONTOLOGY_DOCS_SCRIPT); \
	fi

