from src.pipeline.pipeline import MarketAnalysisPipeline


pipeline = MarketAnalysisPipeline(

    countries=[

        "IDN",
        "MYS",
        "VNM",
        "THA",
        "SGP"

    ]

)

results = pipeline.run()

print(results["topsis_ranking"])