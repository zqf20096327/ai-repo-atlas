# moly-ai/moly-ai

⭐ 423 · Rust · Apache-2.0 · 推送 2026-03-27 · [GitHub](https://github.com/moly-ai/moly-ai) · [官网](https://moly-ai.github.io/moly-ai/) · 组织维护

**纯 Rust 编写的本地+云端 LLM 多平台 GUI 客户端**

Moly 是用 Rust 编写、基于 Makepad UI 与 Robius 框架的 AI LLM 客户端，面向普通使用者与 Rust 开发者。支持三类提供方：OpenAI 兼容云端 API（经 Providers Dashboard 配置）、自带的 Moly Server 本地 LLM 后端（搜索/下载/本地运行开源模型，OpenAI 兼容 API）、以及 MoFa 框架构建的 AI agent 服务。构建产物覆盖 macOS/Linux/Windows/Web/Android/iOS 六端，提供预编译发布包（.dmg/.deb/AppImage/.exe 等），也可从源码 cargo 编译。README 自述处于早期开发阶段，遇 bug 请提 issue。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 纯 Rust 实现，一个代码库构建六端（含 Web/Android/iOS）
- Moly Server 本地后端：搜索、下载并本地运行 OSS LLM（OpenAI 兼容 API）
- 可连接 MoFa 框架构建的 AI agent（Dora 节点暴露 OpenAI 兼容接口）
- OpenAI 兼容提供方通过 Providers Dashboard 配置，可扩展自定义 provider

## 适用场景

- 在一个桌面/移动应用中同时使用云端 API 与本地开源模型对话
- 本地下载并运行 OSS LLM，不依赖云端服务
- 通过 MoFa 服务与 AI agent 交互
- 作为 Makepad/Robius 多平台 Rust 应用开发的参考实现

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: Moly is an AI LLM client written in Rust, that demonstrates the power of the Makepad UI toolkit and Project Robius, 
> L39: 2. **Moly Server**: a local LLM backend that allows exploring, downloading and running OSS LLMs locally. For usage 
> L44: Moly Server is a local HTTP server which provides capabilities for searching, downloading, and running local LLMs o

## 星数曲线

```mermaid
xychart-beta
    title "moly-ai/moly-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 422 --> 424
    line [423, 423]
```

2026-10-18 423 → 2026-10-26 423（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `05d4ed2f351f` · [字段定义](../../DATASET.md)*
