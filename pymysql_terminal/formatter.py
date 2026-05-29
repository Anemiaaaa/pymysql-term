class Formatter:
    """форматирует результаты запросов для вывода в терминал"""

    def print_table(self, rows: list[dict]):
        if not rows:
            return
        headers = list(rows[0].keys())
        col_widths = {h: len(h) for h in headers}
        for row in rows:
            for h in headers:
                col_widths[h] = max(col_widths[h], len(str(row.get(h, ""))))

        sep = "+" + "+".join("-" * (col_widths[h] + 2) for h in headers) + "+"
        header_row = "|" + "|".join(f" {h:<{col_widths[h]}} " for h in headers) + "|"

        print(sep)
        print(header_row)
        print(sep)
        for row in rows:
            line = "|" + "|".join(f" {str(row.get(h, '')):<{col_widths[h]}} " for h in headers) + "|"
            print(line)
        print(sep)
        print(f"строк: {len(rows)}")

    def to_csv(self, rows: list[dict], delimiter=";") -> str:
        """конвертировать результат запроса в csv-строку"""
        if not rows:
            return ""
        headers = list(rows[0].keys())
        lines = [delimiter.join(headers)]
        for row in rows:
            lines.append(delimiter.join(str(row.get(h, "")) for h in headers))
        return "\n".join(lines)
