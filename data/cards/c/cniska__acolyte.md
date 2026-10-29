# cniska/acolyte

⭐ 25 · TypeScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/cniska/acolyte) · [官网](https://acolyte.sh) · 个人维护

**终端里的开源 AI 编码 agent，跨会话记忆用户与项目**

面向开发者的终端 AI 编码代理，以 CLI + 常驻 daemon 架构运行：CLI 通过类型化 RPC 与 daemon 通信，支持编辑器与自定义客户端接入。核心机制包括持久化的会话/项目/用户记忆按需检索、显式的生命周期阶段与完成规则、工具访问的 workspace 边界校验、以及输入预算与 token 用量可见的上下文管理。支持多 provider 凭据配置（openai/anthropic/google 直连或 vercel 网关），每次文件编辑以 Git diff 形式上报。macOS/Linux 提供安装脚本、Homebrew 与 npm 安装二进制，需 Git 2.14+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLI → 类型化 RPC → 任务队列 → 模型+工具 的 daemon 架构
- 持久的会话/项目/用户记忆，按需检索
- workspace 边界校验与 planned input budgets、token 用量可见
- 本地任务 trace 与结构化日志用于运行时检查

## 适用场景

- 在终端里让 AI 代为完成编码任务并复用项目记忆
- 通过 RPC 接入编辑器或自定义客户端驱动 agent
- 不想重复解释项目背景的长期开发工作流

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: Acolyte is an open-source AI coding agent for the terminal. It remembers what it learns about you and your projects
> L40: CLI → typed RPC → task queue → lifecycle → model + tools

## 星数曲线

```mermaid
xychart-beta
    title "cniska/acolyte 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0c07872f78df` · [字段定义](../../DATASET.md)*
