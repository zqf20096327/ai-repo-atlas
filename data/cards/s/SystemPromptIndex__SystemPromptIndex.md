# SystemPromptIndex/SystemPromptIndex

⭐ 37 · 推送 2026-10-13 · [GitHub](https://github.com/SystemPromptIndex/SystemPromptIndex) · [官网](https://systempromptindex.com) · 组织维护

**1,017 条真实 AI 产品系统提示词的逐段审计数据集**

收录来自 413 个组织、1,058 条已公开的系统提示词，按 AISPA 八个保障维度（身份透明、真实性、隐私、工具安全、用户代理、拒绝处理、危害预防、公平中立）逐 span 审计，共 7,484 条审计片段，标注保护性/问题性（6,556/881）及人工/模型标注来源。数据以 Markdown 提示词文件与 JSON 审计文件成对组织，可用 jq/Python 直接查询。提示词来自公共合集，审计方法载于配套论文；收录不声明提示词的真实性或时效性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,058 条提示词 / 413 个组织 / 7,484 条逐 span 审计
- 八维度 AISPA 保障框架，每条发现含字符偏移、分数与理由
- 提示词与审计 JSON 同路径配对，id 即文件路径
- 审计结果（span/分数/维度定义）可署名自由使用

## 适用场景

- 研究系统提示词在隐私、用户代理等维度的保障状况
- 用 jq/Python 查询特定维度或最问题化的产品
- 为提示词审计研究获取带标注的语料

## 场景标签

 · 领域:AI 安全/数据集

## 证据(README 行号)

> L11: **1,017 system prompts from real AI products, read instruction by instruction.**
> L44: prompts/<org>/<product>.md     prompt text, with YAML front matter

## 星数曲线

```mermaid
xychart-beta
    title "SystemPromptIndex/SystemPromptIndex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `18afc2c017ce` · [字段定义](../../DATASET.md)*
