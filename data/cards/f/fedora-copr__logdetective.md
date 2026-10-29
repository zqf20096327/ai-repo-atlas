# fedora-copr/logdetective

⭐ 45 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/fedora-copr/logdetective) · 组织维护

**面向 RPM 构建日志的 LLM 分析服务与 RHEL 流程集成**

Fedora COPR 维护的日志分析服务：通过 HTTP API 提交构建日志，由 LLM（在 BeeAI agentic 框架内）与 Drain 模板挖掘器进行分析并给出解释。后端为 FastAPI + PostgreSQL + Procrastinate 任务队列，推理层不绑定具体实现，仅要求提供 OpenAI 兼容 API；示例部署给出 llama.cpp（开发）与 4 个 vLLM 负载均衡（生产）两种配置，也支持 Vertex AI。CLI 工具自 5.0 版起已废弃移除。另提供 csgrep 片段提取、Jinja 提示模板、Skip Snippets 正则过滤等机制，并与 Koji/GitLab 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HTTP API 提交日志，LLM + Drain 模板挖掘产出分析解释
- 推理无关设计：任意 OpenAI 兼容 API 均可（llama.cpp/vLLM/Vertex AI 示例）
- FastAPI + PostgreSQL + Procrastinate 异步任务队列，30 天结果保留
- 支持 csgrep GCC 日志提取与正则 Skip Snippets 过滤

## 适用场景

- 分析 RPM/操作系统构建日志中的失败原因
- 接入 Koji/GitLab 流水线自动解释构建失败
- 以 OpenAI 兼容的本地或云推理服务自托管日志分析

## 场景标签

 · 领域:开发者工具/日志分析

## 证据(README 行号)

> L5: A tool, service and RHEL process integration to analyze logs using Large Language Model (LLM) and a Drain template m
> L17: For locally setting up the FastAPI server, you would need a postgresql and some inference server.
> L19: Log Detective has been built as inference agnostic service. The only requirement, is that the inference server must

## 星数曲线

```mermaid
xychart-beta
    title "fedora-copr/logdetective 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-29 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c2cdb779af28` · [字段定义](../../DATASET.md)*
