# xrip/tinycode

⭐ 25 · TypeScript · 推送 2026-01-11 · [GitHub](https://github.com/xrip/tinycode) · 个人维护

**单文件 AI 编程助手，调用 Claude 完成代码读写与命令执行**

用 TypeScript 编写的单文件（约 345 行、零依赖）命令行 AI 编程助手，依赖 Bun 运行时，通过 Claude API 的工具调用能力操作代码：内置 read/write/edit/glob/grep/exec/list/delete/move/copy 共 10 个工具，支持实时命令输出、token 用量统计、系统上下文注入（OS/时区/工作目录）与自动忽略常见目录。通过环境变量配置 API 端点、模型与 key，可自定义 API_URL。项目自我定位为极简、教育性质。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件约 345 行、零依赖，仅用 Bun API
- 10 个内置工具覆盖文件操作、正则搜索与 shell 执行
- 通过环境变量自定义 API_URL/MODEL/API key
- 实时流式命令输出与 token 用量统计

## 适用场景

- 在终端里让 AI 生成、重构、修复代码
- 让 AI 代替自己执行构建命令并查看实时输出
- 作为学习极简 AI agent 工具调用实现的参考代码

## 场景标签

 · 领域:开发者工具/AI 编程

## 证据(README 行号)

> L3: A minimal, single-file AI coding assistant built with TypeScript and Bun. Uses Claude AI with tool-calling capabilit
> L9: - 🛠️ **10 Built-in Tools**: File operations, code search, shell execution, and more

## 星数曲线

```mermaid
xychart-beta
    title "xrip/tinycode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `476f3644ce67` · [字段定义](../../DATASET.md)*
