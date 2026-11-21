# michael-kitchin/agent-wars

⭐ 4 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/michael-kitchin/agent-wars) · [官网](https://standingorders.substack.com) · 个人维护

**真实地球六边形地图上的回合制大战略游戏，对手为自选 LLM**

基于 Electron 与 TypeScript 构建的回合制大战略游戏，棋盘为真实地球的 H3 六边形网格（全球与 23 张区域地图，两种尺度），对弈方式为 WEGO 同时下单制。玩家可接入最多 3 个 AI 对手，通过 OpenRouter 选择 Anthropic、Google、OpenAI 等厂商模型充当指挥官；引擎先预计算战报（ASCII 地图、单位与威胁表格），再咨询模型，未咨询回合由常备指令延续计划。无 API key 时应用仍可运行，可关闭 AI 纯人游玩。项目代码主要由编码 agent 生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 真实地球 H3 六边形网格，战略 6 尺度与战术战斗缩放
- WEGO 同时回合制：双方基于部分视野同时下达战斗、移动与生产指令
- 混合 AI 对手：引擎预计算 ASCII 战报与 Markdown 表格后咨询模型，支持无工具调用的模型
- 提供 Windows/macOS/Linux 未签名安装包并附 SHA-256 校验

## 适用场景

- 在真实世界地理地图上与自选 LLM 模型对弈大战略游戏
- 同一局比赛中让多个不同厂商的模型互相对抗
- 通过 .env 日志查看完整的提示词与模型响应调试内容

## 场景标签

 · 领域:游戏/桌面应用

## 证据(README 行号)

> L7: A turn-based grand strategy game on a real-Earth hex map, where your opponent is a large language model you choose. 
> L87: - When the AIs are done planning, the **Ready** button turns green. Click it to execute planned orders and start th
> L143: - **A hybrid AI opponent.** The engine pre-computes a briefing (an ASCII hex map, Markdown tables of units and thr

## 星数曲线

```mermaid
xychart-beta
    title "michael-kitchin/agent-wars 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-20", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `ba8360cdb773` · [字段定义](../../DATASET.md)*
