# isyuhaochen/XiangqiArena

⭐ 16 · JavaScript · 推送 2026-04-15 · [GitHub](https://github.com/isyuhaochen/XiangqiArena) · 个人维护 · 中文 README

**本地中国象棋对战平台：Human/Random/LLM/Pikafish 任意对局与评测**

本地运行的象棋 Arena：FastAPI 后端加原生 HTML/Canvas 前端，支持 Human、Random、LLM、Pikafish 四种玩家类型任意两两对局，可多局并发。LLM 侧统一走 OpenAI Python SDK，支持预设模型与自定义配置、从 YAML 加载 Prompt。评测侧可配置参与方与评估用 Pikafish 分别指定可执行文件，内置排行榜统计胜负与红黑方分项数据，支持暂停、回看与对局日志保存。运行需 Python 3.10+ 并自备 Pikafish 引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种玩家类型任意组合对战，支持多局并发
- LLM 调用统一走 OpenAI Python SDK，可加载 YAML Prompt
- 评估用与参与方 Pikafish 引擎可分开配置
- 内置排行榜统计胜负及红黑方分项数据

## 适用场景

- 让 LLM 与 Pikafish 引擎对局并查看评分走势
- 并发跑多局对局做排行榜统计
- 自定义开局 FEN 与 Prompt 测试 LLM 象棋能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: BattleChess 是一个本地运行的中国象棋 Arena，支持 `Human / Random / LLM / Pikafish` 任意两两对局。
> L7: 前端使用原生 HTML / CSS / JavaScript 与 Canvas，后端使用 FastAPI。LLM 调用统一走 OpenAI Python SDK。
> L27: - 支持专业引擎对局评分

## 星数曲线

```mermaid
xychart-beta
    title "isyuhaochen/XiangqiArena 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `df0792468e14` · [字段定义](../../DATASET.md)*
