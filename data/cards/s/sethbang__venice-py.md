# sethbang/venice-py

⭐ 13 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/sethbang/venice-py) · [官网](https://venice-docs.sbang.dev/) · 个人维护

**Venice.ai 非官方 async Python SDK：聊天/图像/视频/音频一站式接入**

社区维护的 Venice.ai 异步优先 Python SDK（原名 venice-ai，现安装名 venice-py），覆盖 chat completions、流式输出、函数调用、图像/视频/音乐/音频生成、TTS、embeddings、web search 与抓取、决策模型等 API 能力，返回 Pydantic 类型化对象。特色包括 x402 钱包计费（Ethereum SIWE / Solana）、TEE/E2EE 机密计算与客户端 TDX 验证、速率限制与调度配置（可配 Redis 后端）。附带 CLI 与 4 个 Claude Code skills。需 Python 3.11+，v2.x 相对 v1.x 为破坏性重写。

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

- 异步/同步双客户端，Pydantic 类型化响应
- x402 钱包计费（Ethereum SIWE 与 Solana 两种认证）
- TEE 机密计算：enclave 远程证明 + 端到端加密，可选离线 TDX quote 完整验证
- 附带 CLI 与 4 个可安装的 Claude Code skills

## 适用场景

- 在 Python 项目中接入 Venice.ai 的聊天、图像、视频生成 API
- 构建需要钱包计费（x402）的 Venice 应用
- 对隐私敏感场景使用 e2ee-* 模型的端到端加密推理
- 让 Claude Code 按 SDK 惯用法编写 Venice 集成代码

## 场景标签

`图像生成` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: venice-py — unofficial, community-maintained Python SDK for Venice.ai
> L13: **Production-ready Python SDK for Venice.ai with enterprise-grade rate limiting, intelligent scheduling, and compre

## 星数曲线

```mermaid
xychart-beta
    title "sethbang/venice-py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c44cf4ef3c86` · [字段定义](../../DATASET.md)*
