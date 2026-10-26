# ukrserhiy/litios

⭐ 46 · HTML · MIT · 推送 2026-08-10 · [GitHub](https://github.com/ukrserhiy/litios) · [官网](https://liti.fractal.partners/) · 组织维护

**招聘用心理语言学面试转录分析工具（自托管）**

FRACTAL 开发的自托管 Web 应用：读取面试转录文本，通过 OpenRouter 调用 LLM（Claude、GPT、Gemini、DeepSeek 等）分析语言标记，输出 Big Five、HEXACO、Dark Triad、PsyCap、MBTI、DISC 等 28 个心理量表评分，并支持职位匹配分析（简历/面试对照岗位要求生成符合度表）与 PDF 导出。数据存储于本机 SQLite，单用户无鉴权。技术栈为 Python 3.11/Flask/Vanilla JS，提供 Docker 与云平台部署方式；需自备 OpenRouter API key，每次分析按所选模型计费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个心理量表（Big Five/HEXACO/Dark Triad/PsyCap/MBTI/DISC 等）
- 通过 OpenRouter 接入免费到付费多档模型，按 token 计费
- 职位匹配分析：简历与面试转录对照岗位要求输出符合度表
- SQLite 本地存储分析历史，支持 PDF 导出

## 适用场景

- 招聘时分析候选人面试转录的人格特质评分
- 对照岗位要求评估候选人简历与访谈的匹配度
- 在自有服务器上保存历史分析记录并导出报告

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: **LITI** - психолінгвістична діагностика для рекрутингу ШІ-система для глибинного аналізу особистості на основі мовл
> L6: **LITI** — self-hosted інструмент для психолінгвістичного аналізу транскриптів інтерв'ю. Визначає особистісні риси к
> L16: - **28 психологічних шкал**: Big Five, HEXACO, Dark Triad, PsyCap, MBTI, DISC та інші

## 星数曲线

```mermaid
xychart-beta
    title "ukrserhiy/litios 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-26 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2f51958fbb01` · [字段定义](../../DATASET.md)*
