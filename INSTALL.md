# 설치 방법

저장소 루트에 다음 구조로 업로드하세요.

```text
spondylodiscitis/
├── README.md
├── scripts/
│   └── update_military_status.py
└── .github/
    └── workflows/
        └── update-military-status.yml
```

## 웹에서 업로드할 때

1. 기존 `README.md`를 새 파일로 교체합니다.
2. `Add file → Create new file`을 선택합니다.
3. 파일명에 `scripts/update_military_status.py`를 입력하고 스크립트 내용을 붙여 넣습니다.
4. 다시 새 파일을 만들어 `.github/workflows/update-military-status.yml`을 입력합니다.
5. 저장소의 `Actions` 탭으로 이동합니다.
6. `Update military countdown`을 선택합니다.
7. `Run workflow`를 눌러 최초 1회 수동 실행합니다.

## 권한 오류가 발생할 때

저장소에서 다음 설정을 확인하세요.

```text
Settings
→ Actions
→ General
→ Workflow permissions
→ Read and write permissions
```

변경 후 `Save`를 누르고 workflow를 다시 실행합니다.

## 주의

README의 아래 마커는 삭제하면 안 됩니다.

```markdown
<!-- MILITARY_STATUS_START -->
<!-- MILITARY_STATUS_END -->
```

스크립트는 두 마커 사이의 내용만 매일 교체합니다.
