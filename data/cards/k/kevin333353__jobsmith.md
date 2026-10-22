# kevin333353/jobsmith

⭐ 155 · Python · Apache-2.0 · 推送 2026-07-31 · [GitHub](https://github.com/kevin333353/jobsmith) · [官网](https://github.com/kevin333353/jobsmith/releases/latest) · 个人维护 · 中文 README

**台湾求职者的多代理 AI 求职副驾驶：找职缺、健检履历、生成投递包**

面向台湾求职市场的开源桌面应用（FastAPI + React + LangGraph 多代理）。功能包括免 AI 的职缺搜索（104/Cake/Yourator/LinkedIn，本地规则匹配与可解释排序）、AI 履历健检、客制化投递包生成（简历・求职信・面试准备・公司情报）、模拟面试与逐题评分。AI 引擎默认复用本机 Claude Code / Codex CLI 订阅（免 API key），也可接 Ollama/llama.cpp 本机模型或 BYOK 任意 OpenAI 相容端点。任务在后台线程池执行，可多职缺并行，产出需用户逐份核可；本地优先存储（SQLite/.env）。提供 Windows .exe 与 macOS unsigned .dmg，也可从源码运行或使用免 AI 的公开 Web 测试版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免 AI 找职缺：本地规则解析履历、可解释适配排序，0 token 无需 API key
- 投递包后台并行生成，AI 品管只给一次建议不自动重写，需人工核可
- 默认复用本机 Claude Code / Codex CLI 订阅作 AI 引擎，免自行申请 API key
- 本地优先：数据存本机，公开 Web 测试版强制 0 AI 且不保存服务器端履历

## 适用场景

- 上传履历后自动搜索并筛选 104/Cake/Yourator/LinkedIn 职缺
- 为每个心仪职缺生成客制简历、求职信、面试准备与公司情报
- 按 JD 与我的履历进行模拟面试并获得逐题评分
- 用我已有的 Claude Code 订阅驱动 AI 功能，不想另付 API 费用

## 场景标签

`AI 助手` `多智能体` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L5: **針對台灣求職市場的開源多代理（multi-agent）AI 求職 co-pilot。**
> L9: 預設用你本機的 **Claude Code / Codex CLI 訂閱**當 AI 引擎（**免自行申請 API key**），也能改用 **Ollama / llama.cpp 本機模型**，或**自備金鑰**接任何 OpenA
> L107: - **投遞包工作台**：預設「快速投遞」只做客製履歷，也可選「完整申請」「面試準備」或自行勾選文件；公司情報與 AI 品管皆為選配。搜尋結果會沿用已完成的職缺分析，AI 品管只提供一次修改建議、**不自動重寫**。整個流程在*

## 星数曲线

```mermaid
xychart-beta
    title "kevin333353/jobsmith 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 154 --> 156
    line [155, 155]
```

2026-10-18 155 → 2026-10-22 155（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e959c4c00270` · [字段定义](../../DATASET.md)*
