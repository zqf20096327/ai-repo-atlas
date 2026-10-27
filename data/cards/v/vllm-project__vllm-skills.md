# vllm-project/vllm-skills

⭐ 102 · Shell · Apache-2.0 · 推送 2026-04-03 · [GitHub](https://github.com/vllm-project/vllm-skills) · 组织维护

**面向 Claude Code 的 vLLM 部署与基准测试 agent 技能集**

vLLM 项目维护的 agent 技能仓库，遵循 anthropics/skills 的 SKILL.md 规范，以 Claude Code 插件市场形式分发。收录 6 个自包含技能：Docker 部署、Kubernetes 部署、简易部署、前缀缓存基准、随机合成数据基准与服务基准，覆盖 GPU 支持、健康探针、OpenAI 兼容端点配置及吞吐量/TTFT/TPOT 等指标测量。可通过插件市场命令安装，或 git clone 后手动复制技能目录，经斜杠命令或自然语言调用。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个技能覆盖 vLLM 的 Docker/K8s/简易部署与三类基准测试
- 遵循 anthropics SKILL.md 规范，可安装为 Claude Code 插件
- 支持测量吞吐量、TTFT、TPOT 等性能指标
- 提供插件市场安装与手动复制两种安装方式

## 适用场景

- 通过 Claude Code 用自然语言完成 vLLM 部署
- 对 vLLM 服务端点做性能基准测试
- 在 Kubernetes 上部署带 GPU 支持的 vLLM

## 场景标签

`推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A collection of skills for deploying and benchmarking vLLM. This project follows the anthropics/skills template form
> L7: This repository provides modular, reusable agent skills required to operate and benchmark vLLM, following the Anthro
> L13: |vllm-deploy-docker|Deploy vLLM using Docker (pre-built images or build-from-source) with NVIDIA GPU support and ru

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/vllm-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-27 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `49b840acb737` · [字段定义](../../DATASET.md)*
