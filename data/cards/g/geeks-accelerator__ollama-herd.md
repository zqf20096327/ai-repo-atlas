# geeks-accelerator/ollama-herd

⭐ 29 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/geeks-accelerator/ollama-herd) · [官网](https://ollamaherd.com) · 组织维护

**面向 Ollama/MLX 集群的本地 AI 推理路由与负载均衡器**

将多台设备组成单一推理集群：路由端 herd 为 FastAPI 服务器，节点端 herd-node 通过 mDNS 自动发现并上报心跳与系统指标；按温度、内存匹配、队列深度、延迟等评分将请求路由到最优设备，支持 LLM、视觉、图像生成（mflux/DiffusionKit）、语音转写（MLX Qwen3-ASR）与嵌入五类模型，提供 OpenAI 兼容 API 与实时仪表盘，无配置文件。面向拥有多台机器（尤其 Mac）的本地推理用户。需每台设备运行 Ollama、Python 3.11+；图像生成与语音转写的 MLX 后端仅限 Apple Silicon；每日发送一条匿名遥测，可通过环境变量关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mDNS 零配置自动发现节点，herd/herd-node 两条命令组集群
- 智能评分路由：温度、内存匹配、队列深度、延迟、上下文匹配等
- 五类模型路由：LLM、视觉、图像生成、语音转写、嵌入
- OpenAI 兼容 API，Open WebUI/LangChain/CrewAI/Aider 等改 base URL 即可接入

## 适用场景

- 把家里多台 Mac/Linux/Windows 机器的闲置算力汇成一个推理集群
- 多客户端共享本地模型时分散请求、避免单点 Ollama 瓶颈
- 通过一个统一端点同时提供对话、图像生成、转写与嵌入服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Turn all your devices into one local AI cluster. Ollama Herd is a smart inference router and load balancer that auto
> L219: - **`herd`** — FastAPI server with scoring, queues, streaming proxy, trace store, health engine, and dashboard

## 星数曲线

```mermaid
xychart-beta
    title "geeks-accelerator/ollama-herd 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-27", "2026-10-28"]
    y-axis "stars" 25 --> 30
    line [26, 27, 28, 29, 29]
```

2026-10-18 26 → 2026-10-28 29（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8157afc3a0d2` · [字段定义](../../DATASET.md)*
