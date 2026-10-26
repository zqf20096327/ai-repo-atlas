# Iamsdt/chess

⭐ 31 · JavaScript · 推送 2026-10-12 · [GitHub](https://github.com/Iamsdt/chess) · [官网](https://iamsdt.github.io/chess/) · 个人维护

**浏览器内 AI 国际象棋训练平台：引擎分析+LLM 讲解**

基于 React 19 + Vite 6 的网页国际象棋训练应用：Stockfish 18 编译为 WebAssembly 在浏览器本地运行引擎分析（Multi-PV、评估条、最佳着法、威胁检测），并用 Gemini 与 GPT-4o 提供对话式教练讲解、候选着法与战术思路说明。含 44 道战术题、54 条开局线、21 个残局场景训练与整局分析（着法质量分级）。无 API key 时引擎分析与训练功能可离线使用，AI 讲解需配置密钥。通过 git clone + npm 从源码运行，另含 GitHub Pages 部署工作流。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Stockfish 18 以 WASM 在浏览器本地运行引擎分析，无需服务器
- Gemini + GPT-4o 提供对话式教练与人类化着法讲解
- 战术题/开局/残局训练与整局分析（着法分为五级质量）
- 内置 Minimax + Alpha-Beta 剪枝的自定义对弈引擎

## 适用场景

- 对弈时获得每步棋的实时评估与 AI 讲解
- 通过战术题、开局和残局训练提升棋力
- 复盘整局棋并定位失误着法

## 场景标签

 · 领域:游戏/棋类训练

## 证据(README 行号)

> L5: Train like a Grandmaster using **Stockfish 18 + AI coaching (Gemini & GPT-4o)**.
> L28: The application runs **entirely in the browser**, using WebAssembly for engine analysis and modern AI models for na
> L83: All analysis runs **locally in your browser** without server calls.

## 星数曲线

```mermaid
xychart-beta
    title "Iamsdt/chess 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b6d50e13f544` · [字段定义](../../DATASET.md)*
