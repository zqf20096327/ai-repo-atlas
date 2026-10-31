# runloopai/api-client-python

⭐ 28 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/runloopai/api-client-python) · [官网](https://docs.runloop.ai) · 组织维护

**Runloop 平台的官方 Python SDK：管理 AI 代理运行的隔离沙箱**

Runloop 官方 Python SDK，用于创建和管理 Devbox——供 AI 代理和 AI 生成代码运行的隔离 Linux 沙箱（含 shell、文件系统、网络与可选 GPU）。通过该库可创建沙箱、执行命令、读写文件、以 HTTPS 暴露端口，并对整机做快照以暂停/恢复。提供高层 RunloopSDK 面向对象接口与底层生成式 REST 客户端两层，均含同步/异步变体、类型定义、自动分页与默认重试。需 RUNLOOP_API_KEY 凭 PyPI 安装使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 创建/管理隔离 Linux Devbox 沙箱，支持命令执行、文件读写、端口暴露与整机快照
- 提供 RunloopSDK 高层接口与生成式 REST 客户端，同步/异步双变体
- 请求参数 TypedDict、响应 Pydantic 模型，含自动分页迭代器
- 默认自动重试（5 次、指数退避）与可配置超时，支持 aiohttp 可选后端

## 适用场景

- 为 AI 代理提供隔离执行环境以运行不可信代码
- 在沙箱中执行命令、编辑文件并通过 HTTPS 暴露服务端口
- 通过快照暂停/恢复/分支代理的机器状态

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Run AI agents and AI-generated code in **Devboxes**: isolated Linux sandboxes with a shell, a
> L6: filesystem, networking, and optional GPUs. Use this library to create a sandbox, run commands in it,
> L29: Set `RUNLOOP_API_KEY` in your environment (get a free key — new accounts start

## 星数曲线

```mermaid
xychart-beta
    title "runloopai/api-client-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `af8a94886ef7` · [字段定义](../../DATASET.md)*
