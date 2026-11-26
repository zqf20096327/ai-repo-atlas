# gauravjain14/inference-observe

⭐ 12 · TypeScript · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/gauravjain14/inference-observe) · [官网](https://gauravjain14.github.io/inference-observe/) · 个人维护

**面向开发者的 LLM 推理引擎实时观测面板**

以插件（tap）+ 代理 + 收集器 + 浏览器面板的结构观测 SGLang 或 vLLM 推理引擎：tap 由引擎加载并报告每个调度步、KV cache 与前缀缓存命中，代理位于 OpenAI 兼容 API 前计时每个请求，收集器合并 GPU 遥测数据、流式输出到面板并记录到磁盘。安装为源码 clone 加 pip/uv 与 npm 安装，支持无 GPU 时回放录制数据，自带审计脚本将面板数值与引擎独立测量对比。KV 内存映射当前仅支持 SGLang。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 SGLang/vLLM 流式展示每请求、调度步与 KV cache 块
- 代理位于 OpenAI 兼容 API 前计时每个请求（含 TTFT）
- 提供 GitHub Copilot、Mooncake 生产轨迹回放与合成负载
- 审计脚本将面板数值与引擎 gauge 及 API token 计数对比

## 适用场景

- 调试推理引擎的 KV 缓存与调度行为
- 用生产轨迹回放在小 GPU 上复现流量
- 分析 agent 会话的缓存复用与首 token 延迟

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: See inside your LLM inference engine while it runs. inference-observe streams every request, scheduler
> L24: - **The proxy** sits in front of the engine's OpenAI-compatible API and times every request.
> L25: - **The collector** merges both with GPU telemetry, streams them to the dashboard and records them to disk.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `50bf8594c467` · [字段定义](../../DATASET.md)*
