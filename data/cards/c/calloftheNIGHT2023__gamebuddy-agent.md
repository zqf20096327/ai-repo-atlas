# calloftheNIGHT2023/gamebuddy-agent

⭐ 36 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/calloftheNIGHT2023/gamebuddy-agent) · [官网](http://www.gamebuddyagent.site/) · 个人维护 · 中文 README

**浏览器端游戏分析实验室：可玩沙盒加局势解读与复盘**

基于 FastAPI 后端与 Next.js 前端的浏览器端游戏分析工具，包含三款回合制可玩原型（松风镇、河谷争夺、地牢余火）与类宝可梦战斗、MOBA 复盘、RPG 配装等分析 Demo。将游戏状态转换为局势总结、阶段判断、战术建议与复盘报告；无 API Key 时走内置规则路径，数据写入本地 SQLite，可选接入 OpenRouter 以 LLM 增强结果，并支持兼容 Function Calling 的本地工具调用与 Trace 记录。截图分析目前为占位实现。

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

- 游戏状态输入产出局势总结、阶段判断、战术建议与复盘报告
- 无 Key、无 MongoDB 即可运行，数据落本地 SQLite
- 可选 OpenRouter LLM 增强，超时或校验失败回退规则路径并记录降级原因
- 兼容 Function Calling 的本地工具（游戏知识查询、用户画像）

## 适用场景

- 对局后复盘与失误分析
- 理解当前局势并获得面向新手的战术建议
- 在同一项目中体验可玩沙盒与模块化分析流程

## 场景标签

 · 领域:游戏/策略分析工具

## 证据(README 行号)

> L45: GameBuddy Agent is a browser-based game analysis lab. It combines structured review demos with playable sandbox mod
> L152: If `OPENROUTER_API_KEY` is set, the backend can enhance heuristic analysis with an LLM response. If it is not set,

## 星数曲线

```mermaid
xychart-beta
    title "calloftheNIGHT2023/gamebuddy-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-29 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `08d555b2ff0c` · [字段定义](../../DATASET.md)*
