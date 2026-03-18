# Contributing Guide

## Scope
This repository contains public-facing FAQs for Techstorm Semiconductor TS8001/TS8010 BLE chips.

## How to contribute
- **Fix typos / clarify wording**: small PRs welcome.
- **Add a new FAQ**: place it in the correct top-level folder (`01-` … `04-`).
- **Improve AI retrieval assets**: update files under `05-AI适配工具/`.

## Writing conventions (recommended)
Each FAQ should include:
- **问题现象**
- **影响范围**（芯片/SDK/固件/主机系统）
- **根因分析**
- **排查步骤**（从易到难）
- **解决方案**
- **验证方法**

## Naming conventions
- TS8001 specific: `ts8001-*.md`
- TS8010 specific: `ts8010-*.md`
- Shared: `ts-*.md`

## Quality checklist
- No customer secrets or private logs
- Steps are reproducible and ordered
- Parameters have units and ranges where applicable
- Include expected results in verification steps
