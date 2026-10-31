# helloxz/zlite

⭐ 14 · Go · AGPL-3.0 · 推送 2026-08-21 · [GitHub](https://github.com/helloxz/zlite) · [官网](https://note.xiaoz.top/doc/zlite) · 个人维护 · 中文 README

**轻量命令行 AI agent：对话、写代码、自然语言管理服务器**

单文件二进制的 CLI AI agent，体积小于 12MB、内存占用约 20MB，支持 Linux/macOS/Windows。面向日常对话与轻量编码用户，也可作为服务器管理的 agent 大脑，通过自然语言操作 nginx 等服务。可接入任意 OpenAI 或 Anthropic 兼容模型并随时切换，提供 TUI 界面、内置文件/Shell/网页工具、MCP 与 ACP 协议支持、上下文自动压缩与危险操作人工确认机制。通过脚本安装，也可用 Go 1.25+ 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件二进制，<12MB 体积、≈20MB 内存占用
- 兼容任意 OpenAI/Anthropic 兼容模型，多供应商随时切换
- 内置文件读写、Shell 命令、网页抓取/搜索等工具
- MCP、ACP 协议支持与危险操作人工确认

## 适用场景

- 在终端里做日常对话与轻量编码
- 通过自然语言让 agent 操作和排查服务器软件
- 作为 ACP 客户端（如 Zed）的 agent 后端

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L5: Zlite is a lightweight CLI AI agent — small footprint, low memory usage. It's great for everyday conversations and l
> L13: * **Multi-model support**: works with any OpenAI- or Anthropic-compatible model; configure multiple providers and s

## 星数曲线

```mermaid
xychart-beta
    title "helloxz/zlite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `54c8f9f5d35a` · [字段定义](../../DATASET.md)*
