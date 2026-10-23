# Blushyes/coro-code

⭐ 369 · Rust · 推送 2025-10-30 · [GitHub](https://github.com/Blushyes/coro-code) · [官网](https://sofast.fun) · 个人维护 · 中文 README

**Rust 编写的终端 AI 编码 Agent，生成与调试代码**

用 Rust 实现的命令行 AI 编码代理，前身为 Trae Agent Rust，保持与原工具 spec 兼容。提供交互式终端 UI、单任务模式、bash 执行与文件操作等内置工具，支持上下文导出/恢复（JSON 快照）与 token 压缩。模型接入方面 OpenAI 协议已可用（含通过 base_url 接入 OpenAI 兼容 API 如 DeepSeek），Anthropic 与 Google 在路线图标注 Coming Soon；通过环境变量或 coro.json 配置。安装需 Rust 1.70+，使用 cargo install 从 git 构建。

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

- 内置 bash 执行、文件操作与可扩展工具系统
- 多协议 LLM 配置：OpenAI 可用，Anthropic/Google 标注 Coming
- 对话与执行上下文可导出为 JSON 并恢复
- 智能 token 压缩与自适应上下文窗口

## 适用场景

- 在终端中让 AI 代理修复 bug、生成代码
- 通过自定义 base_url 接入 OpenAI 兼容 API（如 DeepSeek）
- 导出并恢复代理会话上下文以便继续任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: _A high-performance AI coding agent written in Rust with a rich terminal UI_
> L12: Coro Code is a high-performance AI coding agent written in Rust with a rich terminal UI. Formerly known as **Trae A
> L19: - 🛠️ **Powerful Tools**: Built-in bash execution, file operations, and extensible tool system

## 星数曲线

```mermaid
xychart-beta
    title "Blushyes/coro-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 368 --> 370
    line [369, 369]
```

2026-10-18 369 → 2026-10-23 369（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8038514df442` · [字段定义](../../DATASET.md)*
