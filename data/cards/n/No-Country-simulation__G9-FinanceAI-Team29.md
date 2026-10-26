# No-Country-simulation/G9-FinanceAI-Team29

⭐ 29 · Jupyter Notebook · 推送 2026-08-27 · [GitHub](https://github.com/No-Country-simulation/G9-FinanceAI-Team29) · [官网](https://finsight.ai.sppa.cl/signin) · 组织维护

**个人财务分析 Web 平台：自动分类支出、算 Financial Score 并给出建议**

Hackathon（Oracle ONE + No Country）产出的全栈个人理财平台：用户导入 CSV 交易数据后，由自训练的 ML 分类器（16 类支出 + 3 类财务画像）自动归类，生成 Financial Score、风险评估与优先级建议，并配备对话助手 Finsi（Groq/Gemini LLM + 确定性引擎混合，RAG 技术支持聊天，流式输出）。技术栈为 React 19 + Spring Boot 3.4 + FastAPI + Supabase，部署于 Vercel/Render。README 明确声明模型用合成数据训练，生产使用前需用真实数据重训并加领域审查。本地运行需分别启动后端（Maven）、AI 服务（pip + uvicorn）与前端（npm）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 类支出分类器（TF-IDF + 校准 SGDClassifier），含质量门控与分组交叉验证
- Financial Score 自有评分 + 风险评估与优先级建议
- Finsi 对话助手：确定性引擎 + LLM 混合，带上下文记忆、流式输出与 prompt injection 防护
- RAG 技术支持聊天（FAISS）与 OWASP 安全审计报告

## 适用场景

- 导入银行/消费 CSV 后自动分类并查看财务画像
- 通过对话助手询问自己的财务状况并获得建议
- 设定储蓄目标、导出 CSV/XLSX/PDF 财务报告

## 场景标签

`数据分析` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L22: A partir de los ingresos, deudas, hábitos de ahorro y transacciones financieras, la plataforma analiza el comportam
> L32: **FinSightAI** convierte esos datos en información clara, explicable y accionable mediante modelos de Machine Learn
> L53: - Asistente conversacional financiero con memoria de contexto (Groq / Gemini).
> L57: - Clasificación de gastos y de perfil financiero vía modelos de ML entrenados en el pipeline de Data Science.

## 星数曲线

```mermaid
xychart-beta
    title "No-Country-simulation/G9-FinanceAI-Team29 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `a62677a0ee25` · [字段定义](../../DATASET.md)*
