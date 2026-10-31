# ayeshamumtaz1057/AI-Business-analytics-studio

⭐ 18 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ayeshamumtaz1057/AI-Business-analytics-studio) · [官网](https://ai-business-analytics-studio-nevsltyu5qtzhgcrzhxzak.streamlit.app/) · 个人维护

**上传业务数据即可获得仪表盘、AI 洞察与预测报告的分析平台**

基于 Streamlit 的 Python 商业分析应用：支持上传 CSV/Excel/JSON/SQLite 及连接 SQL 数据库，提供 KPI 仪表盘、数据画像与清洗、14 种图表、四种模型的时间序列预测（含回测 MAE/MAPE 与 95% 置信带）、异常检测（Z-score/IQR/Isolation Forest）、RFM 客户分群与 PDF/Excel/PowerPoint 报告生成。AI 部分通过 Gemini API 生成八段式经营洞察与自然语言数据问答；无 API key 时由确定性离线分析引擎接管，功能仍可运行。关键机制是语义角色列映射层，不硬编码列名，任意表格数据均可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义角色自动映射列（regex+dtype 打分），适配任意表格数据
- Gemini 生成八段式洞察与受沙箱限制的 pandas 问答，无 key 时回退离线规则引擎
- 预测（4 种模型、回测置信带）、异常检测、RFM 分群、SQL 工作区
- PDF/Excel/CSV/PowerPoint 四格式报告与用户认证、操作历史

## 适用场景

- 把销售导出表快速变成 KPI 仪表盘和汇报材料
- 用自然语言提问探索自己的业务数据
- 无 API key 的离线环境做预测、异常检测与客户分群

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L22: |**No API key?**|Everything still works — the app falls back to a built-in offline analyst|
> L128: |**AI**|Google Gemini|`gemini-2.0-flash` by default, with a deterministic offline fallback|
> L228: ### 3. Offline analyst — the fallback that makes AI optional

## 星数曲线

```mermaid
xychart-beta
    title "ayeshamumtaz1057/AI-Business-analytics-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2c12ba1df919` · [字段定义](../../DATASET.md)*
