# Global-Witness/augmenta

⭐ 21 · Python · Apache-2.0 · 推送 2025-11-06 · [GitHub](https://github.com/Global-Witness/augmenta) · [官网](https://globalwitness.org/en/campaigns/fossil-fuels/augmenta-new-tool-for-ai-classification-and-research/) · 组织维护

**用联网 LLM agent 给 CSV 数据集补充新列信息的工具**

Augmenta 是一个 Python 命令行工具/AI agent，读取 tidy 格式 CSV，按 YAML 配置调用 LLM（需指定 provider 与模型名，如 anthropic claude-3.5-sonnet）并通过搜索引擎从互联网获取信息，为每行实体生成新列（分类、属性补全等）。项目以自包含目录组织：输入 CSV、config.yaml、.env 存放 API key、自动缓存支持中断续跑。可选用 logfire 观测运行过程。通过 uvx/pipx/pip 安装，要求 Python 3.10+。README 提示结果仍可能含幻觉，发布前需人工核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 CSV 并按 YAML 配置的 prompt 与输出结构生成新列
- 通过搜索引擎从互联网检索信息以 grounding LLM
- 缓存机制支持中断后恢复运行
- logfire 集成用于监控运行、工具调用与错误

## 适用场景

- 给公司名单等 CSV 数据集批量补充行业、地址等属性列
- 对数据集做基于联网信息的批量分类
- 断点续跑地处理大规模数据增强任务

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: Augmenta is an AI agent for enhancing datasets with information from the internet (and more).
> L85: - `model`: The LLM you want to use. You can find a list of supported models here. Note that you need to provide bot

## 星数曲线

```mermaid
xychart-beta
    title "Global-Witness/augmenta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6237c4ba0534` · [字段定义](../../DATASET.md)*
