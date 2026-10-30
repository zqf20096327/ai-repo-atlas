# zdt1013/wen-ai-cli

⭐ 15 · Go · 推送 2026-01-23 · [GitHub](https://github.com/zdt1013/wen-ai-cli) · [官网](https://github.com/zdt1013/wen-ai-cli) · 个人维护 · 中文 README

**面向服务器运维的 CLI，用自然语言查找并执行系统命令**

用 Go 编写的命令行工具，面向服务器运维与个人主机管理用户。通过配置 API 密钥与模型接入大模型，提供单轮提问、多轮对话和 man 模式三种交互：用自然语言描述需求获取命令建议，智能解析命令手册，感知当前工作环境。支持 Linux/macOS/Windows（arm、amd）平台与中英文界面，可通过安装脚本下载二进制或本地编译安装；需自行配置 API 密钥、baseUrl 与模型参数。未来计划包含 functioncall、mcp 支持与用户知识库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单轮提问、对话模式与 wen man 命令手册智能查询三种交互方式
- 跨平台支持 Linux/macOS/Windows（arm、amd 架构）
- 智能感知当前工作环境，内置中英文国际化
- 基于 cloudwego/eino 与 go-openai 客户端接入大模型

## 适用场景

- 运维时用自然语言快速查找系统命令
- 通过对话式 AI 获取命令执行方案
- 用大模型查询和解读命令手册（替代原生 man 场景）

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: 问AI (Wen AI) CLI是一个专为服务器运维和个人主机管理设计的CLI工具，通过集成AI能力，帮助用户快速查找和执行系统命令，提升运维效率。它能够智能解析用户需求，提供精准的命令建议和执行方案，是运维人员的得力助手。
> L9: - 🤖 智能对话：支持与AI进行自然语言对话，快速查找应用命令
> L103: > wen config --apiKey YOUR_API_KEY --baseUrl YOUR_API_BASE --model YOUR_API_MODEL

## 星数曲线

```mermaid
xychart-beta
    title "zdt1013/wen-ai-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `09206bad6442` · [字段定义](../../DATASET.md)*
