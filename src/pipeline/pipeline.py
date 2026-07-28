from src.data_collection.worldbank import WorldBankCollector

from src.enrichment.country import CountryEnricher
from src.enrichment.indicator import MetadataEnricher

from src.validation.quality_check import DataQualityChecker

from src.processing.aggregation import AggregationEngine
from src.processing.normalization import DataNormalizer
from src.processing.weighting import WeightAssigner

from src.analysis.mcda import MCDAModel
from src.analysis.topsis import TOPSISModel

from src.financial.config import FinancialConfig
from src.financial.financial_input import FinancialInputBuilder
from src.financial.revenue_projection import RevenueProjection
from src.financial.cashflow import CashFlowGenerator
from src.financial.npv import NPVCalculator
from src.financial.irr import IRRCalculator
from src.financial.payback import PaybackCalculator
from src.financial.sensitivity import SensitivityAnalysis

from src.analysis.recommendation import RecommendationModel
from src.config.recommendation_config import RecommendationConfig
from src.config.indicator_config import IndicatorConfig
from src.utils.csv_exporter import CSVExporter
from src.utils.logger import PipelineLogger


class MarketAnalysisPipeline:


    def __init__(

        self,

        countries,

    ):

        self.countries = countries

        self.indicator_config = "config/indicators.yaml"

        self.indicators = (

            IndicatorConfig(

                self.indicator_config

            )

            .get_required_indicators()

        )

        self.country_config = "config/countries.yaml"

        self.indicator_config = "config/indicators.yaml"

        self.weight_config = "config/weights.yaml"

        self.financial_config = "config/financial.yaml"


    # --------------------------------------------------
    # Execute Pipeline
    # --------------------------------------------------

    def run(self):

        logger = PipelineLogger.get_logger()

        logger.info(
            "Pipeline Started"
        )

        try:

            # ---------------------------------------------
            # Collect
            # ---------------------------------------------

            collector = WorldBankCollector()

            raw_df = collector.get_multiple_countries(

                self.countries,

                self.indicators

            )

            logger.info(
                f"Collected {len(raw_df)} records from World Bank"
            )


            # ---------------------------------------------
            # Country Metadata
            # ---------------------------------------------

            country_enricher = CountryEnricher(

                self.country_config

            )

            country_df = country_enricher.enrich(

                raw_df

            )

            logger.info(
                "Country enrichment completed"
            )


            # ---------------------------------------------
            # Indicator Metadata
            # ---------------------------------------------

            indicator_enricher = MetadataEnricher(

                self.indicator_config

            )

            enriched_df = indicator_enricher.enrich(

                country_df

            )

            logger.info(
                "Indicator enrichment completed"
            )


            # ---------------------------------------------
            # Validation
            # ---------------------------------------------

            checker = DataQualityChecker(

                enriched_df

            )

            quality_report = checker.run_all_checks()

            logger.info(
                "Data quality validation completed"
            )


            # ---------------------------------------------
            # Aggregation
            # ---------------------------------------------

            aggregator = AggregationEngine(

                enriched_df

            )

            aggregated_df = aggregator.aggregate()

            logger.info(
                "Historical aggregation completed"
            )


            # ---------------------------------------------
            # Normalization
            # ---------------------------------------------

            normalizer = DataNormalizer(

                aggregated_df

            )

            normalized_df = normalizer.normalize()

            logger.info(
                "Normalization completed"
            )


            # ---------------------------------------------
            # Weighting
            # ---------------------------------------------

            weight_assigner = WeightAssigner(

                normalized_df,

                self.weight_config

            )

            weighted_df = weight_assigner.apply_weights()

            logger.info(
                "Weight assignment completed"
            )


            # ---------------------------------------------
            # MCDA
            # ---------------------------------------------

            mcda = MCDAModel(

                weighted_df

            )

            mcda_result = mcda.run()

            logger.info(
                "MCDA analysis completed"
            )


            # ---------------------------------------------
            # TOPSIS
            # ---------------------------------------------
            topsis = TOPSISModel(

                mcda_result["dimension_scores"]

            )

            ranking = topsis.run()

            logger.info(
                "TOPSIS ranking completed"
            )


             # ---------------------------------------------
            # Financial Configuration
            # ---------------------------------------------

            financial = FinancialConfig(

                self.financial_config

            )

            logger.info(
                "Financial configuration loaded"
            )

            financial_input = FinancialInputBuilder(

                ranking,

                aggregated_df

            ).run()

            logger.info(
                "Financial inputs prepared"
            )


            # ---------------------------------------------
            # Revenue Projection
            # ---------------------------------------------

            revenue_projection = RevenueProjection(

                financial_input,

                financial

            ).run()

            logger.info(
                "Revenue projection completed"
            )


            # ---------------------------------------------
            # Cash Flow Generation
            # ---------------------------------------------

            cashflow = CashFlowGenerator(

                revenue_projection,

                financial

            ).run()

            logger.info(
                "Cash flow generation completed"
            )


            # ---------------------------------------------
            # Country Financial Analysis
            # ---------------------------------------------

            npv_result = NPVCalculator(

                cashflow,

                financial

            ).run()


            npv = npv_result["summary"]

            irr = IRRCalculator(

                cashflow,

                financial

            ).run()

            payback = PaybackCalculator(

                cashflow,

                financial

            ).run()

            logger.info(
                "Country financial metrics completed"
            )


            recommendation_config = RecommendationConfig(

                "config/recommendation.yaml"

            )


            recommendation = RecommendationModel(

                ranking,

                npv,

                irr,

                payback,

                recommendation_config.get_weights()

            ).run()


            logger.info(
                "Investment recommendation completed"
            )


            # ---------------------------------------------
            # Sensitivity Analysis
            # ---------------------------------------------

            scenarios = financial.scenarios

            sensitivity = SensitivityAnalysis(

                cashflow,

                financial,

                scenarios

            ).run()

            logger.info(
                "Sensitivity analysis completed"
            )

            # ---------------------------------------------
            # Pipeline Results
            # ---------------------------------------------

            results = {

                "raw_data": raw_df,

                "enriched_data": enriched_df,

                "quality_report": quality_report,

                "aggregated_data": aggregated_df,

                "normalized_data": normalized_df,

                "weighted_data": weighted_df,

                "dimension_scores": mcda_result["dimension_scores"],

                "market_scores": mcda_result["market_scores"],

                "topsis_ranking": ranking,
                "financial_input": financial_input,

                "npv": npv,

                "irr": irr,

                "payback": payback,

                "sensitivity": sensitivity,
                "revenue_projection": revenue_projection,
                "cashflow": cashflow,
                "recommendation": recommendation,

            }


            # ---------------------------------------------
            # Export CSV Files
            # ---------------------------------------------

            exporter = CSVExporter()

            exporter.export_pipeline(

                results

            )

            logger.info(
                "CSV export completed"
            )

            logger.info(
                "Pipeline Finished Successfully"
            )

            return results

        except Exception as error:

            logger.exception(

                f"Pipeline Failed: {error}"

            )

            raise