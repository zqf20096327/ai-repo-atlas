# pulkitsharma07/solipsist

⭐ 5 · TypeScript · NOASSERTION · 推送 2026-11-16 · [GitHub](https://github.com/pulkitsharma07/solipsist) · [官网](https://solipsist.sh) · 个人维护

**在本地 Markdown 文档中与 AI agent 协作写作的编辑器**

一个基于 TipTap 的 Markdown 编辑器，用户在写作时通过光标处快捷键向内置 agent（Pi）发起请求：改写选中文本、页面内研究检索、整页审阅留批注，agent 结果以建议形式等待用户接受或拒绝，不直接改动原文。文件保存在本地 .solipsist/ 目录，需手动同步；无账号、无遥测。安装脚本提供 macOS/Linux/Windows 安装包，也可用 Bun 从源码运行；模型经 OpenRouter 或 Pi 登录接入。agent 可在本机执行命令且未做沙箱隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 光标处/选中文本发起 agent 请求，结果以建议形式呈现，由用户决定是否接受
- 每个任务独立 agent，可并行运行并支持保存为可重复执行的按钮或定时任务
- 文件以副本方式工作，手动 Sync to file 才落盘，带冲突检测
- 无账号、无分析、无遥测，数据留在本机

## 适用场景

- 写作时让 AI 改写、润色选中的段落
- 在笔记页面内直接让 agent 检索并整理研究资料
- 让 agent 通读整页并在页边提出问题做审阅

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3:  Think, work, collaborate with your local AI agents in your markdown docs. They suggest; you decide.
> L38: - **Ask at the cursor or about a selection.** Press `Mod-.` and say what you want. An agent works in the background

## 星数曲线

```mermaid
xychart-beta
    title "pulkitsharma07/solipsist 星数(近 3 点)"
    x-axis ["2026-11-18", "2026-11-22", "2026-11-23"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-18 4 → 2026-11-23 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7779b3084139` · [字段定义](../../DATASET.md)*
