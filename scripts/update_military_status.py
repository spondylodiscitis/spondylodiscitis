from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ENLISTMENT_DATE = date(2026, 8, 18)
DISCHARGE_DATE = date(2028, 4, 17)

README_PATH = Path("README.md")

START_MARKER = "<!-- MILITARY_STATUS_START -->"
END_MARKER = "<!-- MILITARY_STATUS_END -->"


def make_progress_bar(progress: float, width: int = 20) -> str:
    filled = round(width * progress / 100)
    filled = max(0, min(width, filled))
    return "█" * filled + "░" * (width - filled)


def build_status(today: date) -> str:
    if DISCHARGE_DATE <= ENLISTMENT_DATE:
        raise ValueError("전역일은 입대일보다 늦어야 합니다.")

    if today < ENLISTMENT_DATE:
        remaining_days = (ENLISTMENT_DATE - today).days

        return f"""<!-- MILITARY_STATUS_START -->
### ⚓ Republic of Korea Navy

**입대까지 D-{remaining_days}**

- 입대일: `{ENLISTMENT_DATE.isoformat()}`
- 전역 예정일: `{DISCHARGE_DATE.isoformat()}`
- 예정 보직: **인공지능개발병**

> Preparing to serve as an Artificial Intelligence Development Specialist in the Republic of Korea Navy.
<!-- MILITARY_STATUS_END -->"""

    if today == ENLISTMENT_DATE:
        return f"""<!-- MILITARY_STATUS_START -->
### ⚓ Republic of Korea Navy

**오늘 입대합니다.**

- 입대일: `{ENLISTMENT_DATE.isoformat()}`
- 전역 예정일: `{DISCHARGE_DATE.isoformat()}`
- 보직: **인공지능개발병**

> Beginning mandatory military service in the Republic of Korea Navy.
<!-- MILITARY_STATUS_END -->"""

    if today < DISCHARGE_DATE:
        total_days = (DISCHARGE_DATE - ENLISTMENT_DATE).days
        elapsed_days = (today - ENLISTMENT_DATE).days
        remaining_days = (DISCHARGE_DATE - today).days
        progress = elapsed_days / total_days * 100
        progress = max(0.0, min(100.0, progress))
        progress_bar = make_progress_bar(progress)

        return f"""<!-- MILITARY_STATUS_START -->
### ⚓ Republic of Korea Navy

**전역까지 D-{remaining_days}**

```text
{progress_bar} {progress:.1f}%
```

- 입대일: `{ENLISTMENT_DATE.isoformat()}`
- 전역 예정일: `{DISCHARGE_DATE.isoformat()}`
- 복무 경과: `{elapsed_days:,} / {total_days:,}일`
- 보직: **인공지능개발병**

> Serving as an Artificial Intelligence Development Specialist in the Republic of Korea Navy.
<!-- MILITARY_STATUS_END -->"""

    if today == DISCHARGE_DATE:
        return f"""<!-- MILITARY_STATUS_START -->
### ⚓ Republic of Korea Navy

**오늘 전역합니다.**

- 입대일: `{ENLISTMENT_DATE.isoformat()}`
- 전역일: `{DISCHARGE_DATE.isoformat()}`
- 복무 보직: **인공지능개발병**

> Mandatory military service completed.
<!-- MILITARY_STATUS_END -->"""

    elapsed_days = (today - DISCHARGE_DATE).days

    return f"""<!-- MILITARY_STATUS_START -->
### ⚓ Republic of Korea Navy

**전역 D+{elapsed_days}**

- 입대일: `{ENLISTMENT_DATE.isoformat()}`
- 전역일: `{DISCHARGE_DATE.isoformat()}`
- 복무 보직: **인공지능개발병**
- 상태: **Military service completed**

> Completed mandatory military service in the Republic of Korea Navy.
<!-- MILITARY_STATUS_END -->"""


def update_readme(today: date) -> None:
    if not README_PATH.exists():
        raise FileNotFoundError(f"README 파일을 찾을 수 없습니다: {README_PATH}")

    content = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in content or END_MARKER not in content:
        raise RuntimeError(
            "README.md에 다음 마커가 필요합니다:\n"
            f"{START_MARKER}\n"
            f"{END_MARKER}"
        )

    before, remainder = content.split(START_MARKER, maxsplit=1)
    _, after = remainder.split(END_MARKER, maxsplit=1)

    updated = (
        before.rstrip()
        + "\n\n"
        + build_status(today)
        + "\n\n"
        + after.lstrip()
    )

    README_PATH.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    korea_today = datetime.now(ZoneInfo("Asia/Seoul")).date()
    update_readme(korea_today)
