from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
ALL_RESULTS = ROOT / "results" / "statistical_summary" / "all_results_long.csv"
FINAL_TABLE = ROOT / "results" / "statistical_summary" / "tabla_final_test_bootstrap_mean_std.csv"


def load_csv(path: Path):
    if not path.exists():
        print(f"[AVISO] No se encuentra: {path}")
        return None
    for encoding in ("utf-8", "latin-1", "cp1252"):
        try:
            return pd.read_csv(path, encoding=encoding)
        except Exception:
            continue
    print(f"[AVISO] No hemos podido leer: {path}")
    return None


def main() -> int:
    all_results = load_csv(ALL_RESULTS)
    final_table = load_csv(FINAL_TABLE)

    if all_results is None:
        return 1

    print("Modelos disponibles:")
    for name in all_results["display_name"].tolist():
        print("-", name)

    print("\nMétricas principales:")
    cols = ["display_name", "accuracy", "balanced_accuracy", "f1_macro", "cohen_kappa", "recall_macro"]
    print(all_results[cols].to_string(index=False))

    best_f1 = all_results.loc[all_results["f1_macro"].idxmax()]
    best_bal = all_results.loc[all_results["balanced_accuracy"].idxmax()]
    best_acc = all_results.loc[all_results["accuracy"].idxmax()]

    print("\nMejor modelo por Macro F1:", best_f1["display_name"], f"({best_f1['f1_macro']:.4f})")
    print("Mejor modelo por Balanced Accuracy:", best_bal["display_name"], f"({best_bal['balanced_accuracy']:.4f})")
    print("Mejor modelo por Accuracy:", best_acc["display_name"], f"({best_acc['accuracy']:.4f})")

    if final_table is not None:
        print("\nResumen final disponible en:", FINAL_TABLE)

    print("\nRutas de figuras disponibles:")
    figure_dirs = [
        ROOT / "figures" / "class_distribution",
        ROOT / "figures" / "learning_curves",
        ROOT / "figures" / "confusion_matrices",
        ROOT / "figures" / "model_comparison",
        ROOT / "figures" / "gradcam_selected",
        ROOT / "figures" / "paper",
    ]
    for folder in figure_dirs:
        print("-", folder)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
