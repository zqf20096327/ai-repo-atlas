# lifan-builds/poe2brain

⭐ 48 · Python · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/lifan-builds/poe2brain) · [官网](https://poe2brain.clifan.com/) · 个人维护 · 中文 README

**为 AI 助手提供 Path of Exile 2 0.5.5 版本计算与数据的 MCP 引擎**

面向玩家与 AI 客户端的 PoE2（0.5.5）情报引擎：通过 45 个 MCP 工具与 JSON CLI，暴露离线 SQLite+FTS5 数据库、headless LuaJIT PathOfBuilding-PoE2 守护进程、官方 trade2 价格、装备打造概率求解与自带校验的 loot filter 编译器。六大模块覆盖机制反幻觉、配装审计、套利扫描、刷图正则等；要求 Python 3.12+ 与 uv，Windows 无需 C 编译器，不使用 POESESSID。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 45 个 MCP 工具与 1:1 JSON CLI 双通道接入
- headless LuaJIT PoB2 守护进程：配装审计、what-if 沙盒、支持宝石/珠宝排名
- 条件词缀池精确打造概率（p50/p80/p95 Monte Carlo）
- 自校验 .filter 编译器与 NeverSink 0.10.4a 重样式化、双语语音提示

## 适用场景

- 让 Claude Code/Cursor 等 AI 客户端直接查询 PoE2 0.5.5 机制与数值
- 导入角色做配装审计并给出前 5 个升级瓶颈
- 计算打造概率与成本，避免被通货膨胀 DPS 误导
- 编译可用的 loot filter 并生成 EN/ZH 语音提示

## 场景标签

 · 领域:游戏/游戏数据分析

## 证据(README 行号)

> L11:  Give Claude Code, Cursor, Antigravity, Codex, or Cherry Studio
> L30: **`poe2brain`** replaces guesswork with a single typed Python 3.12+ engine exposing **45 MCP tools** (`poe2brain-mc
> L105: 2. **Headless Path of Building 2 (`poe2brain.pob`)** — Persistent native `LuaJIT` + `PathOfBuilding-PoE2` (`tree 0


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `226c4983c31b` · [字段定义](../../DATASET.md)*
