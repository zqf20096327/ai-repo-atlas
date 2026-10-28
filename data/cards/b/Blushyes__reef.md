# Blushyes/reef

⭐ 84 · Rust · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/Blushyes/reef) · [官网](https://blushyes.github.io/reef-site) · 个人维护 · 中文 README

**面向 AI 编码时代的单二进制开发终端：浏览、审查、提交代码**

用 Rust 编写的单二进制终端工作台，面向让 AI 写代码、本工具负责其余环节的开发者。功能包括：文件树与只读预览（语法高亮、行内图片、视频首帧预览）、SQLite 数据库浏览、基于 ripgrep 的搜索、Git 状态/暂存/diff/推送、提交 DAG 图、电子表格预览。支持本地与 SSH 远程（自动部署 reef-agent 守护进程），保持同一 UI 与键位。声明为 Alpha 阶段、无插件系统、无编辑器与自动补全。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 本地与 SSH 远程功能对等，远程经自动部署的 reef-agent 守护进程
- 文件/视频/SQLite/电子表格预览与 ripgrep 搜索、Git 操作、提交 DAG 图
- 单 Rust 二进制，macOS/Linux/Windows 多架构支持，npm 一键安装

## 适用场景

- AI 生成代码后，在终端中浏览、审查 diff 并完成提交
- 通过 SSH 在远程机器上用同一 UI 浏览与审查代码
- 快速查看 SQLite 数据库与电子表格文件内容

## 场景标签

 · 领域:开发工具/终端

## 证据(README 行号)

> L3: > **The minimal dev terminal for the AI coding era**
> L5: When AI writes your code, 90% of an IDE becomes dead weight. Reef is the other 10%.
> L10: A single-binary terminal workbench for browsing, reviewing, and shipping — locally or over SSH. No editor, no autoc

## 星数曲线

```mermaid
xychart-beta
    title "Blushyes/reef 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 82 --> 85
    line [83, 84, 84]
```

2026-10-18 83 → 2026-10-28 84（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9ee254f8f888` · [字段定义](../../DATASET.md)*
