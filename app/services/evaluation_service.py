import Levenshtein

class EvaluationService:
    @staticmethod
    def cer(reference: str, hypothesis: str) -> float:
        if not reference:
            return 1.0
        return Levenshtein.distance(reference, hypothesis) / len(reference)
