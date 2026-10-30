# jiseokson/PageBrain

⭐ 15 · Python · 推送 2026-07-19 · [GitHub](https://github.com/jiseokson/PageBrain) · [官网](https://www.youtube.com/watch?v=OtP-kwvESks&t=379s) · 个人维护

**单 GPU 上轻量 LLM 推理服务系统，自研 PagedAttention 与分页 KV 缓存**

从零实现 PagedAttention 与页级 KV 缓存管理的 LLM serving 系统，借鉴操作系统虚拟内存思想，将 GPU 显存划分为固定大小页块，用 BlockTable 维护逻辑到物理映射，避免显存碎片，支持多请求调度（请求队列→Sequence→SequenceGroup）与 prefill/decode 统一前向。当前集成 GPT-2（HuggingFace 模型，其他计划中），提供 CLI 服务器（HTTP API）与 Python API 两种用法。作者声明为毕业设计项目并持续演进的个人研究/工程作品，定位为现代 LLM serving 技术的教学参考实现，受 vLLM 启发但以可读、可改写为目标。

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

- 自研页级 KV 缓存：块表映射与物理显存分配管理
- 自定义 PagedAttention 算子，逐页累积注意力分数，无需重建完整 KV 张量
- 多请求调度器：请求队列→Sequence→SequenceGroup 流水线
- 提供 CLI 推理服务器（HTTP API）与 Python API 两种使用方式

## 适用场景

- 学习 PagedAttention 与分页 KV 缓存的参考实现
- 在单 GPU 上运行支持多请求的 LLM 推理服务
- 研究中改写和扩展 LLM serving 的内存管理机制

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L2: PageBrain is a lightweight LLM serving system that implements PagedAttention and page-level KV cache management from
> L4: This project was developed as a graduation capstone and continues to evolve into a personal research/engineering pro
> L110: - (CLI Server) Launch the full PageBrain inference server with a single command.

## 星数曲线

```mermaid
xychart-beta
    title "jiseokson/PageBrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b17dba39f4bc` · [字段定义](../../DATASET.md)*
