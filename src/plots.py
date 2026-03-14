from __future__ import annotations

import logging
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger(__name__)

# Set default style
sns.set_theme(style="whitegrid")


def save_figure(fig: plt.Figure, path: Path | str, dpi: int = 150) -> None:
    """Save a matplotlib figure to disk."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    logger.info("Figure saved to %s", path)
    plt.close(fig)
