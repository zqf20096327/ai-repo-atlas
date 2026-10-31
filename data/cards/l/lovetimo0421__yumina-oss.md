# lovetimo0421/yumina-oss

⭐ 14 · TypeScript · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/lovetimo0421/yumina-oss) · 个人维护

**AI 原生互动叙事引擎：让模型驱动游戏世界状态与界面**

开源互动叙事引擎，最初是 SillyTavern 与 Godot 的集成 fork，现为独立引擎、编辑器与播放器。创作者在 world 文件中以数据声明故事条目、类型化变量、规则/反应、空间/战斗/多 agent 等系统、界面组件与音频轨道；模型不执行代码，只发出指令（如 [variable: op value]、[audio: track play]），由引擎应用效果并重新渲染界面。支持导入 V2/V3 角色卡与 worldbook，本地版单用户免登录。需 Node.js 22+ 与 pnpm，另提供 Docker 镜像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- world 文件声明式架构：故事/状态/规则/系统/界面/音频均为数据
- 模型仅发出指令、由引擎应用，含沙箱 iframe 内 React 自定义界面
- 会话记忆、分支、回溯与检查点内置
- 支持导入社区 V2/V3 角色卡与 worldbook，导出 PNG 卡

## 适用场景

- 制作 AI 驱动的互动小说、视觉小说或游戏原型
- 在本地自托管运行互动叙事世界并接入自有模型 key
- 通过导入社区角色卡复用现有创作资产

## 场景标签

 · 领域:游戏/互动叙事

## 证据(README 行号)

> L3: An open-source engine for AI-native interactive fiction. Yumina is a toolset that allows creators to use AI as a gam
> L5: Yumina started as a personal project - a fork of SillyTavern, integrated with the Godot game engine, that let AI con
> L11: Everything below is data in a world file. The model never executes code; it emits directives, and the engine applie
> L59: Keys are added in the app, not in config files. Supported: OpenRouter, Anthropic, OpenAI, Google, Ollama (local, de

## 星数曲线

```mermaid
xychart-beta
    title "lovetimo0421/yumina-oss 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `bbbd5e7df39e` · [字段定义](../../DATASET.md)*
