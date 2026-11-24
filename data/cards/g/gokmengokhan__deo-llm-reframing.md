# gokmengokhan/deo-llm-reframing

⭐ 10 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/gokmengokhan/deo-llm-reframing) · 个人维护

**LLM 创意重构提示框架 DEO 的论文复现材料与实验代码**

对应论文《Does AI Dream of Electric Sheep?》的复现材料：将感知重构理论转化为 LLM 提示策略，在 50 个原创问题与 956 个 MacGyver 基准问题上比较 vanilla/distance/engagement/DEO 等六种条件，含实验脚本、统计分析、结果 JSON/CSV 数据与引用格式。生成经 Groq API，评分含 Claude 与 GPT 盲评。提供 Claude Code 的 /reframe 斜杠命令（默认 2 步协议）。需 Python 3.12+、uv 及 Groq/Anthropic/OpenAI 的 API key。2026 年 10 月更正声明标注部分跨模型结果因配置错误实际由 Llama 3.3 70B 生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 50+956 问题、6 条件、3 个开源权重模型的实验设计与全套结果数据
- 实验生成经 Groq API，评分含自评 + Claude Sonnet 4 + GPT-4.1 三方盲评
- 提供 Claude Code 的 /reframe 与 /reframe-long 斜杠命令
- 2026 年 10 月发布结果更正声明并附 Zenodo 更正链接

## 适用场景

- 复现论文中的 DEO 提示策略对比实验
- 在自己的问题上应用 /reframe 重构命令
- 将 results/ 或 paper/ 中的数据用于后续分析

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: Replication materials for the paper:
> L13: Perceptual Reframing Theory (PRT; Gokmen, submitted) identifies nine cognitive paths through which humans shift per

## 星数曲线

```mermaid
xychart-beta
    title "gokmengokhan/deo-llm-reframing 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `eb0ff9a89a56` · [字段定义](../../DATASET.md)*
