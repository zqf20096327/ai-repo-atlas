# Tencent-Hunyuan/AutoCodeBenchmark

⭐ 436 · Python · NOASSERTION · 推送 2026-02-17 · [GitHub](https://github.com/Tencent-Hunyuan/AutoCodeBenchmark) · 组织维护 · 中文 README

**多语言代码生成基准与评测数据集生成管线，含代码沙箱服务**

腾讯混元团队发布的代码生成评测体系：AutoCodeGen 通过 LLM 与沙箱交互动态生成测试输入与输出，构建代码数据集；AutoCodeBench 系列含 ACB-Full（3,920 题、20 种编程语言）、ACB-Lite（1,586 题）与 ACB-Complete（1,000 题、3-shot 补全式）三个基准；AutoCodeInstruct 提供经 DeepSeek-V3 蒸馏答案、Qwen2.5-Coder 过滤的 RL/SFT 训练数据。另含 MultiLanguageSandbox，支持 30+ 语言编译执行的 Docker 沙箱服务，评测流程为模型推理输出后经沙箱执行计算 pass@1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ACB-Full 含 3,920 题、覆盖 20 种编程语言，按难度与语言类别均衡分布
- AutoCodeGen：LLM 生成测试输入、沙箱产生测试输出的自动化数据集构建流程
- MultiLanguageSandbox Docker 沙箱支持 30+ 语言编译执行
- AutoCodeInstruct 提供 RL/SFT 两个版本的训练数据集

## 适用场景

- 评测代码模型在多语言高难度题目上的 pass@1 表现
- 为代码模型 RL/SFT 训练获取带金标答案的多语言数据集
- 搭建本地多语言代码执行沙箱做自动化测试判定

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L22: **AutoCodeGen**: An innovative automated workflow leveraging LLM-Sandbox Interaction, where *LLMs dynamically gener
> L25: - **ACB-Full**: A comprehensive, large-scale code generation benchmark comprising 3,920 carefully curated problems,
> L45: Previous benchmarks mainly focused on Python, with multilingual benchmarks like Fullstackbench and McEval suffering

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/AutoCodeBenchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 436 --> 438
    line [437, 437]
```

2026-10-18 437 → 2026-10-22 437（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1b0993a13f65` · [字段定义](../../DATASET.md)*
