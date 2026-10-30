# meta-llama/llama-verifications

⭐ 28 · Python · MIT · 推送 2026-02-11 · [GitHub](https://github.com/meta-llama/llama-verifications) · 组织维护

**验证 Llama 模型提供商的测试与基准评测库**

Meta Llama 团队维护的轻量级验证库，对提供 OpenAI 兼容推理 API 的任意 Llama Provider 运行两套套件：功能测试（基础对话、图像输入、结构化 JSON 输出、工具调用）和学术评测基准（MMLU-Pro-CoT、GPQA、BFCL V3、MMMU、MTOB、IFEval 等），将结果与 Llama 模型卡数字对比并生成 Markdown 报告。通过 git clone 加 uv 工具安装，以 uvx 命令行使用，需为各 provider 设置 API key；新增 provider 通过添加 YAML 配置实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 功能测试覆盖对话、图像输入、结构化输出与工具调用，期望 100% 通过
- 7 类学术基准与 Llama 模型卡数字对比
- 以 uv/uvx 命令行运行，YAML 配置添加新 provider
- 生成 TESTS_REPORT.md 与 BENCHMARKS_REPORT.md 报告

## 适用场景

- 部署 Llama 后核验推理服务是否正确实现
- 对比不同 provider 的基准分数与模型卡数字
- 以 PR 形式向社区公开 provider 验证结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains a lightweight library to verify model providers via 2 suites,
> L7: Both the suites can be run on any Llama Provider that offers an OpenAI-compliant Inference API.

## 星数曲线

```mermaid
xychart-beta
    title "meta-llama/llama-verifications 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `525162cf0251` · [字段定义](../../DATASET.md)*
