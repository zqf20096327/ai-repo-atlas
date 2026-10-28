# SAP/generative-ai-toolkit-for-sap-hana-cloud

⭐ 30 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/SAP/generative-ai-toolkit-for-sap-hana-cloud) · 组织维护

**SAP HANA Cloud 的生成式 AI 客户端扩展：集成 HANA ML 与向量引擎**

SAP 维护的 Python 包 hana-ai，是 HANA ML Python 客户端库面向生成式 AI 场景的扩展，提供与 HANA ML、HANA 向量引擎及 SAP GenAI Hub SDK 的集成，并捆绑多个开源 GenAI 库。内置文件驱动的 ContextAgent，支持对话式预测与数据准备流程（Markdown 记忆、工具调用、运行时技能选择），覆盖 CSV 导入、时间序列画像、单序列与大规模分组预测、异常检测等技能。python_hanaml_exec 工具默认禁用且非沙箱，需显式受信开启。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ContextAgent：对话式预测与数据准备，Markdown 记忆与工具调用
- 覆盖时间序列预测、分组大规模预测、异常检测等核心技能集
- 集成 HANA ML、HANA 向量引擎与 SAP GenAI Hub SDK
- python_hanaml_exec 默认禁用并有受信边界说明

## 适用场景

- 在 SAP HANA Cloud 上做对话式时间序列预测与数据分析
- 通过 agent 技能完成数据导入、画像、建模与预测全流程
- 结合 HANA 向量引擎构建生成式 AI 应用

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: Generative AI Client for SAP HANA Cloud is an extension of the existing HANA ML Python client library, mainly focusi
> L21: The toolkit includes a file-based ContextAgent for conversational forecasting and data-preparation workflows with M

## 星数曲线

```mermaid
xychart-beta
    title "SAP/generative-ai-toolkit-for-sap-hana-cloud 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-28 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d77c69f16045` · [字段定义](../../DATASET.md)*
