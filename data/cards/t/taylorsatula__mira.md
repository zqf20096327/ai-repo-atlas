# taylorsatula/mira

⭐ 482 · Python · AGPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/taylorsatula/mira) · [官网](https://www.miraos.org) · 个人维护

**持续在线的个人 AI 助手，带长期记忆与自我行为调适**

自托管的持续数字实体：单一永久会话线程，旧对话段折叠为第一人称记忆摘要，活跃上下文通过滚动简报压缩。记忆按使用日衰减并按访问与关联保留，经语义相似度、实体枢纽与重排被动载入上下文。内置 Subcortical 前置检索层与 Peanut Gallery 元认知观察层，以及基于对话评估的 'Text-Based LoRA' 行为适应循环（信号存于 PostgreSQL）。提供浏览器与终端聊天客户端、约 17 个内置工具与文件系统工具自注册机制。AGPL-3.0 许可，另有 miraos.org 托管版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 永久单会话线程 + 对话段折叠为第一人称记忆摘要
- 按使用日衰减、免人工整理的记忆系统（语义检索/实体枢纽/重排）
- Subcortical 前置检索与 Peanut Gallery 元认知观察两层机制
- 工具从文件系统自注册，invokeother_tool 按需启用临时工具

## 适用场景

- 运行一个长期记得我偏好与历史对话的个人 AI 助手
- 通过 Email、Home Assistant、日历提醒等工具接入日常事务
- 自托管并按 HOW_TO_BUILD_A_TOOL.md 扩展自定义工具

## 场景标签

 · 领域:AI 助手/记忆系统

## 证据(README 行号)

> L8: Mira accomplishes the end goal of continuity and recall through a blend of asynchronous conversation processing akin
> L22: Memories are discrete synthesized information that is passively loaded into the context window through semantic sim
> L90: I decided to release MIRA as open source technology because I believe that what I’ve built here has the potential t

## 星数曲线

```mermaid
xychart-beta
    title "taylorsatula/mira 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 481 --> 483
    line [482, 482]
```

2026-10-18 482 → 2026-10-22 482（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4b8a9aa16918` · [字段定义](../../DATASET.md)*
