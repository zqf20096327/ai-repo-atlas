# machinelearningZH/simply-simplify-language

⭐ 51 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/machinelearningZH/simply-simplify-language) · 组织维护

**苏黎世州政府的 LLM 文本简化应用：把公文改写为易懂德语**

苏黎世州政府 2023 年试点项目产出的 Streamlit 应用：通过 OpenRouter 统一接口调用用户配置的多个 LLM，把复杂文本按 «Einfache Sprache»/«Leichte Sprache» 规则改写简化；提供逐句写作分析、基于外部 zix 包的可读性评分（-10 至 +10）与 CEFR 估计，以及向全部配置模型并发发送的 One-Click 功能并导出 Word 文档。模型、超时、评分阈值等在 config.yaml 配置。限制：面向瑞士标准德语、请求会外发文本（仅适合非敏感数据）、不含反向代理与鉴权。可本地（uv/Python 3.12+）、Docker、云端或 Codespace 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 经 OpenRouter 调用可配置的多家 LLM 做文本简化
- zix 可读性评分（-10 至 +10）与 CEFR 估计
- One-Click 并发调用全部配置模型并导出含源文与结果的 Word
- 逐句写作分析反馈，提示词规则可按机构指南修改

## 适用场景

- 把机构公文改写为 Einfache/Leichte Sprache 供公众阅读
- 获得逐句写作反馈以改进机构沟通文本
- 并排比较多个 LLM 的简化结果与各自可读性评分

## 场景标签

 · 领域:公共服务/语言无障碍

## 证据(README 行号)

> L103: - This app **simplifies complex texts, rewriting them according to rules for «Einfache Sprache» or «Leichte Sprach
> L97: The cantonal administration of Zurich has long worked to make its communication more inclusive and accessible. As t

## 星数曲线

```mermaid
xychart-beta
    title "machinelearningZH/simply-simplify-language 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-30 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b10a3d4e7eb4` · [字段定义](../../DATASET.md)*
