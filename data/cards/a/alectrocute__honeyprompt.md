# alectrocute/honeyprompt

⭐ 21 · TypeScript · MIT · 推送 2026-07-15 · [GitHub](https://github.com/alectrocute/honeyprompt) · [官网](https://hub.docker.com/r/alectrocute/honeyprompt) · 个人维护

**面向 Web 开发者的 LLM 蜜罐框架：用 LLM 模拟诱饵服务与攻击者对话**

以 TypeScript/Deno 编写的 LLM-first 欺骗框架：在 SSH、HTTP、TLS、TCP、Telnet 等协议上部署诱饵服务，将攻击者输入交给 LLM 生成逼真响应以延长会话，记录连接、凭据与命令形成威胁情报。支持 Ollama、llama.cpp、OpenAI、Azure、OpenRouter、Anthropic、Gemini 等 provider 池化与故障转移，也可仅用静态规则无 LLM 运行。以容器和单静态二进制分发，含只读 Web 面板、Prometheus 指标与 JSONL 事件持久化，可部署于低配硬件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSH/HTTP/TLS/TCP/Telnet 多协议 LLM 诱饵服务，附 7 个默认 decoy profile
- 8 类 provider 模块 + 负载均衡/故障转移/命名池
- 无需 LLM 即可用静态规则运行；TypeScript hooks 可扩展请求/响应路径
- 只读 Web 面板、Prometheus 指标、JSONL 事件流（可送 SIEM）

## 适用场景

- 在自有基础设施上部署蜜罐引诱并研究攻击者行为
- 采集攻击者使用的工具、凭据与利用手法作为威胁情报
- 低配 VPS 上运行轻量诱饵服务，无需数据库或插件编译

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: Introducing `honeyprompt`, an LLM-first deception framework made by/for web developers. The personal
> L81: ### Running without an LLM
> L117: runs a command the author didn't anticipate. honeyprompt hands that moment to an LLM, so the shell

## 星数曲线

```mermaid
xychart-beta
    title "alectrocute/honeyprompt 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a3c8630fa1d8` · [字段定义](../../DATASET.md)*
