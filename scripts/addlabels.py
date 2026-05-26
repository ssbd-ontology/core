import re
import sys
from pathlib import Path


def camel_to_spaces(text):
    text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return text.lower()


def process_ttl_file(file_path):
    path = Path(file_path)
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    new_lines = []

    pattern = re.compile(
        r'^(?P<indent>\s*)skos:prefLabel\s+"(?P<label>[^"]+)"(?P<lang>@[a-zA-Z-]+)?\s*(?P<end>[;.])\s*$'
    )

    for line in lines:
        match = pattern.match(line)

        if not match:
            new_lines.append(line)
            continue

        indent = match.group("indent")
        original_label = match.group("label")
        lang = match.group("lang") or "@en"
        end = match.group("end")

        new_label = camel_to_spaces(original_label)

        if end == ".":
            new_lines.append(
                f'{indent}skos:prefLabel "{original_label}"{lang} ;\n'
            )
            new_lines.append(
                f'{indent}rdfs:label "{new_label}"{lang} .\n'
            )
        else:
            new_lines.append(line)
            new_lines.append(
                f'{indent}rdfs:label "{new_label}"{lang} ;\n'
            )

    path.write_text("".join(new_lines), encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_rdfs_labels.py file.ttl")
        sys.exit(1)

    process_ttl_file(sys.argv[1])

# sed -i 's/s sb d/SSbD/g' *.ttl
