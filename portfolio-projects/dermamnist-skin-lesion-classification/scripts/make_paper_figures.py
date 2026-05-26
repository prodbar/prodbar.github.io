from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS_CSV = ROOT / "results" / "statistical_summary" / "tabla_final_test_bootstrap_mean_std.csv"
M3_HISTORY_CSV = ROOT / "results" / "histories" / "M3_RESNET50_IMAGENET_DEEP_seed123_history.csv"
OUT_DIR = ROOT / "figures" / "paper"

PALETTE = {
    "primary": "#0f766e",
    "secondary": "#0891b2",
    "accent": "#14b8a6",
    "gray": "#64748b",
}


def read_csv_safe(path: Path) -> pd.DataFrame | None:
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


def normalize_pm(value: str) -> str:
    text = str(value)
    text = text.replace("Ã‚Â±", "±")
    text = text.replace("Â±", "±")
    text = text.replace("Ä…", "±")
    return text


def make_final_metrics_figure(df: pd.DataFrame) -> None:
    df = df.copy()
    df = df.rename(columns={"Modelo": "display_name"})
    plot_cols = ["Macro F1", "Bal. Acc.", "Acc."]
    available = [c for c in plot_cols if c in df.columns]
    if not available:
        print("[AVISO] No hay columnas suficientes para la figura final de métricas.")
        return

    def parse_mean(text):
        token = normalize_pm(text).split("±")[0].strip()
        return float(token)

    fig, axes = plt.subplots(1, len(available), figsize=(6 * len(available), 5))
    if len(available) == 1:
        axes = [axes]

    colors = [PALETTE["primary"], PALETTE["secondary"], PALETTE["accent"]]
    for ax, metric, color in zip(axes, available, colors):
        means = [parse_mean(v) for v in df[metric]]
        bars = ax.bar(df["display_name"], means, color=color)
        ax.set_title(metric)
        ax.set_ylim(0, 1.0)
        ax.set_xticks(range(len(df)))
        ax.set_xticklabels(df["display_name"], rotation=25, ha="right")
        for bar, label in zip(bars, df[metric]):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.01,
                normalize_pm(label),
                ha="center",
                va="bottom",
                fontsize=8,
            )

    fig.suptitle("Comparación final de métricas", fontsize=14)
    fig.tight_layout()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / "final_metrics_comparison.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def make_m3_learning_curves(df: pd.DataFrame) -> None:
    required = {"loss", "val_loss", "train_macro_f1", "val_macro_f1", "val_balanced_accuracy", "val_kappa"}
    missing = required.difference(df.columns)
    if missing:
        print(f"[AVISO] Faltan columnas en el histórico de M3: {sorted(missing)}")
        return

    epochs = range(len(df))
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("M3: ResNet50 ImageNet deep", fontsize=18)

    axes[0].plot(epochs, df["loss"], label="train", color=PALETTE["primary"])
    axes[0].plot(epochs, df["val_loss"], label="val", color=PALETTE["secondary"])
    axes[0].set_title("Loss")
    axes[0].set_xlabel("Epoch")
    axes[0].legend()

    axes[1].plot(epochs, df["train_macro_f1"], label="train", color=PALETTE["primary"])
    axes[1].plot(epochs, df["val_macro_f1"], label="val", color=PALETTE["secondary"])
    axes[1].set_title("Macro F1")
    axes[1].set_xlabel("Epoch")
    axes[1].legend()

    axes[2].plot(epochs, df["val_macro_f1"], label="val Macro F1", color=PALETTE["primary"])
    axes[2].plot(epochs, df["val_balanced_accuracy"], label="val Balanced Acc.", color=PALETTE["secondary"])
    axes[2].plot(epochs, df["val_kappa"], label="Val Kappa", color=PALETTE["accent"])
    axes[2].set_title("validation metrics")
    axes[2].set_xlabel("Epoch")
    axes[2].legend()

    fig.tight_layout()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / "m3_learning_curves.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    results_df = read_csv_safe(RESULTS_CSV)
    history_df = read_csv_safe(M3_HISTORY_CSV)
    if results_df is not None:
        results_df = results_df.apply(lambda col: col.map(normalize_pm))
        make_final_metrics_figure(results_df)
    if history_df is not None:
        make_m3_learning_curves(history_df)
    print(f"Figuras guardadas en: {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
