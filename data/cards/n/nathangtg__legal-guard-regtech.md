# nathangtg/legal-guard-regtech

⭐ 32 · Python · 推送 2026-10-25 · [GitHub](https://github.com/nathangtg/legal-guard-regtech) · 个人维护

**面向企业的 AI 法律文档合规分析平台（黑客松项目）**

IBM TechXchange Hackathon 2025 提交项目，基于 FastAPI + React/TypeScript 前端、IBM watsonx.ai Granite 模型构建。功能包括：将法律文档（PDF/DOCX/TXT）转为通俗语言摘要、合同条款解释、对照 GDPR/PDPA（马新）/CCPA/马来西亚雇佣法的合规检查与 0-100 风险评分、PDF 报告导出。提供 RESTful API（含 Swagger/ReDoc 文档）与 Web 界面，面向中小企业、法律专业人士与企业合规场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 法律文档摘要与条款解释（三种摘要类型）
- 多法域合规检查：GDPR、PDPA（马来西亚/新加坡）、CCPA、马来西亚雇佣法
- 0-100 分合规风险评分与监管检索 API
- React 单页应用前端 + FastAPI 后端，PDF 报告导出

## 适用场景

- 上传合同获得通俗语言摘要与风险评分
- 中小企业签署合同前快速评估 GDPR 等合规风险
- 法务人员为非法律背景客户生成摘要报告
- 跨法域合规状态监控与报告生成

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L27: - **Smart Summarization**: Convert complex legal jargon into plain English
> L29: - **Risk Assessment**: Automated identification of potential compliance issues
> L33: - **Multi-Jurisdiction Support**: GDPR (EU), PDPA (MY/SG), CCPA (US), Employment Act (MY)

## 星数曲线

```mermaid
xychart-beta
    title "nathangtg/legal-guard-regtech 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-25 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6226452017a2` · [字段定义](../../DATASET.md)*
