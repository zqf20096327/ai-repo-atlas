# tegridydev/dnd-llm-game

⭐ 126 · Python · NOASSERTION · 推送 2026-08-22 · [GitHub](https://github.com/tegridydev/dnd-llm-game) · 个人维护

**本地 LLM 驱动的单人 D&D 地下城主应用**

在本地计算机运行的单人 D&D 冒险游戏：由 Ollama 模型流式生成场景叙述，应用自身持有骰子与战斗规则（先攻、 lanes、HP、状态、死亡豁免），并用 SQLite 与 LanceDB 在会话间保存战役、任务、NPC 与世界事实。支持六职业四祖先的可复用角色、DM 控制队友、本地 PDF 设定资料的上传与嵌入索引，可为叙述、规则、检索分别指定模型。技术栈为 React + FastAPI + SQLite + Ollama + LanceDB，仅绑定回环地址，无云端服务与账号。需要 Python 3.11–3.14、uv、Bun 与本地 Ollama，通过 bun run dev 一键启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama 本地模型流式生成场景，叙述/规则/检索可分别指定模型
- 应用持有骰子与回合制战斗规则（先攻、状态、死亡豁免）
- SQLite + LanceDB 持久化战役，支持中断操作的安全重试
- 本地 PDF 设定上传、切分与嵌入索引

## 适用场景

- 独自进行 D&D 风格冒险，让 AI 担任地下城主
- 在战役中导入自己的设定 PDF 供 DM 参考
- 在无云端、数据不出本机的环境下游玩并跨会话延续战役

## 场景标签

 · 领域:游戏/本地 AI 应用

## 证据(README 行号)

> L3: A local AI Dungeon Master for solo D&D-style adventures. It runs on your computer, streams scenes from Ollama, owns 
> L14: - Pick separate Ollama models for narration, rules, and lore search
> L17: Everything stays local: **React + FastAPI + SQLite + Ollama + LanceDB**. There are no accounts, cloud services, or 

## 星数曲线

```mermaid
xychart-beta
    title "tegridydev/dnd-llm-game 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 124 --> 127
    line [125, 126, 126]
```

2026-10-18 125 → 2026-10-28 126（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fd91daf4eb95` · [字段定义](../../DATASET.md)*
