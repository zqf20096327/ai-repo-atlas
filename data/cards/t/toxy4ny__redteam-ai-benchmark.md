# toxy4ny/redteam-ai-benchmark

⭐ 57 · Python · MIT · 推送 2026-06-22 · [GitHub](https://github.com/toxy4ny/redteam-ai-benchmark) · 个人维护

**面向授权红队/攻防场景的 LLM 基座选型 CLI 评测基准**

命令行基准工具，用于在授权红队与攻击性安全工作场景中筛选基座 LLM。v2 版使用 60 题的评分量规（rubric）数据集，按领域与难度分组，覆盖 Windows 战术、AD/ADCS、Web 漏洞利用、云与 IAM、容器、免杀推理等十类主题。运行时评分为确定性量规打分，不需要外部 LLM 裁判；另提供离线 LLM-as-Judge 命令做事后审计。支持 Ollama、LM Studio、OpenWebUI、OpenRouter 四种接入方式，输出 JSON/CSV 审计明细。许可证 MIT，README 注明仅限授权环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 60 题 rubric 数据集，确定性打分无需外部 LLM 裁判
- 报告 refusal_rate、critical_error_rate、幻觉率等审计指标
- 离线 LLM-as-Judge 命令对争议案例做事后审计
- 支持 Ollama/LM Studio/OpenWebUI/OpenRouter 四种接入端点

## 适用场景

- 在授权红队项目中挑选合适的本地基座模型
- 对候选模型比较拒答率与关键错误率等审计指标
- 导出逐题评分明细用于选型评审与合规留档

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L5: Red Team AI Benchmark is a CLI benchmark for choosing base LLMs for authorized red-team and offensive-security work.
> L29: The benchmark reports the total weighted score and separate audit metrics:

## 星数曲线

```mermaid
xychart-beta
    title "toxy4ny/redteam-ai-benchmark 星数(近 4 点)"
    x-axis ["2026-10-19", "2026-10-22", "2026-10-23", "2026-10-24"]
    y-axis "stars" 52 --> 58
    line [53, 55, 56, 57]
```

2026-10-19 53 → 2026-10-24 57（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9beb19aa06a2` · [字段定义](../../DATASET.md)*
