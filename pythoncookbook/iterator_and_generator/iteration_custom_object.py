
class Classroom():
    def __init__(self,bench_count):
        self.benches = [Bench(id) for id in range(bench_count)]
    def __repr__(self):
        header =  "-"*10+"Board"+"-"*10 +"\n"
        benchstruct = ""
        for bench in self.benches:
            benchstruct += str(bench)+"\n" 
        return header + benchstruct
    def __iter__(self):
        return iter(self.benches)

class Bench():
    def __init__(self,id):
        self._id = id
    def __repr__(self):
        return "Bench id-{}".format(self._id)

if __name__ == '__main__':
    print("create bench object")
    b = Bench(1)
    print("print bench object", b)
    


