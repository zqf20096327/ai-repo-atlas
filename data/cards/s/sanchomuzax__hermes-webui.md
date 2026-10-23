# sanchomuzax/hermes-webui

⭐ 114 · Python · 推送 2026-03-24 · [GitHub](https://github.com/sanchomuzax/hermes-webui) · [官网](https://github.com/NousResearch/hermes-agent) · 个人维护

**Hermes Agent 的进程监控与配置管理 Web 面板**

面向 Hermes Agent 用户的 FastAPI + React 监控面板：以只读方式读取 agent 的 state.db、config.yaml 与 .env，提供实时活动流、会话历史（FTS5 搜索）、定时任务管理、技能浏览、成本与模型分布统计。通过 WebSocket 轮询桥接（每 3 秒）获取更新，不修改 agent 核心代码。安装需克隆仓库、pip 安装后端、npm 构建前端，以 CLI 命令 hermes-webui 启动，支持 systemd 服务部署；要求本机已有 ~/.hermes/ 的 Hermes Agent 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时仪表盘：会话、网关状态、平台健康、成本追踪、模型分布
- FTS5 全文搜索浏览完整会话历史
- 只读读取 agent 数据文件，不修改 agent 核心代码
- WebSocket 轮询桥接 + auth token 登录

## 适用场景

- 查看 Hermes Agent 的运行状态与成本开销
- 检索和回放历史会话内容
- 管理定时任务与查看技能源码

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Process monitoring and configuration dashboard for Hermes Agent.
> L145: Hermes WebUI reads from the agent's data files without modifying the agent's core code.

## 星数曲线

```mermaid
xychart-beta
    title "sanchomuzax/hermes-webui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 113 --> 115
    line [114, 114]
```

2026-10-18 114 → 2026-10-23 114（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `14691bd410a1` · [字段定义](../../DATASET.md)*
