# Kordi-Lab/Multi-User-LLM-Agent

⭐ 36 · Python · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/Kordi-Lab/Multi-User-LLM-Agent) · [官网](https://arxiv.org/abs/2604.08567) · 组织维护

**多用户 LLM agent 的评测框架与基准（论文官方代码）**

论文 "Multi-User Large Language Model Agents" 的官方代码，提供多用户 LLM agent 评测的形式化框架与基准：覆盖隐私与访问控制、会议调度协调、共享推理队列资源优化、多用户指令遵循四类场景。提供 JSONL 测试数据与数据构建脚本生成自定义数据集，并附带在多用户对话上微调 LLM 的完整训练流程（数据生成、训练、评测，支持 vLLM 推理与 LoRA）。通过 .env 配置 API 凭证，run.py 运行各场景评测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类多用户场景基准：访问控制/会议调度/共享队列/指令遵循
- 每个场景提供 JSONL 数据集与 data builder 自定义生成脚本
- 多用户对话微调 LLM 的完整训练管线
- 评测支持 OpenAI API 与 vLLM（含 LoRA）

## 适用场景

- 评测 LLM agent 在多用户权限与偏好冲突下的表现
- 生成自定义多用户场景测试数据
- 在多用户对话数据上微调并评测模型

## 场景标签

`模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L13: > LLM-based agents are increasingly capable of navigating complex environments, but prior work overwhelmingly assum
> L17: Multi-User LLM evaluates four fundamental capabilities of multi-user LLM agents:

## 星数曲线

```mermaid
xychart-beta
    title "Kordi-Lab/Multi-User-LLM-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f555848f9760` · [字段定义](../../DATASET.md)*
