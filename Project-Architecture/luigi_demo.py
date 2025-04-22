import luigi

class Printer(luigi.Task):
    def output(self):
        return luigi.LocalTarget('hello-luigi.txt')
    def run(self):
        with self.output().open("w") as outfile:
            outfile.write("Nice to meet you!")
    def requires(self):
        pass