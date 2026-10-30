# mnvsk97/eyeroll

⭐ 19 · Python · MIT · 推送 2026-05-14 · [GitHub](https://github.com/mnvsk97/eyeroll) · [官网](https://mnvsk97.github.io/eyeroll) · 个人维护

**让编码 agent 观看视频/截图并据此修 bug 的 Claude Code 插件**

eyeroll 是一个 Claude Code 插件，同时提供独立 CLI：读取屏幕录制、Loom/YouTube 链接和截图，调用多模态后端（Gemini、TwelveLabs、OpenAI、Ollama 等 9 种）生成结构化分析（展示内容、bug、证据、建议修复），并可执行 watch→诊断→修代码→提 PR 的流程。支持自动发现 CLAUDE.md 等代码库上下文、帧分析缓存与成本估算。面向使用 Claude Code 等 agent 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种后端可选（含本地 Ollama 免费离线）
- /eyeroll:fix 从 bug 视频到诊断、修复、提 PR 的完整链路
- 支持 13 种视频格式、9 种图片格式及 1000+ 站点 URL（经 yt-dlp）
- 帧分析与转录结果全局缓存，重复视频不重复分析

## 适用场景

- 录屏复现 bug 后让 agent 直接定位并提交修复
- 分析 Loom/YouTube 演示视频生成结构化摘要
- 离线（Ollama 后端）分析屏幕录制

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: eyeroll is a Claude Code plugin that analyzes screen recordings, Loom videos, YouTube links, and screenshots, then 
> L74: ## Backends

## 星数曲线

```mermaid
xychart-beta
    title "mnvsk97/eyeroll 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ad8d43e433fe` · [字段定义](../../DATASET.md)*
