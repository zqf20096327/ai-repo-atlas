# groundgrounder/Hortus

⭐ 7 · Rust · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/groundgrounder/Hortus) · 个人维护 · 中文 README

**面向 AI agent 的原生 macOS Markdown 知识库阅读器**

以阅读优先的 macOS 原生 Markdown 知识库查看器：打开普通 Markdown 文件夹（兼容 Obsidian vault），内置终端与 agent 标签页可在 vault 根目录运行命令行 agent，启动 agent 前自动做全库快照（APFS 写时复制），支持在 Changes 面板按 hunk/文件/会话回滚。用 Rust 核心原生解析渲染 Mermaid（分栏排版大图）与 LaTeX 数学（RaTeX/Core Text）。架构为 Rust workspace 加 Swift/AppKit/SwiftUI 前端，经 UniFFI 桥接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 启动前自动全库快照，支持 hunk/文件/会话级回滚
- Rust 原生渲染 Mermaid，宽 mindmap 自动分栏且可折叠
- RaTeX/Core Text 原生排版行内与块级 LaTeX 公式
- 扫描 PATH 探测已装 agent CLI（omp/codex/claude/gemini 等）一键配置

## 适用场景

- 让命令行 agent 编辑笔记，同时保留快照与回滚安全网
- 在原生应用中阅读含大型 Mermaid 图和数学公式的知识库
- 直接打开既有 Obsidian vault 而不写入应用状态

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L4: Hortus is a native macOS Markdown knowledge viewer built for reading alongside AI agents. Open your notes directly, 
> L39: - Before launching an agent, Hortus captures a full-vault snapshot (using APFS copy-on-write clones where supported
> L40: - Open **Settings (`⌘,`) → Agent** to scan your login shell `PATH` and common macOS directories for installed CLIs 

## 星数曲线

```mermaid
xychart-beta
    title "groundgrounder/Hortus 星数(近 3 点)"
    x-axis ["2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-11-22 6 → 2026-11-24 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `5542fd11a999` · [字段定义](../../DATASET.md)*
