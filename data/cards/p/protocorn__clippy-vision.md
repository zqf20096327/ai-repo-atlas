# protocorn/clippy-vision

⭐ 20 · Python · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/protocorn/clippy-vision) · [官网](https://github.com/protocorn/clippy-vision/releases/latest) · 个人维护

**本地屏幕活动记录与检索助手，供 MCP 客户端查询**

Windows 优先的桌面应用（macOS/Linux 支持不完整或实验性）：持续捕获前台窗口、剪贴板、打字指标与截图，在本地做摘要并构建可检索的长期活动历史；通过 MCP 协议接入 Cursor、Claude Desktop、VS Code、LM Studio 等客户端，让 agent 回答“我之前在做什么”类问题。隐私机制包括本地化处理、可暂停捕获、时间线删除与尽力脱敏（含隐私浏览检测）。需系统 PATH 上有 Python 3.11+（安装包不捆绑），首次运行需联网下载模型（如 qwen3:8b 约 4.7 GB）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 捕获前台窗口/剪贴板/打字指标/截图并本地摘要，构建可检索活动历史
- 通过 MCP 接入 Claude Desktop、Cursor、VS Code、LM Studio 等客户端
- 隐私控制：本地运行、暂停捕获、时间线删除、尽力脱敏与隐私浏览检测
- 时间线界面供审查与删除已存活动记录

## 适用场景

- 询问自己之前在电脑上做过什么（如浏览过的酒店、遇到的报错）
- 让 Cursor/Claude Desktop 等 agent 基于屏幕活动历史回答问题，无需手动粘贴上下文
- 在不上传云端的前提下保留并检索本地工作活动记录

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: Clippy Vision watches your work on this computer, stores a searchable activity history locally, and lets you ask abo
> L92: - Clippy captures foreground windows, clipboard, typing metrics, and screenshots.
> L93: - Capture, summarization, and storage run locally on this computer.

## 星数曲线

```mermaid
xychart-beta
    title "protocorn/clippy-vision 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b369da76b570` · [字段定义](../../DATASET.md)*
