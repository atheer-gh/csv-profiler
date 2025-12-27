class Profiler:
    def __init__(self, rows):
        self.rows = rows
        if rows:
            self.columns = list(rows[0].keys())
        else:
            self.columns = []

    def get_profile(self):
        if not self.rows:
            return {"rows": 0, "columns": {}}

       
        results = {}
        for col in self.columns:
            results[col] = {"missing": 0, "types": []}

        
        for row in self.rows:
            for col in self.columns:
                val = row[col].strip()
                if val == "":
                    results[col]["missing"] += 1
                else:
                    
                    data_type = self._check_type(val)
                    results[col]["types"].append(data_type)

    
        for col in results:
            all_types = results[col]["types"]
            if all_types:
                
                results[col]["inferred_type"] = max(set(all_types), key=all_types.count)
            else:
                results[col]["inferred_type"] = "none"
            
          
            results[col]["types"] = list(set(all_types))

        return {"rows": len(self.rows), "columns": results}

    def _check_type(self, value):
       
        if value.isdigit():
            return "integer"
        try:
            float(value)
            return "float"
        except:
            return "string"