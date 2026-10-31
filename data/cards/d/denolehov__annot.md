# denolehov/annot

⭐ 17 · Rust · AGPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/denolehov/annot) · 个人维护

**给人机协同 AI 工作流的结构化标注审核工具**

面向 human-in-the-loop AI 工作流的本地标注审核工具：以 Tauri 桌面应用形式打开代码文件、git/jj diff 或 agent 生成的 markdown，用户点选行区间撰写批注，可编织语义标签（[# VERIFY]）并选择退出模式（Apply/Reject 等），关闭窗口后以 LLM 可读文本或 JSON 形式返回结构化反馈。内置 MCP 服务器（review_file/review_diff/review_content），供 Claude Code 等 agent 调用；也可独立 CLI 使用。本地运行，无账号无云端。macOS 提供 brew 安装，Linux/Windows 需源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件/diff/markdown 审核窗口，行级批注与语义标签
- MCP 工具 review_file / review_diff / review_content 供 agent 调用
- 退出模式（Apply/Reject/自定义）向 agent 传递意图
- 本地运行，无云端无账号，支持 git 与 jj

## 适用场景

- 我在 AI agent 提交改动前逐行给出精确反馈
- 让 Claude Code 在审核窗口里等我的结构化批注
- 对 agent 生成的计划或草稿做带标签的评审

## 场景标签

 · 领域:开发者工具/AI 工作流

## 证据(README 行号)

> L108: claude mcp add --scope user annot annot mcp
> L191: ### `review_file`

## 星数曲线

```mermaid
xychart-beta
    title "denolehov/annot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `edebcee51a51` · [字段定义](../../DATASET.md)*
