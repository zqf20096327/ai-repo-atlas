# KennispuntTwente/KWALLM

⭐ 19 · HTML · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/KennispuntTwente/KWALLM) · [官网](https://kennispunttwente.nl) · 组织维护

**面向非技术用户的 LLM 定性文本分析应用（分类/评分/主题/编码）**

由 Kennispunct Twente 与 GGD Twente 合作开发的 R/Shiny 应用：用户上传文本后由 LLM 执行分类、按特征评分、主题提取（基于 Wanrooij et al. 2024 方法）与按定性编码标注，可自动生成编码。附加功能包括类别摘要、Cohen's Kappa 评分者间信度、人工修订主题、发送外部 API 前的 PII 脱敏（regex 与本地 GLiNER 模型）、语义分块。可连接任意 LLM 提供商（本地 Ollama 或 Azure OpenAI 等），支持本地运行、Windows 桌面包或 Docker 容器三种方式，界面支持英文/荷兰语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种 LLM 分析模式：分类、特征评分、主题提取、按定性编码标注
- PII 脱敏（regex + 本地 GLiNER 模型）在发送外部 API 前移除个人身份信息
- 评分者间信度（Cohen's Kappa）与 human-in-the-loop 主题修订
- 三种运行方式：R 环境、Windows 桌面包（含便携 R）、Docker 容器

## 适用场景

- 分析问卷中的开放题回答并自动分类
- 对访谈或焦点小组转写文本做定性编码与标注
- 在发送外部 API 前脱敏受访者个人信息以满足隐私要求
- 接入本地 Ollama 在本机完成文本分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: KWALLM is an app (developed with R, Shiny) for (automated) qualitative text analysis using large language models (LL
> L13: - **Categorization**: Users provide a list of categories, and the model classifies texts accordingly (e.g., 'positi

## 星数曲线

```mermaid
xychart-beta
    title "KennispuntTwente/KWALLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f19c784be310` · [字段定义](../../DATASET.md)*
