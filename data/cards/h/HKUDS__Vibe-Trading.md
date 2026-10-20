# HKUDS/Vibe-Trading

⭐ 35,802 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/HKUDS/Vibe-Trading) · [官网](https://vibetrading.wiki/) · 组织维护 · 中文 README

**个人量化交易 Agent：回测、实盘与研究一站式**

由 HKUDS 开发的个人交易 Agent，以 Python 包（vibe-trading-ai）分发，通过 FastAPI 后端与 React 前端提供 Web 界面。功能覆盖策略回测（Sortino、Monte Carlo、walk-forward 等指标）、实盘运行调度（决策会话、每日用量预算）、研究工作流（因子计算、SEC 文件、证据溯源 grounding gate）以及多渠道接入（Email、Slack、Discord、飞书、WeChat、WebSocket）。支持 18 家券商连接器与多市场数据（A 股、美港股、加密货币等），v0.1.16 起数字需经工具证据校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.9 天,年发版 13,180 位贡献者
- 涨星:近 1 天 **+87**(自 20261016 起算)
- 安装:pypi 包 `vibe-trading-ai` 月下载 6,681
- 平台:— · 协议:MCP

## 能力要点

- 回测引擎输出 Sortino、turnover、Monte Carlo p 值等结构化指标并以 CSV 佐证
- grounding gate 按数字角色（observed/derived/proposed/cited/count）校验模型输出与工具证据一致性
- 18 家券商连接器（含 KIS、Upbit、Toss Securities、Scalable Capital 等）与多市场数据源
- Email/Slack/Discord/飞书/WeChat/WebSocket 等多渠道接入及定时报告（PDF 支持 AES-256 加密）

## 适用场景

- 用自然语言让 Agent 跑策略回测并出具带证据的报告
- 接入券商做实盘运行并设置每日模型用量预算
- 对 A 股/美港股/加密资产做因子研究与组合分析
- 通过飞书/Slack 等接收定时交易与研究报告

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5:  Vibe-Trading: Your Personal Trading Agent
> L33:  pip install vibe-trading-ai
> L79: - **2026-09-29** 🚀 **v0.1.16 released** (Release notes, `pip install -U vibe-trading-ai`): 492 commits and 116 merg

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `e309c4739710` · [字段定义](../../DATASET.md)*
