# Drlinglong/Remis

⭐ 30 · Python · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/Drlinglong/Remis) · [官网](https://drlinglong.github.io/Remis/) · 个人维护 · 中文 README

**AI 游戏模组本地化桌面系统：术语感知翻译与人工审核**

基于 Tauri 2 + React 19 + FastAPI + SQLite 的 Windows 桌面应用，面向 Paradox 游戏、Surviving Mars: Relaunched（稳定）及 RimWorld、Project Zomboid（预览）的模组本地化。功能包括：解析游戏文件、组装项目与术语上下文、编排云端或本地模型（Ollama/LM Studio/vLLM 等 OpenAI 兼容端点）、对模型输出做确定性格式校验与有界修复循环、翻译记忆增量复用，以及部署前人工审核。项目文件与状态保存在用户本机。另提供 localhost Agent API、Codex 集成与内置 Copilot，写操作需用户批准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 provider 推理：商业 API 与 Ollama/LM Studio/vLLM 等 OpenAI 兼容端点
- 确定性格式校验 + 修复代理循环，写操作需人工批准
- 增量翻译与翻译记忆复用，仅变更条目重走模型管线
- Model Arena 匿名对比 2-3 个配置模型的翻译质量

## 适用场景

- 为 Paradox 等游戏的模组做多语言翻译并保持术语一致
- 模组更新后复用已审核翻译，只重译变更内容
- 在本机编排本地或云端 LLM 执行批量翻译并校验格式
- 通过 Codex 等 agent 以审批制方式操作本地化流程

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L6:  An open-source, AI-native desktop system for glossary-aware, validated,
> L30: Remis is not a thin prompt wrapper. It is a full localization control plane for parsing game files, assembling proj
> L32: Project files, glossaries, checkpoints, translation history, and review state are managed on the user's machine. In

## 星数曲线

```mermaid
xychart-beta
    title "Drlinglong/Remis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-29 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ffc006a36b1e` · [字段定义](../../DATASET.md)*
