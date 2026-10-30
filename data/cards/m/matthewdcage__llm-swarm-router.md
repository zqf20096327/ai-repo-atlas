# matthewdcage/llm-swarm-router

⭐ 26 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/matthewdcage/llm-swarm-router) · 个人维护

**局域网多机本地 LLM 后端的 mesh 路由器：聚合分发推理请求**

面向运行本地推理或使用 base_url 接入工具的用户：在每台机器上运行轻量 agent，自动发现 localhost 的 oMLX、Ollama、LM Studio、vLLM 与自定义 OpenAI 兼容服务器，通过 mDNS 或集群令牌在局域网内发现对等节点，将推理请求分发到各机器以分摊负载，并对外暴露单一 OpenAI/Anthropic 兼容端点（:11400）供 Cursor、Claude Code 等客户端使用。macOS 提供菜单栏应用（需从源码构建，DMG 待公证），Linux/Windows 为 alpha 打包。Windows 服务注册存在已知启动失败问题，需以 netllm serve 方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动发现 oMLX/Ollama/LM Studio/vLLM 本地后端并持久化 URL
- LAN 内 mDNS 或集群令牌组网，同模型负载自动分摊（local_spillover）
- 单一 OpenAI/Anthropic 兼容端点供编辑器与工具接入
- 模型池、模型别名、cloud_priority（cloud/local/none/auto）路由策略

## 适用场景

- 把家里多台不同系统的机器组成本地推理集群
- 让 Cursor、Claude Code 等客户端只配一次 URL 即可使用全部机器的模型
- 多机间分摊同一模型的推理负载以提升吞吐

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L22: **The mesh router for local LLM backends.** Run a lightweight agent on each computer. It finds **oMLX**, **Ollama**
> L45: A **simple-to-install, simple-to-use LLM mesh coordinator** for macOS, Linux, and Windows. Each node runs **indepen
> L49: |OpenAI-compatible|`http://<host>:11400/v1`|

## 星数曲线

```mermaid
xychart-beta
    title "matthewdcage/llm-swarm-router 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-30 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `28c70cdd25f4` · [字段定义](../../DATASET.md)*
