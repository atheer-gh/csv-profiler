class Profiler:
    def __init__(self, rows: list):
        self.rows = rows

    def get_profile(self):
        if not self.rows:
            return {"rows": 0, "columns": {}}
        
       
        num_rows = len(self.rows)
        
        columns = self.rows[0].keys()
        
        column_stats = {}
        for col in columns:
          
            missing = sum(1 for row in self.rows if not row.get(col))
            column_stats[col] = {"missing": missing}
            
        return {
            "rows": num_rows,
            "columns": column_stats
        }