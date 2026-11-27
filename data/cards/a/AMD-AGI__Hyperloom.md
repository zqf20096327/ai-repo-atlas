# AMD-AGI/Hyperloom

⭐ 288 · Python · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/AMD-AGI/Hyperloom) · [官网](https://rocm.docs.amd.com/projects/hyperloom) · 组织维护

**AMD GPU 上自动优化 LLM 推理负载的多 agent 工具**

ROCm Hyperloom 是一个多 agent 编排框架（harness），对 AMD Instinct GPU 上的推理负载做自动优化：测量基线、剖析 roofline、搜索服务框架配置与 GPU kernel 改动，并对每个候选改动端到端验证后写入配方知识库供后续会话复用。支持文本生成、图像生成与自定义管线，面向 vLLM、SGLang、xDiT 框架；基准由协调器运行而非模型，失败改动回滚，仅 MI300X/MI325X/MI355X 平台可用。以 Python CLI 形式提供，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 闭环优化会话：input→optimize→validate→learn，含硬性循环上限
- 配方知识库记录获胜配置、吞吐与失败教训，用于会话热启动
- 风险源码改动经隔离 worktree、diff 门、策略检查与 Critic 签核
- 截至 2026-11-02 有 26 项优化被合并进 vLLM/SGLang 上游

## 适用场景

- 为 AMD Instinct GPU 上的新模型自动搜索推理服务配置与 kernel 优化
- 跨多轮优化会话复用已验证的调优配方
- 审计主机 CPU/BIOS 调优对基准结果的影响

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: **ROCm™ Hyperloom** is a multi-agent harness that autonomously optimizes inference
> L14: It supports text generation, image generation, and custom pipelines on vLLM,
> L127: |Framework|SGLang, vLLM, xDiT|

## 星数曲线

```mermaid
xychart-beta
    title "AMD-AGI/Hyperloom 星数(近 18 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-29", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 251 --> 291
    line [254, 256, 258, 254, 264, 266, 267, 269, 270, 271, 272, 274, 276, 281, 282, 284, 287, 288]
```

2026-10-25 254 → 2026-11-27 288（+34）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `cea4b6b17ba8` · [字段定义](../../DATASET.md)*
