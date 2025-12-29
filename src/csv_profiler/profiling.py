def profile_rows(rows: list[dict]) -> dict:
    if not rows:
        return {"row_count": 0, "col_count": 0, "columns": {}}

    num_rows = len(rows)
    columns = list(rows[0].keys())
    column_stats = {}

    for col in columns:
        values = []
        missing = 0
        
        for row in rows:
            val = str(row.get(col, "")).strip()
            val = str(raw_val).strip() if raw_val is not None else ""
            
            
            if val == "" or val.lower() == "nan":
                missing += 1
            else:
                values.append(val)

        
        is_numeric = True
        numeric_values = []
        
        if not values:
            is_numeric = False
        else:
            for v in values:
                try:
                    
                    numeric_values.append(float(v))
                except ValueError:
                    is_numeric = False
                    break
        
        
        stats = {
            "type": "Number" if is_numeric else "Text",
            "missing": missing
        }

        
        if is_numeric and numeric_values:
            stats["min"] = min(numeric_values)
            stats["max"] = max(numeric_values)
            stats["mean"] = sum(numeric_values) / len(numeric_values)

        column_stats[col] = stats

    return {
        "row_count": num_rows,
        "col_count": len(columns),
        "columns": column_stats
    }