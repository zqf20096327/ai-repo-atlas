# GabrieleLozupone/adni-download-guide

⭐ 3 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/GabrieleLozupone/adni-download-guide) · [官网](https://gabrielelozupone.github.io/adni-download-guide/) · 个人维护

**ADNI 阿尔茨海默影像数据集的下载步骤指南与辅助脚本**

面向从未使用过 LONI IDA 的机器学习研究者的 ADNI 数据集获取指南：覆盖阅读 DUA、申请账户、下载临床表格、筛选影像 ID、建立 collection 下载 ZIP、校验与转 BIDS 六个步骤，并列出常见易错点。附可选的无依赖 Python 辅助脚本（拆分 ID 列表、断点续传、BIDS 转换），并支持用编码类 AI agent 引导完成流程。不含任何数据，需自备已获批的 ADNI 账户，需 Python 3.8+ 与 curl。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 DUA 到 BIDS 转换的完整分步流程与时间估算
- 可选无依赖辅助脚本：ID 列表拆分、断点续传、ida_to_bids.py 转换
- 支持 AI agent 引导：AGENTS.md、CLAUDE.md 与两个 Claude Code skills
- 强调数据合规：禁止将 ADNI 数据输入第三方 AI 工具

## 适用场景

- 首次申请 ADNI 账户并下载 MRI/PET 与临床表格
- 整理下载的影像并转换为 BIDS 格式用于深度学习研究
- 让 AI coding agent 逐步引导完成下载流程

## 场景标签

`教程课程` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: A plain, step-by-step guide to getting **ADNI** (Alzheimer's Disease Neuroimaging Initiative) data (clinical tables 
> L6: **LONI Image & Data Archive (IDA)**, written for machine-learning and deep-learning researchers who have never used
> L52: ## Using an AI agent as your guide (optional)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c44890773c0b` · [字段定义](../../DATASET.md)*
