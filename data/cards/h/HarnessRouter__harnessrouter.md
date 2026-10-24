# HarnessRouter/harnessrouter

⭐ 3,268 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/HarnessRouter/harnessrouter) · [官网](https://harnessrouter.ai/) · 组织维护

**自托管的 agent harness 统一接口：一套 API 运行多种编码代理**

Apache-2.0 的基础设施层：将 Codex、Claude Code、DeepSeek Harness 等 26 种 agent harness 变为可插拔的产品后端，通过实现 Unified Harness Protocol（UHP）的 OpenAI Responses 兼容 API 暴露会话、流式进度、文件、幂等重试、取消与结构化失败处理。面向要在产品中集成代理能力的开发团队，自托管社区版以单条 Docker 命令部署 Console/Gateway/Runner，自带模型提供商密钥，另提供 5 个 Starter Kit（幻灯片/表格/仪表盘/视频/多代理工作区，许可条款与社区版不同）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 接入 26 种 harness 基座
- UHP 协议实现与 OpenAI Responses 兼容 API
- 持久会话、流式、幂等重试、秘密引用与沙箱外脱敏
- 单条 Docker 命令自托管，无需平台账号

## 适用场景

- 产品后端以一套 API 调用多种 agent harness 并按任务切换
- 在不同 harness × 模型配置间比较成本与延迟
- 在自有基础设施上运行代理任务并保留会话与文件

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15: **Build agent products without handling harness engineering.** HarnessRouter is the infrastructure layer that turns
> L25: HarnessRouter implements the Unified Harness Protocol (UHP) and provides an OpenAI Responses-compatible API, handli

## 星数曲线

```mermaid
xychart-beta
    title "HarnessRouter/harnessrouter 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-24"]
    y-axis "stars" 3067 --> 3286
    line [3085, 3141, 3227, 3268]
```

2026-10-18 3,085 → 2026-10-24 3,268（+183）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `a21ece07d420` · [字段定义](../../DATASET.md)*
