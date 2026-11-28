# Hive-Academy/PtahCode

⭐ 35 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Hive-Academy/PtahCode) · [官网](https://ptah.live) · 组织维护

**Electron 桌面端 AI 编排中枢：统一调度 Claude、Codex 等编码 CLI**

面向开发者的 Electron 桌面应用（Windows/macOS/Linux），以 Provider 无关方式编排多个编码代理：主聊天可跑 Claude agent runtime 或 Codex app-server，后台运行已安装的 CLI（claude、codex、copilot、cursor 等）及 API 提供商（Kimi、GLM、DeepSeek、Ollama 等）。机制包括任务分类加 90 天本地成绩矩阵的路由决策、每工作区会话轨（最多 20 块、9 个并发）、本地项目记忆（BM25+向量+RRF 融合）、tree-sitter 索引、成本与计划窗口门控、Telegram/Discord/Slack 网关与本地定时任务。语音需配置 STT/TTS 引擎方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主聊天双运行时：Claude agent runtime 或 Codex app-server 协议
- 路由决策：任务分类 + 90 天本地通过/失败矩阵 + 硬规则（同族模型不得审查自身实现）
- 本地项目记忆：BM25 与向量检索经倒数排名融合，sqlite-vec 缺失时回退 BM25
- tree-sitter 索引覆盖 TypeScript/Python/Go/Rust 等 12 类语言

## 适用场景

- 在一个桌面端统一管理并调度多家编码 CLI 与 API 代理
- 为每个工作区维护本地记忆与代码索引，支撑多代理协作
- 通过 Telegram/Discord/Slack 远程接管桌面会话并审批工具调用
- 按会话/模型/代理查看 token 与成本账目

## 场景标签

`编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **An Electron desktop for Claude, Codex, and the coding CLIs already on your machine.**
> L36: - **Two main-chat runtimes.** Claude’s agent runtime, or Codex through the app-server protocol. Background work can
> L67: - **CLI lanes.** Supervised processes include `claude`, `codex`, `copilot`, `cursor`, `antigravity`, `opencode`, `g

## 星数曲线

```mermaid
xychart-beta
    title "Hive-Academy/PtahCode 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-20", "2026-11-28"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-11-08 34 → 2026-11-28 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `9a927238c175` · [字段定义](../../DATASET.md)*
