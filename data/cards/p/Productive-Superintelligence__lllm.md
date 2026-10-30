# Productive-Superintelligence/lllm

⭐ 99 · Python · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/Productive-Superintelligence/lllm) · [官网](https://lllm.one/) · 组织维护

**构建可复用 LLM agent 战术（Tactic）的轻量协议与服务层框架**

LLLM 是一个小型协议与服务层，核心抽象为 Tactic：类型化、运行时无关的可复用 agent 战术单元，可本地调用、通过 FastAPI 暴露为 /run 与 /stream 服务、写成 PsiHub 包并通过 psi:// 引用组合。运行时由外部框架持有（如 Pydantic AI 包装器），另提供解析器、调用边界代理、应用级沙箱、原生 prompt/dialog 核心、CLI 项目脚手架（lllm create/serve）等。以 pip 包 lllm-core 发布，元数据导出中过滤秘密形状键。沙箱为应用级限制，非 OS 级隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tactic 协议：类型化、运行时无关，可本地调用或经 FastAPI 暴露
- PydanticAI 战术包装器与原生 prompt/dialog 运行时适配
- psi:// 引用解析组合战术，支持本地 URL 绑定与元数据
- CLI 生成可运行 tactic/service 项目（plain/pydantic-ai/native 模板）

## 适用场景

- 把 agent 逻辑封装为可复用、可组合的战术单元
- 通过统一 /run 与 /stream 接口服务化部署 agent 战术
- 在调用边界做观测、守卫与负载限额

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Low-Level Language Models (LLLM) is a small protocol and service layer for
> L8: The center model is `Tactic`: a typed, runtime-agnostic unit that does one
> L9: thing well and can be called locally, exposed through FastAPI, described for a

## 星数曲线

```mermaid
xychart-beta
    title "Productive-Superintelligence/lllm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 98 --> 100
    line [99, 99]
```

2026-10-18 99 → 2026-10-30 99（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1c1017faac84` · [字段定义](../../DATASET.md)*
