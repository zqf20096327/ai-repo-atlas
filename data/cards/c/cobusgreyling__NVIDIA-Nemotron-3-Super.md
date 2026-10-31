# cobusgreyling/NVIDIA-Nemotron-3-Super

⭐ 29 · Python · MIT · 推送 2026-04-02 · [GitHub](https://github.com/cobusgreyling/NVIDIA-Nemotron-3-Super) · 个人维护

**Nemotron 3 Super 可控推理演示集：chat UI、CLI、API 服务器与路由实验**

围绕 NVIDIA Nemotron 3 Super（120B 总参/12B 激活 MoE Hybrid Mamba-Transformer）的演示与应用集合，通过 NVIDIA NIM 端点的 OpenAI 兼容 API 访问模型。提供三档可控推理模式（ON/OFF/Low Effort）与 reasoning_budget 精细控制，包含流式 tool calling 演示、FastAPI SSE 服务器、CLI、Gradio 界面、七档预算扫描实验、基于规则的查询自适应路由器、批量基准与 12 个系统提示模板。需 API key 访问云端端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种推理模式 + reasoning_budget 的可控推理机制
- 自适应路由器按查询类别自动选择模式与预算（规则分类，无需 LLM 调用）
- FastAPI 服务器提供 OpenAI 兼容端点与 SSE 流式、三模式对比端点
- 预算扫描实验：7 档预算下的推理/内容 token 与延迟测量

## 适用场景

- 通过 chat UI 或 CLI 体验可控推理的三种模式
- 本地部署 OpenAI 兼容 API 服务器调用该模型
- 为不同难度查询自动分配合适的推理深度与预算
- 测量推理预算对 token 消耗与延迟的影响

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L89: Nemotron 3 Super uses the NVIDIA NIM endpoint with the OpenAI-compatible API.
> L191: python api_server.py

## 星数曲线

```mermaid
xychart-beta
    title "cobusgreyling/NVIDIA-Nemotron-3-Super 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `602690c5f5c8` · [字段定义](../../DATASET.md)*
