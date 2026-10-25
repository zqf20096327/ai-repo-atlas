# Bobby-Gray/open-tabletop-gm

⭐ 59 · Python · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/Bobby-Gray/open-tabletop-gm) · [官网](https://neuralinitiative.ai) · 个人维护

**LLM 无关的桌面 RPG 主持框架：让任意 LLM 当 Game Master**

面向 TTRPG 玩家的 AI 主持（GM）框架：LLM 负责叙事与判断，骰子、先攻、HP、状态效果等机械部分由本地 Python 脚本执行，不消耗模型调用。战役状态以纯 Markdown 文件持久保存。内置 D&D 5e、PF2e 兼容与 BRP 三个规则模块，可按模板接入其他系统。通过 OpenCode 运行，支持 LM Studio 本地模型或任意 LLM 服务；另含可选的 Flask 网页展示端（局域网/TV 投屏）与关系图谱。安装方式为 git clone 并配置 OpenCode。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 无关：可经 OpenCode 接 LM Studio 本地模型或任意 LLM 服务运行
- 骰子、先攻、HP、状态效果等机械逻辑本地 Python 执行，零 LLM 参与
- 内置 D&D 5e / PF2e 兼容 / BRP 三个规则模块，可按模板扩展任意 TTRPG
- 可选 Flask 展示端：实时数值侧栏、效果标签、玩家输入面板，支持 LAN/TV

## 适用场景

- 用本地或云端 LLM 长期运行持久化的 D&D 战役
- 把跑团机制外包给确定性脚本，让模型专注叙事
- 写一个 system.md 模块把其他规则系统（如 CoC、VtM）接入同一 GM 框架
- 团桌上用浏览器或电视投屏展示实时角色面板

## 场景标签

 · 领域:游戏/娱乐

## 证据(README 行号)

> L5: An LLM-agnostic Game Master framework for persistent tabletop RPG campaigns. Built to run on any model available thr
> L15: A GM framework that offloads everything mechanical to Python so the LLM can focus on narration and judgment:

## 星数曲线

```mermaid
xychart-beta
    title "Bobby-Gray/open-tabletop-gm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-25 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3ae3d0b4495a` · [字段定义](../../DATASET.md)*
