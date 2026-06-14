import numpy as np
from rpy2.robjects.packages import importr
from rpy2.robjects import FloatVector
from rpy2.robjects import default_converter
from rpy2.robjects.conversion import localconverter
import rpy2.robjects as ro

betaARMA = importr("betaARMA")
stats    = importr("stats")


class BARMA_service:

    @staticmethod
    def fit_and_forecast(serie: list[float], steps: int = 1) -> list[float] | None:
        
        #Clipa valores extremos pra .99999 ou 0.0001
        serie_valida = [max(1e-4, min(1 - 1e-4, v)) for v in serie if v is not None]

        if len(serie_valida) < 3:
            print(f"[BARMA] Série curta demais ({len(serie_valida)} pontos válidos)")
            return None

        # Verifica se há variação suficiente
        if max(serie_valida) - min(serie_valida) < 1e-4:
            valor_constante = float(np.mean(serie_valida))
            return [valor_constante] * steps  # ← retorna o valor constante em vez de None

        serie_safe = [max(1e-4, min(1 - 1e-4, v)) for v in serie_valida]

        try:
            with localconverter(default_converter):
                y_r = stats.ts(FloatVector(serie_safe), frequency=1)

                # Tenta primeiro sem ridge
                try:
                    fit = betaARMA.barma(y_r, ar=1, ma=1)
                except Exception:
                    # Se falhar, usa ridge penalization para estabilidade
                    fit = betaARMA.barma(y_r, ar=1, ma=1, ridge=True)

                pred = betaARMA.forecast_barma(fit, h=steps)
                mean_pred = list(pred.rx2("mean"))

            return [float(np.clip(v, 0.0, 1.0)) for v in mean_pred]

        except Exception as e:
            print(f"[BARMA] Erro ao ajustar modelo: {e}")
            return None